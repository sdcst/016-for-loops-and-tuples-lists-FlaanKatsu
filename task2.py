#! python3
"""
###### Task 2
Ask the user to enter a name.
Check the name against a tuple that contains a series of names to see if it is a match. Use a for loop this time instead of a single if with multiple
logical operators
(2 points)

inputs:
str name

outputs:
"That name is in the list"
"That name is not in the list"

example:
Enter a name: Grace
That name is not on the list

example:
Enter a name: Lebron
That name is on the list
"""
NP = 0
nameList = ("Lebron","Kobe","Michale","Shaq","Dennis")
UN = str(input("please enter a name: "))
for i in nameList:
    if UN == i:
        NP = 1
        NN = i
if NP == 1:
    print(f"the name \"{NN}\" is on the list!")
elif NP == 0:
    print(f"unfortunately, the name \"{UN}\" is not on the list!")

##there is probably a better way of coding this, but this works