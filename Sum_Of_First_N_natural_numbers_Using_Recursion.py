def Sum_Of_First_N_natural_numbers_Using_Recursion(sum ,n):
    if n == 0:
        return sum
    else: 
        sum = sum + n
        return  Sum_Of_First_N_natural_numbers_Using_Recursion(sum, n - 1)
print(Sum_Of_First_N_natural_numbers_Using_Recursion(0, 5))

# with new array 