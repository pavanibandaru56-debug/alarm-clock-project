n=int(input("num: "))
temp=n
sum=0
while temp>0:
    rem=temp%10
    temp//=10
    fact=1
    for i in range (1,rem+1):
        fact*=i
    sum+=fact
if sum==n:
    print("strong")
else:
    print("not strong")