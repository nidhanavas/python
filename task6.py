list1=[]
n=int(input("enter the number of element in the list"))
for i in range(0,n):
    b=int(input())
    list1.append(b)
print("the current list:",list1)
new_list = list(set(list1))
print("new list:",new_list)


