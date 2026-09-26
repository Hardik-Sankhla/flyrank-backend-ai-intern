"""Objective to learn about: 
    - In Python we can make same variable name point to different types of objects
    - learn about Type Casting
    - To learn about 'type(Variable_name)' function 

"""

# # Example more then one assignments to same variable
# print("")
# x='abc';print(type(x),x);x=5;print(type(x),x);print(id(x))
# print("" \
# "")

# Example of Float to Int Type Casting 
print("Input any Float value: "); myFloat=float(input()) #input() function in Python always returns a string (str), not a float.
                                # we type casted 'myFloat' to float with float()
print(id(myFloat), myFloat);
myInt=int(myFloat)
print(id(myInt), myInt)