li=[]
lii=[]
print("-"*4,"MENU","-"*4,
'''
1. 콜라 / 300
2. 사이다 / 300
3. 커피 / 200
4. 돈 넣기
5. 잔돈 반환
6. 종료
--------------''')
while True:
    menu=input("메뉴선택: ") 
    if menu.isnumeric():
        menu=int(menu) 
        if menu==1:                     #메뉴 판단(1번부터 4번까지는 순서상관없이 입력하고)
            pass
        elif menu==2:
            pass
        elif menu==3:           #메뉴 복수선택 가능
            pass
        elif menu==4:                           
            pass
        elif menu==5:                       #음료선택, 돈입력을 안하고 5를 누르면
            pass
        elif menu==6:
            pass
        else:
            pass
    else:
        pass
