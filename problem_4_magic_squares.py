from testhelper import test

def is_square_magic(square):
    pass






### TESTS - Run the code that calls the function to check it works.
valid_square = [[4, 9, 2], 
                [3, 5, 7], 
                [8, 1, 6]]

invalid_square = [[4, 9, 2], 
                [8, 1, 6],
                [3, 5, 7]]

test("Magic Square 1", True, is_square_magic(valid_square))
test("Magic Square 2", False, is_square_magic(invalid_square))