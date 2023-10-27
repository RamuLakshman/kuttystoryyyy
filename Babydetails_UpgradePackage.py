from openpyxl.descriptors import String
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

#Chrome driver manager path copied and installed
# assigning driver_service to driver
driver_service = Service(executable_path="C:/selenium browser drivers/chromedriver-win64/chromedriver.exe")
#driver_service = Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.implicitly_wait(20)

#open the browser
driver.get("https://www.kuttystory.com/")
sleep(6)

# finding the LOGIN Element
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#global-nav > ul > li:nth-child(7) > a > span")))
login_command=driver.find_element(By.XPATH, "//*[@id=\"global-nav\"]/ul/li[7]/a/span").click();
print("Welcome to KuttyStory Journey")

# wait until finding the element(usrname,pwd,Submit)
user_name =WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_username")))
pass_wrd = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_password")))
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Submit']")))

#sending the credentials
driver.find_element(By.XPATH,"//*[@id=\"id_username\"]")
user_name.send_keys("ramulakshmanan2010@gmail.com")
pass_wrd=driver.find_element(By.XPATH, "//*[@id=\"id_password\"]")
pass_wrd.send_keys("Superkings9")
sleep(4)

#show_pwd
show_pwd= WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#box")))
show_pwd.click();
sleep(6)

#submit_command
driver.find_element(By.XPATH,"//button[text()='Submit']").click()
sleep(5)
"""
#Star_PACKAGE
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#signout > i")))
driver.find_element(By.XPATH,"//*[@id=\"signout\"]/i").click()
sleep(5)

#Back to homepage
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/a[1]/i[1]").click()
sleep(2)
"""
#UpgradePackage icon and link (Camera)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div.navigation > div.navigation-icons.col-sm-12.col-lg-6.col-md-8.secondbg > div > a:nth-child(5) > i")))
driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/a[4]/i").click()
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div.container-fluid.p-0.m-0 > div > div.row > span > a")))
driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/span/a").click()
sleep(5)

print("Package decription-->Free/Silver/Gold/Platinum")
print("Upgrade package")
sleep(6)

#Silver package
Silver=driver.find_element(By.XPATH,"(//input[@id='submitbutton'])[1]")
driver.execute_script("arguments[0].click();", Silver)
print("willing to join in Silver Package")
sleep(5)
Agree=driver.find_element(By.XPATH,"(//input[@id='checkbox'])[1]")
driver.execute_script("arguments[0].click();",Agree)
sleep(2)
Pay=driver.find_element(By.XPATH,"(//input[@value='Pay Now'])[1]")
driver.execute_script("arguments[0].click();",Pay)
sleep(2)
"""
#phoneno=driver.find_element(By.XPATH,"//*[@id='contact']")
phoneno=driver.find_element(By.XPATH,"//input[@class='input-one-click-checkout phone-field-one-click-checkout main svelte-dau4sx error-field-one-click-checkout'][@id='contact']")
print(phoneno)

sleep(3)
"""
#Proceed=driver.find_element(By.XPATH,"(//button[@id='redesign-v15-cta']")
Proceed=driver.find_element(By.XPATH,"//div[@class='cta-container has-tooltip svelte-s8db8t reduce-amount-size no-shadow']/div[@class='redesign-v15-cta-wrapper svelte-s8db8t']/button[@id='redesign-v15-cta']")
driver.execute_script("arguments[0].click();",Proceed)
print(Proceed)
sleep(5)
#driver.back()



Gold=driver.find_element(By.XPATH,"(//input[@id='submitbutton'])[2]")
driver.execute_script("arguments[0].click();", Gold)
print("willing to join in Gold Package")
sleep(2)
driver.back()


Platinum=driver.find_element(By.XPATH,"(//input[@id='submitbutton'])[3]")
driver.execute_script("arguments[0].click();", Platinum)
print("willing to join in Platinum Package")
sleep(2)
driver.back()


