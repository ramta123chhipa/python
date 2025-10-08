# name = input("name: ");
# age = int(input("age: "));

# print(name)
# print(age)


# name =  input("enter your name: ")
# print("welcome ", name)


#strings

str1 = "this is a string."
str2 = 'this is a string.'
str3 = """this is a string. """

print(str1.endswith("er"))
print(str1.capitalize())
print(str1.replace("is","was"))
print(str1.find("is"))
print(str1.count("a"))

name = input("name: ")
print("length of your name is: ", len(name))

str = "hii, $I am the $ symbol $99.99"
print(str.count("$"))

light = "green"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("GO")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")

# marks = int(input("enter student marks: "))
# if(marks >= 90):
#     grade ="A"
# elif(marks >= 80 and marks <90):
#     grade = "B"
# elif(marks >=70 and marks < 80):
#     grade = "C"
# else:
#     grade ="D"

# print("grade of student is: ",grade)

 

# x = int(input("enter number: "))
# if(x % 7 == 0):
#    print("multiple of 7")
# else:
#     print("not a multiple")
