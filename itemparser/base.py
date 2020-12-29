from model.clothes import Sneaker
from .decorators import attr_error_catcher
from itertools import starmap, repeat


class BaseItemParser:
    price_attrs = None
    name_attrs = None
    url_attrs = None
    sizes_attrs = None
    article_attrs = None

    url_wrapping_tag = None
    img_wrapping_tag = None

    img_url_attr = None

    def __init__(self, container):
        self.container = container
        self.setup()

    def setup(self):
        for key in filter(lambda x: 'attrs' in x, self.__class__.__dict__):  # TODO: names to variables
            setattr(self, key, {'attrs': self.__class__.__dict__[key]})

        attrs = starmap(getattr, list(zip(repeat(self), filter(lambda x: 'get_' in x, dir(self)))))

        for attr in attrs:
            setattr(self, attr.__name__, attr_error_catcher(attr))

    def get_name(self):
        return self.container.find(**self.name_attrs).get_text()

    def get_price(self):
        return self.container.find(**self.price_attrs).get_text()

    def get_url(self):
        return self.container.find(self.url_wrapping_tag)['href']

    def get_sizes(self):
        return list(map(lambda x: x.get_text(), self.container.find_all(**self.sizes_attrs)))

    def get_image_url(self):
        return self.container.find(self.img_wrapping_tag)[self.img_url_attr]

    def get_article(self):
        return self.container.find(**self.article_attrs).get_text()

    def build_parsed_item(self):
        return Sneaker(name=self.get_name(),
                       price=self.get_price(),
                       url=self.get_url(),
                       sizes=self.get_sizes(),
                       image_url=self.get_image_url(),
                       article=self.get_article())
