import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(command_executor='http://172.17.0.1:4444/wd/hub',
         desired_capabilities=DesiredCapabilities.CHROME)

driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('Sotong Kitchen')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.save_screenshot('screenie.png')

driver.quit()
