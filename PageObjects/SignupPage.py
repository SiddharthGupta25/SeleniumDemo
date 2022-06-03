from Utils.CommonUtils import CommonUtils
from selenium.webdriver.common.by import By
import allure


class SignupPage:
    """
    Class representing the register page of AUT on the following 
    url : https://accounts.lambdatest.com/register
    """

    def __init__(self, driver, commonutils: CommonUtils):
        """Constructor"""
        self.element = None
        self.driver = driver
        self.commonutils = commonutils

    # All locators of the given URL

    google_signup_link = (By.XPATH, "//a[@href='/login/google']")
    github_signup_link = (By.XPATH, "//a[@href='/login/github/v1']")
    full_name_field = (By.XPATH, "//input[@placeholder='Full Name*']")
    bussiness_email_field = (By.XPATH, "//input[@type='email' and @placeholder='Business Email*']")
    password_field = (By.XPATH, "//input[@placeholder='Desired Password*']")
    phone_field = (By.XPATH, "//input[@placeholder='Phone*']")
    country_code_dropdown = (By.XPATH, "//select[@data-testid='country_code']")
    i_agree_checbox = (By.XPATH,
                       "//samp[@class='customcheckbox w-20 h-20 inline-block bg-white border border-gray-20 relative cursor-pointer mr-10']")
    free_signup_button = (By.XPATH, "//button[@type='submit' and text()='FREE SIGN UP']")

    @allure.step("Enter Full Name in the Full Name Textbox")
    def set_fullname(self, name):
        """Enter specified username in Full Name textbox"""
        self.element = self.commonutils.seek_element(self.full_name_field)
        self.element.clear()
        self.element.send_keys(name)

    @allure.step("Enter a valid business email in Business Email textbox")
    def set_bussiness_email(self, email):
        """Enter specified email in the Business Email textbox"""
        self.commonutils.do_send_keys(self.bussiness_email_field, email)

    @allure.step("Enter a password in the 'Desired Password' password box")
    def set_password(self, password):
        """Enter specified password in the Desired Password textbox"""
        self.commonutils.do_send_keys(self.password_field, password)

    @allure.step("Select a country code from the Country Code Dropdown")
    def set_country_code(self):
        pass

    @allure.step("Enter a Phone number in the Phone No. textbox")
    def set_phone(self, phoneNo):
        """Enter specified phone number in the Phone Textbox"""
        self.commonutils.do_send_keys(self.phone_field, phoneNo)

    @allure.step("Accept the terms and conditions")
    def set_i_agree_checbox(self):
        """Tick/Untick a specified checkbox"""
        self.commonutils.do_click(self.i_agree_checbox)

    @allure.step("Click on 'Free Signup Button' ")
    def click_free_signup_button(self):
        """Click on free signup button"""
        self.commonutils.do_click(self.free_signup_button)
