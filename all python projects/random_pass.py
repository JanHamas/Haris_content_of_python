import string
import random

characters = list(string.ascii_letters + string.digits + "@#$$%^%$")

def generate_password():
    lenght_password = int(input("Enter the length of the password: "))
    
    random.shuffle(characters)
    
    password = []
    
    for i in range(lenght_password):
        password.append(random.choice(characters))
        
    password = "".join(password)
    print(password)
    
option = input("Do you want to generate a password (Yes/No): ")
if option == "yes":
    generate_password()
elif option == "no":
    print("program ended")
    quit()
else:
    print("Invalid input, please input yes or no")
    quit()