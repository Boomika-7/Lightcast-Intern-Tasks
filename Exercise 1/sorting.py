def insertionSort(arr, ascending=True):
    try:
        n = len(arr)
        if n <= 1:
            return arr
        for i in range(1, n):
            key = arr[i]
            if not isinstance(key, (int, float, str)):
                raise TypeError()
            j = i - 1
            while j >= 0 and ((key < arr[j]) if ascending else (key > arr[j])):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    except TypeError as e:
        return "Exception: Heterogeneous array"