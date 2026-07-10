# student = ("ram","sam","rana")
# print(student)
# print(student[2])
# ####tuple is a collection used to store multiple values####
# numbers = (10,20,30,40)
# print(numbers[2])
# print(numbers[0:2])

# data = (1,2,3)
# data[0] = 100
# print(data)
####multipale values###
# x=(1,2,3,2,1,1,1)
# print(x.count(1))
# print(x.count(2))
# x = ("apple", "banana", "graps", "banana")
# print(x.count("banana"))
# print(x.index("banana"))
# ##### slicing #####
# print(x[1:3])
# print(x[1:4])
# x ={1,2,3,2,1,1,1}
# print(x)
# data = {1,2,3}
# data.add(4)
# print(data)
# data.remove(2)
# print(data)
# a = {1,2,3}
# b = {3,4,5}
# print(a|b)

# a = {1,2,3}
# b = {3,4,5}
# print(a&b)
### function is reusable block of code##
# def greeting():
#     print("hello students")
# greeting()
### return function###
# def add():
#     return 10+20
# result = add()
# print(result)

# def sub():
#     return 20-10
# result = sub()
# print(result)
#arguments#
# def add(a, b):
#     print(a + b)
# add(10, 20)
# def sub(a, b):
#     print(a - b)
# sub(20, 10)
# def mul(a, b):
#     print(a * b)
# mul(10, 20)
# def div(a, b):
#     print(a / b)
# div(20, 10)
# def dinga(*numbers):
#     print(numbers)
# dinga(10, 20, 30, 40, 50,60)
# def add(*num):
#     total = 0
#     for i in num:
#         total += i
#     print(total)
# add(10, 20, 30, 40, 50, 60)

# ###kwargs or keyword arguments###
# def student(**datails):
#     print(datails)
# student(name="dinga", age=20, course="python")
##
# def student(**details):
#     print("name:",details["name"])
#     print("age:",details["age"])
#     print("job:",details["job"])
# student(
#     name="penga",
#     age=22,
#     job="sales"
# )
### squere route function#
# def square(num):
#     return num * num

# n = int(input("Enter a number: "))
# print("Square =", square(n))

# ##another ex
# def squere(x):
#     return x*x
# print(squere(16))
# squere = lambda x:x*x
# print(squere(25))
# add = lambda a,b:a+b
# print(add(10,20))
#even
# thema = lambda n: "Even" if n % 2 == 0 else "Odd"

# print(thema(10))
# print(thema(7))
#lower case
# lower_case=lambda x:x.lower()
# print(lower_case("DEEPA"))
# #upper case
# upper_case=lambda x:x.upper()
# print(upper_case("deepa"))
# #islower case 
# lower_case=lambda x:x.islower()
# print(lower_case("deepa"))p[;]
# lower_case_case=lambda x:x.islower()
# print(lower_case("DEEPA"))
# dinga = lambda text:len(text)
# print(dinga("rukmini vasanta"))
# file = open("student.txt", "w")
# file.write("appu")
# file.close()
# print("data written successfully")
# file = open("student.txt", "r")
# data=file.read()
# print(data)
# file.close()
# file = open("student.txt", "a")
# file.write("How are you")
# file.close()
# print("data appended successfully")
# file = open("student.txt", "r")
# print(file.read())
# file.close()

#exception handling
# try:
#     a=10
#     b=0
#     print(a/b)
# except:
#     print("something went wrong") 
# try:
#     num=int(input("enter number"))
#     print(num)
# except ValueError:
#     print("only number allowed")
#except
# try:
#     a=int(input("enter a:"))
#     b=int(input("enter b:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("cannot division by zero")
# except ValueError:
#     print("only number allowed")
# try:
#     file = open("data.txt")
#     print(file.read())
# except:
#     print("file error")
# finally:
#     print("program complited")
# try:
#     print(10/2)
# except:
#     print("error")
# else:
#     print("success")