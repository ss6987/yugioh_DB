from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def settingDriver():
    options = Options()
    options.add_argument("headless")
    driver = webdriver.Chrome(executable_path="yugioh_cardDB/management/commands/chromedriver.exe",
                              chrome_options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.db.yugioh-card.com")
    driver.find_element_by_css_selector("a.cards").click()

    return driver


def returnSearchPage(driver):
    driver.get("https://www.db.yugioh-card.com")
    driver.find_element_by_css_selector("a.cards").click()
    return driver


def executeSearch(driver):
    driver.execute_script('javascript:Search();')
    dk_container_mode = driver.find_element_by_id("dk_container_mode")
    dk_container_mode.click()
    dk_container_mode.find_elements_by_tag_name("li")[-1].click()
    dk_container_rp = driver.find_element_by_id("dk_container_rp")
    dk_container_rp.click()
    dk_container_rp.find_elements_by_tag_name("li")[-1].click()
