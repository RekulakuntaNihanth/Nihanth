def print_num(n):
    if n > 0:
        print_num(n - 1)  # Recursive call with n-1
        print(n)

print_num(100)
