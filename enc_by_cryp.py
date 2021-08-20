import os
from cryptography.fernet import Fernet

file = open("fkey.key", "wb")
if os.stat("fkey.key").st_size == 0:
    key = Fernet.generate_key()
    fer = Fernet(key)
    file.write(key)
    file.close()
else:                                                                                         #made by Pratik 
    key = file.read()
    fer = Fernet(key)
    file.close()

def view():
    with open("password.txt", "r") as p:
        for line in p.readlines():
            data = line.rstrip()
            acc, pview = data.split("|")
            print("Account:", acc, "\nPassword:", fer.decrypt(pview.encode()).decode())

def add():
    a_name = input("Account Name: ")
    pwd = input("Password: ")
    with open("password.txt", "a") as p:
        p.write(a_name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    do = input("To add an new password type 'add' (OR) to view and existing one type 'view', Press q to exit.....")
    if do == "q":
        break
    if do == "view":                                                                    #made by Pratik
        view()
    elif do == "add":
        add()
    else:
        continue
