import time
import pytest

from base.base_driver import init_driver
from page.page import Page


class TestContact:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize(("name", "phone"), [("zhangsan", "18888888888"), ("lisi", "13333333333"), ("wangwu", "17777777777")])
    def test_contact(self, name, phone):
        # 主页 - 点击 新建联系人
        self.page.contact_list.click_add_contact()
        # 新建联系人 - 输入 姓名
        self.page.new_contact.input_name(name)
        # 新建联系人 - 输入 电话
        self.page.new_contact.input_phone(phone)