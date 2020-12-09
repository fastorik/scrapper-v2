class BaseSelector:
    def __init__(self, api):
        self.api = api

    def get_element(self, container, *args, **kwargs):
        pass

    def get_elements(self, container, *args, **kwargs):
        pass

    def get_element_source(self, container, *args, **kwargs):
        pass

    def get_element_text(self, container, *args, **kwargs):
        pass
