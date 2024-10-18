import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_twitch_search_and_screenshot(driver):
    # 1. Open the Twitch website
    driver.get("https://www.twitch.tv")
    
    # 2. Click on the search icon
    search_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label="Search"]'))
    )
    search_icon.click()
    
    # 3. Input "StarCraft II" into the search bar
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="search"]'))
    )
    search_input.send_keys("StarCraft II")
    search_input.send_keys(Keys.ENTER)

    # 4. Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # 5. Select one streamer (first streamer in the list)
    streamer = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '(//section//a[not(contains(@href,"search"))])[1]'))
    )
    streamer.click()

    # 6. On the streamer page, wait until the page is fully loaded (video player controls appear)
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Pause (space/k)"]'))
    )

    # Save screenshot
    driver.save_screenshot("streamer_page.png")
