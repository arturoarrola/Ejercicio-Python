def count_positives_sum_negatives(arr):
    positivos = 0
    negativos = 0
    if arr ==[]: 
        return []
    for number in arr:
        if number < 0:
            negativos += number
        if number > 0:
            positivos += 1
    return [positivos,negativos]
  correcto
            
