import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import click_sign_in, clip_all_coupons, find_coupons, login, click_sign_out

username = os.environ["albertsons_email"]
password = os.environ["albertsons_password"]

# Selenium Options
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Remote("http://selenium:4444/wd/hub", options=options)

# Go to Albertson's page
driver.get("https://www.albertsons.com/")

for attempt in range(5):
        try:
            click_sign_in(driver)
        except Exception as e:
            print(e)
        else:
            break

for attempt in range(5):
    try:
        login(username, password, driver)
    except Exception as e:
        print(e)
    else:
        break


for attempt in range(5):
    try:
        coupon_css_list = find_coupons(driver)
    except Exception as e:
        print(e)
    else:
        break

for attempt in range(5):
    try:
        clip_all_coupons(driver, coupon_css_list)
    except Exception as e:
        print(e)
    else:
        break

for attempt in range(5):
    try:
        click_sign_out(driver)
    except Exception as e:
        print(e)
    else:
        break