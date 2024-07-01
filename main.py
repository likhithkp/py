password = "qwerty"

def get_passwd():
    passwd = input("Enter the password")
    while passwd != password:
        print("Wrong password")
        break

get_passwd()