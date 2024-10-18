import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_twitch_search_and_screenshot(driver):
    # 1. Open the Twitch website
    driver.get("https://www.twitch.tv")
    
    # 2. Click on the search icon
    search_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-a-target="search-input"]'))
    )
    search_icon.click()
    
    # 3. Input "StarCraft II" into the search bar
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-a-target="search-input"]'))
    )
    search_input.send_keys("StarCraft II")
    search_input.send_keys(Keys.ENTER)

    # 4. Scroll down twice
    body = driver.find_element(By.TAG_NAME, "body")
    for _ in range(2):
        body.send_keys(Keys.PAGE_DOWN)
    
    # 5. Select one streamer (first streamer in the list)
    streamer = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-a-target="preview-card-title-link"]'))
    )
    streamer.click()

    # 6. On the streamer page, wait until the page is fully loaded (video player appears)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'video'))
    )
    
    # Take a screenshot of the streamer page
    driver.save_screenshot("streamer_page.png")

    print("Screenshot saved as streamer_page.png")
