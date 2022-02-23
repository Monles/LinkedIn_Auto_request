from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import dotenv
import os
import time

ACCOUNT_EMAIL = "iceueb@gmail.com"
ACCOUNT_PASSWORD = "fwN8*2=6-rewe2Fd"
PHONE = "981594009"

chrome_driver_path="C:\\Users\\iceue\\Documents\\Development\\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

#wait for the next page to load
time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

#Locate the apply button
time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
# phone = driver.find_element_by_css_selector("fb-single-line-text__input")
# if phone.text == "":
#     phone.send_keys(PHONE)
#
# #Submit the application
# submit_button = driver.find_element_by_css_selector("footer button")
# submit_button.click()
#
#
# job_link: WebElement = driver.find_element(By.CSS_SELECTOR, '.jobs-search-results__list li div div div div div a')
# job_link.click()
# time.sleep(2)
# easy_apply_btn: WebElement = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
# easy_apply_btn.click()
# time.sleep(2)

#####Apply for a job
phone_number_input: WebElement = driver.find_element(By.NAME, 'urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2893016809,9,phoneNumber~nationalNumber)')
phone_number_input.send_keys(PHONE)
next_btn: WebElement = driver.find_element(By.CLASS_NAME, 'display-flex button')
next_btn.click()
time.sleep(2)
cross_button: WebElement = driver.find_element(By.CLASS_NAME, 'artdeco-button')
cross_button.click()
time.sleep(2)
discard_button: WebElement = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/button[2]')

discard_button.click()
#######

###apply for jobs
# find all job elements from left hand column
driver.maximize_window()
job_elements = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")

# create list from elements
all_jobs = [job.text for job in job_elements]
print(all_jobs)
# click individual job element then click apply now
x = range(len(all_jobs))
for n in x:
    try:
        job_elements[n].click()

        time.sleep(5)
        apply_now = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        apply_now.click()
        # check for Submit application button vs Next (stores button text as button_text)
        button = driver.find_element(By.CSS_SELECTOR, "form button span")
        button_text = button.text
        print(button_text)

        # if Next, close window and click discard button, then continue loop
        # if Submit application, click button, break loop
        if button_text == "Next":
            dismiss = driver.find_element(By.XPATH, '//*[@aria-label="Dismiss"]')
            dismiss.click()
            discard = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
            discard.click()
        else:
            submit = driver.find_element(By.XPATH, '//*[@aria-label="Submit application"]')
            submit.click()
            break
    except NoSuchElementException as e:
        print(f"Error: {e}")
        continue




