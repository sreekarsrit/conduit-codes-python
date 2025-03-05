A=[]
print("Enter values for matrix A") 
m=int(input("Number of rows, m = ")) 
n=int(input("Number of columns, n = ")) 
for i in range(m): 
    matrixa=[] 
    for j in range(n): 
        print("Entry in row: {} column: {}".format(i+1,j+1)) 
        matrixa.append(int(input())) 
        A.append(matrixa)

B=[]

print("Enter values for matrix - B") 
m= int(input("Number of rows, m = ")) 
n= int(input("Number of columns, n = ")) 
for i in range(m): 
    matrixb = [] 
    for j in range(n): 
        print("Entry in row: {} column: {}".format(i+1,j+1)) 
        matrixb.append(int(input())) 
        B.append(matrixb) 
sum=[]
sum = A.copy()
print(A)
print(B)
for i in range(m):
    for j in range(n):
        sum[i][j]=A[i][j]+B[i][j]

print(sum)