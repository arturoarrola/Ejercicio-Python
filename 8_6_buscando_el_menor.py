def find_smallest_int(arr):
    small = 100000000000000000000000
    for number in arr:
        if number < small:
            small = number
    return small
    
