#Check the strength of a password

password = (input("Enter your password: "))

results = {}

if len(password) >= 8:
    results["length"] = True
else:
    results["length"] = False

if any(char.isdigit() for char in password):
    results["digits"] = True
else:
    results["digits"] = False

if any(char.isupper() for char in password):
    results["caps"] = True
else:
    results["caps"] = False


print(results)
if all(results.values()) == False:
    print("Weak password")
else:
    print("Strong password")