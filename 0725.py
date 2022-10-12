#함수
# 함수 형태
'''
def [name]("입력값1","입력값2"):
    ["기능 구현"]
    return["반환값"]
'''
#선언부
'''def add(a,b):
    return a+b
#사용부
x= add(10,20)'''

#입력값의 개수, 반환값이 뭐하는지 잘 잡자

#두수의 곱을 구해주는 함수
'''
def times(a,b): #입력값 개수 2개
    return a*b  #반환값은 a와 b를 곱함

print(times(10,10))

'''


# 두 수의 차이를 구해주는 함수
'''def diff (a,b):
    return abs(a-b)

print(diff(30,20))'''


#약수를 구해주는 함수
# li=[]
# def yak(a):
#     for i in range(1,a+1):
#         if a%i==0:
#             li.append(i)
#     return li


# n 입력 , 소수인지 판단(함수)

'''
n=int(input())

def sosu(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=1
    if s==2:
        print("소수")
    else:
        print("소수 x")    

print(sosu(n))'''

#문자열 함수
'''
a = int(input())

def holsu(a):
    for i in str(a):
        if int(i)%2==0:
            return False
    return True
print(holsu(a))
'''
'''
name = input()
def filter(name):
    for i in "?*:<>|/\\\"":
        name = name.replace(i,"")
    return name
print(filter(name))
'''

# # Q7. 문자열과 필터리스트를 입력값으로 받고 해당 문자를 * 로 처리해주는 함수
# # 필터("hello",["l","h"])   >   *e**o
# # 필터("kennen123",["n","2"]) > ke**e*1*3
# name = input()
# filter = input()
# li=[filter]
# def trans(name, filter):
#     for i in li:
#         name = name.replace(i,"*")
#     return name
# print(trans(name))

'''
def letter(sent, lett):
            
    return sent[:lett]+"..."

print(letter("hello everyone",5), )
'''
#함수의 장점: 간결성, 재사용성
'''
1. 반환값 없을 수도 있다. none
2. 함수 ()안쓰면 사용하는게 아니다. ()안쓰면 함수가 존재하는지.
3. print()함수에 대한 이해 
'''

#유효값 입력함수

#class!! (중요!!!!!!)

# class는 객체를 생성하기 위해 만듦

#필드 : class 안의 변수 (어떤 대상이 가지고 있는 속성) 

#메서드 : class 안의 함수(어떤 대상이 할 수 있는 행동)
# A는 객체, A는 모험가 class 의 인스턴스(o)
# A 는 인스턴스, A는 모함가 class 의 객체(x)
#  모험가 class 의 인스턴스에 점찍으면 모험가 class의 메서드/필드에 접근할 수 있음
'''
class advent():
    pass 
    def walk():
        pass
a = advent()
'''

#클래스는 대문자! 개발자들끼리의 약속이에요
# class Maple:
#     strong = 10

# def add():
#     return 10

# a = Maple()
# b =add()
