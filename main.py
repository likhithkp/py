age = int(input("Enter your age\t"))

if age > 18:
    print("Welcome to the club")
elif age == 18:
    print("Perfect, welcome")
elif age < 0:
    print("Not a valid age")
else:
    print("Oops you are a child")