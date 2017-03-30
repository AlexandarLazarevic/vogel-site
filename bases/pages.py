from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bases.locators import HomePageLocators, CommonLocators, DiensLocators, UberUnsLocators,GeschichiteLocators

class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

class CommonForPages(BasePage):

    def title(self):
        return self.driver.title

    def go_back_one_page(self):
        return self.driver.back()

    def logo_is_displayed(self):
        logo = WebDriverWait(self.driver, 10).until(CommonLocators.LOGO)
        return logo.is_displayed()

    def home_in_navbar_is_displayed(self):
        home = WebDriverWait(self.driver, 10).until(CommonLocators.HOME)
        return home.is_displayed()

    def deienstleistungen_in_navbar_is_displayed(self):
        deienstleistungen = WebDriverWait(self.driver, 10).until(CommonLocators.DIENSTLEISTUNGEN)
        return deienstleistungen.is_displayed()

    def uber_uns_in_navbar_is_displayed(self):
        uber_uns = WebDriverWait(self.driver, 10).until(CommonLocators.UBER_UNS)
        return uber_uns.is_displayed()

    def geschichite_in_navbar_is_displayed(self):
        geschichite = WebDriverWait(self.driver, 10).until(CommonLocators.GESCHICHTE)
        return geschichite.is_displayed()

    def okologie_in_navbar_is_displayed(self):
        okologie = WebDriverWait(self.driver, 10).until(CommonLocators.OKOLOGIE)
        return okologie.is_displayed()

    def kontakt_is_navbar_is_displayed(self):
        kontakt = WebDriverWait(self.driver, 10).until(CommonLocators.KONTAKT)
        return kontakt.is_displayed()

    def wir_stellen_title_in_content_is_displayed(self):
        wir_s = WebDriverWait(self.driver, 10).until(CommonLocators.WIR_STELLEN_FUR_DIE_BRANCHEN)
        return wir_s.is_displayed()

    def d_pharma_in_content_is_displayed(self):
        d_pharma = WebDriverWait(self.driver, 10).until(CommonLocators.DER_PHARMA)
        return d_pharma.is_displayed()

    def d_lebensmittel_und_in_content_is_displayed(self):
        d_leb = WebDriverWait(self.driver, 10).until(CommonLocators.DER_LEBENSMITTEL_UND)
        return d_leb.is_displayed()

    def d_chemischen_industrie_in_content_is_displayed(self):
        d_chem = WebDriverWait(self.driver, 10).until(CommonLocators.DER_CHEMISCHEN_INDUSTRIE)
        return d_chem.is_displayed()

    def address_in_footer_is_displayed(self):
        add = WebDriverWait(self.driver, 10).until(CommonLocators.ADDRESS)
        return add.is_displayed()

    def address_text_in_footer_check(self):
        add_text = WebDriverWait(self.driver, 10).until(CommonLocators.ADDRESS)
        return add_text.text

    def phones_in_footer_is_displayed(self):
        phones = WebDriverWait(self.driver, 10).until(CommonLocators.ALL_PHONES)
        return phones.is_displayed()

    def first_phone_in_footer_check(self):
        first = WebDriverWait(self.driver, 10).until(CommonLocators.FIRST_PHONE_TEXT)
        return first.text

    def second_phone_in_footer_check(self):
        second = WebDriverWait(self.driver, 10).until(CommonLocators.SECOND_PHONE_TEXT)
        return second.text

    def home_link_in_footer_is_displayed(self):
        home_link = WebDriverWait(self.driver, 10).until(CommonLocators.HOME_LINK)
        return home_link.is_displayed()

    def dienstleistungen_link_in_footer_is_displayed(self):
        dien_link = WebDriverWait(self.driver, 10).until(CommonLocators.DIENSTLEISTUNGEN_LINK)
        return dien_link.is_displayed()

    def uber_uns_link_in_footer_is_displayed(self):
        uber_uns_link = WebDriverWait(self.driver, 10).until(CommonLocators.UBER_UNS)
        return uber_uns_link.is_displayed()

    def geschichte_link_in_footer_is_displayed(self):
        ges_link = WebDriverWait(self.driver, 10).until(CommonLocators.GESCHICHTE_LINK)
        return ges_link.is_displayed()

    def okologie_link_in_footer_is_displayed(self):
        oko_link = WebDriverWait(self.driver, 10).until(CommonLocators.OKOLOGIE_LINK)
        return oko_link.is_displayed()

    def kontakt_link_in_footer_is_displayed(self):
        kontakt_link = WebDriverWait(self.driver, 10).until(CommonLocators.KONTAKT_LINK)
        return kontakt_link.is_displayed()


