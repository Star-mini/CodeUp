a=input()

b=input().split()

a=int(a)

for i in range(a):
    b[i]=int(b[i])

for i in range(a-1,0-1,-1):
    print(b[i],end=' ') 