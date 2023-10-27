from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
import imaplib,email,time
import datetime as dt
from os import path
from datetime import timezone


driver_service = Service(executable_path="C:/selenium browser drivers/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.implicitly_wait(20)


#OTP Verification Required from Email(Mailinator)
#open the browser
driver.get("https://www.mailinator.com/v4/public/inboxes.jsp")
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#inbox_field")))
#passing the email name
driver.find_element(By.XPATH,"//*[@id=\"inbox_field\"]").send_keys("Gold86")
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
"""
number = re.findall("[0-9]+", msg1)
#for loop
for num in number :

 print (int(result))


#spiliting up the numbers using while if else
test_str=msg1
test_str = input(">>> : ")
while test_str!= "quit":
  numbers = re.findall("[0-9]+",test_str)
  if numbers:
    print("found numbers " + " ".join(numbers))
    test_str = input(">>> : ")
  else:
    print("no numbers found")
    test_str = input(">>> : ")
"""
#spiliting the numbers and string

#assigning original text to another variable
test_str=msg1
print("Full original body message of last received mail-->" +str(test_str))

#spiliting text and OTP number in the original msg
temp=re.compile("([a-zA-Z]+)([0-9]+)")
splitted_up=temp.match(test_str).groups()

#String and Numbers are splitted
print("String and Numbers are Splitted up-->" +str(splitted_up))


"""
#spliting up only numbers by using the group function

test_str=input(">>>:")
while test_str!="quit":
    if re.findall("[0-9]+",test_str):
        OTP=re.findall("[0-9]+",test_str)
        print(OTP.group())
        test_str=input(">>>:")
    else:
        print("No OTP")
        test_str=input(">>>:")

"""





"""
inbox=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#row_platinum86-1695271205-140617579 > td:nth-child(2)")))
driver.find_element(By.XPATH,"//*[@id=\"row_platinum86-1695271205-140617579\"]/td[2]").click()
sleep(5)
msg=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#pills-textbuthtml-tab")))
driver.find_element(By.XPATH,"//*[@id=\"pills-textbuthtml-tab\"]").click()
sleep(5)
driver.switch_to.frame(driver.find_element(By.NAME, "texthtml_msg_body"))
msg1=driver.find_element(By.XPATH,"/html/body").text
sleep(4)
print(msg1)
"""

"""
# gmail automation for inbox
Url=driver.get("https://www.google.com/gmail/about/")
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > header > div > div > div > a.button.button--medium.button--mobile-before-hero-only")))
driver.find_element(By.XPATH,"/html/body/header/div/div/div/a[2]").click()
sleep(6)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#identifierId")))
User=driver.find_element(By.XPATH,"//*[@id=\"identifierId\"]")
User.send_keys("harshithalakshman32@gmail.com")
User.send_keys(Keys.ENTER)
sleep(2)
Pwd=driver.find_element(By.XPATH,"//*[@id=\"password\"]/div[1]/div/div[1]/input")
Pwd.send_keys("Harshitha@2011")
Pwd.send_keys(Keys.ENTER)
sleep(15)

# gmail automation for fetching inbox content
import getpass
imap_url='imap.gmail.com'
sleep(5)
sign_in=imaplib.IMAP4_SSL(imap_url)
sleep(5)
User=getpass.getpass("harshithalakshman32@gmail.com")
Pwd=getpass.getpass("Harshitha@2011")
sign_in.login(User,Pwd)
"""
"""
imap_server="imap.mailinator.com"
email_add="harshithalakshman32@gmail.com"
pwd="Harshitha@2011"
sleep(5)

imap=imaplib.IMAP4_SSL(imap_server)
imap.login(email_add,pwd)

imap.select("Inbox")
msgnum=imap.search(None,"ALL")

for msgnums in msgnum[0].split():
    data=imap.fetch(msgnums,"(RFC822)")
    print(data)
"""




