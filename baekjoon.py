#1

'''print("Hello World!")
'''

#2


#print('''강한친구 대한육군
#강한친구 대한육군''')

#3

# print('''\\    /\\
#  )  ( \')
# (  /  )
#  \\(__)|''')


# #4
# print("|\\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`    |")
# print("||_/=\\\\__|")



#5
'''A, B = map(int,input().split())
print(A+B)'''


#6
'''A, B = map(int,input().split())
print(A-B)'''


#7
'''A, B = map(int,input().split())
print(A*B)'''


#8
'''A, B = map(int,input().split())
print(A/B)'''

#9
'''A, B = map(int,input().split())
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A%B)'''

#10
'''id = input()
print(id+"??!")'''

#11
'''y = int(input())
print(y-543)'''

#12
# A, B, C = map(int,input().split())
# print((A+B)%C)
# print((A%C)+(B%C)%C)
# print((A*B)%C)
# print((A%C)*(B%C)%C)

#13



#
'''
li = [2,3,2,45,2]
lii = [4,5,6,3,2,4]
for i in li:
    for x in lii:
        print(i*x)
'''

# word =input()
# if reversed(word)==word:
#     print(1)
# else:
#     print(2)
# word = input()
# # 문자열 처음부터 끝까지 -1(거꾸로)[start : stop : step] 슬라이싱 이용!
# if word[::-1]==word:
#     print(1)
# else:
#     print(0)


# t=int(input())
# yl=[]
# kl=[]
# for _ in range(t):
#     for i in range(1,10):
#         y,k=map(int,input().split())
#         yl.append(y)
#         kl.append(k)
#     if sum(yl)>sum(kl):
#         print("Yonsei")
#     elif sum(kl)<sum(yl):
#         print("Korea")
#     else:
#         print("Draw")

# cs=input()
# if cs=="A+":
#     print(4.3)
# elif cs=="A0":
#     print(4.0)
# elif cs=="A-":
#     print(3.7)
# elif cs=="B+":
#     print(3.3)
# elif cs=="B0":
#     print(3.0)
# elif cs=="B-":
#     print(2.7)
# elif cs=="C+":
#     print(2.3)
# elif cs=="C0":
#     print(2.0)
# elif cs=="C-":
#     print(1.7)
# elif cs=="D+":
#     print(1.3)
# elif cs=="D0":
#     print(1.0)
# elif cs=="D-":
#     print(0.7)
# else:
#     print(0.0)

#1.그릇은 10cm
#2.(( -5
#3. ()은 그대로 *2

# def solve(a):
#     return sum(a)

# print(solve(1,2))


def d(n):
    n=str(n)
    s=0
    for i in n:
        i=int(i)
        s+=i
        return s+int(n)
print(d(100))