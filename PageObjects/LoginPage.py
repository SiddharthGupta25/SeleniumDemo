from selenium.webdriver.common.by import By
from Utils.CommonUtils import CommonUtils
from selenium.webdriver.common.keys import Keys
import allure


class LoginPage:
    """class representing lambda test login page"""

    def __init__(self, driver, commonutils : CommonUtils):
        """Constructor"""
        self.driver = driver
        self.commonutils = commonutils

    # All the locators of https://accounts.lambdatest.com/login"

    google_sign_in_link = (By.XPATH, "//a[@href='/login/google']")
    github_sign_in_link = (By.XPATH, "//a[@href='/login/github/v1']")
    email_field = (By.XPATH, "//input[@type='email' and @name='email']")
    password_field = (By.XPATH, "//input[@type='password' and @name='password']")
    login_button = (By.XPATH, "//button[text()='Login' and @id='login-button']")
    remember_me_checkbox = (By.XPATH, "//input[@type='checkbox']")
    forgot_password_link = (By.XPATH, "//a[text()='Forgot Password?']")
    sign_up_link = (By.XPATH, "//a[text()='Sign up']")
    google_email_field = (By.XPATH, "//input[@type='email' and @jsname='YPqjbf']")
    google_password_field = (By.XPATH, "//input[@type='password']")

    # actions for https://accounts.lambdatest.com/login" 

    def get_title(self):
        """Returns the title of the page"""
        return self.commonutils.get_title()

    @allure.step("Click on Google Sign-In Button")
    def click_google_sign_in_link(self):
        """clicks on 'Login with Google' link """
        self.commonutils.do_click(self.google_sign_in_link)

    @allure.step("Click on Github Sign-In Button")
    def click_github_sign_in_link(self):
        """clicks on 'Login with Github' link """
        self.commonutils.do_click(self.github_sign_in_link)

    @allure.step("Enter email address")
    def set_email_field(self, email: str):
        """Enters email on the page"""
        self.commonutils.do_send_keys(self.email_field, email)

    @allure.step("Enter Password")
    def set_password_field(self, password: str):
        """Enters password on the page"""
        self.commonutils.do_send_keys(self.password_field, password)

    @allure.step("Click on Login Button")
    def click_login_button(self):
        """clicks on 'Login' button"""
        self.commonutils.do_click(self.login_button)

    def enter_gmail_id(self, gmail_id):
        """Enters gmail id if logging in via google """
        self.element = self.commonutils.seek_element(self.google_email_field)
        self.element.send_keys(gmail_id)
        self.element.send_keys(Keys.ENTER)

    def enter_gmail_password(self, password):
        """Enters gmail password if logging in via google """
        self.element = self.commonutils.seek_element(self.google_password_field)
        self.element.send_keys(password)
        self.element.send_keys(Keys.ENTER)

