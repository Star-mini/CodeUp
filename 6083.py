a,b,c=input().split(" ")

a=int(a)
b=int(b)
c=int(c)

i,j,k = (0,0,0)

'''
i, j, k = [0, 0, 0]
i, j, k = [0] * 3
i, j, k = (0, 0, 0)`
i = j = k = 0
'''

for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i, j, k)

print(a*b*c)