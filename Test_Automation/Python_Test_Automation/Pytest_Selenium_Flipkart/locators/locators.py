def get_path_by_sibling(text):
    return f"//div[text()='{text}']/preceding-sibling::div"


def get_path_by_text(text):
    return f"//div[text()='{text}']"


def get_path_by_contains_text(text):
    return f"//div[contains(text(),'{text}')]"


class Locators:
    dismiss = "_30XB9F"
    search_bar = "q"
    add_to_cart = '//button[@class="_2KpZ6l _2U9uOA _3v1-ww"]'
    missing_cart = "//*[@class='_1LCJ1U']"
    remove_button = '//*[@class="_3dsJAO _24d-qY FhkMJZ"]'
