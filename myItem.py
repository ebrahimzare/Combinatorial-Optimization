class Item(object):

    def __init__(self, n, v, w):
        self.name=n
        self.value=float(v)
        self.weight=float(w)

    def genName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        return '<'+self.name+','+str(self.value)+','+str(self.weight)+'>'

def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()


def OurItems():
    names = ['saat', 'radio', 'ketab', 'gol', 'tablofarsh', 'zarf']
    values = [120, 20, 20, 80, 150, 64]
    weights = [6, 1, 5, 10, 15, 8]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items
