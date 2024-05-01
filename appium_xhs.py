# ---
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: appium_xhs.py
# @Author: sunbcy
# @Institution: SYLG University, LiaoNing, China
# @E-mail: saintbcy@163.com
# @Time: 5月 02, 2024 02:47
# ---

# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:deviceName": "2201123C",
	"appium:appPackage": "com.xingin.xhs",
	"appium:appActivity": "com.xingin.xhs.index.v2.IndexActivityV2",
	"appium:noReset": True,
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="搜索")
el5.click()
el6 = driver.find_element(by=AppiumBy.ID, value="com.xingin.xhs:id/mSearchToolBarEt")
el6.click()
el6.send_keys("python")
el7 = driver.find_element(by=AppiumBy.ID, value="com.xingin.xhs:id/mSearchToolBarSearch")
el7.click()

driver.quit()
