import os, sys

# Create .env file #
print("Creating .env file..")

try:
    # Try to create .env file #
    env_file = open(".env", "x")
except:
    # .env file already exists? #
    env_file = open(".env", "w")

env_file.write(
"""# TOS
AGREED_TOS=False

# Debug
DEBUG_MODE=False

# Twocaptcha
APIKEY_2CAPTCHA=2captcha_apikey

# Accounts
USERNAME1=username
AUTHTOKEN1=authtoken
SESSION1=session
USERAGENT1=useragent
PROXY1=proxy

USERNAME2=username
AUTHTOKEN2=authtoken
SESSION2=session
USERAGENT2=useragent
PROXY2=proxy
""")

env_file.close()
print("Successfully created .env file!")

# Install requirements #
print("Installing requirements..")
os.system(f"{sys.executable} -m pip install -r requirements.txt")
print("Successfully installed requirements!")

print("Ready to go!")
# Copyright © 2022 Odsku. All rights reserved.