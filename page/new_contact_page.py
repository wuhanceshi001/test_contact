import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewContactPage(BaseAction):

    # 姓名输入框
    name_edit_text = By.XPATH, "//*[@text='姓名']"

    # 电话输入框
    phone_edit_text = By.XPATH, "//*[@text='电话']"

    # 输入姓名
    @allure.step(title="输入姓名")
    def input_name(self, text):
        allure.attach("姓名：", text, allure.attach_type.TEXT)
        self.input(self.name_edit_text, text)
        allure.attach("图片：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    # 输入电话
    @allure.step(title="输入电话")
    def input_phone(self, text):
        allure.attach("电话：", text, allure.attach_type.TEXT)
        self.input(self.phone_edit_text, text)
        allure.attach("图片：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)
