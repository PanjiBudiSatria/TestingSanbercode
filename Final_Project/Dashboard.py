import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestDashboard(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_search_list(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_dashboard_index").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/div/div/table/tbody/tr/td[2]/div/a").click()
        time.sleep(2)
        driver.find_element(By.ID,"calFromDate").click()
        time.sleep(2)
        driver.find_element(By.ID,"calFromDate").send_keys("2020-02-01")
        time.sleep(2)
        driver.find_element(By.ID,"btnSearch").click()
        time.sleep(2)
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()