from selenium import webdriver
import time

path = "C:/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://zzzscore.com/1to50/")#사이트 이동
btn = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]') #TypeError: 'WebElement' object is not iterable떠서 s붙임
#버튼 값 모두 가져옴

num = 1#순서대로 버튼 누르기 위한 num 변수

for i in range(1,51):#50까지 반복
    for j in btn:
        if j.text == str(num):#가져온 버튼 text와 num 값이 같으면
            j.click()#누름
            print(str(num)+"클릭")#누른 버튼 출력
            num += 1#num 값 증가




