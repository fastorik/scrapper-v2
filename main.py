from scraper import SklepScraper, AtafScraper
from manager.scraping import ScrapingManager

scr = ScrapingManager(SklepScraper, AtafScraper)

items = scr.scrap()

print(items)

# print(AtafScraper.__name__)

# scr = AtafScraper()
# items = scr.parse()
#
# print(items)
