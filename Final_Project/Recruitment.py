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

class TestRecruitment(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_addUser(self):
        driver=self.driver
        driver.maximize_window()
        #Open Web
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)

        #Proses Login
        driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)

        #Proses Add Data
        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[5]/a/b").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(1)

        driver.find_element(By.ID,"addCandidate_firstName").send_keys("Panji")
        driver.find_element(By.ID,"addCandidate_middleName").send_keys("Budi")
        driver.find_element(By.ID,"addCandidate_lastName").send_keys("Satria")

        driver.find_element(By.ID,"addCandidate_email").send_keys("panjibuds467@gmail.com")
        driver.find_element(By.ID,"addCandidate_contactNo").send_keys("08123199841")

        select = Select(driver.find_element(By.ID,"addCandidate_vacancy"))
        select.select_by_visible_text('Software Engineer')

        driver.find_element(By.ID,"addCandidate_keyWords").send_keys("Developer, Laravel, GO")

        date_input = driver.find_element(By.ID,"addCandidate_appliedDate")
        date_input.click()
        date_input.clear()
        date_input.send_keys("2022-07-11")
        time.sleep(1)
        date_input.send_keys(Keys.ENTER)
        time.sleep(1)
        date_input.send_keys(Keys.ENTER)
        time.sleep(5)

        driver.find_element(By.ID,"btnSave").click()
        time.sleep(3)

        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[5]/a/b").click()
        time.sleep(3)

        empName = driver.find_element(By.ID,"candidateSearch_candidateName")
        empName.send_keys("Panji")
        empName.send_keys(Keys.ARROW_DOWN)
        empName.send_keys(Keys.ENTER)
        time.sleep(1)

        driver.find_element(By.ID,"btnSrch").click()
        time.sleep(1)

        # Verifikasi Data
        response_data_candidate = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr[2]/td[3]/a").text
        response_data_vacancy = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr[2]/td[2]").text
        response_data_hiringManager = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr[2]/td[4]").text
        response_data_status = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr[2]/td[6]").text

        self.assertEqual(response_data_candidate,"Panji Budi Satria")
        self.assertEqual(response_data_vacancy,"Software Engineer")
        self.assertEqual(response_data_hiringManager,"Odis Adalwin")
        self.assertEqual(response_data_status,"Application Initiated")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()