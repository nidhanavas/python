list1=[]
n=int(input("enter the number of element in the list"))
for i in range(0,n):
    b=int(input())
    list1.append(b)
new_lst = list1[::-1]

print("the current list:",list1)
print("the reversed list:",new_lst)
