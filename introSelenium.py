from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

driver = webdriver.Chrome('F:\\code\\test\\chromedriver_win32\\chromedriver')

driver.get('https://www.instagram.com')

login_button = driver.find_element_by_xpath()

# sleep(3)
# login_button = driver.find_element_by_link_text('Log in')
# login_button.click()
# sleep(3)
# driver.get('https://www.google.com')
#
# search_bar = driver.find_element_by_id('lst-ib')
#
# search_bar.send_keys('I want to learn web scraping.')
# search_bar.submit()
# # soup = BeautifulSoup(driver.page_source, 'lxml')
# # print(soup.prettify())
# sleep(10)
driver.close()