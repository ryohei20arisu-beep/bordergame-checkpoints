#part1
def generate_matrix():
    a11 = 1 + 2      
    a12 = 6 - 3     
    a21 = 2 * 1     
    a22 = 10 - 5    

    return [[a11, a12],
            [a21, a22]] 

matrix = generate_matrix()
for row in matrix:
    print(row)
