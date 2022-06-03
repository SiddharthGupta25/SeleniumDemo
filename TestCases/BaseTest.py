import pytest
from Utils.ReadConfig import ReadConfig
from Utils.FrameworkLogger import FrameworkLogger

@pytest.mark.usefixtures("setup")
class BaseTest:
    """Common class for all test cases"""
    pass
