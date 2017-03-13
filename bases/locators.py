class CommonLocators(object):
    # header navbar
    LOGO = lambda driver: driver.find_element_by_css_selector("#header > div > div.col-md-3.no-pm > div > a > img")
    HOME = lambda driver: driver.find_element_by_css_selector("#navbar-pc > ul > li:nth-child(1) > a")
    DIENSTLEISTUNGEN = lambda driver: driver.find_element_by_css_selector("#navbar-pc > ul > li:nth-child(2) > a")
    UBER_UNS = lambda driver: driver.find_element_by_css_selector("#navbar-pc > ul > li:nth-child(3) > a")
    GESCHICHTE = lambda driver: driver.find_element_by_css_selector("#navbar-pc > ul > li:nth-child(4) > a")
    OKOLOGIE = lambda driver: driver.find_element_by_css_selector("#navbar-pc > ul > li:nth-child(5) > a")
    KONTAKT = lambda driver: driver.find_element_by_css_selector("#navbar-pc > ul > li:nth-child(6) > a")
    # text content
    WIR_STELLEN_FUR_DIE_BRANCHEN = lambda driver: driver.find_element_by_css_selector \
        ("#slider-content > div.text-content > h3")
    DER_PHARMA = lambda driver: driver.find_element_by_css_selector \
        ("#slider-content > div.text-content > ul > li:nth-child(1)")
    DER_LEBENSMITTEL_UND = lambda driver: driver.find_element_by_css_selector \
        ("#slider-content > div.text-content > ul > li:nth-child(2)")
    DER_CHEMISCHEN_INDUSTRIE = lambda driver: driver.find_element_by_css_selector \
        ("#slider-content > div.text-content > ul > li:nth-child(3)")
    # footer
    ADDRESS = lambda driver: driver.find_element_by_css_selector \
        ("#footer > div > div > div.col-xs-12.col-sm-12.col-md-2 > div")
    ALL_PHONES = lambda driver: driver.find_element_by_css_selector \
        ("#footer > div > div > div.col-xs-12.col-sm-12.col-md-3 > div")
    FIRST_PHONE_TEXT = lambda driver: driver.find_element_by_css_selector \
        ("#footer > div > div > div.col-xs-12.col-sm-12.col-md-3 > div > span:nth-child(1)")
    SECOND_PHONE_TEXT = lambda driver: driver.find_element_by_css_selector \
        ("#footer > div > div > div.col-xs-12.col-sm-12.col-md-3 > div > span:nth-child(3)")
    # footer navbar
    HOME_LINK = lambda driver: driver.find_element_by_css_selector \
        ("#footer > div > div > div.hidden-sm.hidden-xs.col-md-7 > div > ul > li:nth-child(1) > a")
    DIENSTLEISTUNGEN_LINK = lambda driver: driver.find_element_by_css_selector \
        ("#footer > div > div > div.hidden-sm.hidden-xs.col-md-7 > div > ul > li:nth-child(2) > a")
    UBER_UNS_LINK = lambda driver: driver.find_element_by_css_selector \
        ("#footer > div > div > div.hidden-sm.hidden-xs.col-md-7 > div > ul > li:nth-child(3) > a")
    GESCHICHTE_LINK = lambda driver: driver.find_element_by_css_selector \
        ("#footer > div > div > div.hidden-sm.hidden-xs.col-md-7 > div > ul > li:nth-child(4) > a")
    OKOLOGIE_LINK = lambda driver: driver.find_element_by_css_selector \
        ("#footer > div > div > div.hidden-sm.hidden-xs.col-md-7 > div > ul > li:nth-child(5) > a")
    KONTAKT_LINK = lambda driver: driver.find_element_by_css_selector \
        ("#footer > div > div > div.hidden-sm.hidden-xs.col-md-7 > div > ul > li:nth-child(6) > a")


