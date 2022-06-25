# betterAutoJoiner - simply better
Automatically joins RBLXWILD rains

# Tutorial
  - https://www.youtube.com/watch?v=o2T-XJ3K0UE

# Usage
- Installation
  - python setup.py

- Configuration (.env)
  - APIKEY_2CAPTCHA to your 2captcha apikey (Create an account to [https://2captcha.com](https://2captcha.com?from=14049096))
  - USERNAME to your roblox username (Optional)
  - AUTHTOKEN to your RBLXWILD authToken (Can be found in localstorage)
  - SESSION to your RBLXWILD session (Can be found in cookies)
  - USERAGENT to an browser useragent ([What is my useragent?](https://www.whatismybrowser.com/detect/what-is-my-user-agent/))
  - PROXY to an SOCKS4 or SOCKS5 proxy (Optional)
  
- Start the joiner
  - python main.py

# Features
- Auto joins rain
- Low cpu usage and accurate
- Supports multiple accounts at once by adding them to .env

# Common issues
  - ISSUE: timeout exceed 120.0 (worker failed to complete captcha before the captcha expired) 
    - FIX: send captcha to be completed 100 seconds before the rain can be joined
  - ISSUE: closes instantly after running main.py / setup.py 
    - FIX: make sure you are running the same version as in runtime.txt

# Contact
- Discord: betterSupport#8964
