a=input()

a=int(a)

i=0

for i in range(1,a+1):
    if (i % 10) ==3 :
        print("X")
    elif (i % 10 )== 6:
        print("X")
    elif (i % 10 )== 9:
        print("X")
    else:
        print(i)