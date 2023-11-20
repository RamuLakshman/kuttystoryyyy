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
login_cmd=driver.find_element(By.XPATH, "//*[@id=\"global-nav\"]/ul/li[6]/a/span")
login_cmd.click()
print("Welcome to KuttyStory Journey")
sleep(3)


# wait until finding the element(usrname,pwd,Submit)
user_name =WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_username")))
pass_wrd = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_password")))
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Submit']")))

"""
#sending the credentials
driver.find_element(By.XPATH,"//*[@id=\"id_username\"]")
user_name.send_keys("platinum86@mailinator.com")
pass_wrd=driver.find_element(By.XPATH, "//*[@id=\"id_password\"]")
pass_wrd.send_keys("Superkings9")
sleep(3)

#show_pwd
show_pwd= WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#box")))
show_pwd.click()
sleep(6)

#submit_command
driver.find_element(By.XPATH,"//button[text()='Submit']").click()
sleep(6)



#Logout
driver.find_element(By.XPATH,"//i[@class='fa-solid fa-power-off']").click()
print("logged out to switch to another user")
sleep(3)

#Reset_Pwd
#driver.find_element(By.XPATH,"//a[@href='/userapp/password-reset/']").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/a[2]/i[1]").click()
sleep(3)

#reset
driver.find_element(By.XPATH,"//*[@id=\"id_email\"]").send_keys("platinum86@mailinator.com",Keys.ENTER)
#driver.find_element(By.XPATH,"//*[@id=\"id_email\"]").send_keys(Keys.ENTER)
sleep(4)
print("Processing-->Please Check ur Email or Phone, credentials has been sent to reset Passwrd")
sleep(5)

#OTP Verification Required from Email(Mailinator)
driver.get("https://www.mailinator.com/v4/public/inboxes.jsp")
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#inbox_field")))
driver.find_element(By.XPATH,"//*[@id=\"inbox_field\"]").send_keys("platinum86")
sleep(6)
driver.find_element(By.XPATH,"//*[@id=\"inbox_field\"]").send_keys(Keys.ENTER)
sleep(15)

#Fetch last in first out email
inbox=driver.find_element(By.XPATH,"(//td[@class='ng-binding'])[1]")
inbox.click()
sleep(5)

msg=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#pills-textbuthtml-tab")))
driver.find_element(By.XPATH,"//*[@id=\"pills-textbuthtml-tab\"]").click()
sleep(5)

driver.switch_to.frame(driver.find_element(By.NAME, "texthtml_msg_body"))
msg1=driver.find_element(By.XPATH,"/html/body").text
sleep(4)
print(msg1)
"""


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

#submit_command
driver.find_element(By.XPATH,"//button[text()='Submit']").click()
sleep(6)

#User_login1(human) option menu
driver.find_element(By.XPATH,"//i[@class='fad fa-user-circle']").click()
print("Human User1 Clicked")
sleep(3)

#Sub User(human)-- (displayed family friends details)

driver.find_element(By.XPATH,"//i[@class='fad fa-user-circle addicon4']").click()
print("Family & Friends details page")
sleep(3)

#Timeline
timeline=driver.find_element(By.XPATH,"//a[normalize-space()='Timeline']")
driver.execute_script("arguments[0].click();", timeline)
print("It navigates to Landing page")
sleep(3)




