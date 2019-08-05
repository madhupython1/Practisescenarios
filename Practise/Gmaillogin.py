from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:/Users/MadhusmitaPanda/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("http://www.gmail.com")
driver.maximize_window()
driver.find_element_by_xpath("//*[@type='email']").send_keys("msmita631")
driver.find_element_by_xpath("//*[text()='Next']").click()
# driver.implicitly_wait(20)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@type='password']")))
element.send_keys("Bell@1111")
# driver.find_element_by_xpath("//*[text()='Next']").click()




