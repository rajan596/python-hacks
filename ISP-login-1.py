#! python 3
'''
API Url
http://selenium-python.readthedocs.org/api.html
'''

import time
from selenium import webdriver

def login(uname,pwd):

    try:
        # find elements
        username=driver.find_element_by_name("username")
        password=driver.find_element_by_name("password")

        # fill Keys
        username.send_keys(uname)
        password.send_keys(pwd)

        # submit form
        bSubmit=driver.find_element_by_name("btnSubmit")
        bSubmit.submit()
        
    except NoSuchElementException as e:
        print("You are already logged in")
        time.sleep(5)

def logout():
    try:
        bSubmit=driver.find_element_by_name("btnSubmit")
        bSubmit.submit()
    except NoSuchElementException as e:
        print(str(e))

if __name__=="__main__":
    # setting up browser
    try:
        driver=webdriver.Chrome()
    except Exception as e:
        driver=webdriver.Firefox()
        
    driver.set_window_size(600,700)
    driver.get("http://172.50.1.1:8090/httpclient.html")

    time.sleep(5)

    login(input("Username : "),input("Password : "))
    time.sleep(10)
    #logout()

'''
driver.current_url : TO get url of currently opened window
'''
