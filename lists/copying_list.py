#Example 1
a = ["John", "Mary", "Joseph"]
b = a

a = ["John", "Mary", "Joseph", "Kate"]

#Example 2
a = ["John", "Mary", "Joseph"]
b = a

a.append("Kate")

# Correct way
a = ["John", "Mary", "Joseph"]
b = a.copy()

''' Python assignment statements just references what is being assigned
That being said, if I assign an object "x" to a second object "y",
as long as I don't assign a new object to "x", both will be referencing the
same address in memory. Pretty crappy design, if you ask me'''