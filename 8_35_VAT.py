def excluding_vat_price(price):
    if price == None:
        return -1
    else:
        total = (price/1.15)
        total = round(total,2)
        return total
     
