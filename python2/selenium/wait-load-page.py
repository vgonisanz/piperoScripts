from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def wait_for_page_load(self, timeout=30):
	old_page = self.browser.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.browser, timeout).until(
            staleness_of(old_page)
        )

print 'Loading...'
browser = webdriver.Firefox()
print 'Waiting to load page...'
browser.get("https://moscowsg.megafon.ru/ps/scc/php/cryptographp.php?PHPSESSID=mfc540jkbeme81qjvh5t0v0bnjdr7oc6&ref=114&w=150")
wait_for_page_load(browser)
print 'loaded! exiting...'
browser.quit()
