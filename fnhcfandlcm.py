def hcf(a,b):
    hcf = 1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
           hcf = i
    return hcf
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
print('HCF of %d and %d is %d' %(first, second, hcf(first, second)))
lcm = first * second / hcf(first, second)
print('LCM of %d and %d is %d' %(first, second, lcm))
