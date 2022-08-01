from lib2to3.pgen2 import driver
import unittest
import time
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)

        response_data = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/h1").text

        self.assertEqual(response_data,"Dashboard")

    def test_b_login_salahUsername(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin123123")
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)

        error_message = driver.find_element(By.ID,"spanMessage").text

        self.assertEqual(error_message,"Invalid credentials")

    def test_c_login_passwordSalah(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123321")
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)

        response_message = driver.find_element(By.ID,"spanMessage").text

        self.assertEqual(response_message,"Invalid credentials")

    def test_d_login_kosongIDPASS(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)

        response_message = driver.find_element(By.ID,"spanMessage").text

        self.assertEqual(response_message,"Username cannot be empty")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()