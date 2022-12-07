def remove_every_other(my_list):
    keep=[]
    par = True
    for num in my_list:
        if par == True:
            keep.append(num)
            par = False
        else:
            par =True
    return keep
