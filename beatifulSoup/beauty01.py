# 파이썬 제목만 추출해 오기 (해당페이지)~
# 본문을 구글개발자도구(f12)를 이용해서 클릭을 잘 해준다 (범위 잘 설정)

# %ED%8C%8C%EC%9D%B4%EC%8D%AC  <- '파이썬'이라는 글자의 숫자표현식??

import requests
from bs4 import BeautifulSoup

url = "https://kin.naver.com/search/list.nhn?query=파이썬"

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('ul.basic1')
    titles = ul.select('li > dl > dt > a')
    for title in titles:
        print(title.get_text())
else:
    print(response.status_code)

# 커밋을 위한 용도입니다.
