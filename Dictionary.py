my_dict = {
    "name":"Jhon",
    "age":30,
    "city":"New York"
    }
print(my_dict)
print(type(my_dict))
print(type(my_dict["name"]))
print("My name is ",my_dict["name"])
print(my_dict["city"])
print(my_dict["age"])
my_dict["job"]="Teacher"
print(my_dict)
my_dict["age"]=31
print(my_dict)
del my_dict["city"]
print(my_dict)


book = {
    "title":"Rich dad poor dad",
    "author":"Robert Kiosky",
    "year":2012
}
print(book)
print(book["author"])
book["genre"]="Finance"
print(book)
book["year"] = 2023
print(book)
del book["genre"]
print(book)















