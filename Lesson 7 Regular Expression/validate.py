import re

email = input("WHAT IS YOUR EMAIL ADDRESS? ").strip()
# if "@" in email and "." in email:
#     print("Vaild")
# else:
#     print("Invalid")
# username, domain = email.split("@")
# if (username) and (domain.endswith(".edu") or domain.endswith(".com")):
#     print("Valid")
# else:
#     print("Invalid")

# if re.search((r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$"),email) or re.search((r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$"),email):
# if re.search((r"^\w+@\w+\.(com|edu|gov|net)$"),email, re.IGNORECASE):   
if re.search((r"^\w+@\w+\.\w+\.(com|edu|gov|net)$"),email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")