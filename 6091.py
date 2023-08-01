a,b,c=input().split()

a=int(a)
b=int(b)
c=int(c)

d=2

while 1==1:
    if d%a ==0 and d%b == 0 and d%c == 0 :
        break
    d=d+1

print(d)