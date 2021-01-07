from selenium import webdriver
from time import sleep


class InstaBot:

    def __init__(self, user: str, password: str):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        self.user = user
        self.password = password

        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(
            user)

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(
            password)

        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()

        sleep(3)

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/div/div/div/button").click()

        sleep(2)

        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div/div[3]/button[2]").click()

        sleep(5)

    def get_unfollowers(self):
        # self.driver.find_element_by_xpath(
        #     "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a").click()

        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()

        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()

        following = self._get_names()

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()

        followers = self._get_names()

        not_following_back = [user for user in following if user not in followers]

        print('Not Following you Back: {}'.format(not_following_back))

        me_not_following_back = [user for user in followers if user not in following]

        print("You're not following back: {}".format(me_not_following_back))

        if len(followers) > len(following):
            print('You have {} more followers than following'.format(len(followers)-len(following)))

        elif len(followers) < len(following):
            print('You have {} more following than followers'.format(len(following)-len(followers)))

        else:
            print('You have the same number of followers as following'.format(
                len(following) - len(followers)))

    def _get_names(self):
        sleep(1)
        last_height, height = 0, 1

        scroll_box = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[2]')
        while last_height != height:
            last_height = height
            sleep(1)
            height = self.driver.execute_script("""
                        arguments[0].scrollTo(0, arguments[0].scrollHeight)
                        return arguments[0].scrollHeight
                        """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')

        sleep(1)
        names = [name.text for name in links if name.text != '']

        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()

        return names

bot = InstaBot('', '')
bot.get_unfollowers()
