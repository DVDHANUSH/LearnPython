arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
i = 0
sorted_flag = True
while i < len(arr) - 1:
    if arr[i] > arr[i + 1]:
        sorted_flag = False
        break

    i += 1
if sorted_flag:

    print("sorted")
else:
    print("not sorted")