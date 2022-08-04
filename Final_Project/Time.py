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

class TestTime(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_time_Add_Customer(self):
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

        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[4]/a/b").click()
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewCustomers")
        time.sleep(2)

        driver.find_element(By.ID,"btnAdd").click()

        driver.find_element(By.ID,"addCustomer_customerName").send_keys("ElektroArts")
        driver.find_element(By.ID,"addCustomer_description").send_keys("testing add customer")

        driver.find_element(By.ID,"btnSave").click()
        time.sleep(2)

        response_data_cust = driver.find_element(By.LINK_TEXT,"ElektroArts").text
        self.assertEqual(response_data_cust,"ElektroArts")

    def test_b_time_editUser(self):
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

        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[4]/a/b").click()
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewCustomers")
        time.sleep(2)

        driver.find_element(By.LINK_TEXT,"ElektroArts").click()
        time.sleep(2)

        elements=driver.find_element(By.ID,"btnSave")
        elements.click()
        # for element in elements:
        #     if element.get_attribute("value")=="Edit":
        #         element.click()
        time.sleep(1)

        driver.find_element(By.ID,"addCustomer_customerName").clear()
        driver.find_element(By.ID,"addCustomer_customerName").send_keys("ElektroArts1")

        elements=driver.find_element(By.ID,"btnSave")
        elements.click()
        time.sleep(1)

        response_data_edit = driver.find_element(By.LINK_TEXT,"ElektroArts1").text
        self.assertEqual(response_data_edit,"ElektroArts1")

    # def test_c_time_punchInOUT(self):
    #     driver=self.driver
    #     driver.maximize_window()
    #     driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    #     time.sleep(3)
    #     driver.find_element(By.ID,"txtUsername").send_keys("Admin")
    #     time.sleep(1)
    #     driver.find_element(By.ID,"txtPassword").send_keys("admin123")
    #     time.sleep(1)
    #     driver.find_element(By.ID,"btnLogin").click()
    #     time.sleep(2)

    #     driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[4]/a/b").click()
    #     driver.get("https://opensource-demo.orangehrmlive.com/index.php/attendance/punchIn")
    #     time.sleep(2)

    #     date_input = driver.find_element(By.ID,"attendance_date")
    #     date_input.click()
    #     date_input.clear()
    #     date_input.send_keys("2022-07-11")
    #     time.sleep(1)
    #     date_input.send_keys(Keys.ENTER)
    #     time.sleep(1)
    #     date_input.send_keys(Keys.ENTER)
    #     time.sleep(1)
    #     driver.find_element(By.ID,"attendance_time").clear()
    #     time.sleep(1)
    #     driver.find_element(By.ID,"attendance_time").send_keys("22:11")
    #     time.sleep(1)
    #     driver.find_element(By.ID,"btnPunch").click
    #     time.sleep(1)

    #     date_input = driver.find_element(By.ID,"attendance_date")
    #     date_input.click()
    #     date_input.clear()
    #     date_input.send_keys("2022-07-11")
    #     time.sleep(1)
    #     date_input.send_keys(Keys.ENTER)
    #     time.sleep(1)
    #     date_input.send_keys(Keys.ENTER)
    #     time.sleep(1)
    #     driver.find_element(By.ID,"attendance_time").clear()
    #     time.sleep(1)
    #     driver.find_element(By.ID,"attendance_time").send_keys("23:11")
    #     time.sleep(1)
    #     driver.find_element(By.ID,"punchOutbutton").click
    #     time.sleep(1)

    #     driver.get("https://opensource-demo.orangehrmlive.com/index.php/attendance/viewAttendanceRecord")
    #     time.sleep(1)

    #     empName = driver.find_element(By.ID,"attendance_employeeName_empName")
    #     empName.send_keys("Paul")
    #     empName.send_keys(Keys.ARROW_DOWN)
    #     empName.send_keys(Keys.ENTER)
    #     time.sleep(1)

    #     date_input = driver.find_element(By.ID,"attendance_date")
    #     date_input.click()
    #     date_input.clear()
    #     date_input.send_keys("2022-07-11")
    #     time.sleep(1)
    #     date_input.send_keys(Keys.ENTER)
    #     time.sleep(1)
    #     date_input.send_keys(Keys.ENTER)
    #     time.sleep(1)

    #     driver.find_element(By.ID,"btView").click()
    #     time.sleep(1)

    #     response_data_punchIN = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/div/form/div[3]/table/tbody/tr/td[2]").text
    #     response_data_punchOUT = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/div/form/div[3]/table/tbody/tr/td[4]").text

    #     self.assertEqual(response_data_punchIN,"2022-07-11 22:11 GMT 7")
    #     self.assertEqual(response_data_punchOUT,"2022-07-11 23:11 GMT 7")

if __name__ == "__main__":
    unittest.main()