from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome(ChromeDriverManager().install())


class YoutubeBot():
    def __init__(self, searchTerm):
        self.searchTerm = searchTerm
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://youtube.com')

    def searchYoutube(self):
        search_input = self.driver.find_element_by_xpath(
            "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input")
        search_input.send_keys(self.searchTerm)
        search_input.send_keys(Keys.ENTER)
        sleep(3)

        for x in range(5):

            link = self.driver.find_element_by_xpath(
                f'/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{x+1}]/div[1]/ytd-thumbnail/a')
            ActionChains(self.driver).move_to_element(link).key_down(
                Keys.COMMAND).click(link).key_up(Keys.COMMAND).perform()
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()


bot = YoutubeBot(input("What would you like to search for? "))
bot.searchYoutube()
