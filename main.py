from scraper import SklepScraper, AtafScraper, AsyncSklepScraper
# from manager.scraping import ScrapingManager
# from utils.images import ImageDownloader
import asyncio


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(AsyncSklepScraper().parse())
    # scr = ScrapingManager(SklepScraper, AtafScraper)
    #
    # items = scr.scrap()
    # print(items)

    # ImageDownloader.download(list(map(lambda x: x.image_url, items)))


