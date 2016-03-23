import urllib
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.google.com/recaptcha/demo/recaptcha')

# get the image source
img = driver.find_element_by_xpath('//div[@id="recaptcha_image"]/img')
src = img.get_attribute('src')

# download the image
urllib.urlretrieve(src, "captcha.png")

driver.close()