class HomePageLocators(object):


    SEE_MORE_PRODUCTS = lambda driver: driver.find_element_by_css_selector\
        ("#slider-content > div.sm-box-content > div.header-title-sm")
    DIENSTLEISTUNGEN_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("#slider-content > div.lg-box-content > div.more-products > div:nth-child(1) > div > div")
    DIENSTLEISTUNGEN_TEXT_TITLE = lambda driver: driver.find_element_by_css_selector\
        ("#slider-content > div.lg-box-content > div.more-products > div:nth-child(1) > div > h2")
    DIENSTLEISTUNGEN_TEXT_CONTENT = lambda driver: driver.find_element_by_css_selector\
        ("#slider-content > div.lg-box-content > div.more-products > div:nth-child(1) > div > p")
    DIENSTLEISTUNGEN_READ_MORE = lambda driver: driver.find_element_by_css_selector\
        ("#slider-content > div.lg-box-content > div.more-products > div:nth-child(1) > div > a")
    PRODUKTE_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("#slider-content > div.lg-box-content > div.more-products > div:nth-child(2) > div > div")
    PRODUKTE_TEXT_TITLE = lambda driver: driver.find_element_by_css_selector\
        ("#slider-content > div.lg-box-content > div.more-products > div:nth-child(2) > div > h2")
    PRODUKTE_TEXT_CONTENT = lambda driver: driver.find_element_by_css_selector\
        ("#slider-content > div.lg-box-content > div.more-products > div:nth-child(2) > div > p")
    QUALITAT_ISO_CE_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("#slider-content > div.lg-box-content > div.more-products > div:nth-child(3) > div > div")
    QUALITAT_ISO_CE_TEXT_TITLE = lambda driver: driver.find_element_by_css_selector\
        ("#slider-content > div.lg-box-content > div.more-products > div:nth-child(3) > div > h2")
    QUALITAT_ISO_CE_TEXT_CONTENT = lambda driver: driver.find_element_by_css_selector\
        ("#slider-content > div.lg-box-content > div.more-products > div:nth-child(3) > div > p")
    QUALITAT_ISO_CE_READ_MORE = lambda driver: driver.find_element_by_css_selector\
        ("#slider-content > div.lg-box-content > div.more-products > div:nth-child(3) > div > a")
    FIRST_CHECKER_PICTURE = lambda driver: driver.find_element_by_css_selector("#doot-id-1")
    SECOND_CHECKER_PICTURE = lambda driver: driver.find_element_by_css_selector("#doot-id-2")

    NEWS = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section > div > div.row > div:nth-child(1) > div.title")
    NEWS_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section > div > div.row > div:nth-child(1) > div.img-news > img")
    NEWS_TEXT_CONTENT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section > div > div.row > div:nth-child(1) > div.news-p > p")
    NEWS_READ_MORE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section > div > div.row > div:nth-child(1) > a")
    VERFAHREN = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section > div > div.row > div:nth-child(2) > div.title")
    VERFAHREN_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section > div > div.row > div:nth-child(2) > div.img-news > img")
    VERFAHREN_TEXT_CONTENT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section > div > div.row > div:nth-child(2) > div.news-p > p")
    VERFAHREN_READ_MORE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section > div > div.row > div:nth-child(2) > a")
    LINKS = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section > div > div.row > div:nth-child(3) > div.title")
    LINKS_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section > div > div.row > div:nth-child(3) > div.img-news > img")
    LINKS_TEXT_CONTENT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section > div > div.row > div:nth-child(3) > div.news-p > p")
    LINKS_READ_MORE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section > div > div.row > div:nth-child(3) > a")
    ZERTIFIKAT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section > div > div.col-xs-12.col-sm-6.col-md-2 > a > img")

    # news link lokators
    NEWS_LINK_FIRST_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.news-container > div > div > div:nth-child(1) > div > div > div:nth-child(1) > div > img")
    NEWS_LINK_FIRST_TEXT_CONTENT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.news-container > div > div > div:nth-child(1) > div > div > div:nth-child(2) > div > div")
    NEWS_LINK_ZERTIFIKAT_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.news-container > div > div > div:nth-child(2) > div > div > div:nth-child(1) > div > img")
    NEWS_LINK_ZERTIFIKAT_TEXT_CONTENT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.news-container > div > div > div:nth-child(2) > div > div > div:nth-child(2) > div > div")
    NEWS_LINK_THIRD_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.news-container > div > div > div:nth-child(3) > div > div > div:nth-child(1) > div > img")
    NEWS_LINK_THIRD_TEXT_CONTENT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.news-container > div > div > div:nth-child(3) > div > div > div:nth-child(2) > div > div")
    NEWS_LINK_FOURTH_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.news-container > div > div > div:nth-child(4) > div > div > div:nth-child(1) > div > img")
    NEWS_LINK_FOURTH_TEXT_CONTENT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.news-container > div > div > div:nth-child(4) > div > div > div:nth-child(2) > div > div")

    #verfahren link locators
    VERFAHREN_LINK_FIRST_TEXT_CONTENT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.links-container > div > div > div:nth-child(1) > div > div > div > div")
    VERFAHREN_LINK_SECOND_TEXT_CONTENT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.links-container > div > div > div:nth-child(2) > div > div > div > div")
    VERFAHREN_LINK_THIRD_TEXT_CONTENT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.links-container > div > div > div:nth-child(3) > div > div > div > div")

    # links link locators
    LINKS_FIRST_TITLE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.links-container > div > div > div:nth-child(1) > div > div > div > div > div")
    LINKS_FIRST_TITLE_LINK_1 = lambda driver: driver.find_element_by_css_selector\
        ("body > div.links-container > div > div > div:nth-child(1) > div > div > div > div > a:nth-child(2)")
    LINKS_FIRST_TITLE_LINK_2 = lambda driver: driver.find_element_by_css_selector\
        ("body > div.links-container > div > div > div:nth-child(1) > div > div > div > div > a:nth-child(4)")
    LINKS_SECOND_TITLE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.links-container > div > div > div:nth-child(2) > div > div > div > div > div")
    LINKS_SECOND_TITLE_LINK_1 = lambda driver: driver.find_element_by_css_selector\
        ("body > div.links-container > div > div > div:nth-child(2) > div > div > div > div > a")
    LINKS_THIRD_TITLE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.links-container > div > div > div:nth-child(3) > div > div > div > div > div")
    LINKS_THIRD_TITLE_LINK_1 = lambda driver: driver.find_element_by_css_selector\
        ("body > div.links-container > div > div > div:nth-child(3) > div > div > div > div > a")
    LINKS_FOURTH_TITLE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.links-container > div > div > div:nth-child(4) > div > div > div > div > div")
    LINKS_FOURTH_TITLE_LINK_1 = lambda driver: driver.find_element_by_css_selector\
        ("body > div.links-container > div > div > div:nth-child(4) > div > div > div > div > a:nth-child(2)")
    LINKS_FOURTH_TITLE_LINK_2 = lambda driver: driver.find_element_by_css_selector\
        ("body > div.links-container > div > div > div:nth-child(4) > div > div > div > div > a:nth-child(4)")
    LINKS_FOURTH_TITLE_LINK_3 = lambda driver: driver.find_element_by_css_selector \
        ("body > div.links-container > div > div > div:nth-child(4) > div > div > div > div > a:nth-child(6)")






