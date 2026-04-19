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


# ========================================
#    ZIG-ZAG ROUTE TRANSPOSITION CIPHER
# ========================================

def encrypt_zigzag_route(text, cols):
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
    for i in range(rows):
        if i % 2 == 0:
            for j in range(cols):
                result += grid[i][j]
        else:
            for j in reversed(range(cols)):
                result += grid[i][j]

    return result


def decrypt_zigzag_route(cipher, cols):
    rows = math.ceil(len(cipher) / cols)
    grid = [['' for _ in range(cols)] for _ in range(rows)]

    k = 0
    for i in range(rows):
        if i % 2 == 0:
            for j in range(cols):
                grid[i][j] = cipher[k]
                k += 1
        else:
            for j in reversed(range(cols)):
                grid[i][j] = cipher[k]
                k += 1

    result = ""
    for i in range(rows):
        for j in range(cols):
            result += grid[i][j]

    return result.strip('X')