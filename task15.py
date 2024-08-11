n=int(input("enter the number"))
b=n
s=0
while n>0:
    r=n%10
    s=s+(r**3)
    n=n//10
if(b==s):
    print("the number is armstrong")
else:
    print("the number is not armstrong")


