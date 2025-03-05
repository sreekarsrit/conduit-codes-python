n=int(input("enter any number:"))
flag=True
for i in range(2,(n//2)):
    if n%i==0:
        flag=False
        break
if flag:
    print("given number is prime")
else:
    print("not prime")