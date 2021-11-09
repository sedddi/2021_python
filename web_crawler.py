import urllib.request #url에서 데이터를 가져옴
from bs4 import BeautifulSoup #html 코드를 사용하기 쉽게 파싱해주는 라이브러리

#beautifulSoup 객체 생성
web = urllib.request.urlopen('http://www.swu.ac.kr/www/swuniversity.html')
soup = BeautifulSoup(web, 'html.parser')

print("*** 서울여자대학교 학과 및 홈페이지 정보 ***")
print("학과\t\t\t\t홈페이지")

a_data = soup.findAll("a")


for i in a_data:
    #자율전공학부, 기초교육원, 대학원 제외
    if i.text == "자율전공학부" or i.text == "교양대학" or "대학원" in i.text:
        continue
    
    else:
        #가져올 애들에 대한 beautifulSoup 객체 생성
        h_page = urllib.request.urlopen("http://www.swu.ac.kr" + i['href'])
        h_soup = BeautifulSoup(h_page, 'html.parser')
        h_data = h_soup.find('a',{"class":"btn btn_xl btn_blue_gray"})

        if h_data:
            #홈페이지 존재하면 학과, 홈페이지 출력
            if "홈페이지" in h_data.text:
                print(i.text + "\t\t\t" + h_data['href'])
            #홈페이지 존재하지 않으면 '홈페이지가 존재하지 않음' 문구 출력
            else:
                print(i.text + "\t\t\t" + "홈페이지가 존재하지 않음")
        

        


