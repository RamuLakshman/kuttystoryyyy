from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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
show_pwd.click();
sleep(6)

#submit_command
driver.find_element(By.XPATH,"//button[text()='Submit']").click()
sleep(10)

#Add memory
driver.find_element(By.XPATH,"/html[1]/body[1]/nav[1]/ul[1]/li[1]/a[1]/i[1]").click()
sleep(2)
#Add_memory Close window
driver.switch_to.window(driver.window_handles[0])
#driver.find_element(By.XPATH,"//div[contains(text(),'+')]")


#Trimester (Before/After baby born)
trimester=driver.find_element(By.XPATH,"/html[1]/body[1]/nav[1]/ul[1]/li[2]/a[1]/i[1]")
driver.execute_script("arguments[0].click();", trimester)
sleep(3)

#1-12 
tri_quaters=driver.find_element(By.XPATH,"/html[1]/body[1]/nav[1]/ul[1]/ul[1]/li[2]/form[1]/div[1]/ul[1]/li[2]/a[1]/button[1]")
driver.execute_script("arguments[0].click();", tri_quaters)
sleep(3)

driver.back()

#Theme (Boy/Girl)
theme=driver.find_element(By.XPATH,"/html[1]/body[1]/nav[1]/ul[1]/li[3]/a[1]/i[1]")
driver.execute_script("arguments[0].click();", theme)
sleep(2)
#pink
pink=driver.find_element(By.XPATH,"/html[1]/body[1]/nav[1]/ul[1]/ul[2]/li[2]/div[1]/ul[1]/li[1]/a[1]/i[1]")
driver.execute_script("arguments[0].click();", pink)
sleep(3)
#blue
blue=driver.find_element(By.XPATH,"/html[1]/body[1]/nav[1]/ul[1]/ul[2]/li[2]/div[1]/ul[1]/li[2]/a[1]/i[1]")
driver.execute_script("arguments[0].click();", blue)
sleep(1)
driver.back()

#Missed Notifications (Before/After baby born)
notify=driver.find_element(By.XPATH,"/html[1]/body[1]/nav[1]/ul[1]/li[4]/a[1]/i[1]")
driver.execute_script("arguments[0].click();", notify)
sleep(2)


#Before BABY
before=driver.find_element(By.XPATH,"/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[1]/h5[1]/button[1]")
driver.execute_script("arguments[0].click();", before)
sleep(2)

#After BABY
after=driver.find_element(By.XPATH,"/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[1]/h5[1]/button[2]")
driver.execute_script("arguments[0].click();", after)
sleep(2)


