from selenium.webdriver.common.by import By
class AboutPage():

    def __init__(self, driver):
        self.driver = driver
        self.slide_show_class = 'mySlides'
        self.about_slash_paragraph_class = 'about-my-slash'
        self.castle_link_linkText = 'Castle Creations'

    def click_castle_link(self):
        self.driver.find_element(By.LINK_TEXT, self.castle_link_linkText).click()
