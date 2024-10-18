import pytest
from selenium.webdriver.common.by import By

def test_twitch_logo_visible(driver):
    # Open the Twitch website
    driver.get("https://www.twitch.tv")
    
    # Wait for the logo to be present (you may add WebDriverWait for better stability)
    logo = driver.find_element(By.CSS_SELECTOR, 'a[data-a-target="tw-logo-link"]')

    # Assert that the logo is displayed and visible
    assert logo.is_displayed(), "The Twitch logo should be visible on the homepage"
