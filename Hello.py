# print("Hello Grade 10B")
# num1 = int(input("Please enter first number:"))
# num2 = int(input("Please enter second number:"))
# print(num1 +num2)
# str="Jazzy"
# number  = 5
# f1 = 5.2
# b1 = True
# print("::::::::::::::::::::::::::::::::")
# print(type(str))
# print(type(number))
# print(type(f1))
# print(type(b1))
# print(type(num1))
# today = input("Please enter today's day:")
# if today == "Monday":
#     print("I'm sad")
# elif today=="Tuesday":
#     print("Tacos Tuesday")
# elif today =="Wednesday":
#     print("Half week is gone")
# elif today =="Thursday":
#     print("One day is left")
# elif today =="Friday":
#     print("Happy Friday")

# name = input("Please enter your name: ")
# print("Hello",name,"How are you?")
# print("Hello "+name+" How are you?")

places = ["Bangkok","Huahin","Rayong"]
print(places)
print("I want to go to",places[0])
print("I want to go to",places[1])
print("I want to go to",places[2])
print("By using loop:::::::::::::::")
for place in places:
    print("I want to go to",place)


age = 31
if age<2:
    print("You are a baby")
if age>=2 and age<4:
    print("You are a Toddler")
if age>=4 and age<13:
    print("You are a Kid")
if age>=13 and age<20:
    print("You are a Teenager")
if age>=20 and age<65:
    print("You are an adult")
else:
    print("You are an elder")