a,b,c,d=input().split()

a=int(a)
b=int(b)
c=int(c)
d=int(d)

s=a*b*c*d/8/1024/1024

round_num=round(s,1)

print(round_num, "MB")