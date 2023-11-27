# Problem #1
# Print the following pattern
# 1
# 212
# 32123
# 4321234
# 543212345
# Get user input for how far to go (up to 0)


def print_pattern(n):
    for i in range(1, n + 1):
        print(''.join(map(str, range(i, 0, -1))) + ''.join(map(str, range(2, i + 1))))

limit = int(input("Enter how far to go (up to 0): "))
print_pattern(limit)
