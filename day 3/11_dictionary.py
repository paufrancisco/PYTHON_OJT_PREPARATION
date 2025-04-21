person = {"name": "Paulo" , "age" : 24 , "city" : "Manila" }

# Display the value base on their according keys
print(person["name"])
print(person["age"])
print(person["city"])

# Adding key-value pair
print(person)
person["name"] = "Reignier"

# Removing key-value pair
del person["city"]
print(person)

print(" ")
print(" ")
# Iterating over dictionary
for key, value in person.items():
    print(key, ":", value)
