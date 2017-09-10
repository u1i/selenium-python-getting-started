# Getting started with Selenium using Python

## 1 - Run a local docker instance of selenium

`docker run -it -p 4444:4444 u1ih/selenium
`

web gui now accessible at http://localhost:4444/wd/hub


## 2 Get a website screenshot with Python

import time

from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
driver = webdriver.Remote(command_executor='http://172.17.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

driver.get('http://www.google.com/xhtml');

time.sleep(5) #  give it a moment to load

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # give it a moment to load

driver.save_screenshot('screenshot.png')

print driver.page_source # HTML raw output

driver.quit()
