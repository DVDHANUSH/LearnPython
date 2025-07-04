def printing(i, n):
    if n == 0:
        return 
    else:
        print(i)
        printing(i+1, n - 1)

printing(1, 5)
# since we don't have a global variable, we are passing another variable to the function itself 