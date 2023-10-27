import re

#extracting email id from content
Username="""Hi, Welcome to kuttystory.com please find your login details below.
username : harshitha12@mailinator.com
password : fqcwrphl
click here to Login https://kuttystory.com/userapp/login/
For more information please contact us +91-9841888001 or send mail to admin@kuttystory.com"
"""

# User=open("C:/Users/Toshiba/PycharmProjects/pythonProject4(kutty_storyyyy)/user.txt")
# for line in Username:
#      if line.startswith("username :"):
#        print(line)
# # print("Extracted the username",line)
print Username[1]




# User=re.findall(r'[\w\.-]+@[\w\.-]+' ,Username)
# result = ''.join(str(item) for item in User)
# print(result)
# #if re.search("password","Hi, Welcome to kuttystory.com please find your login details below.username : harshitha12@mailinator.com password : fqcwrphl  click here to Login https://kuttystory.com/userapp/login/ For more information please contact us +91-9841888001 or send mail to admin@kuttystory.com"):
#   #print("there is password")


# #extracting password
# Pwd=Username.split(":")[-1]
# print(Pwd)




