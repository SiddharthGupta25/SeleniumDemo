from TestCases.BaseTest import BaseTest
from Utils.CommonUtils import CommonUtils
from Utils.ReadConfig import ReadConfig
from Utils.FrameworkLogger import FrameworkLogger
from PageObjects.LoginPage import LoginPage
import allure
import pytest


@allure.title("LambdaTest Login Page")
class Test_LoginPage(BaseTest):
    """Login test case class"""

    BASE_URL = ReadConfig.get_url()
    USERNAME = ReadConfig.get_username()
    PASSWORD = ReadConfig.get_password()
    logger = FrameworkLogger().get_framework_logger()

    @allure.title("User should be able to login")
    def test_login(self, setup):
        """Verify that user is able to login to lambdatest web application'"""
        self.driver = setup
        self.commonutils = CommonUtils(self.driver)
        self.commonutils.get_url(self.BASE_URL)
        self.loginPage = LoginPage(self.driver, self.commonutils)
        self.loginPage.set_email_field(self.USERNAME)
        self.logger.info("[+] Email Entered Successfully")
        self.loginPage.set_password_field(self.PASSWORD)
        self.logger.info("[+] Password Entered Successfully")
        self.loginPage.click_login_button()
        self.logger.info("[+] Clicked Login button")
        self.commonutils.wait_for_title_to_be("Welcome - Lambdatest")
        self.logger.info("[+] Title: {}".format(self.loginPage.get_title()))
        if self.commonutils.get_title() == "Welcome - Lambdatest":
            assert True
        else:
            assert False

    @allure.title("User is able to cick on google login button")
    @pytest.mark.skip("Not required right now")
    def test_click_google_login(self, setup):
        """Verify that user is able to click on google login button"""
        self.driver = setup
        self.commonutils = CommonUtils(self.driver)
        self.commonutils.get_url(self.BASE_URL)
        self.loginPage = LoginPage(self.driver, self.commonutils)
        self.commonutils.do_click(self.loginPage.google_sign_in_link)
        self.logger.info("[+] Clikced the button sucessfully")
        self.loginPage.enter_gmail_id(self.USERNAME)
        self.loginPage.enter_gmail_password(self.PASSWORD)
        assert True

    @allure.title("Signup link should be visible to the user")
    @pytest.mark.skip("Not required right now")
    def test_click_signup_link(self, setup):
        """Verify that user is able to click signup link"""
        self.driver = setup
        self.commonutils = CommonUtils(self.driver)
        self.loginPage = LoginPage(self.driver, self.commonutils)
        self.commonutils.is_visible(self.loginPage.sign_up_link)
        self.logger.info("[+] Signup link is visibble")
        assert True
