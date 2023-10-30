data = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}
def lookup_key(data, value):
    keys = []
    for key, val in data.items():
        if val == value:
            keys.append(key)
    return keys

