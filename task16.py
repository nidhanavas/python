n=int(input("enter the number"))
b=n
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if(b==s):
    print("the number is palindrome")
else:
    print("the number is not palindrome")