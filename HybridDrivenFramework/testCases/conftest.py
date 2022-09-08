from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup(browser):
    # Parallel command -pytest -v -s -n=2 testCases/test_login.py --browser chrome
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        print("Launching the Chrome browser************")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching the Firefox browser************")
    return driver


def pytest_addoption(parser):  # it will get the values from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # it will return the browser value to set method
    return request.config.getoption("--browser")


# pip install pytest-html
# Report Generate Command-pytest -v -s -n=2 --html=Reports\report.html testCases/test_login.py --browser chrome
## Generating the HTML report
# It is hook for adding the environment into html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'HybridDrivenFramework'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Sridhar'


# It is hook for delete/modify environment info into html
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
