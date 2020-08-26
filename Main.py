from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains
import sys
import time
import urllib.request
import os
# import pyfiglet
from ctypes import *


options = webdriver.ChromeOptions()
options.add_argument("--disable-setuid-sandbox")
# options.add_argument('headless')
driver = webdriver.Chrome(r"./chromedriver.exe", options=options)
os.system('cls')

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
    global driver
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/nav/div[2]/div[4]/a").click()
    driver.find_element_by_xpath("//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div[2]/a[1]").click()
    time.sleep(2)
    try:
        # driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/header/div[2]/div[1]/div/div[2]/div/div[1]/a").click()
        time.sleep(0.2)
        driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input").send_keys(_id)
        time.sleep(0.2)
 
        driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input").send_keys(_pass)
        time.sleep(0.2)

        driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div").click()
    except:
        print("Login Error")
    return 0

def Download_Images(Save_Path, DownloadedList, ImgLinkList):
    for link in ImgLinkList:
        if link not in DownloadedList:
            ImgName = link.replace("https://pbs.twimg.com/media/", "")
            try:
                with urllib.request.urlopen(link) as res:
                    res_data = res.read()
                    with open(Save_Path + ImgName, 'wb') as file:
                        file.write(res_data)
                        printxy(27, 49, "[!]DownLoading :%s" % len(DownloadedList))
                        del ImgLinkList[ImgLinkList.index(link)]
                        DownloadedList.append(link)
            except Exception as e:
                print(e)
        else:
            del ImgLinkList[ImgLinkList.index(link)]
    return 0

def findLastTweet_Index():      
    for i in range(0, 30):
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[" + str(i + 1) + "]")
        except Exception as e:
            # print(e)
            return i
        
def findAll_Images(_str, OrgImgLinkList):
    strlist = []
    while(True):
        OrgOffset = _str.find("src=\"https://pbs.twimg.com/media/")
        if OrgOffset == -1:
            break
        else:
            From = OrgOffset + 5
            To = OrgOffset + 48
            src = ""
            if "jpg" in _str[OrgOffset + 5 : OrgOffset + 59]:
                src = _str[From : To] + ".jpg"  
                
            elif "png" in _str[OrgOffset + 5 : OrgOffset + 59]:
                src = _str[From : To] + ".png"  
                
            else:
                # print(_str[OrgOffset + 5 : OrgOffset + 59])
                print("Error : FindAll_Images")
                exit(-1)
                
            # print("src :" + src)
            if src not in OrgImgLinkList:
                strlist.append(src)
            _str = _str.replace("src=\"https://pbs.twimg.com/media/", "", 1)
    return strlist


def RemoveLike(maxTweetID):
    ID = 0
    for id in range(0, maxTweetID):
        try:
            html = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[" + str(id + 1) + "]")
            Check1 = html.get_attribute('innerHTML').count("src=\"https://pbs.twimg.com/media/")
            Check2 = html.get_attribute('innerHTML').count("data-testid=\"unlike\"")
            if Check1 == 0 or Check2 == 0:
                continue
            button = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[" + str(id + 1) + "]/div/article/div/div/div[2]/div[2]/div[2]/div[3]/div[3]/div")
            button.click()
            ID = id
        except Exception as e:
            pass
    return ID

if __name__ == "__main__":
    # driver.get("https://twitter.com/D3vFox")
    # time.sleep(2)
    # driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/nav/div[2]/div[4]/a").click()
    # driver.find_element_by_xpath("//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div[2]/a[1]").click()
    url = input('Url ( ex. https://twitter.com/User/likes ) :')
    Save_Path = input('PATH ( ex. C:\\twitter\\ ) :')
    _id = input('ID ( twitter Email ) :')
    _pass = input('PASS ( twitter Password ) :')
    Flag_RemoveLike = input("Remove likes? ( y/n ) :")

    
    os.system('cls')
    OpenPage(url)
    time.sleep(3)
    
    login_twitter(_id, _pass)
    time.sleep(2)
    
    driver.get(url)
    time.sleep(2)
    
    DownloadedList = []
    TweetID = 1
    OrgImgLinkList = []
    
    while(True):
        html = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div")
        temp = findAll_Images(html.get_attribute('innerHTML'), OrgImgLinkList)
        if len(temp) != 0:
            OrgImgLinkList = OrgImgLinkList + temp
            maxTweetID = findLastTweet_Index()
            if Flag_RemoveLike == "y":
                temp = maxTweetID
                maxTweetID = RemoveLike(maxTweetID)
                if maxTweetID == 0:
                    maxTweetID = temp
            time.sleep(2)
            while(True):
                try:
                    Element = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[" + str(maxTweetID) + "]")
                    ActionChains(driver).move_to_element(Element).perform()
                    break
                except Exception as e:
                    pass
            Download_Images(Save_Path, DownloadedList, OrgImgLinkList)
            time.sleep(4)
        else:
            break