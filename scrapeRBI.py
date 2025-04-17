

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Selenium WebDriver
#chrome_options = Options()

#service = Service()  # Update with your actual ChromeDriver path
driver = webdriver.Chrome()  #service=service, options=chrome_options)

# Open RBI website
url = "https://rbi.org.in/"  # Update with actual RBI page link
driver.get(url)

# Step 1: Click the "English" button (if available)

english_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Button2")))
english_button.click()
    



accordion_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div[1]/a')))
accordion_button.click()

for i in range(1,6):
    accordion = WebDriverWait(driver,20).until(
        EC.visibility_of_element_located((By.XPATH,f'//*[@id="wrapper"]/div[2]/table/tbody/tr[{i}]'))).text
    print(accordion)
    


reserve_button = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.XPATH,f'//*[@id="wrapper"]/div[3]/a')))
reserve_button.click()

for i in range(1,3):
    resrve = WebDriverWait(driver,20).until(
        EC.visibility_of_element_located((By.XPATH,f'//*[@id="wrapper"]/div[4]/table/tbody/tr[{i}]'))
    ).text
    print(resrve)
    

exchange_button = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.XPATH,f'//*[@id="wrapper"]/div[5]/a'))
)
exchange_button.click()
for i in range(1,6):
    exchange = WebDriverWait(driver,20).until(
        EC.visibility_of_element_located((By.XPATH,f'//*[@id="wrapper"]/div[6]/table/tbody/tr[{i}]'))
    ).text
    print(exchange)
    

deposite_button = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.XPATH,f'//*[@id="wrapper"]/div[7]/a'))
)
deposite_button.click()

for i in range(1,5):
    deposite = WebDriverWait(driver,20).until(
        EC.visibility_of_element_located((By.XPATH,f'//*[@id="wrapper"]/div[8]/table/tbody/tr[{i}]'))
    ).text
    print(deposite)
    

driver.quit()
 










