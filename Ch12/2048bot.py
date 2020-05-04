# 2048 Game, press automatically up-right-down-left

import sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
#not working, need a function to restart the game in loss screen
def newGameIfLoss(browser):
    try:
        restart_button = browser.find_element('css selector', 'retry-button')
        time.sleep(5)
        restart_button.click()
    except Exception:
        pass
"""

# open the browser and the game
browser = webdriver.Firefox()
browser.get('https://play2048.co/')
el = browser.find_element('tag name', 'html')

# infinite loop until KeyboardInterrupt, exit without errors
print("Ctrl-Z to interupt correctly")
try:
    while True:
        #newGameIfLoss(browser)
        el.send_keys(Keys.UP)
        el.send_keys(Keys.RIGHT)
        el.send_keys(Keys.DOWN)
        el.send_keys(Keys.LEFT)
        
except KeyboardInterrupt:
    browser.quit()
    sys.exit()
