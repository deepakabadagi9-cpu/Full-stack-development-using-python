# product_price=5000
# delivery_charge=100
# total=product_price+delivery_charge
# print(total)

# a=10
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)
# student = 10
# groups =2
# print(student//groups)
###### Assignment ########
# followers = 100
# followers = followers - 1
# print(followers)
#### comparision ######
# saved_password = "abcde"
# entered_password = "abcde"
# print(saved_password == entered_password)
#######logical opertion#####
# balance = 500
# pin_correct = True
# if balance > 1000 and pin_correct:
#     print("You can withdraw money")
# else:
#     print("failed")
 ###### #####
# product_price = int(input("Enter product price: "))
# delivery_charge = int(input("Enter delivery charge: "))
# discount_percent = float(input("Enter discount percentage: "))

# discount_amount = (product_price * discount_percent) / 100

# total_bill = product_price + delivery_charge - discount_amount

# print("\n------ BILL ------")
# print("Product Price    :", product_price)
# print("Delivery Charge  :", delivery_charge)
# print("Discount (%)     :", discount_percent)
# print("Discount Amount  :", discount_amount)
# print("------------------")
# print("Total Bill       :", total_bill)
########
# password = input("Enter your password: ")
# if password == "admin123":
#     print("welcome")
# else:
#     print("wrong password")
###elif###
# marks=85
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >= 50:
#     print("Grade: C")
# else:
#     print("fail")
#####
# marks=7.9
# if marks >= 9.0:
#     print("cgpa: 9.0")
# elif marks >= 8.0:
#     print("cgpa: 8.0")
# elif marks >= 7.0:
#     print("cgpa: 7.0")
# else:
#     print("fail")
####and gate#####
# age=25
# sallary=50000
# if age >= 18 and sallary >= 30000:
#     print("loan approved")
####or gate#####
# day = "sunday"
# if day == "saturday" or day == "sunday":
#     print("holiday")
# not gate#
# is_adult = False

# if not is_adult:
#     print("You are not an adult")
# ##
# pin = int(input("Enter your pin: "))
# bank_balance = 10000

# if pin == 1234:
#     print("Correct pin")
#     amount = int(input("Enter amount to withdraw: "))
#     if amount <= bank_balance:
#         print("Withdrawal successful")
#         print("Remaining balance:", bank_balance - amount)
#     else:
#         print("Insufficient balance")
# else:
#     print("Wrong pin")
##for loop###
# for i in range(5):
#      print("send mail")
# users=["dinga","dingi","penga"]
# for user in users:
#     print("send mail to",user)
# for i in range(2,6):
#      print(i)
# name="dhoni"
# for ch in name:
#     print(ch)
###while loop###
# i=0
# while i<5:
#     print("send mail")
#     i+=1
##do while loop###
# i=0
# while True:
#     print("send mail")
#     i+=1
#     if i>=5:
#         break
# passwoord = ""
# while passwoord != "1234":
#     passwoord = input("Enter your password: ")
#     print("login successful")
###list##
users = ["Alice", "Bob", "Charlie"]

users.remove("Bob")
users.append("aparna")

print(users)
print(users.index("aparna"))
print(users[2].islower())