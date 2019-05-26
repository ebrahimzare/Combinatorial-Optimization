from myItem import * 

def BinaryRep(n, nDigit):
    result=''
    while n>0:
        result+=str(n%2)
        n=n//2
    if len(result)> nDigit:
        raise ValueError('Error')
    for i in range(nDigit-len(result)):
        result='0'+result

    return result

def Powerset(L):
    powerset = []
    for i in range(0, 2**len(L)):
        binStr = BinaryRep(i, len(L))
        subset = []
        for j in range(len(L)):
            if binStr[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset

def chooseOpt(pset, maxWeight, getVal, getWeight):
    optVal = 0.0
    optSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight <= maxWeight and itemsVal > optVal:
            optVal = itemsVal
            optSet = items
    return (optVal, optSet)

def testOpt(maxWeight = 15):
    items = OurItems()
    pset = Powerset(items)
    oV, oS = chooseOpt(pset, maxWeight, Item.getValue, Item.getWeight)
    print('kole value item ha ', oV)
    for item in oS:
        print(item)


