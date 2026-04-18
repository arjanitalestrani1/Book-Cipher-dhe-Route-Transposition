import math;
def decrypt_column_route(cipher, cols):
    rows = math.ceil(len(cipher) / cols)
    grid = [['' for _ in range(cols)] for _ in range(rows)]

    k = 0
    for j in range(cols):
        for i in range(rows):
            grid[i][j] = cipher[k]
            k += 1

    result = ""
    for i in range(rows):
        for j in range(cols):
            result += grid[i][j]

    return result.strip('X')
