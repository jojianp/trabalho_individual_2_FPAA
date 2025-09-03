def max_min_select(arr):
    n = len(arr)

    if n == 1:
        return arr[0], arr[0]

    if n == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]

    mid = n // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    min_left, max_left = max_min_select(left_half)
    min_right, max_right = max_min_select(right_half)

    final_min = min(min_left, min_right)
    final_max = max(max_left, max_right)

    return final_min, final_max