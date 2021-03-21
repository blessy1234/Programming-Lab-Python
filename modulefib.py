def fib(a,b):
    n1=0
    n2=1
    print("Fibonocci series is ",end="")
    n3=0
    for i in range(a,b+1):
        if i==0:
            print(n1,end="")
        elif i==1:
            print(n2,end="")
        else:
            n3=n1+n2
            n1=n2
            n2=n3
            print(n3,end=" ")
