# Project 1
# Developer: Moiseenko Victoria
# The aim: to create the online store shopping cart
import help as h

class Product:

    """Product class"""

    def __init__(self, ean):
        if len(ean) < 13 or len(ean) >13:
            print('Неправильный формат ввода')
            self.ean = None
        else:
            self.ean = str(ean)
            self.country = h.countries_codes[self.ean[:3]]
            self._producer = self.ean[3:7]
            self.name = h.names[self.ean[7]]
            self.pages = h.pages[self.ean[8]]
            self.price = h.prices[self.ean[9]]
            self.article = h.articles[self.ean[10]]
            self.weight = h.weight[self.ean[11]]
            self._scan = self.ean[12]

    def product_characteristics(self):
        self.characteristicss = []
        self.characteristicss.append(self.name)
        self.characteristicss.append(self.pages)
        self.characteristicss.append(self.price)
        self.characteristicss.append(self.article)
        self.characteristicss.append(self.weight)
        return self.characteristicss

    def __str__(self):
        return str(self.ean)


#class Shop(Product):

   # """Online store shopping cart class"""

    #total_summ = 0

    #def







