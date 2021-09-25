import random # 게임에서 답을 랜덤으로 지정하기 위해
import time #시간정보 가져오기 위해
import os.path #파일의 존재여부 확인

#기록 확인에 필요한 두 변수만 전역으로 지정
recordNum=[] #점수기록 리스트
recordName=[]#닉네임 기록 리스트
recordTime=[]#시간 기록 리스트
best = 22 #최고 기록 초기화 - 최고기록으로 나올 수 없는 불가능한 숫자로 초기화
file='C:/Users/user/Desktop/record.txt' #경로 수정 가능

if os.path.isfile(file): #record.txt 파일 존재 한다면
    f=open('record.txt','r') #파일 열기
    record=f.read()
    print(record)
    f.close()

while(1):
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료")
    choose = int(input(">>"))#게임 메뉴 선택
    answer = random.randrange(1, 101, 1)#답은 게임에서 랜덤으로 지정
    num = -1
    t = 1 #시도 횟수
    mini = 1 #최소 범위
    maxi = 100 #최대 범위

    #게임 시작
    if choose==1:

        for i in range(1,11):#최대 기회는 10번
            num = int(input("%d번째 숫자 입력(%d~%d) : " %(t, mini, maxi)))

            if num<1 or num>100:#숫자 범위가 1~100이 아닐 때
                print("숫자 범위는 1에서 100까지입니다.")
                break
            
            elif answer > num: #정답이 입력값보다 클 때
                print("UP")
                t += 1 #시도횟수 1증가
                if mini < num: #피드백1
                    mini = num+1 #최소 범위 수정

            elif answer < num: #정답이 입력값보다 작을 때
                print("DOWN")
                t += 1 #시도횟수 1증가
                if maxi > num:#피드백1
                    maxi = num-1 #최대 범위 수정

            elif answer == num: #정답이 입력값과 같을 때
                print("정답입니다!!")
                print("%d번째만에 맞추셨습니다" %t)
                
                #최고 기록은 전 최고기록만을 비교하면 됨
                if t<best: #현 기록이 전 최고기록보다 작을 때
                    recordNum.append(t)#점수 기록 리스트에 추가 + 피드백2
                    print("최고기록 갱신~!") #최고기록 갱신
                    name = input("닉네임을 입력하세요 >> ")
                    recordName.append(name)#이름 기록 리스트에 추가
                    recordTime.append(time.strftime('%Y-%m-%d', time.localtime(time.time())))
                    
                break


    #기록 확인
    elif choose==2:
        for i in range(0,len(recordNum)):
            recordNum.sort()
            print("%d %s %d %s" %(i+1, recordName[i], recordNum[i], recordTime[i]))
            
    #게임 종료    
    elif choose==3:
        print("게임을 종료합니다.")
        f = open('record.txt','w',encoding="utf8") #파일 열고
        for i in range(0,len(recordNum)):
            recordNum.sort()
            data = ("%d %s %d %s" %(i+1, recordName[i], recordNum[i], recordTime[i]))
        f.write(data) #쓰기
        f.close() #닫기
        break
        
    else:
        print("게임 메뉴는 1, 2, 3만 존재합니다.") #피드백3
        

