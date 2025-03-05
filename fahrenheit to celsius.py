#fahrenheit to celsius
n=input("enter temparature with units:")
ch=n[-1]
n=int(n[:-1])
if ch=='c':
    a=n*(1.8)+32
elif ch=='f':
    a=n*(0.55)-32
print(int(a))
