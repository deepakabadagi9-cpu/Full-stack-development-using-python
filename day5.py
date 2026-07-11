# class bank:
#     def __init__(self):
#         self.balance=10000
# account=bank()
# account.balance=1000000
# print(account.balance)
# class bank:
#     def __init__(self): 
#         self._balence=10000
#     def deposite(self,amount):
#         self._balence+=amount
#     def show_balnce(self):
#             print(self._balence)

# account=bank()
# account.deposite(5000)
# account.show_balnce()
#getter#
# class employee:
#     def __init__(self,salary):
#         self._salary=salary
#     def get_salary(self):
#         return self._salary
# emp=employee(52836)
# print(emp.get_salary())

#setter#
# class employee:
#     def __init__(self):
#         self._salary=0
#     def set_salary(self,amount):
#         if amount>0:
#             self._salary=amount
#         else:
#             print("invald aslary")
#     def get_salary(self):
#         return self._salary
# emp=employee()
# emp.set_salary(536736)
# print(emp.get_salary())

#polymorphism#
# class dog:
#     def sound(self):
#         print("dog braks")
# class cat:
#     def sound(self):
#         print("cat meows") 
# Dog=dog()
# Cat=cat()
# Dog.sound()
# Cat.sound()
# class upi:
#     def pay(self):
#         print("payment done")
# class creditcard:
#     def pay(self):
#         print("payment done")
# Upi=upi()
# CreditCard=creditcard()
# Upi.pay()
# CreditCard.pay()
#abstraction means hiding the internal implimatation
#showing only necessary fearture to the user
# from abc import ABC,abstractmethod
# class vehicle(ABC):
#     @abstractmethod

#     def start(self):
#         pass
# class car(vehicle):
#     def start(self):
#         print("Car started")
# car=car()
# car.start()

#
from abc import ABC,abstractmethod
class Dog(ABC):
    @abstractmethod
    
    def sound(self):
        pass
class Cat(Dog):
    @abstractmethod
    def sound(self):
        pass
class Pig(Cat):
    def sound(self):
        print("pig pig")
Pig=Pig()
Pig.sound()