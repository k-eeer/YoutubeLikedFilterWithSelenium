# -*- coding: utf-8 -*-
import mysql.connector
import time,glob,os,getpass,sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


gmailId=getpass.getpass("please input your Gmail id:\n")
gPasswd=getpass.getpass("please input your Gmail password:\n")
keywd=input(sys.stderr.write("please input keyword that you want to search:\n"))
driver=webdriver.Firefox()

#Login google account with page of stackoverflow
def loginWithOtherSite():
	driver.get("https://stackoverflow.com/users/login")
	time.sleep(4)
	driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/button[1]').click()
	time.sleep(2)
	inputField=driver.find_element_by_id("identifierId")
	inputField.click()
	time.sleep(2)
	inputField.send_keys(gmailId)
	time.sleep(1)
	inputField.send_keys(Keys.RETURN)
	time.sleep(2)
	passwd=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
	passwd.click()
	time.sleep(2)
	passwd.send_keys(gPasswd)
	time.sleep(2)
	passwd.send_keys(Keys.RETURN)
	time.sleep(4)


#Go to youtube.com and page of films you liked.
def goToYoutube():
	driver.get("https://www.youtube.com/")
	time.sleep(4)
	driver.find_element_by_xpath('//*[@id="guide-icon"]').click()
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-collapsible-section-entry-renderer/div[2]/ytd-guide-collapsible-entry-renderer/ytd-guide-entry-renderer/a/paper-item/yt-formatted-string').click()
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-collapsible-section-entry-renderer/div[2]/ytd-guide-collapsible-entry-renderer/div/div/ytd-guide-entry-renderer[1]/a/paper-item/yt-formatted-string').click()
	time.sleep(4)


#Find out all the links which mathces your keyword.
def favFilter():
	for a in driver.find_elements_by_partial_link_text(keywd):
		b=a.get_attribute('href')
		if b.find("watch") !=-1:print(b)


loginWithOtherSite()
goToYoutube()
favFilter()
