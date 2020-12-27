from scraper import SklepScraper, AtafScraper
from manager.scraping import ScrapingManager

scr = ScrapingManager(SklepScraper, AtafScraper)

items = scr.scrap()

print(len(items))
