password = input("Enter a password: ")

result = {}


if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit =  False
for i in password:
    if i.isdigit():
        digit = True 

result["digits"] = digit

uppercase = False
for i in password:
    if i.upper():
        uppercase = True

result["upper-case"] = uppercase

if all(result):
    
    print("Strong password")
else:
    print("Weak password")