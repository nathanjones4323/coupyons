import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import click_sign_in, clip_all_coupons, find_coupons, login, click_sign_out

usernames = [os.environ["albertsons_email_1"], os.environ["albertsons_email_2"]]
passwords = [os.environ["albertsons_password_1"], os.environ["albertsons_password_2"]]


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