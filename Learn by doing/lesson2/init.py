from random import randrange, choice

field = [[0 for i in range(4)] for j in range(4)]
print('field = ', field)

new_element = 4 if randrange(100) > 89 else 2
(i, j) = choice([(i, j) for i in range(4) for j in range(4) if field[i][j] == 0])
print(i, j)
field[i][j] = new_element

print([list(row) for row in zip(*field)])
