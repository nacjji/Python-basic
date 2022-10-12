# t = int(input("몇 회 입력하시겠습니까?: "))
'''
for i in range(t):
    n = int(input("수 입력:"))
    if n%2==0:
        print(n,"은","짝수")
    if n%2!=0:
        print(n,"은","홀수")
'''
'''li=[]
for i in range(t):
    n = int(input("수 입력"))
    li.append(int(n))
for i in li:   #위에서 입력받고 생성된 리스트를 반복
    if i%2==0:
        print(i,"짝")
    else:
        print(i,"홀")'''
'''
li=[]
for i in range(t):
    n = int(input("수 입력"))
    li.append((n))
for i in li:


    a = int(input("연산자 입력(덧셈:1 뺄셈:2)"))
    li.append(i)
    if a==1:
        print(sum(n))


for i in range(t):
    for i in range(t):
        a= int(input())
        b= int(input())
        op=int(input("연산자:"))

        if op==1:
            print(a,"+",b,"=",a+b)
        elif op ==2:
            print(a,"-",b,"=",a-b)
        else:
            print("연산자 오류!")
print("="*40)
'''

# a= int(input("점수1: "))
# b= int(input("점수2: "))
# c= int(input("점수3: "))
# d= int(input("점수4: "))
# e= int(input("점수5: "))

'''li =[]
t = int(input("학생 수:"))
for i in range(t):
    li.append(int(input("수 입력:")))
    avg=(sum(li)/len(li))
print("5과목 평균:", avg)
for i in li: #위 리스트가 반복되며 하나의 숫자열로 나열되면
    if i <= avg: #나열된 수가 평균보다 낮을 시
        print(i,"평균이하") #i 가 출력된다.'''
    
#약수 관련 문제!
'''
n = int(input("수:"))

for i in range(1,n+1):
    if n%i==0:
        print(i,"약수")
    else:
        print(i,"약수x")

li = [] 
for i in range(1,n+1):
    if n %i==0:
        li.append(i)
print(li)
''''''
n = int(input("수:"))

1.
li = [] 
for i in range(1,n+1):
    if n %i==0:
        li.append(i)
print(li) 
[1,2,3,6]


2. 
li = [] 
for i in range(1,n+1):
    if n %i==0:
        li.append(i)
    print(li)
[1]
[1,2]
[1,2,3]
[1,2,3]
[1,2,3]
[1,2,3,6]


3. 
li = [] 
for i in range(1,n+1):
    if n %i==0:
        li.append(i)
        print(li)
[1]
[1,2]
[1,2,3]
[1,2,3,6]

# 반복, if 종속 프린트는 리스트에 담길때마다 출력'''

'''
a = int(input("수 입력:"))
li = []
for i in range(1,a+1):
        if a%i==0:
            li.append(i)        
if len(li)<=2:
    print("소수")
else:
    print("소수x")
'''
'''
if sum(li) == 1+a:
    print("소수")
if li == [1,a]:
    print("소수")
if li[1]==a:
    print("소수")
'''
'''
li2 = []
for i in range(1,N+1):
    if N % i == 0:
        li2.append(i)

if li2 == []:
    print(N, "소수")
if len(li2) == 0:
    print(N, "소수")
if sum(li2) == 0:
    print(N, "소수")
'''
#완전수 구하는 문제(자기 자신을 제외한 약수들의 합이 자기 자신인 수 6,28,496...)
'''
a = int(input("입력:"))
li=[]
for i in range(1,a+1):
        if a%i==0:
            li.append(i)
if sum(li)-a==a:
    print("완전수")
else:
    print("완전수x")
'''

'''li= []
lii=[]
n = int(input())
for i in range(1,n+1):
    if n%i==0:
        if i %2==0:
            li.append(i)
        else:
            lii.append(i)

if len(li)<len(lii):
    print("호올수")
else:
    print("짜악수")'''

#약수 중 두자리수 약수의 개수
#  30
# 123 10 


'''
li = []
lii= [] 
n= int(input())
for i in range(1,n+1):
    if n%i==0:
        if i>=10:
            li.append(i)
        else:
            lii.append(i)
if len(li)>len(lii):
    print(n,"십수")
else:
    print(n,"십수x")

'''
'''
li = []
lii= [] 
n= int(input())
for i in range(1,n+1):
    if n%i==0:
        li.append(i)
if sum(li)%2==0:
    print("쨕수")
else:
    print("쨕수x")

'''


#약수 중 홀수를 뽑아라!



# if li%2==0:
#     print(li,"짜악수")
# else:
#     print(li,"호올수")








'''약수 중 두 번째 약수가 짝수, 세 번째 약수가 홀수인 수를 '홀짝수' 라고 합니다.
 N 을 입력받고 '홀짝수' 인지 판단하는 코드를 짜주세요!


약수 중 세 번째 약수에 2 를 곱했을 때 네 번째 약수가 되는 수를 
"뭐라고불러야할지모르겠수" 라고 하겠습니다. 
N 을 입력받고 "뭐라고불러야할지모르겠수" 
인지 판단하는 코드를 짜주세요'''

#약수가 4개인 애들은 판단이 안됨!!




'''문자열을 for 로 돌렸을 때는 문자하나하나가 i 에 들어가서 for 문이 돌게됩니다. 이 점을 참고하시고 다음문제를 해결해보세요

====================================================
o 는 1점, x 는 0점이다. 만약 o 가 연속으로 등장할 경우 점수가 배가되어 계산된다고 한다. 하지만, 중간에 x 를 만나게 되면 
배수가 끊겨버린다.

ex) oxooxxox  >  1 + 1 + 2 + 1  > 5 점
    xoooxooxx  >  1 + 2 + 4 + 1 + 2 > 10 점
    oooooxoxxx  >  1 + 2 + 4 + 8 + 16 + 1 > 32 점
====================================================

Q. 문자열(ox) 를 입력받고 점수를 계산하여 출력하는 프로그램을 작성하세요'''


'''
a = input("입력:")
li=[a]
for i in li:
    if li[0] and li[1]=="o":
        print(1+2)'''

'''n=int(input("input:"))
li=[]
lii=[]
for i in range(1,n+1):   
    if n%i==0:
        if i%2==0:
            li.append(i)
        else:
            lii.append(i)
if len(lii)>len(li):
    print(li,lii,"호올수")
elif len(lii)<len(li):
    print(li,lii,"짜악수")
else:
    print(li,lii,"가앝은수")'''


'''n= int(input("input:"))
li=[]
lii=[]
for i in range(1,n+1):
    if n%i==0:
        if i>=10:
            li.append(i)
        else:
            lii.append(i)
if len(lii)<len(li):
    print(li,lii,"sipsu")
elif len(lii)>len(li):
    print(li,lii,"no sipsu")
else:
    print(li,lii,"same su")'''


'''n= int(input("input:"))
li=[]
lii=[]
for i in range(1,n+1):
    if n%i==0:
        li.append(i)
if sum(li)%2==0:
    print(sum(li),"jjaksu")
else:
    print(sum(li),"holsu")'''

'''
n=int(input("input:"))
li=[]
for i in range(1,n+1):
    if n%i==0:
        li.append(i)
if len(li)>2:
    if li[1]%2==0 and li[2]%2==1:
        print(li,"holjjaksu")
    else:
        print(li,"holhol su")
else:
    print(li,"sosu")'''


n=int(input("input:"))
li=[]
for i in range(1,n+1):
    if n%i==0:
        li.append(i)
if len(li)>3:
    if li[2]*2==li[3]:
        print(li,"i dont know what to call number")
    else:
        print(li,"just number")
else:
    print(li, "just number")