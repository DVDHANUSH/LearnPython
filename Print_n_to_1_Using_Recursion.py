def printing(n):
    if n == 0:
        return
    else:
        print(n)
        printing(n-1)
printing(5)