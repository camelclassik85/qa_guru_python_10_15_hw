import pytest
from selene import browser


FULL_HD = (1920, 1080)
HD = (1080, 720)
MOB1 = (800, 480)
MOB2 = (480, 320)


@pytest.fixture(params=[FULL_HD, HD])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.base_url = 'https://github.com'

    yield browser

    browser.quit()


@pytest.fixture(params=[MOB1, MOB2])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.base_url = 'https://github.com'

    yield browser

    browser.quit()
