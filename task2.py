str1=input("enter the string ")
p = ""
for char in str1:
    if char not in p:
        p = p+char
print(p)
