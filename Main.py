from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import urllib.request
import os
import pyfiglet
from ctypes import *
import multiprocessing
import asyncio
import threading

path = "‪H:\Parsing\chromedriver.exe"
options = webdriver.ChromeOptions()
# options.add_argument("--disable-setuid-sandbox")
# options.add_argument('headless')
driver = webdriver.Chrome(r"H:\Parsing\chromedriver.exe", options=options)
# os.system('cls')


imageLinks = []
LinkCount = 0
ScrollCount = 20
LoadingDelay = 5
Save_Path = "L:\\"
LoginSuccess = True
GetPage = True
LoadingArt = ["|", "/", "~", "\\"]
ShowLoading = False


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value # bytes 인스턴스



def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


STD_OUTPUT_HANDLE = -11


class COORD(Structure):
    pass


COORD._fields_ = [ ("X", c_short), ("Y", c_short) ]


def printxy(r, c, s):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))

    c = s.encode("windows-1252")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)


class Twitter:
    global driver

    def Loading_UI(self):
        global LoadingArt, ShowLoading
        while True:
            for art in LoadingArt:
                if ShowLoading is True:
                    printxy(21, 50, art)
                    time.sleep(0.2)
                # else:
                #     print("return")
                #     return

    def LoadingThread(self):
        Loading = threading.Thread(target=self.Loading_UI)
        Loading.daemon = True
        Loading.start()

    def login_twitter(self):
        global GetPage, LoginSuccess, ShowLoading
        # self.UI()


        print("Login Check")
        if LoginSuccess is not True:
            printxy(22, 51, "Login Failed")


        print("Get Page")
        if GetPage:
            driver.get("https://twitter.com/i/likes")
            GetPage = False


        print("Input")
        # printxy(15, 45, "ID > ")
        # username = input()
        # printxy(17, 45, "PW > ")
        # password = input()

        username = "mlpmain6@gmail.com"
        password = "happil3571569"

        ShowLoading = True

        username_field = driver.find_element_by_class_name("js-username-field")
        password_field = driver.find_element_by_class_name("js-password-field")

        username_field.send_keys(username)
        driver.implicitly_wait(0.5)

        password_field.send_keys(password)
        driver.implicitly_wait(0.5)
        driver.find_element_by_class_name("EdgeButtom--medium").click()
        # if driver.find_element_by_class_name("EdgeButtom--medium").click() is None:
        #     os.system("cls")
        #     LoginSuccess = False
        #     ShowLoading = False
        #     self.login_twitter()
        # else:
        #     LoginSuccess = True
        #     ShowLoading = False

        return 0

    def LoginThread(self):
        Login = threading.Thread(target=self.login_twitter)
        Login.daemon = True
        Login.start()

    def Get_ImagesThread(self):
        try:

            for link in driver.find_elements_by_css_selector('div.AdaptiveMedia-photoContainer'):
                imageLinks.append(link.get_attribute('data-image-url'))
                print("[!]Found :%s" % len(imageLinks))
                LinkCount += 1

                if imageLinks[LinkCount - 2] == imageLinks[LinkCount - 1] and LinkCount > 1:
                    print('Del')
                    del imageLinks[imageLinks]
                    LinkCount -= 1
                # else:
                #     LinkList.write(imageLinks[LinkCount-1]+ '\n')

                # if LinkCount > 10:
                #     print(imageLinks, LinkCount)
                #     return

        except Exception as e:
            print("error:", e)

    def SaveFile(self):
        if os.path.isfile("L:\LinkList.txt"):
            print("Remove")
            os.remove("L:\LinkList.txt")

        print("File Open")
        html = open("L:\LinkList.txt", 'wb')

        print("data=")
        data = driver.page_source

        print("Write")
        html.write(to_bytes(data))

        html.close()

    def Get_Images(self):
        global LinkCount, ScrollCount, LoadingDelay
        elem = driver.find_element_by_tag_name("body")
        now = time.localtime()
        s = "%04d-%02d-%02d %02d:%02d:%02d" % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        print(s)

        count = 0
        while (ScrollCount > 0):
            count += 1
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("Page Down")
            # elem.send_keys(Keys.PAGE_DOWN)
            elem.send_keys(Keys.END)

            time.sleep(LoadingDelay)
            if count % 5 == 0:
                self.SaveFile()
            # ScrollCount -=1

            print(count)
        return 0

    def Download_Images(self):
        for link in imageLinks:
            Image_name = link.replace("https://pbs.twimg.com/media/", "")
            with urllib.request.urlopen(link) as res:
                res_data = res.read()
                with open(Save_Path + Image_name, 'wb') as file:
                    file.write(res_data)
            print(link)
        return 0

    def UI(self):
        printxy(28, 110, "v 1.0")
        printxy(6, 20, "  _______       _ _   _               _____                    _            ")
        printxy(7, 20, " |__   __|     (_| | | |             / ____|                  | |          ")
        printxy(8, 20, "    | __      ___| |_| |_ ___ _ __  | |     _ __ __ ___      _| | ___ _ __ ")
        printxy(9, 20, "    | \ \ /\ / | | __| __/ _ | '__| | |    | '__/ _` \ \ /\ / | |/ _ | '__|")
        printxy(10, 20, "    | |\ V  V /| | |_| ||  __| |    | |____| | | (_| |\ V  V /| |  __| |   ")
        printxy(11, 20, "    |_| \_/\_/ |_|\__|\__\___|_|     \_____|_|  \__,_| \_/\_/ |_|\___|_|   ")
        printxy(12, 20, "                                                                           ")

    def Run(self):
        self.login_twitter()
        self.Get_Images()
        self.Download_Images()


if __name__ == "__main__":
    t = Twitter()
    # t.LoadingThread()
    # t.LoginThread()
    t.Run()


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
#
# # initialize the driver
# driver = webdriver.Chrome(r"H:\Parsing\chromedriver.exe", options=options)
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

# print(pyfiglet.figlet_format("                         ", font="banner3-D"))
# print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# printxy(2, 2, pyfiglet.figlet_format(" Twitter ", font="banner3-D"))
# print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\r                                                                                                      ")
# x = 5
# for str in pyfiglet.figlet_format(" Twitter ", font="banner3-D"):
#     # if str == '\n':
#     #     break
#     printxy(0, x, str)
#     x += 1
