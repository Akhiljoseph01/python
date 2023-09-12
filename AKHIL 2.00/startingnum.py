n=int(input("enter a number"))
a=int(input("the first digit to check: "))
while n!=0:
    d=n%10
    a=n//10
    if d==a:
        print("starts with",a)
    else:
        print("not starts with",a)