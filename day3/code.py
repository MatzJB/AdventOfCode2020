
def get_number_of_trees(input_file, slope):
    ''' returns the number of trees using the slope tuple describing the movement over the inpu_file '''
    with open(input_file) as f:
        rows = f.readlines()

    number_of_trees = 0
    rows = [row.strip() for row in rows]
    row = 0
    col = 0

    while row < len(rows)-1:
        col = (col + slope[0]) % len(rows[0])
        row = row + slope[1]
        char = rows[row][col]

        if char == '#':
            number_of_trees = number_of_trees + 1

    return number_of_trees


# slopes describes the rate of movement (colums,rows)
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
mult = 1
for slope in slopes:
    number_of_trees = get_number_of_trees('input.txt', slope)
    print(f'slope {slope}, number of trees: {number_of_trees}')
    mult = mult * number_of_trees

print(mult)
