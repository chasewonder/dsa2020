def main():
    r, c, message = input().split(maxsplit = 2)
    r = int(r)
    c = int(c)
    s = []
    for char in message:
        if char == ' ':
            s.append(f"{0:05b}")
        else:
            s.append(f"{ord(char) - ord('A') + 1:05b}")
    secret = "".join(s)
    if len(secret) < r * c:
        secret += '0' * (r * c - len(secret))
    matrix = spiral_fill_matrix(r, c, secret)
    output = ''.join(str(matrix[i][j]) for i in range(r) for j in range (c))
    print(output)

def spiral_fill_matrix(r, c, binary_str):
    matrix = [[0 for _ in range(c)] for _ in range (r)]
    row = 0
    col = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0
    upbd = 0
    bobd = r - 1
    lbd = 0
    rbd = c - 1
    for bit in binary_str:
        matrix[row][col] = int(bit)
        new_row = row + directions[dir_idx][0]
        new_col = col + directions[dir_idx][1]
        if upbd + (dir_idx + 1) // 4 <= new_row <= bobd and lbd <= new_col <= rbd :
            row = new_row
            col = new_col
        else:
            if (dir_idx == 3):
                lbd += 1
                upbd += 1
                bobd -= 1
                rbd -= 1
            dir_idx = (dir_idx + 1) % 4
            row += directions[dir_idx][0]
            col += directions[dir_idx][1]
    return matrix

if __name__ == "__main__":
    main()