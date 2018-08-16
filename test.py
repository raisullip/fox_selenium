#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re, os, time

driver = webdriver.Remote(
   command_executor="http://localhost:4444/wd/hub",
   desired_capabilities={
            "browserName": "chrome",
            "version": "68.0.3440.84",
            "maxInstances": 1,
            "platform": "LINUX",
            "seleniumProtocol": "WebDriver"
        })

try:
    driver.set_window_size(1920,1080)
    driver.get("https://www.fox.com/account/")

    #Sign in
    driver.find_element_by_class_name("Account_signIn_Q0B7n").click()
    email = driver.find_element_by_name("signinEmail")
    password = driver.find_element_by_name("signinPassword")
    email.send_keys("test@gmail.com")
    password.send_keys("123456")
    driver.find_element_by_xpath("//button[contains(.,'Sign In')]").click()
    driver.save_screenshot('screenshots/login.png')

    time.sleep(10)
    #Go to shows
    driver.find_element_by_xpath("//a[@href='/shows/']").click()

    ##########################################################################
    #Display Fox Shows
    fox_shows = driver.find_elements_by_class_name("MovieTile_titleText_1Q4bx")
    with open('shows/fox_shows', "w") as f:
        for show in fox_shows:
            dup = str(show.text)
            if re.match("(.*)(24 Hours To Hell & Back|So You Think You Can Dance|Meghan Markle: An American Princess|Hypnotize Me)(.*)", dup):
                f.write(dup+"\n")
    driver.save_screenshot('screenshots/fox.png')


    ##########################################################################
    #GO to FX tab
    driver.find_element_by_xpath("//a[contains(.,'FX')]").click()
    #Display FX Shows
    fx_shows = driver.find_elements_by_class_name("MovieTile_titleText_1Q4bx")
    with open('shows/fx_shows', "w") as f:
        for show in fx_shows:
            dup = str(show.text)
            if re.match("(.*)(24 Hours To Hell & Back|So You Think You Can Dance|Meghan Markle: An American Princess|Hypnotize Me)(.*)", dup):
                f.write(dup+"\n")
    driver.save_screenshot('screenshots/fx.png')

    ##########################################################################
    #go to NAT GEO tab
    driver.find_element_by_xpath("//a[contains(.,'National Geographic')]").click()
    #Display National Geo Shows
    nat_geo_shows = driver.find_elements_by_class_name("MovieTile_titleText_1Q4bx")
    with open('shows/nat_geo_shows', "w") as f:
        for show in nat_geo_shows:
            dup = str(show.text)
            if re.match("(.*)(24 Hours To Hell & Back|So You Think You Can Dance|Meghan Markle: An American Princess|Hypnotize Me)(.*)", dup):
                f.write(dup+"\n")
    driver.save_screenshot('screenshots/nat_geo_shows.png')

    ##########################################################################
    #go to FOX Sports tab
    driver.find_element_by_xpath("//a[contains(.,'FOX Sports')]").click()
    #Display FOX Sports Shows
    fox_sports_shows = driver.find_elements_by_class_name("MovieTile_titleText_1Q4bx")
    with open('shows/fox_sports_shows', "w") as f:
        for show in fox_sports_shows:
            dup = str(show.text)
            if re.match("(.*)(24 Hours To Hell & Back|So You Think You Can Dance|Meghan Markle: An American Princess|Hypnotize Me)(.*)", dup):
                f.write(dup+"\n")
    driver.save_screenshot('screenshots/fox_sports_shows.png')

    ##########################################################################
    #go to All Shows tab
    driver.find_element_by_xpath("//a[contains(.,'All Shows')]").click()
    #Display All Shows
    all_shows = driver.find_elements_by_class_name("MovieTile_titleText_1Q4bx")
    with open('shows/all_shows', "w") as f:
        for show in all_shows:
            dup = str(show.text)
            if re.match("(.*)(24 Hours To Hell & Back|So You Think You Can Dance|Meghan Markle: An American Princess|Hypnotize Me)(.*)", dup):
                f.write(dup+"\n")
    driver.save_screenshot('screenshots/all_shows.png')

    path = "./shows"
    fox = os.listdir(path)
    for show in fox:
        file = os.path.join(path, show)
        with open(file, "r") as f:
            seen = set()
            for line in f:
                line_lower = line.lower()
                if line_lower in seen:
                    with open('duplicated_records.csv', "w") as f:
                        for i in seen:
                            f.write(show+","+i+"\n")
                        else:
                            print ("No Duplicates")
                            seen.add(line_lower)

finally:
    driver.quit()
