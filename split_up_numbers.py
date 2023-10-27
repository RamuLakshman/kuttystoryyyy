import re
user_sentence = input("otp 7548965 : ")
while user_sentence != "quit":
  numbers = re.findall("[0-9]+", user_sentence)
  if numbers:
        print("found numbers " + " ".join(numbers))
        user_sentence = input("spliting up : ")
  else:
        print("no numbers found")
        user_sentence = input(">>> : ")
