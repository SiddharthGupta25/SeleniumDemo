from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.FrameworkLogger import FrameworkLogger


class CommonUtils:
    """Parent class of all pages representing generic functionality"""

    # duration for explicit wait 
    WAIT_DURATION = 20


    def __init__(self, driver):
        """Constructor for CommonUtils"""
        self.driver = driver
        self.logger = FrameworkLogger().get_framework_logger()

    def do_click(self, by):
        """Base method for clicking an element specified using instance of By"""
        try:
            WebDriverWait(self.driver, self.WAIT_DURATION).until(EC.element_to_be_clickable(by)).click()
        except Exception as e:
            self.logger.exception(e)

    def do_send_keys(self, by, text):
        """Base method for sending keys to an element specified using instance of By"""
        try:
            WebDriverWait(self.driver, self.WAIT_DURATION).until(EC.visibility_of_element_located(by)).clear()
            WebDriverWait(self.driver, self.WAIT_DURATION).until(EC.visibility_of_element_located(by)).send_keys(text)
        except Exception as e:
            self.logger.exception(e)

    def is_visible(self, by):
        """Base method for checking the visibility to an element specified using instance of By"""
        return bool(WebDriverWait(self.driver, self.WAIT_DURATION).until(EC.visibility_of_element_located(by)))

    def get_title(self):
        """Returns the title of the page"""
        return self.driver.title

    def get_url(self, url):
        """Navigates to the specified URL"""
        self.driver.get(url)

    def seek_element(self, by):
        """Returns an element with the specified locator strategy"""
        try:
            return WebDriverWait(self.driver, self.WAIT_DURATION).until(EC.visibility_of_element_located(by))
        except Exception as e:
            self.logger.error("[-] Something went wrong!")
            self.logger.error(e)

    def seek_element_id(self, id):
        """Returns an element with the specified ID"""
        try:
            return WebDriverWait(self.driver, self.WAIT_DURATION).until(EC.visibility_of_element_located((By.ID, id)))
        except Exception as e:
            self.logger.error("[-] Something went wrong!")
            self.logger.error(e)

    def seek_element_name(self, name):
        """Returns an element with the specified name"""
        try:
            return WebDriverWait(self.driver, self.WAIT_DURATION).until(
                EC.visibility_of_element_located((By.NAME, name)))
        except Exception as e:
            self.logger.error("[-] Something went wrong!")
            self.logger.error(e)

    def seek_element_classname(self, classname):
        """Returns an element with the specified class name"""
        try:
            return WebDriverWait(self.driver, self.WAIT_DURATION).until(
                EC.visibility_of_element_located((By.CLASS_NAME, classname)))
        except Exception as e:
            self.logger.error("[-] Something went wrong!")
            self.logger.exception(e)

    def seek_element_linktext(self, linktext):
        """Returns an element with the specified link text"""
        try:
            return WebDriverWait(self.driver, self.WAIT_DURATION).until(
                EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, linktext)))
        except Exception as e:
            self.logger.error("[-] Something went wrong!")
            self.logger.exception(e)

    def wait_for_title_to_be(self, title):
        """Wait for a duration till the title of the current page matches the specification"""
        try:
            WebDriverWait(self.driver, self.WAIT_DURATION).until(EC.title_contains(title))
        except Exception as e:
            self.logger.exception(e)



