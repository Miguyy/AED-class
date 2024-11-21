import random

def generatePassword(userName):
    password = ""
    for i in range(1, len(userName), 2): 
        password += userName[i] + str(random.randint(1, 9))
    
    password += str(len(userName))  
    return password

userName = input("Insira o username: ")
print(generatePassword(userName))

