#elif, else
'''
a = int(input())
if a<10:                       #콜론 꼭!!!!!
    print("1")
elif 10<=a<100:                #elif, else 활용은 자유자재!
    print("10")
else:                          #else 에는 조건이 붙지x, 조건이 붙으면 Syntax 에러 나와용
    print("100^")
'''

'''
a= int(input())
b= int(input())
if a>b:
    print(a)
elif a<b:
    print(b)
else:
    print("=")
'''
'''
Kor = int(input())
Math = int(input())
Avg = ((Kor+Math)/2)

if Avg>=80:
    print("합격!")
else:
    print("불합격ㅜㅜ")
'''

#if 만 사용한것과 elif, else를 사용한 코드의 차이는??=> 전자는 모두 실행되어 True 값 모두 실행됨.
'''
math = int(input("수학:"))
sci = int(input("과학:"))
avg = (math + sci) /2

if avg >=90:
    print("A")
elif avg >=80:
    print("B")
elif avg >=70:
    print("C")
else:
    print("D")
'''
    
'''
a = int(input("1번 수: "))
b = int(input("2번 수: "))
c = input("연산자: ")

if c == "+":
    print(a+b)
elif c =="-":
    print(a-b)
elif c =="*":
    print(a*b)
elif c =="/":
    print(a/b)
else:
    print("연산자가 이상해요")
'''

# if 종속문 내에 if 가 있을 시
'''
id = input("id:")
pw = input("pw:")

# if id =="admin":
#     if pw == "admin":
#         print("login successed!")
#     else:
#         print("wrong password!")
# else: 
#     print("account is not exist!")

'''
# id = input("id:")
# if id == "admin":
#     pw = input("pw:")
#     if pw == "admin":
#         print("login successed!")
#     else:
#         print("wrong password!")
    
# else: 
#     print("wrong id!")


'''
month = int(input("몇월?:"))

if 1<=month<3:
    print("겨울!")
elif month ==12:
    print("겨울!")
elif 3<=month<6:
    print("봄!")
elif 6<=month<9:
    print("여름!")
elif 9<=month<12:
    print("가을!")
else:
    print("입력이 바르지 않습니다.") 
'''
#pass 구문 : 아무런 동작을 하지 않음, 전체적인 틀 잡을 때 유용
#유효값을 검증하고 나서 계절판별
#계절 입력받고, 
#1. 유효값 입력했을 때 
#       -계절 판단
#2. 아닐때
#       -안내


'''
month = int(input("몇월?:"))

#계절 유효값 입력했을 때
if 1<=month<=12:
    if 3<= month <=5:
        print("봄!")
    elif 6<=month<9:
        print("여름!")
    elif 9<=month<12:
        print("가을!")
    else: 
        print("겨울")
#아닐 때
else:
    print("1~12까지의 수만 입력하세요.")
'''



'''
A = int(input("수를 입력하세요: "))
if A<0 :
    print("절대값은", -A, "입니다.")
else:
    print("절대값은", A, "입니다.")

# if A < 0:
#     A=-A
# print(A)
'''

# ap_pr = 3000
# pe_pr = 2000
# ap_qry = int(input("사과 개수: "))
# pe_qry = int(input("배 개수: "))
# my_money = int(input("내 돈: "))
# total_pr = ap_pr*ap_qry+pe_pr*pe_qry

# if my_money >= total_pr:
#     print("잔돈은", my_money-total_pr, "입니다.")
# else:
#     print("구매불가, 필요한 금액은", total_pr-my_money,"입니다.")
#사과 음수 입력시 프로그램 종료 연습





# A = int(input("수를 입력하세요: "))
# if A%15 == 0:
#     print("15의 배수입니다.")
# elif A%3 == 0:
#     print("3의 배수입니다.")
# elif A%5 == 0:
#     print("5의 배수입니다.")

'''
print("="*20)
print("1. 아메리카노")
print("2. 카페라떼")
print("="*20)
menu = int(input("메뉴선택: "))
if 1<=menu<=2:
    print("="*20)
    print("1. ICE")
    print("2. HOT")
    print("="*20)
    temp = int(input("온도 입력: "))
    if 1<= temp <=2:
        if menu ==1:
            if temp ==1:
                print("아이스 아메리카노")
            else:
                print("뜨거운 아메리카노")
        else:
            if temp ==1:
                print("아이스 카페라떼")
            else:
                print("뜨거운 카페라떼")
else:
    print("올바른 메뉴를 입력하세요.")
'''


'''
#메뉴유효
#   -온도 입력
#   1-1온도 유효
#   -선택메뉴 출력
#   1-2 유효x
#       -안내
#유효x
#안내
오늘 복습하세요!!
'''
# pw 3번틀리면 프로그램 종료하는 프로그램 만들어봐라

    
# ap_pr = 3000
# pe_pr = 2000
# ap_qry = int(input("사과 개수: "))
# pe_qry = int(input("배 개수: "))
# my_money = int(input("내 돈: "))
# total_pr = ap_pr*ap_qry+pe_pr*pe_qry

# if my_money >= total_pr:
#     print("잔돈은", my_money-total_pr, "입니다.")
# else:
#     print("구매불가, 필요한 금액은", total_pr-my_money,"입니다.")

'''
N = int(input("오늘은 몇일 째?:"))
if N%4 == 1:
    print("A")
elif N%4 == 2:
    print("B")
elif N%4 == 3:
    print("C")
else:
    print("D")
'''

'''
n = int(input("후 일을 입력하세요: "))
if n%7 == 0:
    print("화요일")
elif n%7 == 1:
    print("수요일")
elif n%7 == 2:
    print("목요일")
elif n%7 == 3:
    print("금요일")
elif n%7 == 4:
    print("토요일")
elif n%7 == 5:
    print("일요일")
else:
    print("월요일")
'''

'''
year = int(input("연도를 입력하세요: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("윤년입니다!")
else: 
    print("윤년이 아닙니다!")
'''
'''
kor = int(input("국어점수를 입력하세요: "))
if 0<=kor<=100:
    math = int(input("수학점수를 입력하세요: "))
    if 0<=math<=100:
        avg = (kor+math)/2
        if avg>=90:
            print("PERFECT!!")
        elif avg >=80:
            print("GREAT!!")
        else:
            print("SOSO...")
    else:
        print("수학점수 이상!!")
else:
    print("국어점수 이상!!")
'''

#국어점수 유효
#   -수학점수 입력
#   수학점수 유효
#       -결과 출력
#   수학 유효x 
#       -프로그램 종료
#국어점수 유효x 
#   -프로그램 종료


