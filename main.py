# from selenium import webdriver
# import datetime
# import os
#
# date_screen = datetime.datetime.now().strftime("%Y_%m_%d")
# cwd = os.getcwd()
# image_site = "site/y8.com"
# image_screen = os.path.join(cwd, image_site)
#
# if not os.path.exists(image_screen):
#     os.makedirs(image_screen)
#
# name = os.path.join(image_screen, "y8_" + date_screen + ".png")
# driver = webdriver.Chrome('./chromedriver')
# driver.get("https://www.y8.com/")
#
# driver.save_screenshot(name)
# driver.close()


#Level 2
from selenium import webdriver
import datetime
import os
import time


date_screen = datetime.datetime.now().strftime("%Y_%m_%d")
cwd = os.getcwd()
image_site = "site/y8.com"
image_screen = os.path.join(cwd, image_site)

if not os.path.exists(image_screen):
    os.makedirs(image_screen)

driver = webdriver.Chrome()
driver.get("http://www.y8.com")
driver.maximize_window()

try:
    all_games = driver.find_elements_by_css_selector('#items_container > div')

    for index, _ in enumerate(all_games, 1):
        css_path = "#items_container > div:nth-of-type({0})"
        game = driver.find_element_by_css_selector(css_path.format(index))
        if game.is_displayed():
            game.click()
            time.sleep(60)
            name = driver.title
            path = os.path.join(image_screen, name + date_screen + ".png")
            driver.save_screenshot(path)
            driver.back()
finally:
    driver.close()

