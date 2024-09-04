from test_api.checks import run_test, skip_test, format_err_msg

# This function that takes a list of triangles.
# Each triangle is represented as a list e.g. [10, 12, 22] where the three
#  numbers are the sides of the triangle.
# The function should return the count of triangles that are valid.
# To be a valid triangle, the sum of any two sides must be larger than the
#  remaining side

# permutations:
# side1 + side2 must be > side3
# side1 + side3 must be > side 2
# side2 + side3 must be > side 1

def valid_triangles(triangles):
    count = 0

    for triangle in triangles:
        side1, side2, side3 = triangle[0], triangle[1], triangle[2]
        if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
            count += 1

    return count
    

@run_test
def test_valid_triangles_returns_0_when_passed_no_triangles():
    assert valid_triangles([]) == 0, \
        format_err_msg(0, valid_triangles([]))


@run_test
def test_valid_triangles_returns_0_when_passed_a_list_with_no_valid_triangles():
    assert valid_triangles([[5, 10, 25]]) == 0, \
        format_err_msg(0, valid_triangles([[5, 10, 25]]))


@run_test
def test_valid_triangles_returns_1_when_passed_a_list_with_a_single_valid_triangle():
    assert valid_triangles([[5, 4, 5]]) == 1, \
        format_err_msg(1, valid_triangles([[5, 4, 5]]))


@run_test
def test_valid_triangles_returns_2_when_passed_a_list_with_2_valid_and_1_invalid_triangle():
    assert valid_triangles([[5, 10, 25], [5, 4, 5], [542, 586, 419]]) == 2, \
        format_err_msg(2, valid_triangles(
            [[5, 10, 25], [5, 4, 5], [542, 586, 419]]))


if __name__ == "__main__":
    test_valid_triangles_returns_0_when_passed_no_triangles()
    test_valid_triangles_returns_0_when_passed_a_list_with_no_valid_triangles()
    test_valid_triangles_returns_1_when_passed_a_list_with_a_single_valid_triangle()
    test_valid_triangles_returns_2_when_passed_a_list_with_2_valid_and_1_invalid_triangle()
