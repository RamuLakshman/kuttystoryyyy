# packages installed (webdriver,chromedrivermanager,implicitwait,expected condn,import service(executable path, time(sleep),BY)
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

# assigning driver_service to driver
driver_service = Service(executable_path="C:/selenium browser drivers/chromedriver-win64/chromedriver.exe")
#driver=webdriver.Chrome(service=driver_service)
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

#open the browser
driver.get("https://kuttystory.com/")


# finding the LOGIN Element
#implicit wait until finding out the element
#WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#global-nav > ul > li:nth-child(7) > a > span")))
login_command=driver.find_element(By.XPATH, "//*[@id=\"global-nav\"]/ul/li[6]/a/span").click()
print("Welcome to KuttyStory Journey")

# wait until finding the element(usrname,pwd,Submit)
user_name =WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_username")))
pass_wrd = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_password")))
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Submit']")))

#sending the credentials
driver.find_element(By.XPATH,"//*[@id=\"id_username\"]")
user_name.send_keys("Indian@mailinator.com")
pass_wrd=driver.find_element(By.XPATH, "//*[@id=\"id_password\"]")
pass_wrd.send_keys("Superkings9")
sleep(4)

#show_pwd
show_pwd= WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#box")))
show_pwd.click()
sleep(6)

#submit_command
driver.find_element(By.XPATH,"//button[text()='Submit']").click()
sleep(6)

#sending Baby details
#Storyname
storyname =  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_story_name")))
driver.find_element(By.XPATH, "//*[@id=\"id_story_name\"]")
storyname.send_keys("Princess$$$$")
sleep(3)

#borndate
borndate= WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_baby_date")))
driver.find_element(By.XPATH, "//*[@id=\"id_baby_date\"]")
borndate.send_keys("10/08/2011")
sleep(3)

#Born state
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_born_status ")))
dropdown=driver.find_element(By.XPATH,"//*[@id=\"id_born_status\"]")
select=Select(dropdown)
select.select_by_value("Born")
sleep(6)

#relationships
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_relationships")))
dropdown_relation=driver.find_element(By.XPATH,"//*[@id=\"id_relationships\"]")
select=Select(dropdown_relation)
select.select_by_value("Mom")
sleep(4)

#gender(Edit details)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_gender")))
dropdown_gender=driver.find_element(By.ID, "id_gender")
select=Select(dropdown_gender)
select.select_by_visible_text("Female")
sleep(4)


#Choose pic1
driver.find_element(By.XPATH,"//*[@id=\"id_profile_pic\"]").send_keys("C:/Users/Toshiba/PycharmProjects/pythonProject4(kutty_storyyyy)/Family pic1.jpeg")
sleep(3)

"""
#Crop/Cancel
driver.find_element(By.XPATH,"//button[@id='crop-btn']").click()
sleep(3)
"""

#sending Personal_details
phone_no =  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_phone")))
driver.find_element(By.XPATH, "//*[@id=\"id_phone\"]")
phone_no.send_keys("9788165600")
sleep(3)

#City
City=  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_city")))
driver.find_element(By.XPATH, "//*[@id=\"id_city\"]")
City.send_keys("DGL")
sleep(3)

#Country
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_country")))
dropdown_country=driver.find_element(By.XPATH,"//*[@id=\"id_country\"]")
select=Select(dropdown_country)
select.select_by_visible_text("Tamilnadu, India")
sleep(4)

#choose pic2
driver.find_element(By.XPATH,"//*[@id=\"id_profile_pic1\"]").send_keys("C:/Users/Toshiba/PycharmProjects/pythonProject4(kutty_storyyyy)/Family pic1.jpeg")
sleep(3)

"""
#Crop/Cancel
#crop
driver.find_element(By.XPATH,"//button[@id='crop-btn1']").click()
"""

#Postalcode
pc=  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_postal_code")))
driver.find_element(By.XPATH, "//*[@id=\"id_postal_code\"]")
pc.send_keys("624001")
sleep(3)


#Family & Friends (name,Email,relationship)
name1=  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_name")))
driver.find_element(By.XPATH, "//*[@id=\"id_name\"]")
name1.send_keys("Laks")
sleep(3)

email=  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_mail_id")))
driver.find_element(By.XPATH, "//*[@id=\"id_mail_id\"]")
email.send_keys("ramulakshmanan2010@gmail.com")
sleep(3)

WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_relationship")))
dropdown_relations=driver.find_element(By.XPATH,"//*[@id=\"id_relationship\"]")
select=Select(dropdown_relations)
select.select_by_value("Dad")
sleep(4)

#name2=driver.find_element(By.XPATH,("(//div[@class='row form_split_bg']/div/div/div/input[@id='id_name'])[2]"))
name2=driver.find_element(By.XPATH,"(//input[@id='id_name'])[2]")
name2.send_keys("Abimanyu")
sleep(3)

#email2=driver.find_element(By.XPATH,("(//div[@class='form-group col-md-4 mb-3']/input[@id='id_mail_id'])[2]"))
email2=driver.find_element(By.XPATH,"(//input[@id='id_mail_id'])[2]")
email2.send_keys("harshithalakshman32@gmail.com")
sleep(3)


#dropdown_relationships=driver.find_element(By.XPATH,("(//div/select[@id='id_relationship'])[2]"))
dropdown_relationships=driver.find_element(By.XPATH,"(//select[contains(@name,'relationship')])[3]")
select=Select(dropdown_relationships)
select.select_by_value("Brother")
sleep(4)



#Submit
submit=driver.find_element(By.XPATH,"(//button[normalize-space()='SUBMIT'])[1]")
print("Submit element-",submit)
driver.execute_script("arguments[0].click();", submit)
sleep(6)


