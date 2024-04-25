# Task 4
# Access list values

"""
Ask the user to enter in a number less than 10
Print out the list element that corresponds to that
position in the tuple
"""

people=("John","Tyler","Dash","Kieran","Jayson","Tomoki","Minji","Dawson","Hewitt","Josh","Anson","Cole")
n = int(input("please input a number less than 10 (9 or less)"))
n = n - 1
if n < 10:
    print(people[n])
elif n >= 10 and n < 0:
    print("error: your input is invalid!")