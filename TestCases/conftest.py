from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
import pytest, allure


# to execute all the test cases within the same browser session, set scope to session

@pytest.fixture(scope="class")
def setup(browser):
    global driver

    if browser == "chrome":
        service_params = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(service=service_params,
                                  options=chrome_options)
    elif browser == "firefox":
        service_params = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service_params)
    else:
        service_params = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service_params)

    driver.maximize_window()

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.mark.hookwrapper
def pytest_runtest_makereport():
    outcome = yield
    file_name = ""
    report = outcome.get_result()
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            try:
                file_name = report.nodeid.replace("::", "_") + ".png"
                if file_name is not None:
                    allure.attach(driver.get_screenshot_as_png(), name=file_name, attachment_type=AttachmentType.PNG)

            except Exception as e:
                print(f"unable to take screenshot as {file_name} is not found")
