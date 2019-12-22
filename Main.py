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
# options.add_argument('headless')
driver = webdriver.Chrome(r"D:\Completed Work\Twitter_Likes\chromedriver.exe", options=options)
os.system('cls')

Save_Path = 'D:\\twitter\\'
DownloadedList = []
OrgImgLinkList = []
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
    global driver
    driver.get(Link)
    return 0

def login_twitter(_id, _pass):
     time.sleep(0.2)
     driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input").send_keys(_id)
     time.sleep(0.2)

     driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input").send_keys(_pass)
     time.sleep(0.2)

     driver.find_element_by_class_name("EdgeButtom--medium").click()
     return 0


def Scroll():
     elem = driver.find_element_by_tag_name("body")
     elem.send_keys(Keys.END)
     return 0


def GetImgLinkAndNameFromSite():
    global OrgImgLinkList, driver
    for link in driver.find_elements_by_class_name('css-9pa8cd'):
        try:
            ImgLink = link.get_attribute('src')
            if 'media' in ImgLink and 'name' in ImgLink:
                temp = ""
                s = ''.join(ImgLink)
                if 'jpg' in ImgLink:
                    temp += s[:ImgLink.find('?')]
                    temp += ".jpg"
                if 'png' in ImgLink:
                    temp += s[:ImgLink.find('?')]
                    temp += ".png"
                if temp not in OrgImgLinkList:
                    OrgImgLinkList.append(temp)
                    printxy(26, 49, "[!]Found :%s" % len(OrgImgLinkList))
        except Exception as e:
            print(e)
    return 0

#https://pbs.twimg.com/media/EMT_lrdUwAAGj-q?format=jpg&name=900x900
#https://pbs.twimg.com/media/EMT_lrdUwAAGj-q?format=jpg&name=medium
def Download_Images():
    global OrgImgLinkList, DownloadedList
    for link in OrgImgLinkList:
        if link not in DownloadedList:
            ImgName = link.replace("https://pbs.twimg.com/media/", "")
            try:
                with urllib.request.urlopen(link) as res:
                    res_data = res.read()
                    with open(Save_Path + ImgName, 'wb') as file:
                        file.write(res_data)
                        printxy(27, 49, "[!]DownLoading :%s" % len(DownloadedList))
            except Exception as e:
                print(e)
            DownloadedList.append(link)
    return 0



if __name__ == "__main__":
    url = 'https://twitter.com/D3vFox/likes'
    _id = 'jyto7034@gmail.com'
    _pass = 'dlrudgus12'
    # OpenPage(url)
    # login_twitter(_id, _pass)
    # print(len(driver.find_elements_by_class_name('css-9pa8cd')))
    # time.sleep(3)
    # GetImgLinkAndNameFromSite()


    # url = input('Url :')
    # _id = input('ID :')
    # _pass = input('PASS :')


    os.system('cls')
    OpenPage(url)
    login_twitter(_id, _pass)
    UI()
    time.sleep(2)
    Scroll()
    os.system('cls')
    UI()
    while(True):
        time.sleep(2)
        Scroll()
        time.sleep(3)
        GetImgLinkAndNameFromSite()
        time.sleep(2)
        Download_Images()
