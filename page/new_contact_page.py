from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewContactPage(BaseAction):

    # 姓名输入框
    name_edit_text = By.XPATH, "//*[@text='姓名']"

    # 电话输入框
    phone_edit_text = By.XPATH, "//*[@text='电话']"

    # 输入姓名
    def input_name(self, text):
        self.input(self.name_edit_text, text)

    # 输入电话
    def input_phone(self, text):
        self.input(self.phone_edit_text, text)