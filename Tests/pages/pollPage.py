from selenium.webdriver.common.by import By

class PollPage():
    def __init__(self, driver):
        self.driver = driver
        self.poll_radial_name = 'poll'
