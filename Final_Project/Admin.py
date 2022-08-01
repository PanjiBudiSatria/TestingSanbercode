from lib2to3.pgen2 import driver
import unittest
import time
from urllib import response
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_addUser(self):
        driver=self.driver
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b").click()
        time.sleep(2)

        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(1)

        select = Select(driver.find_element(By.ID,"systemUser_userType"))
        select.select_by_visible_text('Admin')

        # driver.find_element(By.ID,"systemUser_employeeName_empName").send_keys("Fiona Grace")
        
        role = driver.find_element(By.ID,"systemUser_employeeName_empName")
        role.send_keys("Fion")
        role.send_keys(Keys.ARROW_DOWN)
        role.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.find_element(By.ID,"systemUser_userName").send_keys("panjitest4")

        select = Select(driver.find_element(By.ID,"systemUser_status"))
        select.select_by_visible_text('Enabled')

        driver.find_element(By.ID,"systemUser_password").send_keys("testing123")
        driver.find_element(By.ID,"systemUser_confirmPassword").send_keys("testing123")
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(7)

        driver.find_element(By.ID,"searchSystemUser_userName").send_keys("panjitest4")
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(2)

        response_data_username = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td[2]").text
        response_data_userRole = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr[1]/td[3]").text
        response_data_employeeName = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr[1]/td[4]").text
        response_data_status = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr[1]/td[5]").text

        self.assertEqual(response_data_username,"panjitest4")
        self.assertEqual(response_data_userRole,"Admin")
        self.assertEqual(response_data_employeeName,"Fiona Grace")
        self.assertEqual(response_data_status,"Enabled")


if __name__ == "__main__":
    unittest.main()