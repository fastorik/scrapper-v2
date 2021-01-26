from scraper import SklepScraper, AtafScraper
from manager.scraping import ScrapingManager
from utils.images import ImageDownloader


if __name__ == '__main__':
    scr = ScrapingManager(SklepScraper, AtafScraper)

    items = scr.scrap()
    print(items)

    # ImageDownloader.download(list(map(lambda x: x.image_url, items)))


