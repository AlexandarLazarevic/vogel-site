import unittest
from selenium import webdriver
from bases.pages import CommonForPages, DienstleistungenPage
from bases import datas

class DienstleistungenPageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://developer.digitalcube.rs:1122/products")
        cls.dens_page = DienstleistungenPage(cls.driver)
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

    def test_first_production_picture_is_displayed(self):
        self.assertTrue(self.dens_page.first_production_picture_is_displayed())

    def test_first_production_title_text_is_displayed(self):
        self.assertTrue(self.dens_page.first_production_title_text_is_displayed())

    def test_first_production_title_text_check(self):
        self.assertEqual(self.dens_page.first_production_title_text_check(), datas.first_production_title_text)

    def test_first_production_content_first_paragraph_text_is_displayed(self):
        self.assertTrue(self.dens_page.first_production_content_first_paragraph_text_is_displayed())

    def test_first_production_content_first_paragraph_text_check(self):
        self.assertEqual(self.dens_page.first_production_content_first_paragraph_text_check(), datas.first_production_content_first_paragraph)

    def test_first_production_content_second_paragraph_is_displayed(self):
        self.assertTrue(self.dens_page.first_production_content_second_paragraph_is_displayed())

    def test_first_production_content_second_paragraph_check(self):
        self.assertEqual(self.dens_page.first_production_content_second_paragraph_check(), datas.first_production_content_second_paragraph)

    def test_second_production_title_text_is_displayed(self):
        self.assertTrue(self.dens_page.second_production_title_text_is_displayed())

    def test_second_production_title_text_check(self):
        self.assertEqual(self.dens_page.second_production_title_text_check(), datas.second_production_title)

    def test_second_production_content_text_is_displayed(self):
        self.assertTrue(self.dens_page.second_production_content_text_is_displayed())

    def test_second_production_content_text_check(self):
        self.assertEqual(self.dens_page.second_production_content_text_check(), datas.second_production_content_text)

    def test_second_production_picture_is_displayed(self):
        self.assertTrue(self.dens_page.second_production_picture_is_displayed())

    def test_production_spritzgguss_picture_is_displayed(self):
        self.assertTrue(self.dens_page.production_spritzgguss_picture_is_displayed())

    def test_production_spritzgguss_title_text_is_displayed(self):
        self.assertTrue(self.dens_page.production_spritzgguss_title_text_is_displayed())

    def test_production_spritzgguss_title_text_check(self):
        self.assertEqual(self.dens_page.production_spritzgguss_title_text_check(), datas.prod_spritzguss_title)

    def test_production_spritzgguss_text_paragraph_1_is_displayed(self):
        self.assertTrue(self.dens_page.production_spritzgguss_text_paragraph_1_is_displayed())

    def test_production_spritzgguss_text_paragraph_1_check(self):
        self.assertEqual(self.dens_page.production_spritzgguss_text_paragraph_1_check(), datas.prod_spritzguss_paragraph_1)

    def test_production_spritzgguss_text_paragraph_2_is_displayed(self):
        self.assertTrue(self.dens_page.production_spritzgguss_text_paragraph_2_is_displayed())

    def test_production_spritzgguss_text_paragraph_2_check(self):
        self.assertEqual(self.dens_page.production_spritzgguss_text_paragraph_2_check(), datas.prod_spritzguss_paragraph_2)

    def test_entwicklung_text_title_is_displayed(self):
        self.assertTrue(self.dens_page.entwicklung_text_title_is_displayed())

    def test_entwicklung_text_title_check(self):
        self.assertEqual(self.dens_page.entwicklung_text_title_check(), datas.entwicklung)

    def test_entwicklung_text_paragraph_1_is_displayed(self):
        self.assertTrue(self.dens_page.entwicklung_text_paragraph_1_is_displayed())

    def test_entwicklung_text_paragraph_1_check(self):
        self.assertEqual(self.dens_page.entwicklung_text_paragraph_1_check(), datas.entwicklung_text_paragraph_1)

    def test_entwicklung_text_paragraph_2_is_displayed(self):
        self.assertTrue(self.dens_page.entwicklung_text_paragraph_2_is_displayed())

    def test_entwicklung_text_paragraph_2_check(self):
        self.assertEqual(self.dens_page.entwicklung_text_paragraph_2_check(), datas.entwicklung_text_paragraph_2)

    def test_entwicklung_picture_is_displayed(self):
        self.assertTrue(self.dens_page.entwicklung_picture_is_displayed())

    def test_nachbearbeitung_picture_is_displayed(self):
        self.assertTrue(self.dens_page.nachbearbeitung_picture_is_displayed())

    def test_nachbearbeitung_text_title_is_displayed(self):
        self.assertTrue(self.dens_page.nachbearbeitung_text_title_is_displayed())

    def test_nachbearbeitung_text_title_check(self):
        self.assertEqual(self.dens_page.nachbearbeitung_text_title_check(), datas.nachbearbeitung_title)

    def test_nachbearbeitung_text_content_check(self):
        self.assertEqual(self.dens_page.nachbearbeitung_text_content_check(), datas.nachbearbeitung_content)

    def test_nachbearbeitung_text_content_is_displayed(self):
        self.assertTrue(self.dens_page.nachbearbeitung_text_content_is_displayed())

    def test_siebdruck_title_is_displayed(self):
        self.assertTrue(self.dens_page.siebdruck_title_is_displayed())

    def test_siebdruck_title_check(self):
        self.assertEqual(self.dens_page.siebdruck_title_check(), datas.siebdruck_title)

    def test_siebdruck_text_content_is_displayed(self):
        self.assertTrue(self.dens_page.siebdruck_text_content_is_displayed())

    def test_siebdruck_text_content_check(self):
        self.assertEqual(self.dens_page.siebdruck_text_content_check(), datas.siebdruck_content)

    def test_siebdruck_picture_is_displayed(self):
        self.assertTrue(self.dens_page.siebdruck_picture_is_displayed())

    def test_sieblador_title_is_displayed(self):
        self.assertTrue(self.dens_page.sieblador_title_is_displayed())

    def test_sieblador_title_check(self):
        self.assertEqual(self.dens_page.sieblador_title_check(), datas.sieblabor_title)

    def test_sieblador_text_content_is_displayed(self):
        self.assertTrue(self.dens_page.sieblador_text_content_is_displayed())

    def test_sieblador_text_content_check(self):
        self.assertEqual(self.dens_page.sieblador_text_content_check(), datas.sieblabor_content)

    def test_sieblador_picture_is_displayed(self):
        self.assertTrue(self.dens_page.sieblador_picture_is_displayed())

    def test_werkezeugbau_title_is_displayed(self):
        self.assertTrue(self.dens_page.werkezeugbau_title_is_displayed())

    def test_werkezeugbau_title_check(self):
        self.assertEqual(self.dens_page.werkezeugbau_title_check(), datas.werkzeugbau_title)

    def test_werkezeugbau_text_paragraph_1_is_displayed(self):
        self.assertTrue(self.dens_page.werkezeugbau_text_paragraph_1_is_displayed())

    def test_werkezeugbau_text_paragraph_1_check(self):
        self.assertEqual(self.dens_page.werkezeugbau_text_paragraph_1_check(), datas.werkzeugbau_text_paragraph_1)

    def test_werkezeugbau_text_paragraph_2_is_displayed(self):
        self.assertTrue(self.dens_page.werkezeugbau_text_paragraph_2_is_displayed())

    def test_werkezeugbau_text_paragraph_2_check(self):
        self.assertEqual(self.dens_page.werkezeugbau_text_paragraph_2_check(), datas.werkzeugbau_text_paragraph_2)

    def test_werkezeugbau_picture_is_displayed(self):
        self.assertTrue(self.dens_page.werkezeugbau_picture_is_displayed())


    # testing page od first product
    def test_first_product_page_all_tests_of_that_page(self):
        self.dens_page.click_first_title_click()
        self.assertTrue(self.dens_page.first_product_text_title_link_is_displayed())
        self.assertEqual(self.dens_page.first_product_text_title_link_check(), datas.first_production_title_text.upper())
        self.assertTrue(self.dens_page.first_product_paragraph_1_is_displayed())
        self.assertEqual(self.dens_page.first_product_paragraph_1_check(), datas.first_production_content_first_paragraph)
        self.assertTrue(self.dens_page.first_product_paragraph_2_is_displayed())
        self.assertEqual(self.dens_page.first_product_paragraph_2_check(), datas.first_production_content_second_paragraph)
        self.assertTrue(self.dens_page.first_product_facebook_block_is_displayed())
        self.assertEqual(self.dens_page.first_product_facebook_block_check(), datas.facebook)
        self.assertTrue(self.dens_page.first_product_twetter_block_is_displayed())
        self.assertEqual(self.dens_page.first_product_tweeter_block_check(), datas.twetter)
        self.assertTrue(self.dens_page.first_product_img_tag_is_displayed)
        self.assertTrue(self.dens_page.first_product_box_1_picture_is_displayed)
        self.assertTrue(self.dens_page.first_product_box_2_picture_is_displayed)
        self.assertTrue(self.dens_page.first_product_box_3_picture_is_displayed)
        self.assertEqual(self.dens_page.first_product_img_tag_check_src_atribude(), datas.first_src_img)
        self.assertEqual(self.dens_page.first_product_box_1_picture_check_src_atribude(), datas.first_box_1_src)
        self.assertEqual(self.dens_page.first_product_box_2_picture_check_src_atribude(), datas.first_box_2_src)
        self.assertEqual(self.dens_page.first_product_box_3_picture_check_src_atribude(), datas.first_box_3_src)
        self.assertTrue(self.dens_page.first_product_img_tag_is_displayed)
        self.assertTrue(self.dens_page.first_product_box_1_picture_is_displayed)
        self.assertTrue(self.dens_page.first_product_box_2_picture_is_displayed)
        self.assertTrue(self.dens_page.first_product_box_3_picture_is_displayed)
        self.dens_page.first_product_next_button()
        self.assertEqual(self.dens_page.first_product_img_tag_check_src_atribude(), datas.first_box_1_src)
        self.assertEqual(self.dens_page.first_product_box_1_picture_check_src_atribude(), datas.first_box_2_src)
        self.assertEqual(self.dens_page.first_product_box_2_picture_check_src_atribude(), datas.first_box_3_src)
        self.assertEqual(self.dens_page.first_product_box_3_picture_check_src_atribude(), datas.first_src_img)
        self.assertTrue(self.dens_page.first_product_img_tag_is_displayed)
        self.assertTrue(self.dens_page.first_product_box_1_picture_is_displayed)
        self.assertTrue(self.dens_page.first_product_box_2_picture_is_displayed)
        self.assertTrue(self.dens_page.first_product_box_3_picture_is_displayed)
        self.dens_page.first_product_next_button()
        self.assertEqual(self.dens_page.first_product_img_tag_check_src_atribude(), datas.first_box_2_src)
        self.assertEqual(self.dens_page.first_product_box_1_picture_check_src_atribude(), datas.first_box_3_src)
        self.assertEqual(self.dens_page.first_product_box_2_picture_check_src_atribude(), datas.first_src_img)
        self.assertEqual(self.dens_page.first_product_box_3_picture_check_src_atribude(), datas.first_box_1_src)
        self.assertTrue(self.dens_page.first_product_img_tag_is_displayed)
        self.assertTrue(self.dens_page.first_product_box_1_picture_is_displayed)
        self.assertTrue(self.dens_page.first_product_box_2_picture_is_displayed)
        self.assertTrue(self.dens_page.first_product_box_3_picture_is_displayed)
        self.dens_page.first_product_next_button()
        self.assertEqual(self.dens_page.first_product_img_tag_check_src_atribude(), datas.first_box_3_src)
        self.assertEqual(self.dens_page.first_product_box_1_picture_check_src_atribude(), datas.first_src_img)
        self.assertEqual(self.dens_page.first_product_box_2_picture_check_src_atribude(), datas.first_box_1_src)
        self.assertEqual(self.dens_page.first_product_box_3_picture_check_src_atribude(), datas.first_box_2_src)
        self.assertTrue(self.dens_page.first_product_img_tag_is_displayed)
        self.assertTrue(self.dens_page.first_product_box_1_picture_is_displayed)
        self.assertTrue(self.dens_page.first_product_box_2_picture_is_displayed)
        self.assertTrue(self.dens_page.first_product_box_3_picture_is_displayed)
        self.dens_page.first_product_next_button()
        self.assertEqual(self.dens_page.first_product_img_tag_check_src_atribude(), datas.first_src_img)
        self.assertEqual(self.dens_page.first_product_box_1_picture_check_src_atribude(), datas.first_box_1_src)
        self.assertEqual(self.dens_page.first_product_box_2_picture_check_src_atribude(), datas.first_box_2_src)
        self.assertEqual(self.dens_page.first_product_box_3_picture_check_src_atribude(), datas.first_box_3_src)
        self.dens_page.go_back_one_page()









