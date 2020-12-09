from dataclasses import dataclass
from typing import List


@dataclass
class BaseItem:
    name: str
    price: float
    sizes: List[str]
    url: str
