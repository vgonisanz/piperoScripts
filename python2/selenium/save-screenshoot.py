from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://moscowsg.megafon.ru/ps/scc/php/cryptographp.php?PHPSESSID=mfc540jkbeme81qjvh5t0v0bnjdr7oc6&ref=114&w=150')

driver.save_screenshot("screenshot.png")

driver.close()
