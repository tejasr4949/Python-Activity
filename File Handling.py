with open("new_file", "w") as file:
    data = file.write("Welcome to this file")

with open("new_file", "a") as file:
    append = file.write("\nThis is new line")
    
with open("new_file", "r") as file:
    data = file.read()
    print(data)

