import time

import pytest
from pages.homepage import Homepage
from pages.loginpage import LoginPage
from pages.pimpage import PIMPage
from pages.employeeInfopage import EmployeeInfo
from pages.verifyemppage import VerifyEmpPage


class Test_Demo:

    @pytest.mark.verifyInfo
    @pytest.mark.addInfo
    def testHomepage(self):
        hp = Homepage(self.driver)
        hp.home_page("OrageHRM")

    @pytest.mark.verifyInfo
    @pytest.mark.addInfo
    def test_loginpage(self):
        lp = LoginPage(self.driver)
        lp.set_username()
        lp.set_password()
        lp.click_login_button()
        assert lp.verify_title() == "Dasboard"

    @pytest.mark.addInfo
    def test_PIMbutton_addButton(self):
        pp = PIMPage(self.driver)
        assert "PIM" in pp.click_pim_button()
        assert pp.click_add_emp_button() == "PIM"

    @pytest.mark.addInfo
    def test_employeeInfo(self):
        ei = EmployeeInfo(self.driver)
        ei.set_firstname()
        ei.set_lastname()
        ei.click_create_login_details_button()
        ei.add_username()
        ei.add_password()
        ei.confirm_password()
        ei.click_save_button()

    @pytest.mark.verifyInfo
    def test_verify_empInfo(self):
        vp = VerifyEmpPage(self.driver)
        vp.click_pim_button()
        vp.set_emp_name()
        vp.click_search_button()
        assert vp.verify_emp() == "8o Records Found"

    # def test_deleteEmployee(self):
    #     fn=self.driver.find_element(By.XPATH,self.firstName).text
    #     ln = self.driver.find_element(By.XPATH, self.firstName).text
    #     time.sleep(20)
    #     if(fn=="Gayathri" and ln=="kurapati"):
    #         self.driver.find_element(By.XPATH, self.deleteEmployee).click()
    #     time.sleep(20)
