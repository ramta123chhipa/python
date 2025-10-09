# marks1 = 94.9
# marks2 = 89.0
# marks3 = 98.7
# marks4 = 78.8
# marks5 = 93.7

#instead of writing evrytime marks we can 
# make a list in pyhthon which is a 
# in-built data-type which can store multiple values

marks = [94.5,97.9,89.9,78.45,78.59]
# print(marks)
# print(type(marks))

# print(len(marks))
# marks[0] = 99

# print(marks[0])

student = [19,"ramta",98.9,"ajmer"]
print(student)

#string are immutable in python
#list are immutable in python


# print(marks[1:4])
# print(marks[-3:-1])


#list method
# list.append(4)
# list.sort()
# list.sort(reverse=True)
# list.reverse()
# list.inser(idx, el)

list = [2,1,3]
# list.append(4)
# print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list = [2,1,3]
list.insert(1,5)
print(list)
list.remove(2)
print(list)
list.pop(0)
print(list)
