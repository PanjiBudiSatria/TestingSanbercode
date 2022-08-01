from lib2to3.pgen2 import driver
from select import select
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
from selenium.webdriver.remote.webelement import WebElement

class TestAdmin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # def test_a_addEntitlements(self):
    #     driver=self.driver
    #     driver.maximize_window()
    #     driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    #     time.sleep(3)

    #     #Proses Login
    #     driver.find_element(By.ID,"txtUsername").send_keys("Admin")
    #     driver.find_element(By.ID,"txtPassword").send_keys("admin123")
    #     driver.find_element(By.ID,"btnLogin").click()
    #     time.sleep(2)

    #     #sementara hover
    #     driver.get("https://opensource-demo.orangehrmlive.com/index.php/leave/addLeaveEntitlement")
    #     time.sleep(2)

    #     empName = driver.find_element(By.ID,"entitlements_employee_empName")
    #     empName.send_keys("Fion")
    #     empName.send_keys(Keys.ARROW_DOWN)
    #     empName.send_keys(Keys.ENTER)
    #     time.sleep(1)

    #     select = Select(driver.find_element(By.ID,"entitlements_leave_type"))
    #     select.select_by_visible_text("US - Personal")
    #     time.sleep(1)

    #     select = Select(driver.find_element(By.ID,"period"))
    #     select.select_by_visible_text("2022-01-01 - 2022-12-31")
    #     time.sleep(1)

    #     driver.find_element(By.ID,"entitlements_entitlement").send_keys("15")

    #     driver.find_element(By.ID,"btnSave").click()
    #     time.sleep(5)

    #     validation_text = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr/td[5]/a").text
    #     self.assertEqual(validation_text,"15.00")

    def test_b_assignLeave(self):
        driver=self.driver
        driver.maximize_window()

        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)

        driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[3]/a/b").click()
        time.sleep(1)
        driver.find_element(By.ID,"menu_leave_assignLeave").click()
        time.sleep(2)

        empName = driver.find_element(By.ID,"assignleave_txtEmployee_empName")
        empName.send_keys("Fion")
        empName.send_keys(Keys.ARROW_DOWN)
        empName.send_keys(Keys.ENTER)

        select = Select(driver.find_element(By.ID,"assignleave_txtLeaveType"))
        select.select_by_visible_text("US - Personal")

        date_input = driver.find_element(By.ID,"assignleave_txtFromDate")
        date_input.click()
        date_input.send_keys("2022-07-11")
        date_input.send_keys(Keys.ENTER)
        date_input.send_keys(Keys.ENTER)
        time.sleep(5)

        date_input = driver.find_element(By.ID,"assignleave_txtToDate")
        date_input.click()
        date_input.clear()
        date_input.send_keys("2022-07-12")
        date_input.send_keys(Keys.ENTER)
        date_input.send_keys(Keys.ENTER)
        time.sleep(5)

        select = Select(driver.find_element(By.ID,"assignleave_partialDays"))
        select.select_by_visible_text("None")

        driver.find_element(By.ID,"assignBtn").click()
        time.sleep(3)

        driver.find_element(By.ID,"menu_leave_viewLeaveList").click()
        time.sleep(2)

        driver.find_element(By.ID,"leaveList_chkSearchFilter_checkboxgroup_allcheck").click()

        empName = driver.find_element(By.ID,"leaveList_txtEmployee_empName")
        empName.send_keys("Fion")
        empName.send_keys(Keys.ARROW_DOWN)
        empName.send_keys(Keys.ENTER)

        driver.find_element(By.ID,"btnSearch").click()
        time.sleep(1)

        validation_balance_leave = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[3]/table/tbody/tr/td[4]").text
        self.assertEqual(validation_balance_leave,"13.00")

if __name__ == "__main__":
    unittest.main()