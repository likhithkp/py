import os

files = os.listdir()

main_file_found = False

for file in files:
    if file == "main.py":
        main_file_found = True
        break

if main_file_found:
    print("File found")
else:
    print("No main file found")
