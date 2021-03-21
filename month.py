month={'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
m=input("enter a month:")
print("Number of days in ",m,"=",month [m])
print( "According to alphabetic order:")
print(sorted(month))
print( "Month which have 30 days: ")
for i in month:
    if month[i]==30:
        print(i,end='')
print()
