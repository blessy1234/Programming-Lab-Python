import modulereverse as r
choice=1
while (choice!=0):
    str=input("enter the string")
    s=r.reverse(str)
if(s==str):
    print("palindrome")
else:
    print("not palindrome")
choice=int(input("enter the choice"))