class HomePage(BasePage):

    def see_more_products_is_displayed(self):
        see = WebDriverWait(self.driver, 10).until(HomePageLocators.SEE_MORE_PRODUCTS)
        return see.is_displayed()

    def dienstleistungen_picture_is_displayed(self):
        d_pic = WebDriverWait(self.driver, 10).until(HomePageLocators.DIENSTLEISTUNGEN_PICTURE)
        return d_pic.is_displayed()

    def dienstleistungen_title_is_displayed(self):
        die_title = WebDriverWait(self.driver, 10).until(HomePageLocators.DIENSTLEISTUNGEN_TEXT_TITLE)
        return die_title.is_displayed()

    def dienstleistungen_text_content_check(self):
        die_text = WebDriverWait(self.driver, 10).until(HomePageLocators.DIENSTLEISTUNGEN_TEXT_CONTENT)
        return die_text.text

    def dienstleistungen_read_more_link_is_displayed(self):
        die_read = WebDriverWait(self.driver, 10).until(HomePageLocators.DIENSTLEISTUNGEN_READ_MORE)
        return die_read.is_displayed()

    def produkte_picture_is_displayed(self):
        pro_pic = WebDriverWait(self.driver, 10).until(HomePageLocators.PRODUKTE_PICTURE)
        return pro_pic.is_displayed()

    def produkte_title_is_displayed(self):
        pro_title = WebDriverWait(self.driver, 10).until(HomePageLocators.PRODUKTE_TEXT_TITLE)
        return pro_title.is_displayed()

    def produkte_text_content_check(self):
        pro_text = WebDriverWait(self.driver, 10).until(HomePageLocators.PRODUKTE_TEXT_CONTENT)
        return pro_text.text

    def qualitat_iso_ce_picture_is_displayed(self):
        qua_pic = WebDriverWait(self.driver, 10).until(HomePageLocators.QUALITAT_ISO_CE_PICTURE)
        return qua_pic.is_displayed()

    def qualitat_iso_ce_title_is_displayed(self):
        qua_tit = WebDriverWait(self.driver, 10).until(HomePageLocators.QUALITAT_ISO_CE_TEXT_TITLE)
        return qua_tit.is_displayed()

    def qualitat_iso_ce_text_content_check(self):
        qua_text = WebDriverWait(self.driver, 10).until(HomePageLocators.QUALITAT_ISO_CE_TEXT_CONTENT)
        return qua_text.text

    def qualitat_iso_ce_read_more_link_is_displayed(self):
        qua_read = WebDriverWait(self.driver, 10).until(HomePageLocators.QUALITAT_ISO_CE_READ_MORE)
        return qua_read.is_displayed()

    def first_checker_picture_is_displayed(self):
        first = WebDriverWait(self.driver, 10).until(HomePageLocators.FIRST_CHECKER_PICTURE)
        return first.is_displayed()

    def second_checker_picture_is_displayed(self):
        second = WebDriverWait(self.driver, 10).until(HomePageLocators.SECOND_CHECKER_PICTURE)
        return second.is_displayed()

    def new_in_container_is_displayed(self):
        new = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS)
        return new.is_displayed()

    def new_picture_in_conteiner_is_displayed(self):
        new_picture = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_PICTURE)
        return new_picture.is_displayed()

    def new_text_content_in_container_check(self):
        new_text = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_TEXT_CONTENT)
        return new_text.text

    def new_read_more_link_in_conteiner_is_displayed(self):
        new_ream = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_READ_MORE)
        return new_ream.is_displayed()

    def verfahren_in_container_is_displayed(self):
        verfahren = WebDriverWait(self.driver, 10).until(HomePageLocators.VERFAHREN)
        return verfahren.is_displayed()

    def verfahren_picture_in_container_is_displayed(self):
        ver_picture = WebDriverWait(self.driver, 10).until(HomePageLocators.VERFAHREN_PICTURE)
        return ver_picture.is_displayed()

    def verfahren_text_content_in_container_check(self):
        ver_text = WebDriverWait(self.driver, 10).until(HomePageLocators.VERFAHREN_TEXT_CONTENT)
        return ver_text.text

    def verfahren_read_more_link_is_displayed(self):
        ver_read = WebDriverWait(self.driver, 10).until(HomePageLocators.VERFAHREN_READ_MORE)
        return ver_read.is_displayed()

    def links_in_container_is_displayed(self):
        links = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS)
        return links.is_displayed()

    def links_picture_in_container_is_displayed(self):
        links_picture = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_PICTURE)
        return links_picture.is_displayed()

    def links_text_content_in_container_check(self):
        links_text = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_TEXT_CONTENT)
        return links_text.text

    def links_read_more_link_in_container_is_displayed(self):
        links_read = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_READ_MORE)
        return links_read.is_displayed()

    def zertifikat_is_displayed(self):
        zert = WebDriverWait(self.driver, 10).until(HomePageLocators.ZERTIFIKAT)
        return zert.is_displayed()

    #TODO: napraviti module za svaki link sa home strane
    #NEWS link check everything on that page

    def click_news_read_more_link(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_READ_MORE)
        c.click()

    def first_picture_news_link_is_dispayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_FIRST_PICTURE)
        return d.is_displayed()

    def first_picture_news_link_check_src_atribute(self):
        img = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_FIRST_PICTURE)
        return img.get_attribute("src")

    def first_text_content_news_link_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_FIRST_TEXT_CONTENT)
        return d.is_displayed()

    def first_text_content_news_link_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_FIRST_TEXT_CONTENT)
        return c.text

    def zertifikat_news_link_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_ZERTIFIKAT_PICTURE)
        return d.is_displayed()

    def zertifikat_news_link_check_src_atribute(self):
        img = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_ZERTIFIKAT_PICTURE)
        return img.get_attribute("src")

    def zertifikat_news_link_text_content_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_ZERTIFIKAT_TEXT_CONTENT)
        return d.is_displayed()

    def zertifikat_news_link_text_content_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_ZERTIFIKAT_TEXT_CONTENT)
        return c.text

    def third_picture_news_link_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_THIRD_PICTURE)
        return d.is_displayed()

    def third_picture_news_link_check_src_atribute(self):
        img = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_THIRD_PICTURE)
        return img.get_attribute("src")

    def third_text_content_news_link_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_THIRD_TEXT_CONTENT)
        return d.is_displayed()

    def third_text_content_news_link_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_THIRD_TEXT_CONTENT)
        return c.text

    def fourth_picture_news_link_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_FOURTH_PICTURE)
        return d

    def fourth_picture_news_link_check_src_atribute(self):
        img = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_FOURTH_PICTURE)
        return img.get_attribute("src")

    def fourth_text_content_news_link_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_FOURTH_TEXT_CONTENT)
        return d.is_displayed()

    def fourth_text_content_news_link_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.NEWS_LINK_FOURTH_TEXT_CONTENT)
        return c.text

    # VERFAHREN link check everything on that page
    def click_verfahren_read_more_link(self):
        verf = WebDriverWait(self.driver, 10).until(HomePageLocators.VERFAHREN_READ_MORE)
        verf.click()

    def verfahren_link_first_text_content_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.VERFAHREN_LINK_FIRST_TEXT_CONTENT)
        return d.is_displayed()

    def verfahren_link_first_text_content_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.VERFAHREN_LINK_FIRST_TEXT_CONTENT)
        return c.text

    def verfahren_link_second_text_content_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.VERFAHREN_LINK_SECOND_TEXT_CONTENT)
        return d.is_displayed()

    def verfahren_link_second_text_content_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.VERFAHREN_LINK_SECOND_TEXT_CONTENT)
        return c.text

    def verfahren_link_third_text_content_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.VERFAHREN_LINK_THIRD_TEXT_CONTENT)
        return d.is_displayed()

    def verfahren_link_third_text_content_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.VERFAHREN_LINK_THIRD_TEXT_CONTENT)
        return c.text

    # LINKS link check everything on that page
    def click_links_read_more_link(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_READ_MORE)
        c.click()

    def first_title_links_page_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_FIRST_TITLE)
        return d.is_displayed()

    def first_title_links_page_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_FIRST_TITLE)
        return c.text

    def first_title_link_1_on_links_page_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_FIRST_TITLE_LINK_1)
        return d.is_displayed()

    def first_title_link_1_on_links_page_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_FIRST_TITLE_LINK_1)
        return c.text

    def first_title_link_1_on_links_page_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_FIRST_TITLE_LINK_2)
        return d.is_displayed()

    def first_title_link_2_on_links_page_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_FIRST_TITLE_LINK_2)
        return c.text

    def second_title_on_links_page_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_SECOND_TITLE)
        return d.is_displayed()

    def second_title_on_links_page_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_SECOND_TITLE)
        return c.text

    def second_title_link_1_on_links_page_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_SECOND_TITLE_LINK_1)
        return d.is_displayed()

    def second_title_link_1_on_links_page_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_SECOND_TITLE_LINK_1)
        return c.text

    def third_title_on_links_page_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_THIRD_TITLE)
        return d.is_displayed()

    def third_title_on_links_page_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_THIRD_TITLE)
        return c.text

    def third_title_link_1_on_links_page_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_THIRD_TITLE_LINK_1)
        return d.is_displayed()

    def third_title_link_1_on_links_page_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_THIRD_TITLE_LINK_1)
        return c.text

    def fourth_title_on_links_page_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_FOURTH_TITLE)
        return d.is_displayed()

    def fourth_title_on_links_page_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_FOURTH_TITLE)
        return c.text

    def fourth_title_link_1_on_links_page_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_FOURTH_TITLE_LINK_1)
        return d.is_displayed()

    def fourth_title_link_1_on_links_page_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_FOURTH_TITLE_LINK_1)
        return c.text

    def fourth_title_link_2_on_links_page_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_FOURTH_TITLE_LINK_2)
        return d.is_displayed()

    def fourth_title_link_2_on_links_page_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_FOURTH_TITLE_LINK_2)
        return c.text

    def fourth_title_link_3_on_links_page_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_FOURTH_TITLE_LINK_3)
        return d.is_displayed()

    def fourth_title_link_3_on_links_page_check(self):
        c = WebDriverWait(self.driver, 10).until(HomePageLocators.LINKS_FOURTH_TITLE_LINK_3)
        return c.text





