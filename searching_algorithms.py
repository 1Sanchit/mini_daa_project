def binary_search(data, target, key):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid][key].lower() == target.lower():
            return data[mid]
        elif data[mid][key].lower() < target.lower():
            low = mid + 1
        else:
            high = mid - 1
    return None
