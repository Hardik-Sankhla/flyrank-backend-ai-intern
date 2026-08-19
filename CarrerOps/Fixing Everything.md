Building a distributed task queue from scratch is an incredible way to master distributed systems, concurrency, and database internals. To build **Hydra-Queue**, you don't need to read a single "how to build a queue" tutorial—you need to understand the underlying primitives and piece them together.

Here is a curated list of free resources, books, and open-source references to guide you through implementing the core mechanics of this project.

### 1. Core Distributed Systems & Queue Concepts

Before writing code, you need to understand the theoretical challenges of distributed systems, specifically **delivery guarantees** (at-most-once, at-least-once, exactly-once) and **idempotency**.

- **Book (Free/Accessible):** _"Designing Data-Intensive Applications"_ by Martin Kleppmann.
    - _Focus:_ Chapter 11 (Stream Processing) covers message brokers, AMQP, and log-based message brokers. This is the absolute gold standard for understanding _why_ systems like Celery or Kafka are built the way they are.
- **Article:** [Exactly-Once Delivery in Distributed Systems](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/) by Tyler Treat.
    - _Focus:_ Understand why "exactly-once" delivery over a network is technically impossible without idempotency, and how to fake it using database transactions and deduplication.
- **Video/Lecture:** [MIT 6.824: Distributed Systems](https://pdos.csail.mit.edu/6.824/schedule.html) (Available on YouTube).
    - _Focus:_ Watch Lecture 1 (Introduction) and Lecture 11 (Quorum/Fault Tolerance). You don't need the whole course, but these will change how you view distributed failures.

### 2. The Database Layer (PostgreSQL `SKIP LOCKED`)

If you choose PostgreSQL as your broker, `FOR UPDATE SKIP LOCKED` is the magic command that prevents multiple workers from grabbing the same task, eliminating lock contention.

- **Article:** [What is SKIP LOCKED for in PostgreSQL 9.5?](https://www.2ndquadrant.com/en/blog/what-is-select-skip-locked-for-in-postgresql-9-5/) (by 2ndQuadrant)
    - _Focus:_ The definitive explanation of how Postgres handles row-level locking for queue workers.
- **Article:** [Using PostgreSQL as a Message Queue](https://chimpler.wordpress.com/2021/04/05/using-postgresql-as-a-message-queue/)
    - _Focus:_ Practical SQL schemas and implementation logic for building the queue tables.
- **Code Reference (Open Source):** Look at the source code of [Procrastinate](https://github.com/procrastinate-org/procrastinate) (Python) or [River](https://github.com/riverqueue/river) (Go). Both are modern, production-grade task queues built entirely on Postgres `SKIP LOCKED`. Reading their schema and SQL queries will teach you how to implement priorities, scheduling, and dead-letter queues.

### 3. The Database Layer (Redis Streams Alternative)

If you prefer an in-memory approach, Redis Streams provides a native consumer-group architecture.

- **Official Doc:** [Redis Streams Tutorial](https://redis.io/docs/data-types/streams-tutorial/)
    - _Focus:_ Specifically read the section on **Consumer Groups** (`XREADGROUP`, `XACK`, `XPENDING`). This is how you implement multiple workers pulling tasks without stepping on each other's toes.
- **Article:** [Building a Task Queue with Redis Streams](https://redis.com/blog/build-message-queue-using-redis-stream/)
    - _Focus:_ Explains how to handle failed tasks and claim pending messages that crashed workers left behind.

### 4. Python Concurrency & Worker Pools

Your workers will need to pull from the DB continuously without blocking, spawn processes, and handle OS signals (like `SIGTERM` when shutting down) gracefully.

- **Resource:** [SuperFastPython by Jason Brownlee](https://superfastpython.com/)
    - _Focus:_ This site is the modern bible for Python concurrency. Read his guides on `multiprocessing.Pool`, `concurrent.futures.ProcessPoolExecutor`, and _graceful shutdown of worker pools_.
- **Documentation:** Read the Python standard library docs for `asyncio` and `multiprocessing`. You will likely need `asyncio` to efficiently poll the database/Redis, and `multiprocessing` to execute the actual CPU-heavy tasks without blocking the event loop.
- **Video:** [David Beazley - Python Concurrency From the Ground Up (LIVE)](https://www.youtube.com/watch?v=MCs5OvhV9S4)
    - _Focus:_ A legendary talk that explains how concurrent workers actually operate under the hood in Python.

### 5. Advanced Mechanics: Dead Letters and Zombie Detection

To make your queue production-ready, it needs to handle failure states.

- **Concept: The "Heartbeat" / Visibility Timeout:** Look into how Amazon SQS handles [Visibility Timeouts](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html).
    - _Implementation:_ When a worker grabs a task, it writes its `worker_id` and a `locked_until` timestamp to the row. A background "reaper" thread constantly looks for tasks where `status = 'processing'` but `locked_until < NOW()`. These are "zombie" tasks whose workers crashed. The reaper resets them to `pending`.
- **Concept: Dead Letter Queues (DLQ):** Read [RabbitMQ's documentation on DLQs](https://www.rabbitmq.com/dlx.html).
    - _Implementation:_ Add a `retries` column. If a task crashes and `retries > max_retries`, move it to a `dead_letters` table so it doesn't infinitely crash your workers.

### Suggested Implementation Steps for You:

1. **Phase 1:** Write a simple Python script that connects to Postgres, inserts a row into a `tasks` table, and another script that runs `SELECT ... FOR UPDATE SKIP LOCKED`, prints the payload, and `DELETE`s the row.
2. **Phase 2:** Wrap the consumer script in a `multiprocessing` pool. Run 10 consumers at once and verify they never process the same row twice.
3. **Phase 3:** Add error handling. Instead of `DELETE`, update the status to `completed` or `failed`.
4. **Phase 4:** Add the "Zombie Reaper" logic to handle workers that you abruptly kill via `Ctrl+C`.

11:23 AM