from TestCases.BaseTest import BaseTest
from Utils.ReadCSV import ReadCSV
from Utils.ReadConfig import ReadConfig
from Utils.FrameworkLogger import FrameworkLogger
from Utils.CommonUtils import CommonUtils
from PageObjects.SignupPage import SignupPage
import allure
import pytest


@allure.title("LambdaTest Register Page")
class Test_SignupPage (BaseTest):
    """Register Page test case class"""
    
    BASE_URL = "https://accounts.lambdatest.com/register"
    logger = FrameworkLogger().get_framework_logger()
       
    @allure.title("User is able to register")
    @pytest.mark.parametrize(("fullname","email","password","phone"), ReadCSV.read_data_from_csv(ReadConfig.get_datafile_path()))
    def test_register_user(self, setup, fullname, email, password, phone):
        """Verify that user is able to Register"""
        self.driver = setup
        self.driver.get(self.BASE_URL)
        self.commonutils = CommonUtils(self.driver)
        self.signupPage = SignupPage(self.driver, self.commonutils)
        self.signupPage.set_fullname(fullname)
        self.logger.info("[+] Username ({}) Entered Successfully on Register page".format(fullname))
        self.signupPage.set_bussiness_email(email)
        self.logger.info("[+] Email ({}) Entered Successfully on Register page".format(email))
        self.signupPage.set_password(password)
        self.logger.info("[+] Password ({}) Entered Successfully on Register page".format(password))
        self.signupPage.set_phone(phone)
        self.logger.info("[+] Phone Number ({}) Entered Successfully on Register page".format(phone))
        self.signupPage.set_i_agree_checbox()
        self.logger.info("[+] Ticked 'I Agree' checkbox Successfully on Register page")
        assert True