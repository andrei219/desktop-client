

class Partner:

    def __init__(self):
        self._fiscal_name = None

    @property
    def fiscal_name(self):
        return self._fiscal_name
    
    @fiscal_name.setter
    def fiscal_name(self, value):
        self._fiscal_name = value

        