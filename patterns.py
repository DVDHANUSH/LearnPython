# print this pattern
n = 5
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# for i in range(1, n + 1):
#     for j in range(1, n +1):
#         print("*", end=" ")
#     print()


# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("*", end = " ")
#     print()

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# for i in range(n):
#     for j in range(n - i):
#         print("*", end=" ")
#     print()


#the same pattern can be printed with the following code 
# for i in range(n, 0, -1):     # since range can take step index, reverse order is possible. Since the start point is "n" 
#     for j in range(i):
#         print("*" , end= " ")
#     print()
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

# for i in range(1, n + 1):  # Outer loop for n
#     for j in range(n  - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  # Inner loop for stars
#         print("*", end=" ")
#     print()

# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 

# for i in range(n , 0, -1):  # Outer loop for n in reverse
#     for j in range(n  - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  # Inner loop for stars
#         print("*", end=" ")
#     print()  # Move to the next line


#       * 
#     * * * 
#   * * * * * 
# * * * * * * * 
#   * * * * * 
#     * * * 
#       * 

for i in range(1, n + 1):
    for  j in range(n - i):
        print(" ", end=" ")
    for k in range(1, 2*i):
        print("*", end=" ")
    print()
for i in range(n - 1, 0, -1):
    for  j in range(n - i):
        print(" ", end=" ")
    for k in range(1, 2*i):
        print("*", end=" ")
    print()