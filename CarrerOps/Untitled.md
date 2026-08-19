Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\DELL> hermes --version
Hermes Agent v0.20.0 (2026.8.3)
Install directory: C:\Users\DELL\AppData\Local\hermes\hermes-agent
Python: 3.11.15
OpenAI SDK: 2.24.0
Run 'hermes version' for update status.
PS C:\Users\DELL> hermes doctor

┌─────────────────────────────────────────────────────────┐
│                 🩺 Hermes Doctor                        │
└─────────────────────────────────────────────────────────┘

◆ Security Advisories
  ✓ No active security advisories

◆ MCP Server Security
  ✓ No suspicious MCP stdio commands

◆ Python Environment
  ✓ Python 3.11.15
  ✓ SQLite 3.53.1
    → SQLite source id: 2026-05-05 10:34:17 c88b22011a54b4f6fbd149e9f8e4…
    → state.db: WAL journal mode (15.1 MB)
    → cron/executions.db: WAL journal mode (20.0 KB)
    → projects.db: WAL journal mode (44.0 KB)
    → kanban.db: WAL journal mode (120.0 KB)
  ✓ Virtual environment active
  ✓ Version files consistent (0.20.0)

◆ SSL / CA Certificates
  ✓ SSL CA certificate bundle is valid

◆ Required Packages
  ✓ OpenAI SDK
  ✓ Rich (terminal UI)
  ✓ python-dotenv
  ✓ PyYAML
  ✓ HTTPX
  ✓ Croniter (cron expressions) (optional)
  ✓ python-telegram-bot (optional)
  ⚠ discord.py (optional, not installed)

◆ Configuration Files
  ✓ ~/AppData\Local\hermes/.env file exists
  ✓ API key or custom endpoint configured
  ✓ ~/AppData\Local\hermes/config.yaml exists
  ✓ Config version up to date (v34)
  ✓ No deprecated config keys or env vars

◆ xAI Model Retirement (May 15, 2026)
  ✓ No retired xAI models in config

◆ Auth Providers
  ⚠ Nous Portal auth (not logged in)
  ✓ OpenAI Codex auth (logged in)
  ⚠ MiniMax OAuth (not logged in)
  ⚠ xAI OAuth (not logged in)
    → No xAI OAuth credentials stored. Select xAI Grok OAuth (SuperGrok / Premium+) in `hermes model`.

◆ Directory Structure
  ✓ ~/AppData\Local\hermes directory exists
  ✓ ~/AppData\Local\hermes/cron/ exists
  ✓ ~/AppData\Local\hermes/sessions/ exists
  ✓ ~/AppData\Local\hermes/logs/ exists
  ✓ ~/AppData\Local\hermes/skills/ exists
  ✓ ~/AppData\Local\hermes/memories/ exists
  ✓ ~/AppData\Local\hermes/SOUL.md exists (persona configured)
  ✓ ~/AppData\Local\hermes/memories/ directory exists
    → MEMORY.md not created yet (will be created when the agent first writes a memory)
  ✓ USER.md exists (746 chars)
  ✓ ~/AppData\Local\hermes/state.db exists (10 sessions)
    → state.db logical size 15.1 MB, 3,867 pages, 53 free, WAL 0 B
    → 531 messages, 10 sessions, journal_mode=wal
    → FTS tables: messages_fts, messages_fts_trigram

◆ External Tools
  ✓ git
  ✓ ripgrep (rg) (faster file search)
  ⚠ docker not found (optional)
  ✓ Node.js
  ✓ agent-browser (Node.js) (browser automation)
  ✓ Playwright Chromium (browser engine)
  ✓ Browser tools (agent-browser) deps (no known vulnerabilities)
  ✓ web workspace deps (no known vulnerabilities)
  ✓ ui-tui workspace deps (no known vulnerabilities)

◆ API Connectivity
  ✓ OpenRouter API
  ✓ NVIDIA NIM

