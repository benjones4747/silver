import math
import lib.scraper

class Variable():
    # defines variables in econometric models
    def __init__(self, arg):
        super(Variable, self).__init__()
        self.arg = arg

class Popularity(Variable):
    # defines variables relating to Popularity (approval)
    def __init__(self, arg):
        super(Popularity, self).__init__()
        self.arg = arg

class Economy(object):
    # defines variables relating to Economy (GDP growth)
    def __init__(self, arg):
        super(Economy, self).__init__()
        self.arg = arg
