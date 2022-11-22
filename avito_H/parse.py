from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                     "106.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
# options.headless = True

s = Service(executable_path="/usr/lib/chromium-browser/chromedriver")

driver = webdriver.Chrome(service=s, options=options)
url_main = 'https://www.avito.ru/moskva/kvartiry'

try:
    driver.get(url_main)
    time.sleep(15)
    print('МЭЙН')

    # Ввод суммы ОТ
    element_category1 = driver.find_element(
        By.XPATH,
        '''/html/body/div[1]/div/div[3]/div[3]/div[1]/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div/div/div/div/div
        /label[1]/input'''
    )
    element_category1.send_keys('5000000')
    time.sleep(2)
    print('ОТ')

    # Ввод суммы ДО
    element_category2 = driver.find_element(
        By.XPATH,
        '''/html/body/div[1]/div/div[3]/div[3]/div[1]/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div/div/div/div/div
        /label[2]/input'''
    )
    element_category2.send_keys('12000000')
    time.sleep(8)
    print('ДО')

    # Произвести поиск по параметрам
    try:
        element_category3 = driver.find_element(
            By.XPATH,
            '''/html/body/div[1]/div/div[3]/div[3]/div[1]/div/div[2]/div[2]/div/button[1]'''
        )
        element_category3.click()
    except:
        element_category3 = driver.find_element(
            By.XPATH,
            '''/html/body/div[1]/div/div[3]/div[3]/div[1]/div/div[2]/div[2]/div'''
        )
        element_category3.click()
    print('ПОИСК')
    time.sleep(10)

    # Парсим html (driver.current_url)
    html = driver.execute_script("return document.body.innerHTML;")

    soup = BeautifulSoup(html, 'html.parser')
    soup_div1 = soup.find_all('h3', class_='title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR '
                                           'title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL '
                                           'text-bold-SinUO')
    soup_div2 = soup.find_all('span', class_='price-text-_YGDY text-text-LurtD text-size-s-BxGpL')

    titles = [i.text.lstrip().rstrip() for i in soup_div1]
    prices = [i.text for i in soup_div2]
    result = dict(zip(titles, prices))
    for i in result:
        print(f'\nTitle: {i}\nPrice: {result[i]}')


except:
    # print(ex)
    print('exit')
finally:
    driver.close()
    driver.quit()
