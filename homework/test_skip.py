"""
Параметризуйте фикстуру несколькими вариантами размеров окна.
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from homework.conftest import DESCTOP, MOB
from selene import browser, command


def test_github_desktop(common_browser):
    screen = (common_browser.config.window_width, common_browser.config.window_height)
    if screen in DESCTOP:
        browser.open('/')
        browser.element('.HeaderMenu-link--sign-in').click()
    else:
        pytest.skip(reason=f'размеры экрана {screen} не десктопные({DESCTOP})')


def test_github_mobile(common_browser):
    screen = (common_browser.config.window_width, common_browser.config.window_height)
    if screen in MOB:
        browser.open('/')
        browser.element('.Button--link').click()
        browser.element('a[class*="HeaderMenu-link--sign-in"]').perform(command.js.scroll_into_view).click()
    else:
        pytest.skip(reason=f'размеры экрана {screen} не мобильные({MOB})')
