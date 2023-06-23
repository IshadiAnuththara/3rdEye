import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplication(self):
        url = config.get('common data', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common data', 'password')
        return password

    @staticmethod
    def getInvalidUsername():
        invalidUsername = config.get('common data', 'invalidUsername')
        return invalidUsername

    @staticmethod
    def getInvalidPassword():
        invalidPassword = config.get('common data', 'invalidPassword')
        return invalidPassword
