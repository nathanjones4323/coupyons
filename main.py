import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import click_sign_in, clip_all_coupons, find_coupons, login

username = os.environ["albertsons_email"]
password = os.environ["albertsons_password"]

# Selenium Options
options = Options()
options.add_argument("--start-maximized")
# options.add_argument('--headless')

driver = webdriver.Remote("http://selenium:4444/wd/hub", options=options)

# Go to Albertson's page
driver.get("https://www.albertsons.com/")

click_sign_in(driver)

login(username, password, driver)

coupon_css_list = find_coupons(driver)

clip_all_coupons(driver, coupon_css_list)