from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import requests
import subprocess

username = "you@yourdomain.com"
authkey  = "yourauthkey"

def before_feature(context, feature):
    caps = {}
    caps['name'] = 'Behave Example'
    caps['build'] = '1.0'
    caps['browserName'] = "Chrome"      # pulls the latest version of Chrome by default
    caps['platform'] = "Windows 10"     # to specify a version, add caps['version'] = "desired version"
    caps['screen_resolution'] = '1366x768'
    caps['record_video'] = 'true'
    caps['record_network'] = 'true'
    caps['take_snapshot'] = 'true'

    context.driver = webdriver.Chrome('./chromedriver')

    
def after_feature(context, feature):
    context.driver.quit() 
