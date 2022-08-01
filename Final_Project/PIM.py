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
        
        driver.find_element(By.LINK_TEXT,"Panji Budi").click()
        time.sleep(2)

        response_data_FirstName = driver.find_element(By.ID,"personal_txtEmpFirstName").get_attribute("value")
        response_data_MiddleName = driver.find_element(By.ID,"personal_txtEmpMiddleName").get_attribute("value")
        response_data_LastName = driver.find_element(By.ID,"personal_txtEmpLastName").get_attribute("value")

        self.assertEqual(response_data_FirstName,"Panji")
        self.assertEqual(response_data_MiddleName,"Budi")
        self.assertEqual(response_data_LastName,"Satria")

    def test_b_addUser_KosonginMandatory(self):
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
        time.sleep(1)

        fileInput = driver.find_element(By.ID,"photofile")
        fileInput.send_keys("C:/Users/Gamatechno/Testing/BootcampQA/Assets/image.jpeg")
        time.sleep(1)

        driver.find_element(By.ID,"btnSave").click()
        time.sleep(2)

        response_data_validation_error = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/ol/li[3]/span").text

        self.assertEqual(response_data_validation_error,"Required")

    def test_c_addEmployee_withLoginDetails(self):
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

        driver.find_element(By.ID,"chkLogin").click()
        
        driver.find_element(By.ID,"user_name").send_keys("panjibuds01")
        driver.find_element(By.ID,"user_password").send_keys("testing123")
        driver.find_element(By.ID,"re_password").send_keys("testing123")

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

        driver.find_element(By.LINK_TEXT,"Panji Budi").click()
        time.sleep(2)

        response_data_FirstName = driver.find_element(By.ID,"personal_txtEmpFirstName").get_attribute("value")
        response_data_MiddleName = driver.find_element(By.ID,"personal_txtEmpMiddleName").get_attribute("value")
        response_data_LastName = driver.find_element(By.ID,"personal_txtEmpLastName").get_attribute("value")

        self.assertEqual(response_data_FirstName,"Panji")
        self.assertEqual(response_data_MiddleName,"Budi")
        self.assertEqual(response_data_LastName,"Satria")

if __name__ == "__main__":
    unittest.main()