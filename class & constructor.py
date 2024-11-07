class flower:
    def __init__(self,name,petals,price):
        self._name=name
        self._petals=petals
        self._price=price
    def set_name(self,name):
        self._name=name
    def set_petals(self,petals):
        self._petals=petals
    def set_price(self,price):
        self._price=price
    def get_name(self):
        return self._name
    def get_petals(self):
        return self._petals
    def get_price(self):
        return self._price

flower=flower("g       ",3,5.4)
    
print("name",flower.get_name())
print("petals:",flower.get_petals())
print("price:",flower.get_price())
    
flower.set_name('sun flower')
flower.set_petals(15)
flower.set_price(7.8)
    
    
print("updated name",flower.get_name())
print('updated petals',flower.get_petals())
print('updated price',flower.get_price())
    
    
        