import requests
from driver.session import SessionDriver
from scraper import SklepScraper, AtafScraper, AsyncSklepScraper
from manager.scraping import ScrapingManager
# from utils.images import ImageDownloader
# import asyncio


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(AsyncSklepScraper().parse())
    scr = ScrapingManager(AtafScraper)#, AtafScraper)

    items = scr.scrap()
    print(items)
    print(len(items))

    # ImageDownloader.download(list(map(lambda x: x.image_url, items)))

    # api_kwargs = {
    #     'headers': {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    #         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #         'accept-encoding': 'gzip, deflate, br',
    #         'accept-language': 'ru-BY,ru;q=0.9',
    #     },
    #     # 'mount': requests.sessions.HTTPAdapter(max_retries=10)
    # }
    #
    # driver = SessionDriver(**api_kwargs)
    # print(driver.get_page_with_source('https://www.adidas.pl/mezczyzni-buty-koszykowka'))
