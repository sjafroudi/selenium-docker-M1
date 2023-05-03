# credits: https://intoli.com/blog/clear-the-firefox-browser-cache/
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

dialog_selector = '#dialogOverlay-0 > groupbox:nth-child(1) > browser:nth-child(2)'

accept_dialog_script = (
    f"const browser = document.querySelector('{dialog_selector}');" +
    "browser.contentDocument.documentElement.querySelector('#clearButton').click();"
)

def get_clear_site_data_button(driver):
    return driver.find_element(By.CSS_SELECTOR,'#clearSiteDataButton')


def get_clear_site_data_dialog(driver):
    return driver.find_element(By.CSS_SELECTOR,dialog_selector)


def get_clear_site_data_confirmation_button(driver):
    return driver.find_element(By.CSS_SELECTOR,'#clearButton')


def clear_cache(driver, timeout=10):
    time.sleep(5)
    driver.get('about:preferences#privacy')
    wait = WebDriverWait(driver, timeout)

    # Click the "Clear Data..." button under "Cookies and Site Data".
    wait.until(get_clear_site_data_button)
    get_clear_site_data_button(driver).click()

    # Accept the "Clear Data" dialog by clicking on the "Clear" button.
    wait.until(get_clear_site_data_dialog)
    driver.execute_script(accept_dialog_script)

    # Accept the confirmation alert.
    wait.until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()