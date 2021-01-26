from scraper import SklepScraper
import aiohttp
import asyncio
import itertools


class AsyncSklepScraper(SklepScraper):

    async def parse(self, executor=None):
        async with aiohttp.ClientSession(headers=self.api_kwargs['headers']) as self.api:
            pages = await self.get_pages()
            # print(pages)
            results = await asyncio.gather(*map(self.parse_page_items, pages))
            items = list(map(self.to_item_model, itertools.chain.from_iterable(results)))
            print(items)

    async def parse_page_items(self, page_url):
        source = await self.get_page_results(page_url)
        soup = self.selector(source, 'html.parser')  # TODO: user defined behaviour

        # print(f'Parser name: {self.__class__.__name__}')
        # print(soup)

        container = self.get_items_container(soup)

        return self.get_items(container)

    async def get_page_results(self, url):
        async with self.api.get(url) as response:
            return await response.text()

    async def get_pages(self):
        source = await self.get_page_results(self.start_url)

        pages_number = self.get_pages_number(self.selector(source, 'html.parser'))

        # print(f'Pages number: {pages_number}')
        return map(lambda x: self.url_pattern.format(x), range(1, pages_number + 1))
