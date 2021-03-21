list1=[]
list2=[]
for i in range(3):
    a=str(input("enter the colours for first list:"))
    list1.append(a)
for i in range(3):
    b=str(input("enter the clours for second list:"))
    list2.append(b)
m=[x for x in list1 if x not in list2]
print(m)
