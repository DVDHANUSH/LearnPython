arr = [199, 2, 3, 4, 5, 6, 7, 8, 9, 99]
largest = arr[0]
slargest = float('-inf')
for i in range(len(arr)):
    if arr[i] > largest:
        slargest = largest
        largest = arr[i]
    if slargest < arr[i] and arr[i] != largest:
        slargest = arr[i]
print("the", (slargest))