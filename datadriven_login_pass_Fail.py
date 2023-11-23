# Driving data from Excel to Webpage for multiple users with single testcase
# Maintain default read/write function in xl manager
import alert as alert
import xlmanager
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from validator_collection import validators,checkers
from time import sleep

#Chrome driver manager path copied and installed#
# assigning driver_service to driver
driver_service = Service(executable_path="C:/selenium browser drivers/chromedriver-win64/chromedriver.exe")
#driver_service = Service(executable_path=ChromeDriverManager().install())
#driver=webdriver.Chrome(service=driver_service)
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)



#excel location
path="C://Users//Toshiba//PycharmProjects//pythonProject4(kutty_storyyyy)//Login.xlsx"

#Passing excel location and sheet name)
rows=xlmanager.getrowcount(path,'Login_Credentials')

#forloop to read the data
for r in range(2,rows+1):
    Username=xlmanager.readdata(path,'Login_Credentials',r,1)
    Password=xlmanager.readdata(path,'Login_Credentials',r,2)
#open the browser
    driver.get("https://kuttystory.com/")
    sleep(3)

#login xpath
    driver.find_element(By.XPATH, "//*[@id=\"global-nav\"]/ul/li[6]/a/span").click()
    # print("Welcome to KuttyStory Journey")
    sleep(3)


#Credentials
    driver.find_element(By.XPATH,"//*[@id=\"id_username\"]").send_keys(Username)
    driver.find_element(By.XPATH, "//*[@id=\"id_password\"]").send_keys(Password)
    driver.find_element(By.XPATH,"//button[text()='Submit']").click()
    sleep(6)


#comparing title with automation

    actual_result=driver.current_url

    expected_result="https://kuttystory.com/notification/memory_view/"

    if actual_result==expected_result:
        print("Test case-->Passed")
        xlmanager.writedata(path,"Login_Credentials",r,3,"Passed")
    else:
        print("Test case-->Failed")
        xlmanager.writedata(path,"Login_Credentials",r,3,"failed")

