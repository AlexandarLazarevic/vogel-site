import unittest
from selenium import webdriver
from bases.pages import UberUnsPage, CommonForPages
from bases import datas


class HomePageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://developer.digitalcube.rs:1122/aboutus")
        cls.common_pages = CommonForPages(cls.driver)
        cls.uber_uns_page = UberUnsPage(cls.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_title(self):
        self.assertEqual(self.common_pages.title(), datas.title)

    def test_uber_uns_title_text_is_displayed(self):
        self.assertTrue(self.uber_uns_page.uber_uns_title_text_is_displayed())

    def test_uber_uns_title_text_check(self):
        self.assertEqual(self.uber_uns_page.uber_uns_title_text_check(), datas.uber_uns_title_text)

    def test_uber_uns_picture_is_displayed(self):
        self.assertTrue(self.uber_uns_page.uber_uns_picture_is_displayed())

    def test_uber_uns_picture_src_check(self):
        self.assertEqual(self.uber_uns_page.uber_uns_picture_src_check(), datas.uber_uns_picture_src)

    def test_uber_uns_paragraph_content_text_is_displayad(self):
        self.assertTrue(self.uber_uns_page.uber_uns_paragraph_content_text_is_displayad())

    def test_uber_uns_paragraph_content_text_check(self):
        self.assertEqual(self.uber_uns_page.uber_uns_paragraph_content_text_check(), datas.uber_uns_paragraph)


if __name__ == "__main__":
    unittest.main()