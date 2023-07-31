a,b,c,d=input().split()

a=int(a)
b=int(b)
c=int(c)
d=int(d)

i=0

s=a

for i in range(1,d):
    s=(s*b)+c
print(s) 