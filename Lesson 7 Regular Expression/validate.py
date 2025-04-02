email = input("What is your email address? ").strip()
# This is simple testing of the user input gmail!
# if "@" in email:
#     print("Valid")
# else:
#     print("Invalid")

#This is a bit stricter testing of the user gmail
# if "@" and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# This is like a handy testing (Manually)
# username, domain = email.split('@')
# if  username and '.' in domain:
#     print("Valid")
# else:
#     print("Invalid")

#This is testing the gmail ends with .edu or not!
# username, domain = email.split("@")
# if username and domain.endswith(".edu"):
#     print("This is Valid Gmail")
# else:
#     print("This is invalid")

import re

#Simple searching using regular expression!

# if re.search("@", email):
#     print("Valid")
# else:
#     print("Invalid")

# .   any character except a new line
# *   0 or more repetitions
# +   1 or more repetitions
# ?   0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions


# This code will recoginize everything like this abc@abc !! very loosely coded one
# if re.search(".+@.+", email):
#     print("Valid")
# else:
#     print("Invalid")

# ဒီကောင်က အလုပ်လုပ်တာ အဆင်တော့ပြေပမဲ့ လိုနေသေးတယ်။ ငါတို့ .edu ရှေ့က . ကို ပုံစံပြောင်းမှ ရမယ်။
# if re.search(".+@.+.edu", email):
#     print("Valid")
# else:
#     print("Invalid")
# ဒီမှာ Escape \ ကို သုံးထားတယ်။
# if re.search(r".+@.+\.edu", email):
#     print("Valid")
# else:
#     print("Invalid")

# Regex Breakdown
# ^ → Start of the string (ensures matching starts at the beginning)

# .+ → One or more of any character before @ (ensures there's at least one character before @)

# @ → A literal @ symbol (ensures the email contains @)

# .+ → One or more of any character after @ (ensures there's something between @ and .edu)

# \. → A literal dot . (escaped because . is a special character in regex)

# edu → Matches "edu" exactly (ensures the domain ends with .edu)

# $ → End of the string (ensures nothing comes after .edu)
# while True:
#     if re.search(r"^.+@.+\.edu$",email):
#         print("valid")
#         break
#     else:
#         print("Invalid")
#         break

# ^ means to match at the start of the string. 
# $ means to match at the end of the string. 
# [^@]+ means any character except an @.
# [^@]+\.edu means any character except an @ followed by an expression ending in .edu
# malan@@@harvard.edu will be invalid!

# if re.search(r"^[^@]+@[^@]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# \w is the same with [a-zA-Z0-9_]

# if re.search(r"^\w+@\w+\.edu$",email):
#     print("valid")
# else:
#     print("invalid")

# \d    decimal digit
# \D    not a decimal digit
# \s    whitespace characters
# \S    not a whitespace character
# \w    word character, as well as numbers and the underscore
# \W    not a word character
# A|B     either A or B
# (...)   a group
# (?:...) non-capturing version
# if re.search(r"^\w+@+\w+\.(com|edu|gov|net|org)$", email):
#     print("Valid")
# else:
#     print("Invalid")

#Flags!!
# re.IGNORECASE
# re.MULTILINE
# re.DOTALL
if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")