import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import click_sign_in, clip_all_coupons, find_coupons, login, click_sign_out

usernames = ["lizette_juarez@ucsb.edu", "natejones4323@gmail.com"]
passwords = ["ChDa1013", "450030778Nj!"]


# Selenium Options
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Remote("http://selenium:4444/wd/hub", options=options)

# Go to Albertson's page
driver.get("https://www.albertsons.com/")

for i in range(0, len(usernames)):
    # Go to Albertson's page
    driver.get("https://www.albertsons.com/")

    
    click_sign_in(driver)



    login(usernames[i], passwords[i], driver)




    coupon_css_list = find_coupons(driver)



    clip_all_coupons(driver, coupon_css_list)



    click_sign_out(driver)