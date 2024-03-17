import pytest

from pages.add_to_cart_page import Add_to_cart_Page
from pages.home_page import Homepage
from pages.remove_item_page import Remove_Item_Page
from pages.search_category_page import Search_Category_Page


class Test_Mobile:

    @pytest.mark.mobile
    def test_Mobile(self, setup):
        self.driver = setup
        hp = Homepage(self.driver)
        hp.home_page("Online Shopping Site")
        sm = Search_Category_Page(self.driver)
        sm.search_category("Mobile")
        sm.select_brand("APPLE")
        sm.sort_by_newest("Newest First")
        ap = Add_to_cart_Page(self.driver)
        ap.select_mobile("APPLE iPhone 14")
        ap.click_addtocart()
        ri = Remove_Item_Page(self.driver)
        ri.click_remove("Remove")
        ri.confirm_remove("Remove")
        ri.verify_cart("Missing Cart items?")







# @pytest.mark.usefixtures("setup")
# class Test_Mobile:
#
#     def test_Homepage(self):
#         hp = Homepage(self.driver)
#         hp.home_page("Online Shopping Site")
#
#     def test_search_categoty(self):
#         sm=Search_Category_Page(self.driver)
#         sm.search_category("Mobile")
#         sm.select_brand("APPLE")
#         sm.sortBy_newest("Newest First")
#
#     def test_addtocart(self):
#         ap=Add_to_cart_Page(self.driver)
#         ap.select_mobile("APPLE iPhone 14")
#         ap.click_addtocart()
#
#     def test_remove_item(self):
#         ri=Remove_Item_Page(self.driver)
#         ri.click_remove("Remove")
#         ri.confirm_remove("Remove")
#         ri.verify_cart("Missing Cart items?")
#
