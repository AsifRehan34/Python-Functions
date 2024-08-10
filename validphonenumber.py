number = input("Enter a number: ")
valid = "1234567890+"
for i in number:
    if i not in valid:
        print("invalid number", number)
        break
