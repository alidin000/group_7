# storage = open("passwords","a")
file_name = "passwords.txt"
try:
    f = open(file_name, "r")
except FileNotFoundError as e:
    print("creating a new file")
    f = open(file_name, "w")
    f.close()
else:
    print("File exists")
class Account:
    def __init__(self,name, password):
        self.__name = name
        self.__password = password
    
    def get_name(self):
        return self.__name
    
    def get_password(self):
        return self.__password
    
    def __str__(self):
         return f'{self.__name}, {self.__password}'
    
def get_name_and_password():
    name = input("your name:")
    password = input("your password:")  
    return (name,password)  

def login():
    name, password = get_name_and_password()
    acc = Account(name, password)
    storage = open(file_name,'r')
    accounts_and_passwords = storage.read()
    output = accounts_and_passwords.find(acc.__str__())
    if output != -1:
        print("logged in succesfully")
    else:
        print("User doesn't exist")
def sign_up():
    name, password = get_name_and_password()
    acc = Account(name, password)
    storage = open(file_name,'a')
    storage.write(f"{acc.__str__()}\n")
    print("signed up successfully")

while True:
    print("1. login")
    print("2. sign up")
    print("3. exit")

    inp = int(input("your choice:"))

    if inp == 1:
        login()
    elif inp == 2:
        sign_up()
    else:
        print("program ended")
        break
    

# storage.close()

p = Account("t", "12")
ff = open("t.txt","w")
ff.write(p.__str__())

