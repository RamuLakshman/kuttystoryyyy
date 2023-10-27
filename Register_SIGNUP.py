# packages installed (webdriver,chromedrivermanager,implicitwait,expected condn,import service(executable path, time(sleep),BY)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

#installing chromedriver and assigning executable_path to service
driver_service = Service(executable_path="C:/selenium browser drivers/chromedriver-win64/chromedriver.exe")
# driver_service1 = Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.implicitly_wait(20)

#open the browser
driver.get("https://www.kuttystory.com/")
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#global-nav > ul > li.cta > a > span")))


# finding the SIGN_UP Element
SIGNUP_command=driver.find_element(By.XPATH, "//*[@id=\"global-nav\"]/ul/li[8]/a/span ").click()
sleep(5)
print("Welcome to kuttystory Journey")

# wait until finding the element (Name,Email,Phone,Pwd,ConfirmPwd,Submit)
Name =  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_name")))
Email = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_username ")))
Phone = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_phonenumber")))
Password= WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_password1")))
ConfirmPwd= WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_password2")))
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"contact-section\"]/div/div/div/div[2]/form/div/button")))

#sending the credentials
driver.find_element(By.XPATH, "//*[@id=\"id_name\"]")
Name.send_keys("HarsheeLaks")
Email=driver.find_element(By.XPATH, "//*[@id=\"id_username\"]")
Email.send_keys("kuttystory2000@mailinator.com")
Phone=driver.find_element(By.XPATH, "//*[@id=\"id_phonenumber\"]")
Phone.send_keys(7540045610)
Password=driver.find_element(By.XPATH, "//*[@id=\"id_password1\"] ")
Password.send_keys("superkings9")
ConfirmPwd =driver.find_element(By.XPATH, "//*[@id=\"id_password2\"] ")
ConfirmPwd.send_keys("superkings9")
sleep(5)

# show_pwd
show_pwd=driver.find_element(By.XPATH,"//input[@class='form-check-input'][@type='checkbox']")
driver.execute_script("arguments[0].click();", show_pwd)
sleep(5)


#submit(Enterkey)
driver.find_element(By.XPATH,"//*[@id=\"contact-section\"]/div/div/div/div[2]/form/div/button").send_keys(Keys.ENTER)
sleep(8)


#Error_message
Error_Msg= driver.find_element(By.XPATH,"//*[@id=\"contact-section\"]/div/div/div/div[2]/form/p").text
print("Rules for User credentials--->",Error_Msg)







