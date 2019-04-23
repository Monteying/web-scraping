from selenium import webdriver
import time
import pprint
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
chrome_driver_binary = "C:\\Users\\39411\\Desktop\\chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

# global var
links = []
info_titles = []
info_contacts = []
info_emails = []
info_phones = []

# 0 -> 15 [ page ]
for i in range(0,20,15):
    driver.get('https://www.chineseinsfbay.com/f/page_viewforum/f_29/key_%E4%BB%93%E5%BA%93/start_' + str(i) + '.html')
    elems = driver.find_elements_by_css_selector('a.title')

    
    for elem in elems:
        links.append(elem.get_attribute('href'))
        
        
    # click button to next page
    python_button = driver.find_element_by_link_text('下一页')
    python_button.click()
    
for link in links:
    driver.get(link)
    
    
    try:
        info_titles.append(driver.find_element_by_xpath('//*[@id="pageCenter"]/div[6]/table[1]/tbody/tr/td[2]/div/div[1]/span/h1').text)
    except NoSuchElementException:
        info_titles.append('None')
        pass
    
    
    try:
        info_contacts.append(driver.find_element_by_xpath("//*[@id='pageCenter']/div[6]/table[1]/tbody/tr/td[2]/div/div[3]/div[8]/img").get_attribute('src'))
    except NoSuchElementException:
        info_contacts.append('None')
        pass
  
  
    try:
        info_emails.append(driver.find_element_by_xpath("//*[@id='pageCenter']/div[6]/table[1]/tbody/tr/td[2]/div/div[3]/div[9]/img").get_attribute('src'))
    except NoSuchElementException:
        info_emails.append('None')
        pass
    
    
    try:
        info_phones.append(driver.find_element_by_xpath("//*[@id='pageCenter']/div[6]/table[1]/tbody/tr/td[2]/div/div[3]/div[10]/img").get_attribute('src'))
    except NoSuchElementException:
        info_phones.append('None')
        pass
    
    
    pprint.pprint(info_titles)
    pprint.pprint(info_contacts)
    pprint.pprint(info_emails)
    pprint.pprint(info_phones)
    
    time.sleep(3)

driver.close()