import unittest
from selenium import webdriver
from bases.pages import HomePage, CommonForPages
from bases import datas

class HomePageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://developer.digitalcube.rs:1122/")
        cls.home_page = HomePage(cls.driver)
        cls.common_pages = CommonForPages(cls.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_title_check(self):
        self.assertEqual(self.common_pages.title(), datas.title)

    def test_logo_on_header_is_displayed(self):
        self.assertTrue(self.common_pages.logo_is_displayed())

    def test_home_link_in_header_is_displayed(self):
        self.assertTrue(self.common_pages.home_in_navbar_is_displayed())

    def test_dienstleistungen_link_in_header_is_displayed(self):
        self.assertTrue(self.common_pages.deienstleistungen_in_navbar_is_displayed())

    def test_uber_uns_in_header_is_displayed(self):
        self.assertTrue(self.common_pages.uber_uns_in_navbar_is_displayed())

    def test_geschichite_in_header_is_displayed(self):
        self.assertTrue(self.common_pages.geschichite_in_navbar_is_displayed())

    def test_okologie_in_header_is_displayed(self):
        self.assertTrue(self.common_pages.okologie_in_navbar_is_displayed())

    def test_kontakt_is_header_is_displayed(self):
        self.assertTrue(self.common_pages.kontakt_is_navbar_is_displayed())

    def test_wir_stellen_title_in_content_is_displayed(self):
        self.assertTrue(self.common_pages.wir_stellen_title_in_content_is_displayed())

    def test_der_pharma_in_content_is_displayed(self):
        self.assertTrue(self.common_pages.d_pharma_in_content_is_displayed)

    def test_der_lebensmittel_und_in_content_is_displayed(self):
        self.assertTrue(self.common_pages.d_lebensmittel_und_in_content_is_displayed)

    def test_der_chemischen_industrie_in_content_is_displayed(self):
        self.assertTrue(self.common_pages.d_chemischen_industrie_in_content_is_displayed)

    def test_see_more_products_is_displayed(self):
        self.assertTrue(self.home_page.see_more_products_is_displayed)

    def test_dienstleistungen_picture_is_displayed(self):
        self.assertTrue(self.home_page.dienstleistungen_picture_is_displayed)

    def test_dienstleistungen_title_is_displayed(self):
        self.assertTrue(self.home_page.dienstleistungen_title_is_displayed)

    def test_dienstleistungen_text_content_check(self):
        self.assertEqual(self.home_page.dienstleistungen_text_content_check, datas.dienstleistungen_text)

    def test_dienstleistungen_read_more_link_is_displayed(self):
        self.assertTrue(self.home_page.dienstleistungen_read_more_link_is_displayed)

    def test_produkte_picture_is_displayed(self):
        self.assertTrue(self.home_page.produkte_picture_is_displayed)

    def test_produkte_title_is_displayed(self):
        self.assertTrue(self.home_page.produkte_title_is_displayed)

    def test_produkte_text_content_check(self):
        self.assertEqual(self.home_page.produkte_text_content_check, datas.produkte_text)

    def test_qualitat_iso_ce_picture_is_displayed(self):
        self.assertTrue(self.home_page.qualitat_iso_ce_picture_is_displayed)

    def test_qualitat_iso_ce_title_is_displayed(self):
        self.assertTrue(self.home_page.qualitat_iso_ce_title_is_displayed)

    def test_qualitat_iso_ce_text_content_check(self):
        # print(self.home_page.qualitat_iso_ce_text_content_check)
        self.assertEqual(self.home_page.qualitat_iso_ce_text_content_check, datas.qualitat_iso_ce)

    def test_qualitat_iso_ce_read_more_link_is_displayed(self):
        self.assertTrue(self.home_page.qualitat_iso_ce_read_more_link_is_displayed)

    def test_first_checker_picture_is_displayed(self):
        self.assertTrue(self.home_page.first_checker_picture_is_displayed)

    def test_second_checker_picture_is_displayed(self):
        self.assertTrue(self.home_page.second_checker_picture_is_displayed)

    def test_new_in_container_is_displayed(self):
        self.assertTrue(self.home_page.new_in_container_is_displayed)

    def test_new_picture_in_conteiner_is_displayed(self):
        self.assertTrue(self.home_page.new_picture_in_conteiner_is_displayed)

    def test_new_text_content_in_container_check(self):
        self.assertEqual(self.home_page.new_text_content_in_container_check, datas.news_text)

    def test_new_read_more_link_in_conteiner_is_displayed(self):
        self.assertTrue(self.home_page.new_read_more_link_in_conteiner_is_displayed)

    def test_verfahren_in_container_is_displayed(self):
        self.assertTrue(self.home_page.verfahren_in_container_is_displayed)

    def test_verfahren_picture_in_container_is_displayed(self):
        self.assertTrue(self.home_page.verfahren_picture_in_container_is_displayed)

    def test_verfahren_text_content_in_container_check(self):
        self.assertEqual(self.home_page.verfahren_text_content_in_container_check, datas.verfahren_text)

    def test_verfahren_read_more_link_is_displayed(self):
        self.assertTrue(self.home_page.verfahren_read_more_link_is_displayed)

    def test_links_in_container_is_displayed(self):
        self.assertTrue(self.home_page.links_in_container_is_displayed)

    def test_links_picture_in_container_is_displayed(self):
        self.assertTrue(self.home_page.links_picture_in_container_is_displayed)

    def test_links_text_content_in_container_check(self):
        self.assertEqual(self.home_page.links_text_content_in_container_check, datas.links_text)

    def test_links_read_more_link_in_container_is_displayed(self):
        self.assertTrue(self.home_page.links_read_more_link_in_container_is_displayed)

    def test_zertifikat_is_displayed(self):
        self.assertTrue(self.home_page.zertifikat_is_displayed)

    def test_address_in_footer_is_displayed(self):
        self.assertTrue(self.common_pages.address_in_footer_is_displayed)

    def test_address_text_in_footer_check(self):
        self.assertTrue(self.common_pages.address_text_in_footer_check)

    def test_phones_in_footer_is_displayed(self):
        self.assertTrue(self.common_pages.phones_in_footer_is_displayed)

    def test_first_phone_in_footer_check(self):
        self.assertEqual(self.common_pages.first_phone_in_footer_check, datas.first_phone)

    def test_second_phone_in_footer_check(self):
        self.assertEqual(self.common_pages.second_phone_in_footer_check, datas.second_phone)

    def test_home_link_in_footer_is_displayed(self):
        self.assertTrue(self.common_pages.home_link_in_footer_is_displayed)

    def test_dienstleistungen_link_in_footer_is_displayed(self):
        self.assertTrue(self.common_pages.dienstleistungen_link_in_footer_is_displayed)

    def test_uber_uns_link_in_footer_is_displayed(self):
        self.assertTrue(self.common_pages.uber_uns_link_in_footer_is_displayed)

    def test_geschichte_link_in_footer_is_displayed(self):
        self.assertTrue(self.common_pages.geschichte_link_in_footer_is_displayed)

    def test_okologie_link_in_footer_is_displayed(self):
        self.assertTrue(self.common_pages.okologie_link_in_footer_is_displayed)

    def test_kontakt_link_in_footer_is_displayed(self):
        self.assertTrue(self.common_pages.kontakt_link_in_footer_is_displayed)



if __name__ == "__main__":
    unittest.main()