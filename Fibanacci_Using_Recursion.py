def fibanacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibanacci(n - 1) + fibanacci (n - 2)
    
print(fibanacci(2))
# number Line =      0 1 2 3 4 5 6 etc., its corresponding fibanacci series is 
# fibanacci series = 0 1 1 2 3 5 8 etc., 