class DienstleistungenPage(BasePage):

    def first_production_picture_is_displayed(self):
        first = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCTION_PICTURE)
        return first.is_displayed()

    def first_production_title_text_is_displayed(self):
        title = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCTION_TITLE_TEXT)
        return title.is_displayed()

    def first_production_title_text_check(self):
        title_check = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCTION_TITLE_TEXT)
        return title_check.text

    def first_production_content_first_paragraph_text_is_displayed(self):
        par = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCTION_CONTENT_FIRST_PARAGRAPH_TEXT)
        return par.is_displayed()

    def first_production_content_first_paragraph_text_check(self):
        par_c = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCTION_CONTENT_FIRST_PARAGRAPH_TEXT)
        return par_c.text

    def first_production_content_second_paragraph_is_displayed(self):
        par = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCTION_CONTENT_SECOND_PARAGRAPH_TEXT)
        return par.is_displayed()

    def first_production_content_second_paragraph_check(self):
        par_c = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCTION_CONTENT_SECOND_PARAGRAPH_TEXT)
        return par_c.text

    def second_production_title_text_is_displayed(self):
        title = WebDriverWait(self.driver, 10).until(DiensLocators.SECOND_PRODUCTION_TITLE_TEXT)
        return title.is_displayed()

    def second_production_title_text_check(self):
        title_c = WebDriverWait(self.driver, 10).until(DiensLocators.SECOND_PRODUCTION_TITLE_TEXT)
        return title_c.text

    def second_production_content_text_is_displayed(self):
        par = WebDriverWait(self.driver, 10).until(DiensLocators.SECOND_PRODUCTION_CONTENT_TEXT)
        return par.is_displayed()

    def second_production_content_text_check(self):
        par_c = WebDriverWait(self.driver, 10).until(DiensLocators.SECOND_PRODUCTION_CONTENT_TEXT)
        return par_c.text

    def second_production_picture_is_displayed(self):
        pic = WebDriverWait(self.driver, 10).until(DiensLocators.SECOND_PRODUCTION_PICTURE)
        return pic.is_displayed()

    def production_spritzgguss_picture_is_displayed(self):
        pic = WebDriverWait(self.driver, 10).until(DiensLocators.PRODUCTION_SPRITZGGUSS_PICTURE)
        return pic.is_displayed()

    def production_spritzgguss_title_text_is_displayed(self):
        title = WebDriverWait(self.driver, 10).until(DiensLocators.PRODUCTION_SPRITZGGUSS_TITLE_TEXT)
        return title.is_displayed()

    def production_spritzgguss_title_text_check(self):
        title_c = WebDriverWait(self.driver, 10).until(DiensLocators.PRODUCTION_SPRITZGGUSS_TITLE_TEXT)
        return title_c.text

    def production_spritzgguss_text_paragraph_1_is_displayed(self):
        par_1 = WebDriverWait(self.driver, 10).until(DiensLocators.PRODUCTION_SPRITZGGUSS_TEXT_PARAGRAPH_1)
        return par_1.is_displayed()

    def production_spritzgguss_text_paragraph_1_check(self):
        par_1_c = WebDriverWait(self.driver, 10).until(DiensLocators.PRODUCTION_SPRITZGGUSS_TEXT_PARAGRAPH_1)
        return par_1_c.text

    def production_spritzgguss_text_paragraph_2_is_displayed(self):
        par_2 = WebDriverWait(self.driver, 10).until(DiensLocators.PRODUCTION_SPRITZGGUSS_TEXT_PARAGRAPH_2)
        return par_2.is_displayed()

    def production_spritzgguss_text_paragraph_2_check(self):
        par_2_c = WebDriverWait(self.driver, 10).until(DiensLocators.PRODUCTION_SPRITZGGUSS_TEXT_PARAGRAPH_2)
        return par_2_c.text

    def entwicklung_text_title_is_displayed(self):
        title = WebDriverWait(self.driver, 10).until(DiensLocators.ENTWICKLUNG_TEXT_TITLE)
        return title.is_displayed()

    def entwicklung_text_title_check(self):
        title_c = WebDriverWait(self.driver, 10).until(DiensLocators.ENTWICKLUNG_TEXT_TITLE)
        return title_c.text

    def entwicklung_text_paragraph_1_is_displayed(self):
        par = WebDriverWait(self.driver, 10).until(DiensLocators.ENTWICKLUNG_TEXT_PARAGRAPH_1)
        return par.is_displayed()

    def entwicklung_text_paragraph_1_check(self):
        par = WebDriverWait(self.driver, 10).until(DiensLocators.ENTWICKLUNG_TEXT_PARAGRAPH_1)
        return par.text

    def entwicklung_text_paragraph_2_is_displayed(self):
        par = WebDriverWait(self.driver, 10).until(DiensLocators.ENTWICKLUNG_TEXT_PARAGRAPH_2)
        return par.is_displayed()

    def entwicklung_text_paragraph_2_check(self):
        par = WebDriverWait(self.driver, 10).until(DiensLocators.ENTWICKLUNG_TEXT_PARAGRAPH_2)
        return par.text

    def entwicklung_picture_is_displayed(self):
        pic = WebDriverWait(self.driver, 10).until(DiensLocators.ENTWICKLUNG_PICTURE)
        return pic.is_displayed()

    def nachbearbeitung_picture_is_displayed(self):
        pic = WebDriverWait(self.driver, 10).until(DiensLocators.NACHBEARBEITUNG_PICTURE)
        return pic.is_displayed()

    def nachbearbeitung_text_title_is_displayed(self):
        title = WebDriverWait(self.driver, 10).until(DiensLocators.NACHBEARBEITUNG_TEXT_TITLE)
        return title.is_displayed()

    def nachbearbeitung_text_title_check(self):
        title = WebDriverWait(self.driver, 10).until(DiensLocators.NACHBEARBEITUNG_TEXT_TITLE)
        return title.text

    def nachbearbeitung_text_content_check(self):
        cont = WebDriverWait(self.driver, 10).until(DiensLocators.NACHBEARBEITUNG_CONTENT_TEXT)
        return cont.text

    def nachbearbeitung_text_content_is_displayed(self):
        cont = WebDriverWait(self.driver, 10).until(DiensLocators.NACHBEARBEITUNG_CONTENT_TEXT)
        return cont.is_displayed()

    def siebdruck_title_is_displayed(self):
        title = WebDriverWait(self.driver, 10).until(DiensLocators.SIEBDRUCK_TITLE)
        return title.is_displayed()

    def siebdruck_title_check(self):
        title_c = WebDriverWait(self.driver, 10).until(DiensLocators.SIEBDRUCK_TITLE)
        return title_c.text

    def siebdruck_text_content_is_displayed(self):
        cont = WebDriverWait(self.driver, 10).until(DiensLocators.SIEBDRUCK_TEXT_CONTENT)
        return cont.is_displayed()

    def siebdruck_text_content_check(self):
        cont = WebDriverWait(self.driver, 10).until(DiensLocators.SIEBDRUCK_TEXT_CONTENT)
        return cont.text

    def siebdruck_picture_is_displayed(self):
        pic = WebDriverWait(self.driver, 10).until(DiensLocators.SIEBDRUCK_PICTURE)
        return pic.is_displayed()

    def sieblador_title_is_displayed(self):
        title = WebDriverWait(self.driver, 10).until(DiensLocators.SIEBLADOR_TITLE)
        return title.is_displayed()

    def sieblador_title_check(self):
        title = WebDriverWait(self.driver, 10).until(DiensLocators.SIEBLADOR_TITLE)
        return title.text

    def sieblador_text_content_is_displayed(self):
        cont = WebDriverWait(self.driver, 10).until(DiensLocators.SIEBLADOR_TEXT_CONTENT)
        return cont.is_displayed()

    def sieblador_text_content_check(self):
        cont = WebDriverWait(self.driver, 10).until(DiensLocators.SIEBLADOR_TEXT_CONTENT)
        return cont.text

    def sieblador_picture_is_displayed(self):
        picture = WebDriverWait(self.driver, 10).until(DiensLocators.SIEBLADOR_PICTURE)
        return picture.is_displayed()

    def werkezeugbau_title_is_displayed(self):
        title = WebDriverWait(self.driver, 10).until(DiensLocators.WERKZEUGBAU_TITLE)
        return title.is_displayed()

    def werkezeugbau_title_check(self):
        title = WebDriverWait(self.driver, 10).until(DiensLocators.WERKZEUGBAU_TITLE)
        return title.text

    def werkezeugbau_text_paragraph_1_is_displayed(self):
        par = WebDriverWait(self.driver, 10).until(DiensLocators.WERKZEUGBAU_TEXT_PARAGRAPH_1)
        return par.is_displayed()

    def werkezeugbau_text_paragraph_1_check(self):
        par = WebDriverWait(self.driver, 10).until(DiensLocators.WERKZEUGBAU_TEXT_PARAGRAPH_1)
        return par.text

    def werkezeugbau_text_paragraph_2_is_displayed(self):
        par = WebDriverWait(self.driver, 10).until(DiensLocators.WERKZEUGBAU_TEXT_PARAGRAPH_2)
        return par.is_displayed()

    def werkezeugbau_text_paragraph_2_check(self):
        par = WebDriverWait(self.driver, 10).until(DiensLocators.WERKZEUGBAU_TEXT_PARAGRAPH_2)
        return par.text

    def werkezeugbau_picture_is_displayed(self):
        pic = WebDriverWait(self.driver, 10).until(DiensLocators.WERKZEUGBAU_PICTURE)
        return pic.is_displayed()

    #TODO: odavde pocinje pojedinacno testiranje stane


    def click_first_title_click(self):
        c = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_TITLE_LINK_CLICK)
        c.click()

    def first_product_text_title_link_is_displayed(self):
        t = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_TEXT_TITLE_LINK)
        return t.is_displayed()

    def first_product_text_title_link_check(self):
        c = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_TEXT_TITLE_LINK)
        return c.text

    def first_product_img_tag_is_displayed(self):
        i = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_IMG_TAG)
        return i.is_displayed()

    def first_product_img_tag_check_src_atribute(self):
        image = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_IMG_TAG)
        return image.get_attribute("src")

    def first_product_next_button_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_NEXT_BUTTON)
        return d.is_displayed()

    def first_product_next_button(self):
        b = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_NEXT_BUTTON)
        b.click()

    def first_product_paragraph_1_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_PARAGRAPH_1)
        return d.is_displayed()

    def first_product_paragraph_1_check(self):
        c = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_PARAGRAPH_1)
        return c.text

    def first_product_paragraph_2_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_PARAGRAPH_2)
        return d.is_displayed()

    def first_product_paragraph_2_check(self):
        c = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_PARAGRAPH_2)
        return c.text

    def first_product_facebook_block_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_FACEBOOK_BLOCK)
        return d.is_displayed()

    def first_product_facebook_block_check(self):
        c = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_FACEBOOK_BLOCK)
        return c.text

    def first_product_twetter_block_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_TWETTER_BLOCK)
        return d.is_displayed()

    def first_product_tweeter_block_check(self):
        c = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_TWETTER_BLOCK)
        return c.text

    def first_product_box_1_picture_is_displayed(self):
        i = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_BOX_1_PICTURE)
        return i.is_displayed()

    def first_product_box_1_picture_check_src_atribute(self):
        image = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_BOX_1_PICTURE)
        return image.get_attribute("src")

    def first_product_box_2_picture_is_displayed(self):
        i = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_BOX_2_PICTURE)
        return i.is_displayed()

    def first_product_box_2_picture_check_src_atribute(self):
        image = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_BOX_2_PICTURE)
        return image.get_attribute("src")
    def first_product_box_3_picture_is_displayed(self):
        i = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_BOX_3_PICTURE)
        return i.is_displayed()

    def first_product_box_3_picture_check_src_atribute(self):
        image = WebDriverWait(self.driver, 10).until(DiensLocators.FIRST_PRODUCT_BOX_3_PICTURE)
        return image.get_attribute("src")



