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
options.add_argument('headless')
driver = webdriver.Chrome(r"D:\Completed Work\Twitter_Likes\chromedriver.exe", options=options)
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

     driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/header/div[2]/div[1]/div/div[2]/div/div[1]/a").click()

     time.sleep(0.2)
     driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input").send_keys(_id)
     time.sleep(0.2)

     driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input").send_keys(_pass)
     time.sleep(0.2)

     driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/form/div/div[3]/div").click()
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
    
    
def GetImageXpathPattern(Count_of_Image, TweetCount, Current_Image_Index):
    STweetCount = str(TweetCount)
    if Count_of_Image == 1:
        return "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[" + STweetCount + "]/div/article/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/a/div/div[2]/div/img"

    elif Count_of_Image == 2:
        return "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[" + STweetCount + "]/div/article/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/a[" + str(Current_Image_Index) + "]/div/div/img"
        
    elif Count_of_Image == 3:
        if Current_Image_Index == 1:
            return "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[" + STweetCount + "]/div/article/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/a/div/div/img"
        else:
            return "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[" + STweetCount + "]/div/article/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/a[" + str(Current_Image_Index) + "]/div/div/img"
            
    elif Count_of_Image == 4:
        if Current_Image_Index == 1:
            return "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[" + STweetCount + "]/div/article/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[" + str(1) + "]/a[" + str(1) + "]/div/div/img"
        elif Current_Image_Index == 2:
            return "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[" + STweetCount + "]/div/article/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[" + str(1) + "]/a[" + str(2) + "]/div/div/img"
        elif Current_Image_Index == 3:
            return "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[" + STweetCount + "]/div/article/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[" + str(2) + "]/a[" + str(1) + "]/div/div/img"
        elif Current_Image_Index == 4:
            return "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[" + STweetCount + "]/div/article/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[" + str(2) + "]/a[" + str(2) + "]/div/div/img"

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
                # print("Error")
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
    start = time.time()
    
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
    print(len(OrgImgLinkList),  " Images")
    print("time :", time.time() - start)
    
    
    #/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/article/div/div/div[2]/div[2]/div[2]/div[4]/div[3]/div
    #/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[2]/div/article/div/div/div[2]/div[2]/div[2]/div[3]/div[3]/div
    #/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[3]/div/article/div/div/div[2]/div[2]/div[2]/div[3]/div[3]/div
    
    
    # # html 에서 이미지소스 위치 얻기
    # OrgOffset = html.find("src=\"https://pbs.twimg.com/media/")
    
    # # https:// ~ 사진이름 까지의 슬라이싱을 위한 변수
    # From = OrgOffset + 5
    # To = OrgOffset + 48
    
    # # https:// ~ 확장자까지 슬라이싱
    # src = html[OrgOffset + 5 : OrgOffset + 59]
    
    # # 사진의 링크얻고 확장자 판별 및 수정하는 부분
    # if "jpg" in src:
    #     ImgLink = html[From : To] + ".jpg"
    # elif "png" in src:
    #     ImgLink = html[From : To] + ".png"
    # else:
    #     print("Cannot find extension")

    # for Current_ImageID in range(0, ImgCnt):
    #     try:
    #         # 이미지가 존재하는 xpath 얻기
    #         xpath = GetImageXpathPattern(ImgCnt, TweetID, Current_ImageID + 1)
    #         # 사진의 element 얻기
    #         link = driver.find_element_by_xpath(xpath)
    #         # 사진의 링크 얻기
    #         imgLink = link.getattribute('src')
    #     except Exception as e:
    #         if e == exceptions.NoSuchElementException:
    #             TweetID = findLastTweet_Index(10, 0, TweetID)
    #         else:
    #             print(e)
    #             exit(-1)
    
    # while(True):
    #     while(True):
    #         try:
    #             xpath = GetImageXpathPattern(Count_of_Image, TweetCount, Current_Image_Index)
    #             Link = driver.find_element_by_xpath(xpath)
    #             ImgLink = Link.get_attribute('src')
    #             if ImgLink not in ImgLinkList:
    #                 ImgLinkList.append(ImgLink)
    #                 print(ImgLink)
    #             else:
    #                 break
    #             Current_Image_Index += 1

    #         except Exception as e:
    #             if Count_of_Image == 4:
    #                 break 
    #             Count_of_Image += 1
    #             if e == exceptions.StaleStaleElementReferenceException:
    #                 TweetCount = 1

    #     body.send_keys(Keys.PAGE_DOWN)
    #     Current_Image_Index = 1
    #     Count_of_Image = 1
    #     TweetCount += 1
    #     time.sleep(2)
    


# 1
#/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[ N ]/div/article/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/a/div/div[2]/div/img

# 2
#/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[ N ]/div/article/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/a[ ImgCount ]/div/div/img

# 3
#/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[ N ]/div/article/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/a/div/div/img
#/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[ N ]/div/article/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/a[ ImgCount ]/div/div/img

# 4
#/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[ N ]/div/article/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[ ImgCount_1D ]/a[ ImgCount_2D ]/div/div/img

# Button
#/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[ N ]/div/article/div/div/div[2]/div[2]/div[2]/div[3]/div[3]/div
