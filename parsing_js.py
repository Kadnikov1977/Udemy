from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://coronavirus-monitor.ru/coronavirus-v-rossii')
assert "5841" in driver.page_source
driver.quit()