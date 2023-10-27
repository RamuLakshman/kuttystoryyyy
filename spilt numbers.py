import re

msg1="this is your otp 987667"
number = re.findall("[0-9]+", msg1)
print(number)


result = ''.join(str(item) for item in number)
print(result)
