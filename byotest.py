def number_of_evens(numbers):
    return 0
    
def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
test_are_equal(number_of_evens([1, 2, 3, 4, 5]), 2)