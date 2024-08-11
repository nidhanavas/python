string1=input("enter a string")
for i in range(int(len(string1)/2)):
    if string1[i]!=string1[len(string1)-i-1]:
      print("string is not palindrome")
      break
    else:
        print("string is palindrome")
        break

