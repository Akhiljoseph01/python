a=int(input("enter a number"))
sum=0
while(a!=0):
    b=(a%10)
    if b%2=0:
        sum=sum+b
        a=a//10
        print("sum=",sum)
