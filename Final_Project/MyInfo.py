import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class TestContact(unittest.TestCase):
    def test_a_contact_details(self):
        base_url = 'https://opensource-demo.orangehrmlive.com/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        username.clear()
        username.send_keys('Admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()
        time.sleep(1)

        # My Info Link Click
        driver.find_element(By.LINK_TEXT, 'My Info').click()

        # Click Contact Details
        driver.find_element(By.LINK_TEXT, 'Contact Details').click()

        # Click Edit
        edit = driver.find_element(By.ID, 'btnSave')
        edit.click()
        time.sleep(3)

        address_street1 = driver.find_element(By.ID, 'contact_street1')
        address_street1.clear()
        address_street1.send_keys('1 Austin Terrace, Toronto, ON M5R 1X8, Canada')

        address_street2 = driver.find_element(By.ID, 'contact_street2')
        address_street2.clear()
        address_street2.send_keys('317 Dundas St W, Toronto, ON M5T 1G4, Canada')

        city = driver.find_element(By.ID, 'contact_city')
        city.clear()
        city.send_keys('Toronto')

        state_province = driver.find_element(By.ID, 'contact_province')
        state_province.clear()
        state_province.send_keys('Toronto')

        zip_postal_code = driver.find_element(By.ID, 'contact_emp_zipcode')
        zip_postal_code.clear()
        zip_postal_code.send_keys('1216')

        country = driver.find_element(By.ID, 'contact_country')
        sel = Select(country)
        sel.select_by_value('CA')

        home_telephone = driver.find_element(By.ID, 'contact_emp_hm_telephone')
        home_telephone.clear()
        home_telephone.send_keys('+14169231171')

        mobile = driver.find_element(By.ID, 'contact_emp_mobile')
        mobile.clear()
        mobile.send_keys('01746604763')

        work_telephone = driver.find_element(By.ID, 'contact_emp_work_telephone')
        work_telephone.clear()
        work_telephone.send_keys('+14169231171')

        work_email = driver.find_element(By.ID, 'contact_emp_work_email')
        work_email.clear()
        work_email.send_keys('panjibuds467@gmail.com')

        other_email = driver.find_element(By.ID, 'contact_emp_oth_email')
        other_email.clear()
        other_email.send_keys('panjibuds467@gmail.com')

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

    def test_b_dependents_details(self):
        base_url = 'https://opensource-demo.orangehrmlive.com/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        # Find Elements
        username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        # Login Action
        username.clear()
        username.send_keys('Admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()

        # My Info Link Click
        driver.find_element(By.LINK_TEXT, 'My Info').click()

        # Click Dependents
        driver.find_element(By.LINK_TEXT, 'Dependents').click()

        add = driver.find_element(By.ID, 'btnAddDependent')
        add.click()
        time.sleep(2)

        name = driver.find_element(By.ID, 'dependent_name')
        name.click()
        name.send_keys('testing 123')

        relationship = driver.find_element(By.ID, 'dependent_relationshipType')
        sel = Select(relationship)
        sel.select_by_value('child')

        date_of_birth = driver.find_element(By.ID, 'dependent_dateOfBirth')
        date_of_birth.clear()
        date_of_birth.send_keys('01-01-2020')
        time.sleep(2)

        save = driver.find_element(By.ID, 'btnSaveDependent')
        save.click()
        time.sleep(2)

    def test_c_emergency_contacts_details(self):
        base_url = 'https://opensource-demo.orangehrmlive.com/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        # Find Elements
        username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        # Login Action
        username.clear()
        username.send_keys('Admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()

        # My Info Link Click
        driver.find_element(By.LINK_TEXT, 'My Info').click()

        # Click Emergency Contacts
        driver.find_element(By.LINK_TEXT, 'Emergency Contacts').click()

        add = driver.find_element(By.ID, 'btnAddContact')
        add.click()
        time.sleep(2)

        name = driver.find_element(By.ID, 'emgcontacts_name')
        name.clear()
        name.send_keys('Jarvish amergency person')

        relationship = driver.find_element(By.ID, 'emgcontacts_relationship')
        relationship.clear()
        relationship.send_keys('Brother')

        home_telephone = driver.find_element(By.ID, 'emgcontacts_homePhone')
        home_telephone.clear()
        home_telephone.send_keys('+14109678910')

        mobile = driver.find_element(By.ID, 'emgcontacts_mobilePhone')
        mobile.clear()
        mobile.send_keys('01746604763')

        work_telephone = driver.find_element(By.ID, 'emgcontacts_workPhone')
        work_telephone.clear()
        work_telephone.send_keys('+1409645678')

        save = driver.find_element(By.ID, 'btnSaveEContact')
        save.click()
        time.sleep(2)

    def test_d_immigration_records(self):
        base_url = 'https://opensource-demo.orangehrmlive.com/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        # Find Elements
        username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        # Login Action
        username.clear()
        username.send_keys('Admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()

        # My Info Link Click
        driver.find_element(By.LINK_TEXT, 'My Info').click()

        # Click Immigration
        driver.find_element(By.LINK_TEXT, 'Immigration').click()

        # Assigned Immigration Records
        add = driver.find_element(By.ID, 'btnAdd')
        add.click()
        time.sleep(1)

        document = driver.find_element(By.ID, 'immigration_type_flag_1')
        status = document.is_selected()
        if not status:
            document.click()
            time.sleep(1)

        number = driver.find_element(By.ID, 'immigration_number')
        number.clear()
        number.send_keys('19813090639100765')
        time.sleep(1)

        issued_date = driver.find_element(By.ID, 'immigration_passport_issue_date')
        issued_date.clear()
        issued_date.send_keys('21-05-2022')
        time.sleep(1)

        expiry_date = driver.find_element(By.ID, 'immigration_passport_expire_date')
        expiry_date.clear()
        expiry_date.send_keys('16-06-2027')
        time.sleep(1)

        eligible_status = driver.find_element(By.ID, 'immigration_i9_status')
        eligible_status.clear()
        eligible_status.send_keys('Eligible')
        time.sleep(1)

        issued_by = driver.find_element(By.ID, 'immigration_country')
        sel = Select(issued_by)
        sel.select_by_value('BD')
        time.sleep(1)

        eligible_review_date = driver.find_element(By.ID, 'immigration_i9_review_date')
        eligible_review_date.clear()
        eligible_review_date.send_keys('12-06-2022')
        time.sleep(1)

        comments = driver.find_element(By.ID, 'immigration_comments')
        comments.clear()
        comments.send_keys('Immigration was granted.')
        time.sleep(1)

        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

    def test_e_personal_details(self):
        base_url = 'https://opensource-demo.orangehrmlive.com/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        # Find Elements
        username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        # Login Action
        username.clear()
        username.send_keys('jarvis')

        password.clear()
        password.send_keys('masuk123')

        login_btn.click()

        # My Info Click
        driver.find_element(By.LINK_TEXT, 'My Info').click()
        time.sleep(2)

        # Click Edit
        edit = driver.find_element(By.ID, 'btnSave')
        edit.click()
        time.sleep(2)

        first_name = driver.find_element(By.XPATH, '//*[@id="personal_txtEmpFirstName"]')
        first_name.clear()
        first_name.send_keys('Jarvis')
        time.sleep(1)

        middle_name = driver.find_element(By.XPATH, '//*[@id="personal_txtEmpMiddleName"]')
        middle_name.clear()
        middle_name.send_keys('Friday')
        time.sleep(1)

        last_name = driver.find_element(By.XPATH, '//*[@id="personal_txtEmpLastName"]')
        last_name.clear()
        last_name.send_keys('Test')
        time.sleep(1)

        employee_id = driver.find_element(By.ID, 'personal_txtEmployeeId')
        employee_id.clear()
        employee_id.send_keys('464026')
        time.sleep(1)

        other_id = driver.find_element(By.ID, 'personal_txtOtherID')
        other_id.clear()
        other_id.send_keys('4147852')
        time.sleep(1)

        driver_license_number = driver.find_element(By.ID, 'personal_txtLicenNo')
        driver_license_number.clear()
        driver_license_number.send_keys('DK0405837C00000')
        time.sleep(1)

        license_expiry_date = driver.find_element(By.ID, 'personal_txtLicExpDate')
        license_expiry_date.clear()
        license_expiry_date.send_keys('15-06-2024')

        ssn_number = driver.find_element(By.ID, 'personal_txtNICNo')
        ssn_number.clear()
        ssn_number.send_keys('123456')
        time.sleep(1)

        sin_number = driver.find_element(By.ID, 'personal_txtSINNo')
        sin_number.clear()
        sin_number.send_keys('78910')
        time.sleep(1)

        gender = driver.find_element(By.ID, 'personal_optGender_2')
        status = gender.is_selected()

        if not status:
            gender.click()
            time.sleep(1)

        marital_status = driver.find_element(By.ID, 'personal_cmbMarital')
        sel = Select(marital_status)
        sel.select_by_value('Single')
        time.sleep(1)

        nationality = driver.find_element(By.ID, 'personal_cmbNation')
        sel = Select(nationality)
        sel.select_by_value('83')
        time.sleep(1)

        date_of_birth = driver.find_element(By.XPATH, '//*[@id="personal_DOB"]')
        date_of_birth.clear()
        date_of_birth.send_keys('01-01-1996')
        time.sleep(1)

        nick_name = driver.find_element(By.ID, 'personal_txtEmpNickName')
        nick_name.clear()
        nick_name.send_keys('Jarvish')
        time.sleep(1)

        military_service = driver.find_element(By.ID, 'personal_txtMilitarySer')
        military_service.clear()
        military_service.send_keys('No')
        time.sleep(1)

        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

        # Custom Fields
        edit = driver.find_element(By.ID, 'btnEditCustom')
        edit.click()
        time.sleep(1)

        blood_type = driver.find_element(By.XPATH, '//*[@id="frmEmpCustomFields"]/ol/li/select')
        sel = Select(blood_type)
        sel.select_by_value('A+')
        time.sleep(1)

        save = driver.find_element(By.ID, 'btnEditCustom')
        save.click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()