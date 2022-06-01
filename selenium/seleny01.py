from urllib.parse import quote_plus
import time

# 여기부터
from selenium import webdriver
import chromedriver_autoinstaller

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

driver.implicitly_wait(10)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# 여기까지는 크롬드라이버의 버전을 알아서 관리해 준다. 편하다


# 여기서 kword를 입력하면 알아서??  -> 맞다
# Run창에  검색어 입력해주면 해당 검색어를 입력하고 나서 스샷 찍음
# 그다음 save_screenshot에 path까지 입력하거나 저장될 이름 입력해주면 된다.

driver.get('http://naver.com')
url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
kword = input('검색어를 입력 :')
base_url = url + quote_plus(kword)

driver.get(base_url)
time.sleep(1)
driver.save_screenshot('website.png')