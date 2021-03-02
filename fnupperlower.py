def word(new):
    upper=0
    lower=0
    print("length of string is :",len(new))
    for i in range(0,len(new)):
        if new[i].isupper():
            upper=upper+1
        else:
            lower=lower+1
    print("upper case letter are:",upper)
    print("lower case letter are:",lower)
new="aniMAL"
word(new)
