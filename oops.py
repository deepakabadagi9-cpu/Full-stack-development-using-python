# class student:
#     name="penga"
#     def study(self):
#         print("penga is studying")
# s1=student() #s1 is object
# print(s1.name)
# s1.study() #study is method

# class student:
#     def details(self):
#         print("had breakfast")
# s1=student()
# s1.details()
# student.details(s1)

# class student():
#     def __init__(self,name,age):
#         self .name = name
#         self.age = age
# s1 = student("Dinga",22)
# s2 = student("Riya",20)
# print(s1.name, s2.name)
# print(s1.age,s2.age)

# class bank:
#     def __init__(self ,balence):
#         self.balence=balence
#     def check_balence(self):
#         print(self.balence)
# account=bank(5000)
# account.check_balence()
 
# class user:
#     def __init__(self,name):
#         self.name=name
#     def login(self):
#         print(self.name,"logged in")

# u1=user("nibba")
# # u1.login()        
# class father:
#     def house(self):
#         print("father has a house")
# class son(father):
#     def bike(self):
#         print("son has a bike")
# s=son()
# s.house()
# s.car()
# s.bike()
# class thatta:
#     def land(self):
#         print("thatta's land")
# class appa(thatta):
#     def house(self):
#         print("app's house")
# class maga(appa):
#     def bike(self):
#         print("son has a bike")

# obj=maga()
# obj.land()
# obj.house()
# obj.bike()
# class appa:
#     def house(self):
#         print("app's house")
# class amma:
#     def car(self):
#         print("amma's car")
# class son(appa,amma):
#     def bike(self):
#         print("son's bike")

# thirdclass = son()
# thirdclass.house()
# thirdclass.car()
# thirdclass.bike()
# class student:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return self.name
    
# s=student("king")
# print(s)
# def login(func):
#     def wrapper():
#         print("checking login")
#         func()
#     return wrapper
# @login
# def dashboard():
#     print("dashboard login")
# dashboard()
# def message(func):
#     def wrapper():
#         print("function started")
#         func()
#         print("function ended")
#     return wrapper
# @message
# def hello():
#     print("hello python")
# hello()
# @message
# def fruit():
#     print("mango")
# fruit()
# @message 
# def animal():
#     print("lion")
# animal()
# import json
# student={
#     "name":"dinga",
#     "age":22
# }
# data=json.dumps(student)
# print(data)
import requests
response=requests.get("https://api.github.com/users/python")
data=response.json()
print(data)

