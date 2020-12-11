from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.bbc.co.uk")

# Eddy goes to site.com and expects to see Home in the title
assert "Home" in driver.title

# close the browser
driver.close()