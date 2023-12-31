# packages installed (webdriver,chromedrivermanager,implicitwait,expected condn,import service(executable path, time(sleep),BY)
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#Chrome driver manager path copied and installed#
# assigning driver_service to driver
Chromeoptions=Options()
Chromeoptions.add_experimental_option("debuggerAddress","localhost:9222")

driver_service = Service(executable_path="C:/selenium browser drivers/chromedriver-win64/chromedriver.exe")
driver_service1 = Service(executable_path=ChromeDriverManager().install(),options=Options)
driver=webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.implicitly_wait(20)


#open the browser
driver.get("https://www.kuttystory.com/")
sleep(3)

# finding the LOGIN Element
#implicit wait until finding out the element
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#global-nav > ul > li:nth-child(7) > a > span")))
login_command=driver.find_element(By.XPATH, "//*[@id=\"global-nav\"]/ul/li[7]/a/span").click()
print("Welcome to KuttyStory Journey")
sleep(3)

# wait until finding the element(usrname,pwd,Submit)
user_name =WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_username")))
pass_wrd = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_password")))
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Submit']")))

#sending the credentials
driver.find_element(By.XPATH,"//*[@id=\"id_username\"]")
user_name.send_keys("ramulakshmanan2010@gmail.com")
pass_wrd=driver.find_element(By.XPATH, "//*[@id=\"id_password\"]")
pass_wrd.send_keys("Superkings9")
sleep(3)

#show_pwd
show_pwd= WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#box")))
show_pwd.click()
sleep(6)
