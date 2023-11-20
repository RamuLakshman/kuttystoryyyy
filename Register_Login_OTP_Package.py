# packages installed (webdriver,chromedrivermanager,implicitwait,expected condn,import service(executable path, time(sleep),BY)
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import re

#installing chromedriver and assigning executable_path to service
driver_service = Service(executable_path="C:/selenium browser drivers/chromedriver-win64/chromedriver.exe")
# driver_service1 = Service(executable_path=ChromeDriverManager().install())
#driver=webdriver.Chrome(service=driver_service)
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

#open the browser
driver.get("https://kuttystory.com/")
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#global-nav > ul > li.cta > a > span")))


# finding the SIGN_UP Element
SIGNUP_command=driver.find_element(By.XPATH, "//*[@id=\"global-nav\"]/ul/li[7]/a/span ").click()
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
Email.send_keys("kuttyyystorieee@mailinator.com")
Phone=driver.find_element(By.XPATH, "//*[@id=\"id_phonenumber\"]")
Phone.send_keys(7540045610)
Password=driver.find_element(By.XPATH, "//*[@id=\"id_password1\"] ")
Password.send_keys("Superkings9")
ConfirmPwd =driver.find_element(By.XPATH, "//*[@id=\"id_password2\"] ")
ConfirmPwd.send_keys("Superkings9")
sleep(5)

#submit(Enterkey)
driver.find_element(By.XPATH,"//*[@id=\"contact-section\"]/div/div/div/div[2]/form/div/button").send_keys(Keys.ENTER)
sleep(10)


#opening in the second tab
driver.execute_script("window.open('about:blank','secondtab');")
driver.switch_to.window("secondtab")

#OTP Verification Required from Email(Mailinator)
#open the browser
driver.get("https://www.mailinator.com/v4/public/inboxes.jsp")
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#inbox_field")))
#passing the email name
driver.find_element(By.XPATH,"//*[@id=\"inbox_field\"]").send_keys("kuttyyystorieee")
sleep(6)
driver.find_element(By.XPATH,"//*[@id=\"inbox_field\"]").send_keys(Keys.ENTER)
sleep(15)

#Fetch last in first out email
#clicking the Last in first out Email
inbox=driver.find_element(By.XPATH,"(//td[@class='ng-binding'])[1]")
inbox.click()
sleep(5)

#inspecting the placeholder of the TEXT(where the body msg occurs)
msg=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#pills-textbuthtml-tab")))
driver.find_element(By.XPATH,"//*[@id=\"pills-textbuthtml-tab\"]").click()
sleep(5)

#Retrieving the body content of last in First out mail
driver.switch_to.frame(driver.find_element(By.NAME, "texthtml_msg_body"))
msg1=driver.find_element(By.XPATH,"/html/body").text
sleep(4)
print(msg1)


#closing the current(mailinator window)
driver.close()

#Extracting OTP from Email
number = re.findall("[0-9]+", msg1)
print(number)
result = ''.join(str(item) for item in number)
print(result)

#switching to kuttystory window
driver.switch_to.window(driver.window_handles[0])
sleep(5)


#Pushing OTP into textbox(kuttystory)

driver.find_element(By.XPATH,"//body/div[@id='contact-section']/div[1]/div[1]/form[1]/fieldset[1]/div[1]/input[1]").send_keys(result)
driver.find_element(By.XPATH,"//body/div[@id='contact-section']/div[1]/div[1]/form[1]/fieldset[1]/div[1]/input[1]").send_keys(Keys.ENTER)
sleep(5)

# wait until finding the element(usrname,pwd,Submit)
user_name =WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_username")))
pass_wrd = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_password")))
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Submit']")))

#sending the credentials_login
driver.find_element(By.XPATH,"//*[@id=\"id_username\"]")
user_name.send_keys("kuttyyystorieee@mailinator.com")
pass_wrd=driver.find_element(By.XPATH, "//*[@id=\"id_password\"]")
pass_wrd.send_keys("Superkings9")
sleep(3)
#submit_command
driver.find_element(By.XPATH,"//button[text()='Submit']").click()
sleep(10)

"""
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
"""
#Crop/Cancel
driver.find_element(By.XPATH,"//button[@id='crop-btn']").click()
sleep(3)


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
"""
#Crop/Cancel
#crop
driver.find_element(By.XPATH,"//button[@id='crop-btn1']").click()
"""
"""
#Postalcode
pc=  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_postal_code")))
driver.find_element(By.XPATH, "//*[@id=\"id_postal_code\"]")
pc.send_keys("624001")
sleep(3)

#Submit
submit=driver.find_element(By.XPATH,"(//button[normalize-space()='SUBMIT'])[1]")
print("Submit element-",submit)
driver.execute_script("arguments[0].click();", submit)
sleep(6)

#Next
next=driver.find_element(By.XPATH,"(//a[normalize-space()='Next'])[1]")
driver.execute_script("arguments[0].click();", next)
print("It navigates to landing page")
sleep(5)



#package upgrade details
#Silver package
Silver=driver.find_element(By.XPATH,"(//input[@id='submitbutton'])[1]")
driver.execute_script("arguments[0].click();", Silver)
print("willing to join in Silver Package")
sleep(5)

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
"""
Agree=driver.find_element(By.XPATH,"(//input[@id='checkbox'])[1]")
driver.execute_script("arguments[0].click();",Agree)
sleep(2)
Pay=driver.find_element(By.XPATH,"(//input[@value='Pay Now'])[1]")
driver.execute_script("arguments[0].click();",Pay)
sleep(2)

"""


"""
#below code if we give OTP after login(if we not access thru register)
otp=driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/form/center/fieldset/div/input").send_keys(result)
sleep(5)

"""
