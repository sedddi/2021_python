import urllib.request #url에서 데이터를 가져옴
from bs4 import BeautifulSoup #html 코드를 사용하기 쉽게 파싱해주는 라이브러리
import os

#beautifulSoup 객체 생성
web = urllib.request.urlopen("https://comic.naver.com/webtoon/list?titleId=738145")
soup = BeautifulSoup(web, 'html.parser')

#이미지 저장 전 오프너 객체 생성해 헤더 추가
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

#코드 작성 시 편리를 위해 넣은 숲속의 담 파일 생성 판별 부분
cwd = os.getcwd()
files = os.listdir(cwd)

if os.path.isdir(os.path.join(cwd,  "숲속의 담")) == False: 
    os.mkdir("숲속의 담")

#파일 이동
os.chdir("숲속의 담")

#회차 목록(이름) 찾기
t_data = soup.findAll("td",{"class":"title"}) 

for t in t_data:

    t_page = urllib.request.urlopen("https://comic.naver.com" + t.a['href'])
    t_soup = BeautifulSoup(t_page, "html.parser")

    i_data = t_soup.find("div", {"class", "wt_viewer"})
    i_list = i_data.findAll("img")
    index = 1 #이미지 인덱스

    os.mkdir((t.text).strip()) #회차 목록(이름) 가져오기
    os.chdir(os.getcwd() + "//" + (t.text).strip()) #회차 목록(이름)으로 이동
    
    for i in i_list:
        urllib.request.urlretrieve(i['src'], str(index)+".jpg") #url 주소의 문서를 다운로드 하는 함수
        index += 1
    os.chdir('../')
    






