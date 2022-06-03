import json
import base64

class ReadConfig:
    """Class representing the common properties"""
    
    @staticmethod
    def _read_config():
        """method to read the config file"""
        with open(".\\Configurations\\Config.json", "r") as configFile:
            return json.loads(configFile.read()) 

    @staticmethod
    def get_url():
        """get URL from the config file"""
        configData = ReadConfig._read_config()
        return configData['url']
    
    @staticmethod
    def get_username():
        """get username from the config file"""
        configData = ReadConfig._read_config()
        username_bytes = configData['username'].encode('ascii')
        ascii_bytes = base64.b64decode(username_bytes)
        return ascii_bytes.decode('ascii')

    @staticmethod
    def get_password():
        """get password from the config file"""
        configData = ReadConfig._read_config()
        password_bytes = configData['password'].encode('ascii')
        ascii_bytes = base64.b64decode(password_bytes)
        return ascii_bytes.decode('ascii')

    
    @staticmethod
    def get_screenshotpath():
        """get screenshot path from the config file"""
        configData = ReadConfig._read_config()
        return configData['screenshotpath']
    
    @staticmethod
    def get_datafile_path():
        """get data file path from the config file"""
        configData = ReadConfig._read_config()
        return configData['datafilepath']
    
    @staticmethod
    def get_gh_token():
        """get github token from the config file"""
        configData = ReadConfig._read_config()
        return configData['token']