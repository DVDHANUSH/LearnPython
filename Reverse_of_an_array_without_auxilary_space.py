def reverse_an_array(arr, start, end):
    if start > end:
        return arr
    else : 
        arr[start], arr[end] = arr[end], arr[start]
        return reverse_an_array(arr, start + 1, end - 1)
arr = [1, 2, 3, 4, 5]
print(reverse_an_array(arr, 0, len(arr) - 1))