from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

game_url = "chrome://dino"
chromebrowser_path = r"D:\Work\python\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("disable-infobars")

browser = webdriver.Chrome(executable_path=chromebrowser_path, chrome_options=chrome_options)
browser.get('chrome://dino')
browser.maximize_window()

# add comment