# ---
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: appium_damai.py
# @Author: sunbcy
# @Institution: SYLG University, LiaoNing, China
# @E-mail: saintbcy@163.com
# @Time: 5月 02, 2024 02:39
# ---

"""虽然能用,但是appium很慢"""
# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
# from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
DESIRED_CAPABILITIES = {
	"platformName": "Android",
	"appium:deviceName": "2201123C",
	"appium:appPackage": "cn.damai",
	"appium:appActivity": ".homepage.MainActivity",
	"appium:noReset": True
	# "appium:ensureWebviewsHavePages": True,
}
PACKAGE_NAME = DESIRED_CAPABILITIES['appium:appPackage']
options.load_capabilities(DESIRED_CAPABILITIES)

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
wait = WebDriverWait(driver, 10)

el1 = driver.find_element(by=By.XPATH, value=f"//android.widget.TextView[@resource-id=\"{PACKAGE_NAME}:id/tab_text\" and @text=\"我的\"]")
el1.click()
el2 = driver.find_element(by=By.XPATH, value=f"//android.widget.TextView[@resource-id=\"{PACKAGE_NAME}:id/tv_name\" and @text=\"想看&想玩\"]")
el2.click()

driver.quit()
