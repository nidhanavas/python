list1=[]
count=0
n=int(input("enter the number of element in the list"))
for i in range(0,n):
    b=int(input())
    list1.append(b)
b=int(input("enter the number should be searched"))
for i in list1:
    if i==b:
        count+=1

print("the count of occurence of number is:",count )
