from scraper import SklepScraper, AtafScraper
from manager.scraping import ScrapingManager

# scr = ScrapingManager(SklepScraper, AtafScraper)
#
# items = scr.scrap()
#
# print(items)

# print(AtafScraper.__name__)

scr = SklepScraper()
items = scr.parse()

print(len(items))


# class PropertyTest:
#
#     @property
#     def text(self):
#         return self._text()
#
#     def _text(self):
#         pass
#
#
# class IheritedTest(PropertyTest):
#     def _text(self):
#         return 'jopa'
#
#
# tst = IheritedTest()
# print(tst.text)
