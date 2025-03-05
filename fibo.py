a=0
b=1
n=int(input("number:"))
print(a)
print(b)
for i in range (2,n):
    temp=a+b
    a=b
    b=temp
    print(temp)