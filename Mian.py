from selenium import webdriver
import sys

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
imageLinks = []
LinkCount=0

class Twitter():
    global driver
    def login_twitter(username, password):
        driver.get("https://twitter.com/i/likes")
        username_field = driver.find_element_by_class_name("js-username-field")
        password_field = driver.find_element_by_class_name("js-password-field")

        username_field.send_keys(username)
        driver.implicitly_wait(1)

        password_field.send_keys(password)
        driver.implicitly_wait(1)

        driver.find_element_by_class_name("EdgeButtom--medium").click()


    def Get_Images(self):
        global LinkCount
        try:
            for link in driver.find_elements_by_css_selector('div.AdaptiveMedia-photoContainer'):
                imageLinks.append(link.get_attribute('data-image-url'))
                LinkCount += 1
                if imageLinks[LinkCount-2] == imageLinks[LinkCount-1] and LinkCount > 1:
                    print('Del')
                    del imageLinks[imageLinks]
                    LinkCount -= 1
                if LinkCount > 10 :
                    print(imageLinks, LinkCount)
                    sys.exit(1)
            print(imageLinks, LinkCount)
        except Exception as e:
            print( "error:")
            print(e)



if __name__ == "__main__":
    Twitter.login_twitter("mlpmain6@gmail.com", "dlrudgus12")
    ti = Twitter()
    # driver.implicitly_wait(10)
    ti.Get_Images()




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
