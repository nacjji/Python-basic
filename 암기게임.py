# 1. 숫자 다섯자리(easy) 난이도에 맞춰 깜빡거린다. 
# 2. 입력하기!
# 3. 기회는 3번 
# 4. 10번 맞출때마다 기회가 한 개씩 늘어남



# 1. 난이도 설정
#    -easy : 5자리 1초
#    -normal : 6자리 0.7초
#    -hard :  7자리 0.5초
# 2. 랜덤하게 숫자를 출력시킴(time.sleep(n)쓰기)
# 3. 입력한 숫자가 제시된 숫자와 일치할 경우 카운트 1
#    -5초 안에 입력안하면 하트-1

# 4. 연속되게 맞춰 카운트가 10이 되면 하트 +1
# 5. 틀릴경우 하트 초기화 


import random
import time
import os
while True:
    life = 3
    cnt = 0
    score = 0
    print( f"easy : 5자리, 1초\nnormal : 6자리,0.8초,점수 2배\nhard : 7자리, 0.7초, 점수 3배")
    print("10배수 콤보마다 LIFE + 1, SCORE 1000 점!!!")
    level= input("난이도를 선택하세요.easy(1)/normal(2)/hard(3) >>>")
    while True:
        if level=="1":
            n = random.randint(11111,99999)
        elif level=="2":
            n = random.randint(111111,999999)   
        elif level =="3":
            n = random.randint(1111111,9999999)
        else:
            print("올바른 난이도를 입력하세요")
        os.system("cls")
            
        #게임플레이!

        #현황판
        print("♥"*life) 
        print(f"score:{score}")
        print(f"{cnt} COMBO!!!")
        print("="*40)


        print(n)
        print("지금은 입력하지 마세요!!")
        if level =="1":
            time.sleep(1)
        elif level =="2":
            time.sleep(0.8)
        else:
            time.sleep(0.7)
        os.system("cls")
        print("♥"*life)
        print(f"score:{score}")
        print(f"{cnt} COMBO!!!") 
        print("="*40)  
        ans=input("뭐였게~?>>>")
        os.system("cls")
        if ans.isnumeric():
            ans=int(ans)
            if ans == n:
                cnt+=1
                score +=100
                if cnt%10==0:
                    life+=1
                    score+=1000
                    print("="*40)
            elif ans!=n:
                cnt=0
                life-=1
                print("♥"*life) 
                print(f"score:{score}")
                print(f"{cnt} COMBO...")
                print("="*40)  
                print("땡!")
                time.sleep(1)
                os.system("cls")

                if life==0:
                    print("GAME OVER!")
                    if level=="1":
                        print(f"EASY 모드, 당신의 점수는 {score} 입니다.")
                    elif level=="2":
                        print(f"NORMAL 모드, 당신의 점수는 {score*2} 입니다.")
                    else:
                        print(f"HARD 모드, 당신의 점수는 {score*3} 입니다.")
                    
                    re_game = input("다시 도전하시겠습니까? y/n : ")
                    if re_game == "n":
                        break
                    else:
                        os.system("cls")
                        break
        else:
            cnt=0
            life-=1 
            print("♥"*life) 
            print(f"score:{score}")
            print(f"{cnt} COMBO...")
            print("="*40) 
            print("제대로 입력하세요!")
            time.sleep(1)