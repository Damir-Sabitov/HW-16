import pytest
from selene import browser, have


@pytest.fixture (params=[(844,390),(414,896),(430,932)])
def browser_mobile_setup(request):
    browser.config.window_height, browser.config.window_width = request.param
    yield
    browser.quit()

@pytest.fixture (params=[(1920,1080),(2560,1440),(2000,1200)])
def browser_desktop_setup(request):
    browser.config.window_height, browser.config.window_width = request.param
    yield
    browser.quit()


def test_github_desktop(browser_desktop_setup):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('html').should(have.text('Sign up for GitHub'))


def test_github_mobile(browser_mobile_setup):
    browser.open('https://github.com')
    browser.element('.js-header-menu-toggle').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('html').should(have.text('Sign up for GitHub'))