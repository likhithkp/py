password = "qwerty"

def get_passwd():
    passwd = input("Enter the password\n")
    if passwd != password:
        print("Wrong password")
        get_passwd()
    else:
        print("Welcome!!")

get_passwd()