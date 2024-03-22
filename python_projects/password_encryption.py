master_pwd = input("What is your master password? ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw, = data.split("|",)
            print("User:", user, "Password:", passw)
         
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n") 

while True:
    mode = input("would like to create or view password? (Add/View) or q to Quit: ").lower()

    if mode == "q":
        print("Bye!!!")
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid selection")
        continue