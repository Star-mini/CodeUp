a,b=input().split(" ")

a=int(a) 
b=int(b) 

a=bool(a)       #불리안으로 만들기
b=bool(b)

if a&b == True :
    print("True")
else:
    print("False")
    
