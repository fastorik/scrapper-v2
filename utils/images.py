import requests
from concurrent.futures import ThreadPoolExecutor


class ImageDownloader:
    @staticmethod
    def download(urls):
        with ThreadPoolExecutor(max_workers=20) as executor:
            for index, url in enumerate(urls):
                print(url)
                executor.submit(ImageDownloader.download_image, url, f'{str(index)}sneaker')

    @staticmethod
    def download_image(url, name):
        content = requests.get(url).content
        with open(f'images\\{name}.jpg', 'wb') as image:
            image.write(content)
            print('written')