◆ Tool Availability
  ✓ browser-use
  ✓ clarify
  ✓ code_execution
  ✓ computer_use
  ✓ cronjob
  ✓ delegation
  ✓ desktop_ui
  ✓ file
  ✓ memory
  ✓ project
  ✓ session_search
  ✓ skills
  ✓ terminal
  ✓ todo
  ✓ tts
  ✓ video
  ✓ vision
  ✓ kanban (runtime-gated; loaded only for dispatcher-spawned workers)
  ⚠ bfl (system dependency not met)
  ⚠ browser (system dependency not met)
  ⚠ browser-cdp (system dependency not met)
  ⚠ discord (missing DISCORD_BOT_TOKEN)
  ⚠ discord_admin (missing DISCORD_BOT_TOKEN)
  ⚠ feishu_doc (system dependency not met)
  ⚠ feishu_drive (system dependency not met)
  ⚠ hermes-yuanbao (system dependency not met)
  ⚠ homeassistant (system dependency not met)
  ⚠ image_gen (system dependency not met)
  ⚠ spotify (system dependency not met)
  ⚠ video_gen (system dependency not met)
  ⚠ web (missing EXA_API_KEY, PARALLEL_API_KEY, TAVILY_API_KEY, FIRECRAWL_API_KEY, FIRECRAWL_API_URL, FIRECRAWL_GATEWAY_URL, TOOL_GATEWAY_DOMAIN, TOOL_GATEWAY_SCHEME, TOOL_GATEWAY_USER_TOKEN)
  ⚠ x_search (missing XAI_API_KEY)

◆ Skills Hub
  ⚠ Skills Hub directory not initialized (run: hermes skills list)
  ⚠ No GITHUB_TOKEN (60 req/hr rate limit — set in ~/AppData\Local\hermes/.env for better rates)

◆ Memory Provider
  ✓ Built-in memory active (no external provider configured — this is fine)

────────────────────────────────────────────────────────────
  Found 1 issue(s) to address:

  1. Run 'hermes setup' to configure missing API keys for full tool access

  Tip: run 'hermes doctor --fix' to auto-fix what's possible.

PS C:\Users\DELL> hermes tools

⚕ Hermes Tool Configuration
  Enable or disable tools per platform.
  Tools that need API keys will be configured when enabled.
  Guide: https://hermes-agent.nousresearch.com/docs/user-guide/features/tools


  Select an option:
  Select by number, Enter to confirm.

  (●)  1. Configure 🖥️  CLI  (22/27 enabled)
  (○)  2. Configure 📱 Telegram  (21/27 enabled)
  (○)  3. Configure all platforms (global)
  (○)  4. Reconfigure an existing tool's provider or API key
  (○)  5. Configure MCP server tools
  (○)  6. Done

  Choice [default 1]: 6

  Tool configuration saved to ~/AppData\Local\hermes/config.yaml
  Changes take effect on next 'hermes' or gateway restart.

PS C:\Users\DELL> hermes skills
Usage: hermes skills

Run 'hermes skills <command> --help' for details.

PS C:\Users\DELL> hermes mcp list

  MCP Servers:

  Name             Transport                      Tools        Status
  ──────────────── ────────────────────────────── ──────────── ──────────
  filesystem       npx -y @modelcontextproto...   all          ✓ enabled

PS C:\Users\DELL>
PS C:\Users\DELL> node --version
v22.16.0
PS C:\Users\DELL> npm --version
11.8.0
PS C:\Users\DELL> git --version
git version 2.47.1.windows.2
PS C:\Users\DELL> agy --version
1.0.8
PS C:\Users\DELL> hermes --version
Hermes Agent v0.20.0 (2026.8.3)
Install directory: C:\Users\DELL\AppData\Local\hermes\hermes-agent
Python: 3.11.15
OpenAI SDK: 2.24.0
Run 'hermes version' for update status.
PS C:\Users\DELL>