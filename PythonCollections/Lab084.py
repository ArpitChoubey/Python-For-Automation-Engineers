# Dict
# Key and Value
# name -> "Pramod"

# A dictionary is an unordered collection of data
# in a key-value pair format.

my_dict2 = {
    "name": "Arpit",
    "age" : 36 ,
    "address" : "Bangalore"
}

print(len(my_dict2))
print(my_dict2["name"])
my_dict2["name"] = "Ankit"
print(my_dict2)
print(my_dict2["age"])
print(my_dict2["address"])

phone_book = dict(name="Abhi",age=31,address="Delhi")
print(phone_book)