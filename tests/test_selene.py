from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_classic_selene(open_browser):
    browser.open("https://github.com")

    s(".header-search-button").click()
    s("#query-builder-test").type("nxplosive/HW_QA_Guru_9_8_Nick")
    s("#query-builder-test").submit()

    s(by.link_text("nxplosive/HW_QA_Guru_9_8_Nick")).click()

    s("#issues-tab").click()

    s(by.partial_text("#1")).should(be.visible)