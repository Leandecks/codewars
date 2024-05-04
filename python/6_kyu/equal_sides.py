def find_even_index(arr):
    result = -1
    for k in range(len(arr)):
        if sum(arr[:k]) == sum(arr[k + 1:]):
            result = k
            break
    return result

print(find_even_index([0,0,0,0,0]))