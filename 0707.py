#출력은 문자, 숫자 혼합 가능
print("제 나이는",28, "입니다.")

print(1, end=" ")
print(3.23,end="\t")
print(32.23,end=" ")
print("dd","ss","dd")
#sep=""(구문 사이 띄어쓰기 삽입)
#end=""(구문 마지막 줄바꿈, 추가 설정 없을 시.)
#sep: string inserted between values, default a space.
#end: string appended after the last value, default a newline.



#주석 
# print(1) #1출력(한 줄 주석)
#"ctrl + /" 여러줄 주석 처리

#여러 줄 문자열(한 줄 주석과 달리 실행에 관여하는 자료)
print('''
동해물과
백두산이
''')

print("""마르고
닳도록""")



("sdfsdfsdf")
"""sdfsdfsffsd"""

print()

# 노래가사 여러줄 문자열로 출력하기
print("백예린","Square")

print(""""Come on let's go to bed
We gonna rock the night away
Who did that to you, babe
If you're not in the right mood to sleep now then
Come on, let's drink and have very unmanageable day
Would you want me in, bae
If you're not in the right mood to sleep now then
Come, take my arms and go
I'll be yours for sure" """)
print()


#변수
# 변수에 값 대입
# 대입연산자 : 오른쪽에 있는 값을 왼쪽으로 대입, 
# 특성까지 옮겨간다.(Python 에만 해당)
# x(변수) = 10(값)
# x == 정수형 자료
# 문자열 밖에 있어야 함 print("x의 값은", x , "입니다.")

x=10
print(x)
print("x의 값은", x , "입니다.")

y="hello"
print(y)


d = 1+2
e = 3
print(e*d) #3*1+2 라고 해서 5가 되는 것이 아닌 1+2의 결과를 e 와 연산하기 때문에 결과는 9

#예약어 : python에서 특수한 역할을 하는 키워드(변수 사용 금지)

import keyword #예약어 리스트 불러오기
print(keyword.kwlist)
#함수는 변수로 사용하지 말기!

name = "나지원"
age = 28
email = "najiwon1106@gmail.com"

print(' '"이름:",name, "\n", "나이:", age, "\n", "이메일:",email)


#에러 학습
# 1) SyntaxError : 문법오류(오타)
# 2) NameError : 선언되지 않은 변수 사용
# 3) IndentationError : 띄어쓰기 관련 에러




#연산자
# type(자료)

print(type(1)) #int
print(type(3.2)) #float
print(type(3-2j)) #complex
print(type("hello")) #str

#함수 안에 함수 : 안쪽부터 실행!



# #연산자
# a = 10
# b = 3

# # b=0 일시 ZeroDivisionError: division by zero
# print(a+b) #합
# print(a-b) #차
# print(a*b) #곱
# print(a/b) #분
# print(a//b) #몫
# print(a%b) #나머지 
# print(a**b) #제곱
# print((a+a)*b) #()를 이용하여 우선계산 할 수 있음
# print()


# A = "Hello" 
# B = "World!"
# print("A는", A, "입니다.")
# print("B는", B, "입니다.")
# print()
# print("A+B = ",A+B)
# # print("A-B = ",A-B)
# # print("A*B = ",A*B)
# # print("A/B = ",A/B)
# # print("A//B = ",A//B)
# # print("A%B = ",A%B)
# # print("A**B = ",A**B)
# print((A+B)*3)

A= "대한독립"
B= "만세"
C= "~"

D = A + " " + B*3+C*3
print(D)

print(9%2)

# %연산자 활용
# 짝수%2 = 0, 홀수%2 = 1 

# A 가 B 의 약수다.
# B % A = 0 

# A 가 B 의 배수다.
# A % B = 0


# N 개 상황 규정
# %상황


print()

a=564
print(a//100) # a를 100으로 나눈 몫
print(a//10%10) # a 를 10으로 나눈 몫 56을 10으로 다시 나눈 후의 나머지 6
print(a%10) # a를 10으로 나눈 나머지 4

print()

b=1234
print(b//1000)
print(b//100%10)
print(b//10%10)
print(b%10)

