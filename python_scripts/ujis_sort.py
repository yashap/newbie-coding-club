def bucket_sort(d):
    lowest, highest = None, None
    for key in d:
        if not lowest or d[key] < lowest:
            lowest = d[key]
        if not highest or d[key] > highest:
            highest = d[key]
 
    bucket = [[] for _ in range(lowest, highest + 1)]
    for key in d:
        bucket[d[key] - lowest].append(key)
 
    result = []
    for i in range(lowest, highest + 1):
        for x in bucket[i - lowest]:
            result.append((x, i))
    return result
 
print(bucket_sort({'a': 2, 'b': 1, 'c': 3, 'd': 2, 'e': 1}))