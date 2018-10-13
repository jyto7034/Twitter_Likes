from selenium import webdriver
import sys
import time
import urllib.request
import os

path ="‪H:\Parsing\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(r"H:\Parsing\chromedriver.exe", options=options)
os.system('cls')
imageLinks = []
LinkCount=0
ScrollCount=10
LoadingDelay = 3
Save_Path = "L:\\"

LinkList = open("L:\LinkList.txt", 'w')

class Twitter():
    global driver
    def login_twitter(self, username, password):
        driver.get("https://twitter.com/i/likes")
        username_field = driver.find_element_by_class_name("js-username-field")
        password_field = driver.find_element_by_class_name("js-password-field")

        username_field.send_keys(username)
        driver.implicitly_wait(1)

        password_field.send_keys(password)
        driver.implicitly_wait(1)

        driver.find_element_by_class_name("EdgeButtom--medium").click()

    def Get_Images(self):
        global LinkCount, ScrollCount, LoadingDelay
        while(ScrollCount > 0):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            ScrollCount-=1
            time.sleep(LoadingDelay)

        try:

            for link in driver.find_elements_by_css_selector('div.AdaptiveMedia-photoContainer'):
                imageLinks.append(link.get_attribute('data-image-url'))
                print("[!]Found :%s" % len(imageLinks))
                LinkCount += 1

                if imageLinks[LinkCount-2] == imageLinks[LinkCount-1] and LinkCount > 1:
                    print('Del')
                    del imageLinks[imageLinks]
                    LinkCount -= 1
                # else:
                #     LinkList.write(imageLinks[LinkCount-1]+ '\n')

                if LinkCount > 10:
                    print(imageLinks, LinkCount)
                    # sys.exit(1)
                    return

        except Exception as e:
            print( "error:")
            print(e)

    def Download_Images(self):
        print("cALL")
        for link in imageLinks:
            Image_name = link.replace("https://pbs.twimg.com/media/", "")
            with urllib.request.urlopen(link) as res:
                res_data = res.read()
                with open(Save_Path  + Image_name, 'wb') as file:
                    file.write(res_data)
            print(link)
    def Run(self, usernamep, passwordp):
        self.login_twitter(usernamep, passwordp)
        self.Get_Images()
        self.Download_Images()

    def UI(self):
        print(" _______       _ _   _              _      _ _           _____                    _           ")
        print(" |__   __|     (_| | | |            | |    (_| |         / ____|                  | |          ")
        print("    | __      ___| |_| |_ ___ _ __  | |     _| | _____  | |     _ __ __ ___      _| | ___ _ __ ")
        print("    | \ \ /\ / | | __| __/ _ | '__| | |    | | |/ / _ \ | |    | '__/ _` \ \ /\ / | |/ _ | '__|")
        print("    | |\ V  V /| | |_| ||  __| |    | |____| |   |  __/ | |____| | | (_| |\ V  V /| |  __| |   ")
        print("    |_| \_/\_/ |_|\__|\__\___|_|    |______|_|_|\_\___|  \_____|_|  \__,_| \_/\_/ |_|\___|_|   ")




if __name__ == "__main__":
    t = Twitter()
    # t.Run("mlpmain6@gmail.com", "dlrudgus12")
    t.UI()

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
#
# # initialize the driver
# driver = webdriver.Chrome(options=options)
#
# driver.get("https://www.naver.com/")
#
# from selenium import webdriver
#
# options = webdriver.FirefoxOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# # 혹은 options.add_argument("--disable-gpu")
#
# driver = webdriver.Firefox(options=options)
#
# driver.get('http://naver.com')
# driver.implicitly_wait(3)
# driver.get_screenshot_as_file('naver_main_headless.png')
#
# driver.quit()
#
#
# from selenium import webdriver
# from requests import *
#
# driver = webdriver.Firefox()
# driver.get("https://twitter.com/login")
#
