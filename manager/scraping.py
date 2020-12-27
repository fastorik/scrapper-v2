from itertools import chain
from concurrent.futures import ThreadPoolExecutor, as_completed


class ScrapingManager:
    def __init__(self, *scrapers):
        self.scrapers = scrapers
        self.items = []

    def scrap(self):
        # return list(chain(*map(lambda x: x().parse(), self.scrapers)))
        with ThreadPoolExecutor(max_workers=len(self.scrapers)) as executor:
            items = list(chain(*executor.map(self._scrap, self.scrapers)))
            # futures = [executor.submit(self.init_scraper, scraper) for scraper in self.scrapers]
            #
            # for future in as_completed(futures):
            #     self.items.extend(future.result())

        return items

    def _scrap(self, scraper):
        return scraper().parse()
