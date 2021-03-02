def amstrong(n):
    for i in range(1,n+1):
        sum=0
        temp=i
        while(temp>0):
            x=temp%10
            sum+=x**3
            temp=temp//10
            if(i==sum):
                print(i,end=" ")
num=int(input("enter the number of terms:"))
amstrong(num)
