def positive_sum(arr):
    result = 0
    for number in arr:
        if number > 0:
            result += number
    return result
