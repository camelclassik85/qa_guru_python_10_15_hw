import time

from selene import browser, command

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


def test_github_desktop(desktop_browser):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(mobile_browser):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('a[class*="HeaderMenu-link--sign-in"]').perform(command.js.scroll_into_view).click()
