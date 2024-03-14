"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, command


@pytest.mark.parametrize('desktop_browser', [(1600, 900), (1280, 1000)], indirect=True)
def test_github_desktop(desktop_browser):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('mobile_browser', [(880, 700), (640, 480)], indirect=True)
def test_github_mobile(mobile_browser):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('a[class*="HeaderMenu-link--sign-in"]').perform(command.js.scroll_into_view).click()
