tupple1 = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
count=0
b=int(input("enter the number should be searched"))
for i in tupple1:
    if i==b:
        count+=1

print("the count of occurence of number is:",count )

