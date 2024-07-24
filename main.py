from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)



URL = 'JOB SEARCH URL'
driver.get(URL)
driver.maximize_window()
time.sleep(5)
login = driver.find_element(By.CSS_SELECTOR, value='.nav__button-secondary')
login.click()
time.sleep(2)

email = driver.find_element(By.ID, value='username').send_keys('YOUR EMAIL')
password = driver.find_element(By.ID,value='password').send_keys('YOUR PASSWORD')

driver.find_element(By.CLASS_NAME,value='btn__primary--large').click()
time.sleep(5)

msg_overlay = driver.find_element(By.CSS_SELECTOR, ".msg-overlay-bubble-header")
msg_overlay.click()

job_listings = driver.find_elements(By.CSS_SELECTOR, value='.jobs-search-results__list-item')
action = Keys()
action.ENTER

time.sleep(4)

# reject_cookies = driver.find_element(By.XPATH, value='//*[@id="ember52"]').click()
for index, li in enumerate(job_listings):
    try: 
        print(f'apro offerta di lavoro {index}')
        li.click()
        time.sleep(4)
        save_job = driver.find_element(By.CLASS_NAME, value='jobs-save-button').click()
        print(f'offerta di lavoro salvata ')
       
        time.sleep(4)
        follow = driver.find_element(By.CLASS_NAME, value='follow')
        driver.execute_script("arguments[0].scrollIntoView(true);", follow)
        try:
            follow.click()
        except NoSuchElementException:
            continue
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].scrollIntoView(true);", follow) 
        
        print(f'azienda seguita {index}')
    except Exception as e:
        print(f"Error processing job listing {index}: {e}")
