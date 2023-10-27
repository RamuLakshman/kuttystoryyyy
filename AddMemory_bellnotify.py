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
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#global-nav > ul > li:nth-child(7) > a > span")))
login_command=driver.find_element(By.XPATH, "//*[@id=\"global-nav\"]/ul/li[7]/a/span").click()
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
show_pwd.click()
sleep(6)

#submit_command
driver.find_element(By.XPATH,"//button[text()='Submit']").click()
sleep(15)


#Add memory
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"load-memory1\"]/i")))
driver.find_element(By.XPATH,"//*[@id=\"load-memory1\"]/i").click()
sleep(5)

# #Add_memory Close window
# driver.switch_to.window(driver.window_handles[0])
# driver.close()


#Memory_name
driver.find_element(By.XPATH,"//input[@id='id_memory_name']").send_keys("Crawling moment")
sleep(3)

#Mem_date
driver.find_element(By.XPATH,"//input[@id='date']").send_keys("08/09/2023")
sleep(3)

#Mem_PICTURE
driver.find_element(By.XPATH,"//input[@id='id_picture_tn']").send_keys("C:/Users/Toshiba/PycharmProjects/pythonProject4(kutty_storyyyy)/Family pic1.jpeg")
sleep(15)

#crop
driver.find_element(By.XPATH,"//button[@id='crop-btn']").click()

#Mem_desc
driver.find_element(By.XPATH,"//textarea[@id='id_body']").send_keys("Stepping into the world by intial crawling steps")
sleep(3)


#Upload_Memory
#WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#login-btn")))
driver.find_element(By.XPATH,"//button[@id='login-btn']").click()
print("Memory Succesfully uploaded")
sleep(4)

#Back to home page
driver.switch_to.default_content()
sleep(8)


#bell
driver.find_element(By.XPATH,"//a[@role='button']//i[contains(@class,'fa-solid fa-bell')]").click()
sleep(4)
print("Notifications listed up")


