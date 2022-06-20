from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import sys
from os.path import exists
import colorama

# coded for python3.10+

# banner
colorama.init()
print(colorama.Fore.YELLOW + '''
   ___       __                       
  / _ \___  / /_____ __ _  ___  ___   
 / ___/ _ \/  '_/ -_)  ' \/ _ \/ _ \  
/_/___\___/_/\_\\\\__/_/_/_/\___/_//_/
    / _ \___ ___/ /__ ___ __ _  ___ ____
   / , _/ -_) _  / -_) -_)  ' \/ -_) __/
  /_/|_|\__/\_,_/\__/\__/_/_/_/\__/_/   
                                      ''' + colorama.Fore.RESET)

# arg check
if len(sys.argv) != 2:
    print(colorama.Fore.BLUE + "[*]" + colorama.Fore.RESET + f" usage: python3 {sys.argv[0]} <codes file>")
    sys.exit(1)

# get codes from file
codes_file = sys.argv[1]
if not exists(codes_file):
    print(colorama.Fore.RED + "[!]" + colorama.Fore.RESET + f" codes file '{codes_file}' does not exist")
    sys.exit(1)

CODES = []
with open(codes_file, "r") as rf:
    for c in rf.readlines():
        CODES.append(c.rstrip())

# let's go
print(colorama.Fore.BLUE + "[*]" + colorama.Fore.RESET + f" redeeming {str(len(CODES))} codes")

# get login info  
username = input(colorama.Fore.YELLOW + "[?]" + colorama.Fore.RESET + " username: ")
password = input(colorama.Fore.YELLOW + "[?]" + colorama.Fore.RESET + " password: ")

wd = webdriver.Firefox()

try:
    # login
    wd.get("https://sso.pokemon.com/sso/login?locale=en&service=https://www.pokemon.com/us/pokemon-trainer-club/caslogin")

    element = wd.find_element(By.ID, "username")
    element.send_keys(username)

    element = wd.find_element(By.ID, "password")
    element.send_keys(password)

    e2 = wd.find_element(By.ID, "btnLogin")
    e2.click()    

    # redeem codes
    wd.get("https://www.pokemon.com/us/pokemon-trainer-club/enter-codes")
    input(colorama.Fore.BLUE + "[*]" + colorama.Fore.RESET + " tell them that you're not a robot and hit enter..")

    # submit codes - 10 at a time max
    count = 0    
    for CODE in CODES:
        e3 = wd.find_element(By.ID, "id_redemption_code")
        e3.send_keys(CODE)
        sleep(1)

        e4 = wd.find_element(By.ID, "verify-code")
        e4.click()
        sleep(1)

        print(colorama.Fore.GREEN + "[+]" + colorama.Fore.RESET + f" redeeming '{CODE}'")

        count += 1

        if count % 10 == 0 or count == len(CODES):
            # check redeem all
            e5 = wd.find_element(By.ID, "redemption-check-all")
            e5.click()
            sleep(1)

            # redeem codes
            e6 = wd.find_element(By.ID, "redeem-code")
            e6.click()
            sleep(5)
    
    # all done
    print(colorama.Fore.BLUE + "[*]" + colorama.Fore.RESET + f" redeemed {str(count)} codes!")
except Exception as e:
    print(str(e))
finally:
    # logout
    wd.get("https://www.pokemon.com/us/pokemon-trainer-club/logout")
    wd.close()
    print(colorama.Fore.BLUE + "[*]" + colorama.Fore.RESET + " logged out")