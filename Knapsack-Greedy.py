from myItem import *



def greedy(items, maxWeight, keyFunction):
    sortedItems = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue = 0.0
    totalWeight = 0.0
    for i in range(len(sortedItems)):
        if (totalWeight + sortedItems[i].getWeight()) <= maxWeight:
            result.append(sortedItems[i])
            totalWeight += sortedItems[i].getWeight()
            totalValue += sortedItems[i].getValue()
    return (result, totalValue)



res, val = greedy(OurItems(), 15, density)
print('Value Sum Is: ', val)
for item in res:
     print( item)
