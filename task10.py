list1=[]
s=0
n=int(input("enter the number of data"))
print("enter the name")
for i in range(0,n):
    b=(input())
    list1.append(b)
list2=[]
m=int(input("enter the number of  data of age"))
print("enter the age respectively")
for i in range(0,m):
    c=int(input())
    list2.append(c)
    s=s+c
result = ([(list1,list2)])
print(result)
avg=s//m
print("avrage age is :",avg)
