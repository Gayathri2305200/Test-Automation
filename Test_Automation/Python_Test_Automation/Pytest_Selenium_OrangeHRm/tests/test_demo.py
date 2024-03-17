import pytest

from pages.employee_info_page import EmployeeInfo
from pages.home_page import Homepage
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from pages.verify_emp_page import VerifyEmpPage


class TestDemo:

    @pytest.mark.verifyInfo
    @pytest.mark.addInfo
    def test_homepage(self):
        hp = Homepage(self.driver)
        hp.home_page("OrangeHRM")

    @pytest.mark.verifyInfo
    @pytest.mark.addInfo
    def test_login_page(self):
        lp = LoginPage(self.driver)
        lp.set_username()
        lp.set_password()
        lp.click_login_button()
        assert lp.verify_title() == "Dashboard"

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
