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
            menu=300
            print("콜라를 선택합니다.")
            li.append(menu)
        elif menu==2:
            menu=300
            print("사이다를 선택합니다.")
            li.append(menu)
        elif menu==3:           #메뉴 복수선택 가능
            menu=200   
            print("커피를 선택합니다.")
            li.append(menu)
        elif menu==4:                           
            money=input("돈을 넣어주세요:")
            if money.isnumeric():
                money=int(money)
                lii.append(money)
            else:
                print("돈을 넣어주세요.")
        elif menu==5:                       #음료선택, 돈입력을 안하고 5를 누르면
            if li and lii:
                if sum(lii)>sum(li):
                    print("거스름돈은",sum(lii)-sum(li))
                else:
                    print("잔액이 부족합니다.")
            elif li:
                print("돈을 넣어주세요.")    # 선행작업 해달라고 안내
            else:
                print("메뉴를 골라주세요.")
        elif menu==6:
            print("안녕히가세요")
            break
        else:
            print("올바른 메뉴를 입력하세요")
    else:
        print("올바른 메뉴를 입력하세요")
