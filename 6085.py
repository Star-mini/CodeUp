a,b,c=input().split()

a=int(a)
b=int(b)
c=int(c)

s=a*b*c/8/1024/1024

#print(round_num, "MB")

print("{:.2f} MB".format(s))
