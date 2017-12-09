#!/usr/bin/env python
import os
from Facebook_Creds import Event_Url,App_Name
import urllib	
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import Authentication
from selenium.webdriver.chrome.options import Options
from Notification import notify_event,success_notification,no_birthday_today
import xpaths
import base64 
from selenium.webdriver.support.ui import WebDriverWait
##Login Module for logging the user into facebook
def login(driver):
	email = driver.find_element_by_xpath(xpaths.creds["input_login"])
	email.send_keys(base64.b64decode(Authentication.Facebook_User_Id))
	#print("Email Id entered...")
	password = driver.find_element_by_xpath(xpaths.creds["input_password"])
	password.send_keys(base64.b64decode(Authentication.Facebook_Password))
	#print("Password entered...")
	button = driver.find_element_by_xpath(xpaths.creds["button_login"])
	button.click()
	#print "Logged into Facebook"
	Wish_Birthdays(driver)

## gets all the friends whose birthday is today and 
def Wish_Birthdays(driver):
		wishes = driver.find_elements_by_class_name(xpaths.Birthday_xpath_creds)
		print "wishing happy birthday"
		print len(wishes)
		if(len(wishes) == 0):
			no_birthday_today().show()
			return

		try:			
			for birthday in wishes:
				birthday.send_keys("Happy Belated Birthday :-) ")
				birthday.send_keys(Keys.ENTER)	
			success_notification().show()
			time.sleep(5)
			driver.quit()
		except:
 			BaseException("Could not decode the response from the Server")				

#main function that drives the Birthday
def main():
	notify_event().show()
	chrome_options = Options()
	#chrome_options.add_argument("--headless")
	chrome_options.add_argument("--window-size=1920x1080")
	driver = webdriver.Chrome(chrome_options = chrome_options,executable_path="/home/geekowl/Desktop/chromedriver")
	driver.get(Event_Url)
	
	login(driver)
