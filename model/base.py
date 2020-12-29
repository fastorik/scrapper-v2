from dataclasses import dataclass
from typing import List


@dataclass
class BaseItem:
    name: str
    price: str
    sizes: List[str]
    url: str
    image_url: str
    article: str

    def __str__(self):
        return f'{self.name}|{self.price}|{self.sizes}|{self.article}|{self.url}|{self.image_url}'