class UberUnsPage(BasePage):

    def uber_uns_title_text_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(UberUnsLocators.UBER_UNS_TITLE_TEXT)
        return d.is_displayed()

    def uber_uns_title_text_check(self):
        c = WebDriverWait(self.driver, 10).until(UberUnsLocators.UBER_UNS_TITLE_TEXT)
        return c.text

    def uber_uns_picture_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(UberUnsLocators.UBER_UNS_PICTURE)
        return d.is_displayed()

    def uber_uns_picture_src_check(self):
        image = WebDriverWait(self.driver, 10).until(UberUnsLocators.UBER_UNS_PICTURE)
        return image.get_attribute("src")

    def uber_uns_paragraph_content_text_is_displayad(self):
        d = WebDriverWait(self.driver, 10).until(UberUnsLocators.UBER_UNS_PARAGRAPH_CONTENT_TEXT)
        return d.is_displayed()

    def uber_uns_paragraph_content_text_check(self):
        c = WebDriverWait(self.driver, 10).until(UberUnsLocators.UBER_UNS_PARAGRAPH_CONTENT_TEXT)
        return c.text


class Geschichite(BasePage):

    def geschichite_year_1956_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1956)
        return d.is_displayed()

    def geschichite_year_1956_check_year_number(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1956)
        return c.text

    def geschichite_year_1956_text_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1956_TEXT)
        return d.is_displayed()

    def geschichite_year_1956_text_check(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1956_TEXT)
        return c.text

    def geschichite_year_1977_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1977)
        return d.is_displayed()

    def geschichite_year_1977_check_year_number(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1977)
        return c.text

    def geschichite_year_1977_text_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1977_TEXT)
        return d.is_displayed()

    def geschichite_year_1977_text_check(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1977_TEXT)
        return c.text

    def geschichite_year_1979_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1979)
        return d.is_displayed()

    def geschichite_year_1979_check_year_number(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1979)
        return c.text

    def geschichite_year_1979_text_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1979_TEXT)
        return d.is_displayed()

    def geschichite_year_1979_text_check(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1979_TEXT)
        return c.text

    def geschichite_year_1980_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1980)
        return d.is_displayed()

    def geschichite_year_1980_check_year_number(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1980)
        return c.text

    def geschichite_year_1980_text_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1980_TEXT)
        return d.is_displayed()

    def geschichite_year_1980_text_check(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1980_TEXT)
        return c.text

    def geschichite_year_1981_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1981)
        return d.is_displayed()

    def geschichite_year_1981_check_year_number(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1981)
        return c.text

    def geschichite_year_1981_text_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1981_TEXT)
        return d.is_displayed()

    def geschichite_year_1981_text_check(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1981_TEXT)
        return c.text

    def geschichite_year_1992_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1992)
        return d.is_displayed()

    def geschichite_year_1992_check_year_number(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1992)
        return c.text

    def geschichite_year_1992_text_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1992_TEXT)
        return d.is_displayed()

    def geschichite_year_1992_text_check(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1992_TEXT)
        return c.text

    def geschichite_year_1997_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1997)
        return d.is_displayed()

    def geschichite_year_1997_check_year_number(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1997)
        return c.text

    def geschichite_year_1997_text_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1997_TEXT)
        return d.is_displayed()

    def geschichite_year_1997_text_check(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_1997_TEXT)
        return c.text

    def geschichite_year_2007_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2007)
        return d.is_displayed()

    def geschichite_year_2007_check_year_number(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2007)
        return c.text

    def geschichite_year_2007_text_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2007_TEXT)
        return d.is_displayed()

    def geschichite_year_2007_text_check(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2007_TEXT)
        return c.text

    def geschichite_year_2010_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2010)
        return d.is_displayed()

    def geschichite_year_2010_check_year_number(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2010)
        return c.text

    def geschichite_year_2010_text_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2010_TEXT)
        return d.is_displayed()

    def geschichite_year_2010_text_check(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2010_TEXT)
        return c.text

    def geschichite_year_2013_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2013)
        return d.is_displayed()

    def geschichite_year_2013_check_year_number(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2013)
        return c.text

    def geschichite_year_2013_text_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2013_TEXT)
        return d.is_displayed()

    def geschichite_year_2013_text_check(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2013_TEXT)
        return c.text

    def geschichite_year_2014_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2014)
        return d.is_displayed()

    def geschichite_year_2014_check_year_number(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2014)
        return c.text

    def geschichite_year_2014_text_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2014_TEXT)
        return d.is_displayed()

    def geschichite_year_2014_text_check(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2014_TEXT)
        return c.text

    def geschichite_year_2015_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2015)
        return d.is_displayed()

    def geschichite_year_2015_check_year_number(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2015)
        return c.text

    def geschichite_year_2015_text_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2015_TEXT)
        return d.is_displayed()

    def geschichite_year_2015_text_check(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2015_TEXT)
        return c.text

    def geschichite_year_2016_1_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2016_1)
        return d.is_displayed()

    def geschichite_year_2016_1_check_year_number(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2016_1)
        return c.text

    def geschichite_year_2016_text_1_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2016_TEXT_1)
        return d.is_displayed()

    def geschichite_year_2016_text_1_check(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2016_TEXT_1)
        return c.text

    def geschichite_year_2016_2_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2016_2)
        return d.is_displayed()

    def geschichite_year_2016_2_check_year_number(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2016_2)
        return c.text

    def geschichite_year_2016_text_2_is_displayed(self):
        d = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2016_TEXT_2)
        return d.is_displayed()

    def geschichite_year_2016_text_2_check(self):
        c = WebDriverWait(self.driver, 10).until(GeschichiteLocators.YEAR_2016_TEXT_2)
        return c.text