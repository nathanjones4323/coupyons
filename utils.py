from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import random
from bs4 import BeautifulSoup

def timer_func(func):
    # This function shows the execution time of the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(
            f'********\nFunction `{func.__name__}` executed in {(t2-t1):.2f}s\n********\n')
        return result
    return wrap_func

def check_exists_by_css_selector(driver, css_selector):
    try:
        WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
    except NoSuchElementException:
        return False
    except TimeoutException:
        return False
    return True

@timer_func
def click_sign_in(driver):
    try:
        # sign_in = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sign-in-modal-link')))
        pre_sign_in = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.main-wrapper.www-wrapper.nextgen-main-wrapper > div > div > div:nth-child(1) > div > div > div > div > div.unified-header-v3.unified-header.aem-GridColumn.aem-GridColumn--default--12 > div.unified-header.unified-header--sticky-enabled.header-version-2 > div.menu-nav.unified-walled-header > div > div > div.menu-nav__navigation > ul > li.menu-nav__list-item.first__item > a > svg')))
        pre_sign_in.click()
        real_sign_in = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'sign-in-modal-link')))
        real_sign_in.click()
    except Exception as e:
        print("Fix the click_sign_in() function")
        print(e)

@timer_func
def login(username, password, driver):
    try:
        # time.sleep(random.randint(1,3))
        albertsons_username = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'label-email')))
        time.sleep(0.25)
        albertsons_username.send_keys(username)
        albertsons_password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'label-password')))
        time.sleep(0.25)
        albertsons_password.send_keys(password)
        login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'btnSignIn')))
        login.click()
        time.sleep(2)
        print(f"WebDriver Current URL {driver.current_url}")
        if driver.current_url in ["https://www.albertsons.com/account/sign-in.html#error=login_required", "https://www.albertsons.com/account/sign-in.html"]:
            albertsons_username.send_keys(username)
            albertsons_password.send_keys(password)
            login.click()
    except Exception as e:
        print(f"WebDriver Current URL {driver.current_url}")
        print("Fix the login(username, password, driver) function")
        print(e)

# def change_store_location(driver):
#     """BROKEN FUNCTION"""
#     time.sleep(3)
#     change_store = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'openFulfillmentModalButton')))
#     change_store.click()
#     time.sleep(2)
#     location_input = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, '#storeFulfillmentModal > div > div > div:nth-child(3) > store-fulfillment-tabs > div > div.fulfillment-content__search-wrapper.form-group.dst__form-group--position > input')))
#     location_input.send_keys('93013')
#     location_input.send_keys(Keys.ENTER)
#     my_store = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, '#fulfilmentInStore > div > div > div:nth-child(1) > store-card > div.col-4.col-sm-4.card-store__location > div > a')))
#     my_store.click()
@timer_func
def find_coupons(driver):
    try:
        driver.get("https://www.albertsons.com/foru/coupons-deals.html")
        if check_exists_by_css_selector(driver, '#onetrust-close-btn-container > button'):
            cookies = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#onetrust-close-btn-container > button')))
            cookies.click()
        # Keep clicking load more until its gone
        while check_exists_by_css_selector(driver, '#coupon-grid_0 > div > div.load-more-container > button'):
            load_more = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#coupon-grid_0 > div > div.load-more-container > button')))
            load_more.click()
        time.sleep(random.randint(1,3))
        html = driver.page_source
        # convert to beautiful soup object
        soup = BeautifulSoup(html, 'html.parser')
        coupons = soup.find_all('button', class_= 'btn grid-coupon-btn btn-default')
        coupon_css_list = ['#' + coupon['id'] for coupon in coupons]
        print(f"{len(coupon_css_list)} Coupons found")
        time.sleep(random.randint(1,3))
        return coupon_css_list
    except Exception as e:
        print("Fix find_coupons(driver) function")
        print(e)

@timer_func
def clip_all_coupons(driver, coupon_css_list):
    try:
        if len(coupon_css_list) == 0 or coupon_css_list == None:
            print("No coupons website elements found via CSS")
            print("Fix find_coupons(driver) function")
        else:
            # Scroll to top of the page
            driver.execute_script("window.scrollTo(0, 0)")
            for coupon_css in coupon_css_list:
                clip_coupon = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, coupon_css)))
                clip_coupon.click()
            print(f"{len(coupon_css_list)} Coupons clipped")
    except Exception as e:
        print("Fix clip_all_coupons(driver, coupon_css_list) function")
        print(e)

def click_sign_out(driver):
    driver.get("https://www.albertsons.com/")
    try:
        pre_sign_in = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.main-wrapper.www-wrapper.nextgen-main-wrapper > div > div > div:nth-child(1) > div > div > div > div > div.unified-header-v3.unified-header.aem-GridColumn.aem-GridColumn--default--12 > div.unified-header.unified-header--sticky-enabled.header-version-2 > div.menu-nav.unified-walled-header > div > div > div.menu-nav__navigation > ul > li.menu-nav__list-item.first__item > a > svg')))
        pre_sign_in.click()
        sign_out = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#menu > div.sidebar-myaccount-flyout > ul > div.sidebar__nav > div > a')))
        sign_out.click()
    except Exception as e:
        print("Fix the click_sign_out() function")
        print(e)