'''
n = int(input("몇일 째?: "))
a = n%4
if a == 1:
    print("오늘은 A!")
elif a == 2:
    print("오늘은 B!")
elif a == 3:
    print("오늘은 C!")
else:
    print("오늘은 D!")
'''
'''
n = int(input("몇일 후?:"))
b = n%7

if b == 0:
    print("월M!")
elif b ==1:
    print("화T!")
elif b ==2:
    print("수W!")
elif b ==3:
    print("목T!")
elif b ==4:
    print("금F!")
elif b ==5:
    print("토S!")    
else:
    print("일S!")
#FTMFMTMT
'''
'''
year = int(input("올해는 몇년도?:"))

if year%4==0 and year%100!=0 or year%400==0:
    print("윤년입니다!") 
else:
    print("윤년이 아닙니다!")

if year %400 ==0:
    print("윤년")
elif year%100 == 0:
    pass
elif y%4 == 0:
    print("윤년")
'''
#FFTFTF
#1 26765 06002 28229 40149 67032 05376
'''
c= float(input("섭씨:"))
print(c*(9/5)+32)
'''
'''
h = int(input("시"))
m = int(input("분"))
s = int(input("초"))

hs = h*3600
ms = m*60

hms = hs+ms

print(hms+83720)
'''
'''
hms = int(input())
'''
'''
hms//60+
'''
#116420


# 반복문 for!
'''
for - 반복횟수 명확
while - 반복횟수 명확x 
'''

#리스트, 튜플!
'''
대괄호: 리스트
소괄호: 튜플

'''
'''
li = [1,]
tu = ("hello",)
print(type(li))
print(type(tu))
'''
#subscriptable = 연속적임, 자료마다 번호표가 있다.(index!!!, 0 부터 시작!!!!!!)
#iterable

#str list tuple 만 순서가 있음!!
#인덱싱 : index 를 활용하여 자료에 접근
# 리스트, 튜플 [index]
#index error
#-indexing은 왜 1부터 시작?

'''
li = [1,2,3]
li[0] = "one"
print(li)
# 인덱싱 변형 가능!

tu=(1,2,3)
tu[0] = 10
# 변형 불가능!!
'''
'''
li = []
# li.append(1)
# print(li)
# li.append("hello")
# print(li)

#1. ★★★★★자료 추가(맨뒤)
#2. list.append(x)      <--- x 가 맨 뒤에 추가된다!!
#3. 자료추가(원하는 위치)
#-list.insert(idx,x) idx에 x 추가
li.insert(0,True)
print(li)
li.insert(1,10)
print(li)

#  자료제거(원하는 위치)
#list.pop(idx)    idx 위치의 자료가 제거 및 반환(idx default 맨뒤)
li.pop(0)
print(li)

# 자료 개수 세기 list.count(x)
li1=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(li1.count(1))

# 특정 자료 인덱스 구하기
# list.index(x)

#정렬 list.sort(), 자료형태가 동일한 경우만 사용가능


#리스트 뒤집기 list.reverse()
#리스트 비우기 list.clear()

'''


'''
#사용자에게 입력받은 단어를 삭제하는 프로그램!!
d = ["apple","banana","air","marvel"]
user = input("삭제할 단어: ")
idx = d.index(user)
d.pop(idx)
print(d)
'''



'''

# ✨✨✨✨ 1. 자료추가 (맨뒤)
# 리스트.append(x)   x가 맨뒤에 추가
li.append(1)
print(li)
li.append('hello')
print(li)

# 2. 자료추가 (원하는 위치)
# 리스트.insert(idx, x)   idx(인덱스) 에 x 추가
li.insert(0, True)
print(li)
li.insert(2, 10)
print(li)

# 3. 자료제거 (원하는 위치)
# 리스트.pop(idx)    idx 위치의 자료가 제거 및 반환  (idx default 맨뒤)
x = li.pop(0)
print(x, "가 제거된 리스트", li)


# 4. ✨ 자료개수세기
# 리스트.count(x)    리스트 내의 x 의 개수 반환
li1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]
print( li1.count(1) )


# 5. 특정 자료 인덱스 구하기
# 리스트.index(x)    자료 x 의 인덱스 반환
l = ["hello", 1, False, 1.2]
print(l.index(1.2))


# d = ["apple", "banana", "air", "marvel"]
# print(d)
# # 사용자에게 단어를 입력받고, 해당단어를 리스트에서 제거하는 프로그램!!
# user = input("삭제할 단어 : ")
# idx = d.index(user)
# d.pop(idx)
# print(d)

# 6. 정렬 
# 리스트.sort( )    단, 자료형태가 동일한 경우에만 사용가능!!
li = [6,1,2,3,8,4,8,19,12,7,21,8,]
li.sort()
print(li)

li = ["가", "磨", "@", "=", "?"]
li.sort()
print(li)

# 7. 뒤집기
# 리스트.reverse()
li.reverse()
print(li)

# 8. 비우기
# 리스트.clear()
li.clear()
print(li)
'''

#sum, len
'''
# li = [1,2,3,4,5,6,6,1,23,5]
print(sum(li)) # list에 숫자열만 사용!
print(len(li))
#list 평균 구하는 공식 sum()/len()
#iterable == 반복가능함!!!
print(sum(li)/len(li))
'''
#for [] in []:
#range(start,stop,step)


# 0~23
# 10~83
# 21 24 27 
# for i in range(1,1001):
#     print(i)



'''#역방향 반복!!!
n = int(input("수:"))
for i in range(n,0,-1):
    print(i)
'''

'''a= int(input("입력1: "))
b= int(input("입력2: "))
for i in [a,b]:
    if a<b:
        i[0] = str(a-1)
        print(i)
           '''
        
# range(n+1,m):
# range(n-1,m,-1):

#1. n,m 입력
#2. 반복문 변수 선언 n,m 사이의 수 
#3. n>m일 시 n-1,m,-1
#4. n<m일 시 n+1


'''li = [1,2]
li[0]=2
print(li)'''


'''math, sci = map(int,input("math: , science: ").split())
li=[math,sci]
avg = sum(li)/len(li)
if avg>=90:
    print(avg,"A")
elif avg>=80:
    print(avg,"B")
elif avg>=70:
    print(avg,"C")
else:
    print(avg,"D")'''


# a, b = map(int,input("input:").split())
# c = int(input("연산자 입력: "))

# li = []
# for i in li:
#     a, b, c =map(int,input().split())
#     li.append(i)
# print(li)


'''a, b =map(int,input().split())
c = input()
if c=="+":
    print(a,"+",b,"=",a+b)
elif c == "-":
    print(a,"-",b,"=",a-b)
elif c=="*":
    print(a,"x",b,"=",a*b)
elif c=="/":
    print(a,"/",b,"=",a/b)
else:
    print("연산자가 이상해요")
'''

# a = int(input())
# b = int(input())
# li=[a]
# lii =[b]
# li.reverse()
# lii.reverse()
# print(li,lii)

# 123 = 321

a= int(input())
for i in range(1,a+1,-1):
    print(i)