class DiensLocators(object):

    FIRST_PRODUCTION_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(1) > div.container > div > div.col-xs-12.col-md-6.col-lg-6.pull-left > div > img")
    FIRST_PRODUCTION_TITLE_TEXT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(1) > div.container > div > div:nth-child(2) > div > div > a")
    FIRST_PRODUCTION_CONTENT_FIRST_PARAGRAPH_TEXT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(1) > div.container > div > div:nth-child(2) > div > p:nth-child(2)")
    FIRST_PRODUCTION_CONTENT_SECOND_PARAGRAPH_TEXT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(1) > div.container > div > div:nth-child(2) > div > p:nth-child(4)")
    SECOND_PRODUCTION_TITLE_TEXT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(2) > div.container > div > div:nth-child(2) > div > div > a")
    SECOND_PRODUCTION_CONTENT_TEXT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(2) > div.container > div > div:nth-child(2) > div > p")
    SECOND_PRODUCTION_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(2) > div.container > div > div.col-xs-12.col-md-6.col-lg-6.pull-right > div > img")
    PRODUCTION_SPRITZGGUSS_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(3) > div.container > div > div.col-xs-12.col-md-6.col-lg-6.pull-left > div > img")
    PRODUCTION_SPRITZGGUSS_TITLE_TEXT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(3) > div.container > div > div:nth-child(2) > div > div > a")
    PRODUCTION_SPRITZGGUSS_TEXT_PARAGRAPH_1 = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(3) > div.container > div > div:nth-child(2) > div > p:nth-child(2)")
    PRODUCTION_SPRITZGGUSS_TEXT_PARAGRAPH_2 = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(3) > div.container > div > div:nth-child(2) > div > p:nth-child(4)")
    ENTWICKLUNG_TEXT_TITLE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(4) > div.container > div > div:nth-child(2) > div > div > a")
    ENTWICKLUNG_TEXT_PARAGRAPH_1 = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(4) > div.container > div > div:nth-child(2) > div > p:nth-child(2)")
    ENTWICKLUNG_TEXT_PARAGRAPH_2 = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(4) > div.container > div > div:nth-child(2) > div > p:nth-child(4)")
    ENTWICKLUNG_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(4) > div.container > div > div.col-xs-12.col-md-6.col-lg-6.pull-right > div > img")
    NACHBEARBEITUNG_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(5) > div.container > div > div.col-xs-12.col-md-6.col-lg-6.pull-left > div > img")
    NACHBEARBEITUNG_TEXT_TITLE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(5) > div.container > div > div:nth-child(2) > div > div > a")
    NACHBEARBEITUNG_CONTENT_TEXT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(5) > div.container > div > div:nth-child(2) > div > p")
    SIEBDRUCK_TITLE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(6) > div.container > div > div:nth-child(2) > div > div > a")
    SIEBDRUCK_TEXT_CONTENT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(6) > div.container > div > div:nth-child(2) > div > p")
    SIEBDRUCK_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(6) > div.container > div > div.col-xs-12.col-md-6.col-lg-6.pull-right > div > img")
    SIEBLADOR_TITLE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(7) > div.container > div > div:nth-child(2) > div > div > a")
    SIEBLADOR_TEXT_CONTENT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(7) > div.container > div > div:nth-child(2) > div > p")
    SIEBLADOR_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(7) > div.container > div > div.col-xs-12.col-md-6.col-lg-6.pull-left > div > img")
    WERKZEUGBAU_TITLE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div.product-box.none-box > div.container > div > div:nth-child(2) > div > div > a")
    WERKZEUGBAU_TEXT_PARAGRAPH_1 = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div.product-box.none-box > div.container > div > div:nth-child(2) > div > p:nth-child(2)")
    WERKZEUGBAU_TEXT_PARAGRAPH_2 = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div.product-box.none-box > div.container > div > div:nth-child(2) > div > p:nth-child(3)")
    WERKZEUGBAU_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div.product-box.none-box > div.container > div > div.col-xs-12.col-md-6.col-lg-6.pull-right > div > img")

    # get ich link on product page
    # first link element
    FIRST_TITLE_LINK_CLICK = lambda driver: driver.find_element_by_css_selector\
        ("body > div.product-container > div > div > div:nth-child(1) > div.container > div > div:nth-child(2) > div > div > a")
    FIRST_PRODUCT_TEXT_TITLE_LINK = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section.home-news-section-inside > div > div > div > div > div > div > div > div > div > div.title")
    FIRST_PRODUCT_IMG_TAG = lambda driver: driver.find_element_by_css_selector("#img-0")
    FIRST_PRODUCT_NEXT_BUTTON = lambda driver: driver.find_element_by_css_selector("#changer-btn")
    FIRST_PRODUCT_PARAGRAPH_1 = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section.home-news-section-inside > div > div > div > div > div > div > div > div > div > div:nth-child(3) > div.product-content > p:nth-child(1)")
    FIRST_PRODUCT_PARAGRAPH_2 = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section.home-news-section-inside > div > div > div > div > div > div > div > div > div > div:nth-child(3) > div.product-content > p:nth-child(2)")
    FIRST_PRODUCT_FACEBOOK_BLOCK = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section.home-news-section-inside > div > div > div > div > div > div > div > div > div > div:nth-child(3) > div.social-share > a.button-share.fb-btn-share")
    FIRST_PRODUCT_TWETTER_BLOCK = lambda driver: driver.find_element_by_css_selector\
        ("body > div.home-news-section.home-news-section-inside > div > div > div > div > div > div > div > div > div > div:nth-child(3) > div.social-share > a.button-share.tw-btn-share")
    FIRST_PRODUCT_BOX_1_PICTURE = lambda driver: driver.find_element_by_css_selector("#img-1")
    FIRST_PRODUCT_BOX_2_PICTURE = lambda driver: driver.find_element_by_css_selector("#img-2")
    FIRST_PRODUCT_BOX_3_PICTURE = lambda driver: driver.find_element_by_css_selector("#img-3")


class UberUnsLocators(object):

    UBER_UNS_TITLE_TEXT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.about-container > div > div > div > div > div > div:nth-child(1) > div.title")
    UBER_UNS_PICTURE = lambda driver: driver.find_element_by_css_selector\
        ("body > div.about-container > div > div > div > div > div > div:nth-child(1) > div.img-cover > img")
    UBER_UNS_PARAGRAPH_CONTENT_TEXT = lambda driver: driver.find_element_by_css_selector\
        ("body > div.about-container > div > div > div > div > div > div:nth-child(2) > div > p")






















