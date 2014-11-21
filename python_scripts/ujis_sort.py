def bucket_sort(d):
    lowest, highest = None, None
    for key in d:
        if not lowest or d[key] < lowest:
            lowest = d[key]
        if not highest or d[key] > highest:
            highest = d[key]

    num_buckets = highest - lowest

    bucket = [[] for x in range(num_buckets + 1)]
    for key in d:
        bucket[d[key] - lowest].append((key, d[key]))

    result = []
    for b in bucket:
        for pair in b:
            result.append(pair)

    return result


print(bucket_sort({'the': 10, 'and': 11, 'hello': 15, 'goodbye': 11}))
