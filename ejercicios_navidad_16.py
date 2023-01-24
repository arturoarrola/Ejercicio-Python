def invert(lst):
    totales=[]
    number = 0
    total = len(lst)
    while number < total:
        totales.append(lst[number] * -1)
        number += 1
    return totales
