
a=input()

b=input().split()

a=int(a)

for i in range(a):
    b[i]=int(b[i])

c=[0]*25

for i in range(1,25):
    for j in range(a):
        if b[j]==i :
            c[i]=c[i]+1


for i in range(1,24):
    print(c[i],end=' ')




#내가 생각한 원리인데 그걸 컴퓨터가 연산할수있도록 코딩하자
'''
n = int(input())
b = list(map(int, input().split()))

c = [0]*24  # 24명의 학생에 대한 정보를 담을 수 있는 리스트를 생성

for i in b:
    c[i] += 1

for i in range(1, 24):  # 1부터 23까지만 출력하도록 범위를 지정
    print(c[i], end=' ')
'''