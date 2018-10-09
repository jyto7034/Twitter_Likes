from selenium import webdriver

driver = webdriver.Firefox()
imageLinks = []
LinkCount=0

class Twitter():
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
                print(imageLinks)
                # LinkCount += 1
                # if imageLinks[LinkCount-2] == imageLinks[LinkCount-1] and LinkCount >1 or LinkCount < 10 :
                #     del imageLinks[imageLinks]
                #     LinkCount -=1
                #     print('Succ')
                # print(imageLinks)
        except Exception as e:
            print(e)



if __name__ == "__main__":
    Twitter.login_twitter("mlpmain6@gmail.com", "dlrudgus12")
    ti = Twitter()
    driver.implicitly_wait(10)
    ti.Get_Images()