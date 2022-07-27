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
        driver.get("http://barru.pythonanywhere.com/daftar") #Buka Situs
        time.sleep(3) #Stop code fo 3sec
        driver.find_element(By.ID,"email").send_keys("tester@jagoqa.com") #input email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("testerjago") #input password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click() #Hit Button Login
        time.sleep(2)

        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data,"Welcome tester jago")
        self.assertEqual(response_message,"Anda Berhasil Login")

        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click() #hit button ok

    def test_b_login_gagal_salahid(self):
        driver=self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("qweqweqwe@mail.com")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("testerjago")
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data_b = driver.find_element(By.ID,"swal2-title").text
        response_message_b = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data_b,"User's not found")
        self.assertEqual(response_message_b,"Email atau Password Anda Salah")

        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click()


    # def test_c_register_user_success(self):
    #     driver=self.driver
    #     driver.get("http://barru.pythonanywhere.com/daftar")
    #     time.sleep(3)
    #     driver.find_element(By.ID,"signUp").click()
    #     time.sleep(1)
    #     driver.find_element(By.ID,"name_register").send_keys("PanjiBudss")
    #     time.sleep(1)
    #     driver.find_element(By.ID,"email_register").send_keys("panjibudiis467@gmail.com")
    #     time.sleep(1)
    #     driver.find_element(By.ID,"password_register").send_keys("testing123")
    #     time.sleep(1)
    #     driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").click()
    #     time.sleep(2)

    #     response_data_c = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/h2").text
    #     response_message_c = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]").text

    #     self.assertEqual(response_data_c,"berhasil")
    #     self.assertEqual(response_message_c,"created user!")

    #     driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click()

    def test_d_register_user_failed_email_sama(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")

        driver=self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.ID,"signUp").click()
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("PanjiBudss")
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("panjibudiis467@gmail.com")
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("testing123")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").click()
        time.sleep(2)

        response_data_d = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/h2").text
        response_message_d = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]").text

        self.assertEqual(response_data_d,"Email sudah terdaftar, gunakan Email lain")
        self.assertEqual(response_message_d,"Gagal Registrasi")

        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

