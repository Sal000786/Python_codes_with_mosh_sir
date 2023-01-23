customer={
    "name":"salman faizi",
    "cont": 9502250076,
    "email": "salmanfaizi60@gmail.com0",
    "course": "Btech in cse"
}
print(customer["name"])
# print(customer["Name"]) Throws key error
print(customer.get("name"))
print(customer.get("Name")) #It doesn't throws an error it just says None
print(customer.get("Name","Ayub Alam"))

print("previous Dictionary",customer)

customer["add"]="at+post_mirzapur kothi"
print("updated dictionary",customer)
