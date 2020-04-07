from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
opts = Options()
opts.headless = True
prefs = {"profile.managed_default_content_settings.images": 2, 'profile.managed_default_content_settings.javascript': 2}
opts.add_experimental_option("prefs", prefs)
opts.add_argument('log-level=3')
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
assert opts.headless  # Operating in headless mode

def get_browser_context():
      browser = webdriver.Chrome(executable_path='chromedriver.exe', options=opts)
      browser.get('https://www.ijunoon.com/transliteration/urdu-to-roman')
      return browser


def transliterate(browser_context, text):
      browser_context.find_element_by_class_name('translatetext').clear()
      browser_context.find_element_by_class_name('translatetext').send_keys(text)   
      browser_context.find_element_by_class_name("translatesubmit").click()
      return wait(browser_context, 15).until(EC.presence_of_element_located((By.ID , "ctl00_inpageResult"))).text