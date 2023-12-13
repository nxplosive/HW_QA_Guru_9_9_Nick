import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_with_allure_steps(open_browser):
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").type("nxplosive/HW_QA_Guru_9_8_Nick")
        s("#query-builder-test").submit()

    with allure.step("Переходим по ссылке репо"):
        s(by.link_text("nxplosive/HW_QA_Guru_9_8_Nick")).click()

    with allure.step("Открываем Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue #1"):
        s(by.partial_text("#1")).should(be.visible)