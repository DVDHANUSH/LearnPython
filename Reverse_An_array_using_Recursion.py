def Reverse_An_array_using_Recursion(ans, n, arr):
    if n == 0:
        return ans 
    else: 
        ans.append(arr[n - 1])
        return Reverse_An_array_using_Recursion(ans, n - 1, arr)
    
print(Reverse_An_array_using_Recursion([], 5, [1,2,3,4,5]))
