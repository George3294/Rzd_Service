def build_hash_table(keys):
    hash_table = [[] for _ in range(10)]

    for key in keys:
        hash_key = key % 10
        hash_table[hash_key].append(key)
    return hash_table
keys = [10, 22, 31, 4, 15, 28, 17, 88, 59]
print(build_hash_table(keys))