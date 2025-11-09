import pytest
from util.browser_factory import get_browser
from config.config import Config

@pytest.fixture(scope="class")
def setup(request):
    driver = get_browser('edge')
    print('Launch browser successfully!')
    driver.maximize_window()
    driver.get(Config.BASE_URL)
    print('Load browser successfully')
    request.cls.driver = driver
    yield
    driver.quit()
