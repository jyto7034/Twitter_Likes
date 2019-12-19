from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import urllib.request
import os
# import pyfiglet
from ctypes import *


options = webdriver.ChromeOptions()
# options.add_argument("--disable-setuid-sandbox")
options.add_argument('headless')
driver = webdriver.Chrome(r"C:\Users\BlasterDinray\Desktop\Twitter_Likes\chromedriver.exe", options=options)
os.system('cls')

Save_Path = 'D:\\twitter\\'
DownloadedList = []
OrgImgLinkList = []
DownSuccess = 0
STD_OUTPUT_HANDLE = -11
class COORD(Structure):
    pass
COORD._fields_ = [ ("X", c_short), ("Y", c_short) ]
def printxy(r, c, s):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
    c = s.encode("windows-1252")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)
    return 0


def UI():
    printxy(28, 110, "v 1.0")
    printxy(6, 20, "  _______       _ _   _               _____                    _            ")
    printxy(
        7, 20, " |__   __|     (_| | | |             / ____|                  | |          ")
    printxy(
        8, 20, "    | __      ___| |_| |_ ___ _ __  | |     _ __ __ ___      _| | ___ _ __ ")
    printxy(
        9, 20, "    | \ \ /\ / | | __| __/ _ | '__| | |    | '__/ _` \ \ /\ / | |/ _ | '__|")
    printxy(
        10, 20, "    | |\ V  V /| | |_| ||  __| |    | |____| | | (_| |\ V  V /| |  __| |   ")
    printxy(
        11, 20, "    |_| \_/\_/ |_|\__|\__\___|_|     \_____|_|  \__,_| \_/\_/ |_|\___|_|   ")
    printxy(
        12, 20, "                                                                           ")
    return 0


def OpenPage(Link):
    driver.get(Link)
    return 0

def login_twitter(_id, _pass):
     driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input").send_keys(_id)
     driver.implicitly_wait(0.5)

     driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input").send_keys(_pass)
     driver.implicitly_wait(0.5)

     driver.find_element_by_class_name("EdgeButtom--medium").click()
     return 0


def Scroll():
     elem = driver.find_element_by_tag_name("body")
     elem.send_keys(Keys.END)
     return 0


def GetImgLinkAndNameFromSite():
    global OrgImgLinkList
    for link in driver.find_elements_by_css_selector('div.AdaptiveMedia-photoContainer'):
        ImgLink = link.get_attribute('data-image-url')
        if ImgLink not in OrgImgLinkList:
            OrgImgLinkList.append(ImgLink)
            printxy(26, 49, "[!]Found :%s" % len(OrgImgLinkList))
    return 0


def Download_Images():
    global DownSuccess, OrgImgLinkList, DownloadedList
    for link in OrgImgLinkList:
        if link not in DownloadedList:
            ImgName = link.replace("https://pbs.twimg.com/media/", "")
            try:
                with urllib.request.urlopen(link) as res:
                    res_data = res.read()
                    with open(Save_Path + ImgName, 'wb') as file:
                        file.write(res_data)
                        DownSuccess = DownSuccess + 1
                        printxy(27, 49, "[!]DownLoading :%s" % DownSuccess)
            except Exception as e:
                return 0
            DownloadedList.append(link)
    return 0



if __name__ == "__main__":
    UI()
    OpenPage('https://twitter.com/WTFCats3')
    driver.implicitly_wait(2)
    Scroll()
    driver.implicitly_wait(2)
    GetImgLinkAndNameFromSite()
    driver.implicitly_wait(2)
    Download_Images()
    os.system('cls')
    UI()
    while(True):
        driver.implicitly_wait(2)
        Scroll()
        driver.implicitly_wait(2)
        GetImgLinkAndNameFromSite()
        driver.implicitly_wait(2)
        Download_Images()
