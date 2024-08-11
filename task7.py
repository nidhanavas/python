list1=[]
n=int(input("enter the number of element in the list"))
for i in range(0,n):
    b=int(input())
    list1.append(b)
list2=[]
m=int(input("enter the number of element in the list"))
for i in range(0,m):
    c=int(input())
    list2.append(c)
result = [i for i in list1 if i in list2]
print(result)