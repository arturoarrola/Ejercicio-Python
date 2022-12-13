def warn_the_sheep(queue):
    encontrado = False
    i = len(queue) - 1 
    while encontrado == False:
        if queue[i] == "wolf":
            encontrado = True
        else:
            i -= 1
    return "Oi! Sheep number " , (i+1) ,"! You are about to be eaten by a wolf!" 
