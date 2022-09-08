import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getBaseURL():
        url = config.get("common info", "base_url")
        return url

    @staticmethod
    def getUserName():
        user_name = config.get("common info", "user")
        return user_name

    @staticmethod
    def getPwd():
        password = config.get("common info", "pwd")
        return password
