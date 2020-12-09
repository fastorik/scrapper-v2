from .base import BaseSelector


class SoupSelector(BaseSelector):
    def get_element(self, container, *args, **kwargs):
        return container.find(**kwargs)

    def get_elements(self, container, *args, **kwargs):
        return container.find_all(**kwargs)

    def get_element_source(self, container, *args, **kwargs):
        return str(container)

    def get_element_text(self, container, *args, **kwargs):
        return container.get_text()
