from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver import ActionChains


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
show_pwd.click()
sleep(6)

#submit_command
driver.find_element(By.XPATH,"//button[text()='Submit']").click()
sleep(15)

"""
#User_login1(human) option menu
driver.find_element(By.XPATH,"//i[@class='fad fa-user-circle']").click()
print("Human User1 Clicked")
sleep(3)


#Edit_Babydetails icon (conceived to born details)
driver.find_element(By.XPATH,"//i[@class='fa-solid fa-user-pen addicon4']").click()
print("Need to update Baby details")
sleep(4)
driver.find_element(By.XPATH,"//button[normalize-space()='EDIT']").click()


#Storyname
storyname=driver.find_element(By.XPATH, "//input[@id='id_story_name']")
storyname.clear()
storyname.send_keys("Princess$$$$")
sleep(3)

#borndate

driver.find_element(By.XPATH, "//input[@id='id_baby_date']").send_keys("10/08/2023")
sleep(3)

#Born state
dropdown=driver.find_element(By.XPATH,"//select[@id='id_born_status']")
select=Select(dropdown)
select.select_by_value("Born")
sleep(6)

#gender(Edit details)
dropdown_gender=driver.find_element(By.XPATH,"//select[@id='id_gender']")
select=Select(dropdown_gender)
select.select_by_visible_text("Female")
sleep(4)

#ChangeNew pic
#WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//i[@class='fa fa-plus-circle']")))
#driver.find_element(By.XPATH,"//i[@class='fa fa-plus-circle']").send_keys("C:/Users/Toshiba/PycharmProjects/pythonProject4(kutty_storyyyy)/Family pic1.jpeg")
driver.find_element(By.XPATH,"//*[@id=\"id_profile_pic1\"]").send_keys("C:/Users/Toshiba/PycharmProjects/pythonProject4(kutty_storyyyy)/Family pic1.jpeg")
sleep(3)


#Crop/Cancel
driver.find_element(By.XPATH,"//button[@id='crop-btn1']").click()
sleep(3)


#update
driver.find_element(By.XPATH,"//small[normalize-space()='UPDATE']").click()
print("updated successfully")

"""
#User_login1(human) option menu
driver.find_element(By.XPATH,"//i[@class='fad fa-user-circle']").click()
print("Human User1 Clicked")
sleep(3)

#adding member icon
driver.find_element(By.XPATH,"//i[@class='fa-solid fa-user-plus addicon4']").click()
sleep(3)

#adding member details
name="Vaishaliii"
driver.find_element(By.XPATH,"//input[@id='id_name']").send_keys(name)
driver.find_element(By.XPATH,"//input[@id='id_mail_id']").send_keys("harshitha12@mailinator.com")
sleep(2)

#relationship
dropdown_relation=driver.find_element(By.XPATH,"//select[@id='id_relationship']")
select=Select(dropdown_relation)
select.select_by_value("Sister")
sleep(3)


#Addingmem_Submit
submit=driver.find_element(By.XPATH,"//div[@class='form-group']/center/button[@type='submit']")
print("Submit element-",submit)
driver.execute_script("arguments[0].click();", submit)
sleep(5)

#click HumanUser
driver.find_element(By.XPATH,"//i[@class='fad fa-user-circle']").click()
print("Human User1 Clicked")
sleep(3)

#Sub User(human)-- (displayed family friends details)
driver.find_element(By.XPATH,"//i[@class='fad fa-user-circle addicon4']").click()
print("Family & Friends details page")
sleep(3)

"""
#Check whether new user added in the family details page
new_user=driver.find_element(By.XPATH,"(/html/body/div[3]/div/div[1]/div/div/div[1]/div/div[2]/h4)")
print(new_user)
# if new_user==name
#     print("New Family added")

"""





