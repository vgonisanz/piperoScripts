from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import urllib2
import os
from bs4 import BeautifulSoup

def wait_for_page_load(self, timeout=30):
        old_page = self.browser.find_element_by_tag_name('html')
        yield
	WebDriverWait(self.browser, timeout).until(
            staleness_of(old_page)
        )

VAR_URL="https://www.google.es/"
VAR_PATH="/home/vgoni/tmp"

print 'Loading...'
browser = webdriver.Firefox()
opener = urllib2.build_opener()
urllib2.install_opener(opener)

print 'Waiting to load page...'
browser.get(VAR_URL)
wait_for_page_load(browser)

print 'Parsing source code...'
soup = BeautifulSoup(browser.page_source,"lxml")
imgs = soup.findAll("img",{"alt":True, "src":True})
for img in imgs:
    print img["src"]
    img_url = img["src"]
    img_url_absolute = VAR_URL + img_url
    print img_url_absolute
    filename = os.path.join(VAR_PATH, img_url.split("/")[-1])
    img_data = opener.open(img_url_absolute)
    f = open(filename,"wb")
    f.write(img_data.read())
    f.close()

print 'loaded! exiting...'
browser.quit()

