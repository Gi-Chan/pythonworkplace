import requests
from selenium.webdriver.common.by import By
from selenium import webdriver



max_cnt = 20
keyword = 'wallpaper'
url=f'https://www.pexels.com/ko-kr/search/{keyword}/'

browser = webdriver.Chrome()
# browser.maximize_window()
browser.get(url)

photo_items = browser.find_elements(By.CLASS_NAME, 'BreakpointGrid_item__erUQQ')
img_urls = [x.find_element(By.TAG_NAME, 'img').get_attribute('src') for x in photo_items]

idx=1
for img_url in img_urls:
    browser.get(img_url)

    res = requests.get(img_url)
    if res.ok:
        file_name = f'{keyword}_{idx}.jpeg'
        with open(file_name, 'wb') as f:
            f.write(res.content)
        print(f'({idx}) {file_name}')
        idx+=1
        
    if idx > max_cnt:
        break
browser.quit()

