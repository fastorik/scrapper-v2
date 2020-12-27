from dataclasses import dataclass
from typing import List


@dataclass
class BaseItem:
    name: str
    price: str
    sizes: List[str]
    url: str

    def __str__(self):
        return f'{self.name}|{self.price}|{self.sizes}|{self.url}'
