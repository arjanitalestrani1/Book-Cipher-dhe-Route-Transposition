import math

# =======================================
#   COLUMN ROUTE TRANSPOSITION CIPHER
# =======================================

def encrypt_column_route(text, cols):
    text = text.replace(" ", "").upper()
    rows = math.ceil(len(text) / cols)

    grid = [['' for _ in range(cols)] for _ in range(rows)]

    k = 0
    for i in range(rows):
        for j in range(cols):
            if k < len(text):
                grid[i][j] = text[k]
                k += 1
            else:
                grid[i][j] = 'X'

    result = ""
    for j in range(cols):
        for i in range(rows):
            result += grid[i][j]

    return result


