students = ["mamadou","juldeh","bah"]

print(students)

# accessing item in the list
print(f"My best friend is {students[0]}")
print(f"My best friend is {students[1]}")
print(f"My best friend is {students[2]}")

# get the index of an item in a list
print(students.index("mamadou"))
print(students.index("juldeh"))

# Know the number of item in a list
print(f"The total items in the list is:{len(students)}")

# Add items to a list
students.append("Isatu")
print(students)
students +=["kadiatu","john","Bintu"]

print(students)
students.insert(4, "Donald")
print(students)

# Extending a list
fruits = ["Apple","Banana",'Mango']
students.extend(fruits)
print(students)

# Removing an item from a list
fruits.remove("Mango")

students.pop()
students.pop()
students.pop()
thirditem = students.pop()
print(students)
print(thirditem)