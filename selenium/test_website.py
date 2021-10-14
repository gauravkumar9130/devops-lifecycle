from selenium import webdriver 
from selenium.webdriver.support.ui import Select

def test_setup():
 global driver 
 driver=webdriver.Chrome(executable_path="C:/Users/gaura/Downloads/chromedriver_win32/chromedriver.exe")
 driver.get("C:/Users/gaura/Desktop/DevOps Tools/website/index.html")
 driver.maximize_window()

def test_signup():
 driver.find_element_by_class_name("first-name").send_keys("Gaurav")
 driver.find_element_by_class_name("sur-name").send_keys("Kumar")
 driver.find_element_by_class_name("enter-email").send_keys("gauravkumar9130@gmail.com")
 driver.find_element_by_class_name("new-password").send_keys("gaurav@123")
 driver.find_element_by_class_name("confirm-password").send_keys("gaurav@123")
 date = Select(driver.find_element_by_name("Date"))
 date.select_by_index(1)
 month = Select(driver.find_element_by_name("Month"))
 month.select_by_index(1)
 year = Select(driver.find_element_by_name("Year"))
 year.select_by_index(1)
 driver.find_element_by_id("male").click()
 driver.find_element_by_class_name("signup").click() 