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

    def test_a_lupaPassword(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/div/a").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[3]/form/fieldset/ol/li/input").send_keys("Orange")
        time.sleep(1)
        driver.find_element(By.ID,"btnSearchValues").click()

        response_data = driver.find_element(By.XPATH,"").text

        self.assertEqual(response_data,"Please contact HR admin in order to reset the password")

if __name__ == "__main__":
    unittest.main()