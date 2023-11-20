from selenium import webdriver
from selenium.common import NoSuchElementException
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
print("opened the browser")

#kuttystory logo & homepage tabs
def is_logo_present(how,what):
    try:
        driver.find_element(by=how,value=what)
        return True
    except NoSuchElementException:
        return False
#Logo
print(is_logo_present(By.XPATH,"//*[@id=\"mobile-head\"]/img"))
print("Baby sleeping kutty story logo")
sleep(2)

#home_page_tabs
print("Home page Tabs")
print(is_logo_present(By.XPATH,"//*[@id=\"global-nav\"]/ul/li[1]/a"))
print(is_logo_present(By.XPATH,"//*[@id=\"global-nav\"]/ul/li[2]/a"))
print(is_logo_present(By.XPATH,"//*[@id=\"global-nav\"]/ul/li[3]/a"))
print(is_logo_present(By.XPATH,"//*[@id=\"global-nav\"]/ul/li[4]/a"))
print(is_logo_present(By.XPATH,"//*[@id=\"global-nav\"]/ul/li[5]/a"))
print(is_logo_present(By.XPATH,"//*[@id=\"global-nav\"]/ul/li[6]/a"))
sleep(5)

#Sign_up & Login
print("Sign_up & Login")
print(is_logo_present(By.XPATH,"//*[@id=\"global-nav\"]/ul/li[7]/a/span"))
print(is_logo_present(By.XPATH,"//*[@id=\"global-nav\"]/ul/li[6]/a/span"))

#BestGift
print("Create a Treasure for your Little one")
print(is_logo_present(By.XPATH, "//*[@id=\"home-section\"]/div/div/div[1]/div[1]"))
print(is_logo_present(By.XPATH,"//*[@id=\"home-section\"]/div/div/div[2]/div[1]/div[1]/div/div[3]/img"))
sleep(2)

#a=driver.find_element(By.XPATH, "//*[@id=\"home-section\"]/div/div/div[1]/div[1]").text
#print(a)
#print(is_logo_present(By.XPATH,"//*[@id=\"home-section\"]/div/div/div[2]/div[1]/div[1]/div/div[3]/img"))
#sleep(3)

#left_Right Click buttons for pictures & Quotes
print ("To move back and forth around baby pics & Quotes")
print(is_logo_present(By.XPATH,"//*[@id=\"home-section\"]/div/div/div[2]/div[2]/a[1]/span/i"))
print(is_logo_present(By.XPATH,"//*[@id=\"home-section\"]/div/div/div[2]/div[2]/a[2]/span/i"))
print(is_logo_present(By.XPATH,"//*[@id=\"home-section\"]/div/div/div[2]/div[2]/a[3]/span/i"))
print(is_logo_present(By.XPATH,"//*[@id=\"home-section\"]/div/div/div[2]/div[2]/a[4]/span/i"))
sleep(3)

#Sign_up logo
driver.find_element(By.XPATH, "//*[@id=\"global-nav\"]/ul/li[7]/a/span ").click()
sleep(3)
print("Welcome to kuttystory Journey")
print("Mom & Baby")
print(is_logo_present(By.XPATH,"//*[@id=\"contact-section\"]/div/div/div/div[1]/img"))

#Login Logo
#WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#global-nav > ul > li:nth-child(7) > a > span")))
login_command=driver.find_element(By.XPATH, "//*[@id=\"global-nav\"]/ul/li[6]/a/span").click()
sleep(3)
print("Dad & son for photography")

#BabydetailsPage design after Login
user_name =WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_username")))
pass_wrd = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_password")))
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Submit']")))
driver.find_element(By.XPATH,"//*[@id=\"id_username\"]")
user_name.send_keys("Queen86@mailinator.com")
pass_wrd=driver.find_element(By.XPATH, "//*[@id=\"id_password\"]")
pass_wrd.send_keys("Superkings9")
sleep(3)
driver.find_element(By.XPATH,"//button[text()='Submit']").click()
sleep(10)


print("Welcome,Story begins here")
print(is_logo_present(By.XPATH,"/html/body/div[1]/div[1]/div/h1[2]"))
print(is_logo_present(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/center[1]"))
print(is_logo_present(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[2]/center[1]"))
print(is_logo_present(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[3]/center[1]"))
print(is_logo_present(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[4]/center[1]"))
sleep(2)

print("3 babies pics")
print(is_logo_present(By.XPATH,"/html/body/div[1]/div[3]"))
sleep(2)

print("Logout & Change_Pwd icons")
print(is_logo_present(By.XPATH,"//*[@id=\"signout\"]/i"))
print(is_logo_present(By.XPATH,"//*[@id=\"signout\"]"))
sleep(2)

