b = input("Enter a string: ")
a = set()
for char in b:
    if char in a:
        print("False")
        break
    else:
         a.add(char)
else:
    print("True")