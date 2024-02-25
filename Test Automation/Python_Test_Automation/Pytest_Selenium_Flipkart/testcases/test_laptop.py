import pytest
from pages.add_to_cart_page import Add_to_cart_Page
from pages.home_page import Homepage
from pages.remove_item_page import Remove_Item_Page
from pages.search_category_page import Search_Category_Page


class Test_Laptop:

    @pytest.mark.laptop
    def test_laptop(self, setup):
        self.driver = setup
        hp = Homepage(self.driver)
        hp.home_page("Online Shopping Site")
        sm = Search_Category_Page(self.driver)
        sm.search_category("Laptop")
        sm.select_brand("APPLE")
        sm.sort_by_newest("Newest First")
        ap = Add_to_cart_Page(self.driver)
        ap.select_mobile("APPLE 2023 Macbook")
        ap.click_addtocart()
        ri = Remove_Item_Page(self.driver)
        ri.click_remove("Remove")
        ri.confirm_remove("Remove")
        ri.verify_cart("Missing Cart items?")
