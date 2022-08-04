import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestPerformance(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
  
    def test_search_data_review(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu__Performance").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_performance_ManageReviews").click()
        time.sleep(2)
        driver.find_element(By.ID,"menu_performance_searchPerformancReview").click()
        time.sleep(2)
        driver.find_element(By.ID,"performanceReview360SearchForm_status").send_keys("In Progress")
        time.sleep(2)
        driver.find_element(By.ID,"btnSearch").click()
        time.sleep(2)

        response = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/form/div[4]/table/tbody/tr[1]/td[6]").text
        self.assertEqual(response, "In Progress")
        self.driver.close()

    def test_add_log(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)
        driver.find_element(By.ID, "menu__Performance").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu_performance_viewEmployeePerformanceTrackerList").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div[2]/form/div[3]/table/tbody/tr[1]/td[2]/a").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID,"addperformanceTrackerLog_log").send_keys("Training Onsite")
        time.sleep(2)
        driver.find_element(By.ID,"addperformanceTrackerLog_achievement").send_keys("Positive")
        time.sleep(2)
        driver.find_element(By.ID,"addperformanceTrackerLog_comment").send_keys("Melakukan training kepada klien")
        time.sleep(2)
        driver.find_element(By.ID,"saveBtn").click()
        time.sleep(2)
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()