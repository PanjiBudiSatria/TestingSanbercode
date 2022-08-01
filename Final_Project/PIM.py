from cmd import IDENTCHARS
from lib2to3.pgen2 import driver
import unittest
import time
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement

class TestPIM(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_addEmployee(self):
        driver=self.driver
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[2]/a/b").click()
        driver.find_element(By.ID,"menu_pim_addEmployee").click()
        time.sleep(2)

        driver.find_element(By.ID,"firstName").send_keys("Panji")
        driver.find_element(By.ID,"middleName").send_keys("Budi")
        driver.find_element(By.ID,"lastName").send_keys("Satria")
        time.sleep(1)

        fileInput = driver.find_element(By.ID,"photofile")
        fileInput.send_keys("C:/Users/Gamatechno/Testing/BootcampQA/Assets/image.jpeg")
        time.sleep(1)

        driver.find_element(By.ID,"btnSave").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[2]/a/b").click()
        time.sleep(2)

        # driver.find_element(By.ID,"empsearch_employee_name_empName").send_keys("Panji Budi")
        empName = driver.find_element(By.ID,"empsearch_employee_name_empName")
        empName.send_keys("Panji")
        empName.send_keys(Keys.ARROW_DOWN)
        empName.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(2)

        response_data_FirstMiddleName = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr/td[3]/a").text
        response_data_LastName = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr/td[4]/a").text

        self.assertEqual(response_data_FirstMiddleName,"Panji Budi")
        self.assertEqual(response_data_LastName,"Satria")

if __name__ == "__main__":
    unittest.main()