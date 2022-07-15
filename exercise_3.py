def detonating(r, c, grid):
    detonated_grid = [['O'] * c for i in range(r)]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':
                detonated_grid[i][j] = '.'
                if i + 1 <= r - 1:
                    detonated_grid[i + 1][j] = '.'
                if i - 1 >= 0:
                    detonated_grid[i - 1][j] = '.'
                if j + 1 <= c - 1:
                    detonated_grid[i][j + 1] = '.'
                if j - 1 >= 0:
                    detonated_grid[i][j - 1] = '.'
    return detonated_grid

def bomber_man(r, c, n, grid):
    if n % 2 == 0:
        return [['O'] * c for i in range(r)]
    elif n < 4:
        return grid if n == 1 else detonating(r, c, grid)
    else:
        return detonating(r, c, grid)

    
output = bomber_man(r, c, n, grid)
print([''.join(row) for row in output])


