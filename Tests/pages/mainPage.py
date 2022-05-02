from selenium.webdriver.common.by import By

class MainPage():

    def __init__(self, driver):
        self.driver = driver
        self.kv_text_id = 'motorkV'
        self.battVolt_text_id = 'battVolt'
        self.pinion_text_id = 'pinion'
        self.spur_text_id = 'spur'
        self.fgr_text_id = 'fgr'
        self.radius_text_id = 'wheelradius'
        self.calculate_button = '/html/body/div[2]/div[1]/form/input[7]'
        self.navbar_about_link_text = 'About My RC Truck'
        self.navbar_questionOfDay_link_text = 'Question of the Day'

    def enter_motorKV(self, kV):
        self.driver.find_element(By.ID, self.kv_text_id).clear()
        self.driver.find_element(By.ID, self.kv_text_id).send_keys(kV)

    def enter_battVolt(self, volt):
        self.driver.find_element(By.ID, self.battVolt_text_id).clear()
        self.driver.find_element(By.ID, self.battVolt_text_id).send_keys(volt)

    def enter_pinion(self, pinion):
        self.driver.find_element(By.ID, self.pinion_text_id).clear()
        self.driver.find_element(By.ID, self.pinion_text_id).send_keys(pinion)

    def enter_spur(self, spur):
        self.driver.find_element(By.ID, self.spur_text_id).clear()
        self.driver.find_element(By.ID, self.spur_text_id).send_keys(spur)

    def enter_fgr(self, fgr):
        self.driver.find_element(By.ID, self.fgr_text_id).clear()
        self.driver.find_element(By.ID, self.fgr_text_id).send_keys(fgr)

    def enter_wheelRadius(self, rad):
        self.driver.find_element(By.ID, self.radius_text_id).clear()
        self.driver.find_element(By.ID, self.radius_text_id).send_keys(rad)

    def click_calculate(self):
        self.driver.find_element(By.XPATH, self.calculate_button).click()

    def click_navbar_aboutPage_link(self):
        self.driver.find_element(By.LINK_TEXT, self.navbar_about_link_text).click()

    def click_navbar_questions_link(self):
        self.driver.find_element(By.LINK_TEXT, self.navbar_questionOfDay_link_text).click()
