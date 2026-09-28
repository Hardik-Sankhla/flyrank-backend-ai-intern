"""Basic Sequnced and Unsequenced Containers tutorials
"""

# Strings
myString=input("Enter your Name: "); myString; print(myString*2 +" Welcome");

# List - python sequenced container

myL=['cat','dog','lion','lion','panther',]

# Dictionary

myD ={
    "A":"Cat",
    "B":"Dog",
    "C":"Cat"
    } ; print(myD["A"]);print(myD["C"])

# Creating a Set from a String

mySet=set("Creating a Set from a String")
print(mySet)

# Creating a Set from a list

mySet2=set(myL);print(mySet2)