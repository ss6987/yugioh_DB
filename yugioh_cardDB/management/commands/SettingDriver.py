from selenium import webdriver


def settingDriver():
    driver = webdriver.Chrome('yugioh_cardDB/management/commands/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get("https://www.db.yugioh-card.com")
    driver.find_element_by_css_selector("a.cards").click()
    driver.execute_script('jacascript:Search();')
    dk_container_mode = driver.find_element_by_id("dk_container_mode")
    dk_container_mode.click()
    dk_container_mode.find_elements_by_tag_name("li")[-1].click()
    dk_container_rp = driver.find_element_by_id("dk_container_rp")
    dk_container_rp.click()
    dk_container_rp.find_elements_by_tag_name("li")[-1].click()
    return driver
