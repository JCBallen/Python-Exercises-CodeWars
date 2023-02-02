import os

os.system("cls")

email = input("Type your email: ")

# trick to store splited string with unpacking variables
# ex: juan@gmail.com
name, domain = email.split("@") # juan / gmail.com
domain, ext = domain.split(".") # gmail / com

print(f"User: {name}\nDomain: {domain}\nExtension: {ext}\n")
