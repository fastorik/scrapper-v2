from concurrent.futures.thread import ThreadPoolExecutor
import requests
from driver.session import SessionDriver


class SessionDriverMixin:
    api_class = SessionDriver
    api_kwargs = {
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        },
        'mount': requests.sessions.HTTPAdapter(max_retries=10)
    }

    def parse(self, executor=None):
        with ThreadPoolExecutor(max_workers=4) as executor:
            return super().parse(executor)


class FirefoxDriverMixin:
    pass
