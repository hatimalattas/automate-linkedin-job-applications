from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import time

linkedin_username = os.environ.get("USERNAME")
linkedin_password = os.environ.get("PASSWORD")

chrome_driver_path = "/Users/hatimalattas/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=100459316&keywords=python%20developer&location"
           "=Saudi%20Arabia&sortBy=R")

sign_in_btn = driver.find_element_by_xpath('/html/body/div[1]/header/nav/div/a[2]')
sign_in_btn.click()

email_field = driver.find_element_by_xpath('//*[@id="username"]')
email_field.send_keys(linkedin_username)

password_field = driver.find_element_by_xpath('//*[@id="password"]')
password_field.send_keys(linkedin_password)

sign_in_btn = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
sign_in_btn.click()

try:
    not_now_btn = driver.find_element_by_xpath('//*[@id="remember-me-prompt__form-secondary"]/button')
    not_now_btn.click()

except NoSuchElementException as e:
    pass

time.sleep(1)
search_result_elements = driver.find_elements_by_css_selector(".jobs-search-results__list-item")

for element in search_result_elements:
    try:
        element.click()
        time.sleep(1)
        apply_btn = driver.find_element_by_class_name("jobs-apply-button")
        apply_btn.click()

        time.sleep(1)
        submit_btn = driver.find_element_by_css_selector(".artdeco-button--primary")
        if submit_btn.text == "Submit application":
            submit_btn.click()
        else:
            time.sleep(1)
            dismiss_btn = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
            dismiss_btn.click()

            time.sleep(1)
            discard_btn = driver.find_element_by_css_selector(".artdeco-modal--layer-confirmation "
                                                              ".artdeco-modal__actionbar--confirm-dialog "
                                                              ".artdeco-button--primary")
            discard_btn.click()

    except NoSuchElementException as e:
        pass

driver.quit()
