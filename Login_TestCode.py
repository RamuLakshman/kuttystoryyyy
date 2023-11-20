# packages installed (webdriver,chromedrivermanager,implicitwait,expected condn,import service(executable path, time(sleep),BY)
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

#Chrome driver manager path copied and installed#
# assigning driver_service to driver
driver_service = Service(executable_path="C:/selenium browser drivers/chromedriver-win64/chromedriver.exe")
#driver_service = Service(executable_path=ChromeDriverManager().install())
#driver=webdriver.Chrome(service=driver_service)
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

#open the browser
driver.get("https://kuttystory.com/")
sleep(3)

# finding the LOGIN Element
#implicit wait until finding out the element
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#global-nav > ul > li:nth-child(7) > a > span")))
login_command=driver.find_element(By.XPATH, "//*[@id=\"global-nav\"]/ul/li[6]/a/span").click()
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

"""
try:
    if pass_wrd!="Superkings9" and user_name!="ramulakshmanan2010@gmail.com":
            WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div.container.mt-5 > div > div.col-md-6.mr-auto.order-2.order-md-1 > div > div")))
            Error_Msg=driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/div").text
            print("Invalid credentials-->",Error_Msg)


except:
    print("Successfully Logged")
"""

#show_pwd
show_pwd= WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#box")))
show_pwd.click()
sleep(6)

#submit_command
driver.find_element(By.XPATH,"//button[text()='Submit']").click()
sleep(10)
"""
#ForgotPwdlink & changepwd
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/form/fieldset/b/b/div[3]/small[2]/a/p").click()
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_email ")))
driver.find_element(By.XPATH,"//*[@id=\"id_email\"]").send_keys("ramulakshmanan2010@gmail.com")
driver.find_element(By.XPATH,"//*[@id=\"id_email\"]").send_keys(Keys.ENTER)
print("Credentials has been sent to Email and SMS(Phone)")
sleep(5)

#Specific Rules
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div.container.mt-5 > div > div.col-md-6.mr-auto.order-2.order-md-1 > div > div")))
Warning_Msg= driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div").text
print("Invalid Username & Pwd --->",Warning_Msg)
"""

#comments


driver.find_element(By.XPATH,"(//div[contains(@class,'emojionearea-editor')])[1]").send_keys("Greetings")
comment=driver.find_element(By.XPATH,"(//i[contains(@class,'fa-solid fa-paper-plane px-2')])[1]").click()
sleep(5)

comment_list=driver.find_element(By.XPATH,"(//p[contains(@type,'button')][normalize-space()='COMMENTS'])[1]")
driver.execute_script("arguments[0].click();", comment_list)
sleep(6)

driver.find_element(By.XPATH,"(//div[contains(@class,'emojionearea-editor')])[2]").send_keys("Hearty Welcome")
comment=driver.find_element(By.XPATH,"(//i[contains(@class,'fa-solid fa-paper-plane px-2')])[2]").click()
sleep(5)

comment_list=driver.find_element(By.XPATH,"(//p[contains(@type,'button')][normalize-space()='COMMENTS'])[2]")
driver.execute_script("arguments[0].click();", comment_list)
sleep(6)






