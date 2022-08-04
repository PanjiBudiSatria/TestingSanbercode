import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Module_Buzz(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path='C:/Users/Gamatechno/.wdm/drivers/chromedriver/win32/103.0.5060.53/chromedriver.exe')
  
    # test case : Input status field update status
    def test_update_status(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_buzz_viewBuzz").click()
        time.sleep(2)
        driver.find_element(By.ID,"createPost_content").send_keys("Testing add status")
        time.sleep(2)
        driver.find_element(By.ID,"postSubmitBtn").click()
        time.sleep(2)
        self.driver.close()

    def test_input_komentar(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu_buzz_viewBuzz").click()
        time.sleep(2)
        driver.find_element(By.ID,"commentBoxNew_listId17").send_keys("testing komen")
        time.sleep(2)
        driver.find_element(By.ID,"commentBoxNew_listId17").click()
        time.sleep(2)
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()