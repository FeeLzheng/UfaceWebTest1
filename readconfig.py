import os
import configparser


prodir=os.path.split(os.path.realpath(__file__))[0]
configPath=os.path.join(prodir,"config.ini")


class readconfig():
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_HTTP(self, name):
        value = self.cf.get("HTTP", name)
        return value