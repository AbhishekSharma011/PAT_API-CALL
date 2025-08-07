import pytest

# Unit Test - simple addition
def test_addition():
    result = 1 + 2
    assert result == 3, f"Expected 3, but got {result}"

# Unit Test - simple subtraction
def test_subtraction():
    result = 5 - 3
    assert result == 2, f"Expected 2, but got {result}"

# Unit Test - multiplication
def test_multiplication():
    result = 4 * 3
    assert result == 12, f"Expected 12, but got {result}"

# Unit Test - division
def test_division():
    result = 10 / 2
    assert result == 5.0, f"Expected 5.0, but got {result}"

# Edge Case - dividing by zero (should raise an exception)
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0

# Test a string method
def test_string_methods():
    sample_string = "Hello, World!"
    assert sample_string.lower() == "hello, world!", "String lower method failed"
    assert sample_string.upper() == "HELLO, WORLD!", "String upper method failed"
    assert sample_string.strip() == "Hello, World!", "String strip method failed"

# Integration Test - testing list sorting
def test_sorting():
    unsorted_list = [5, 3, 8, 1, 2]
    sorted_list = sorted(unsorted_list)
    assert sorted_list == [1, 2, 3, 5, 8], f"Expected [1, 2, 3, 5, 8], but got {sorted_list}"

# Test for a custom function
def add_numbers(a, b):
    return a + b

def test_add_numbers():
    result = add_numbers(3, 4)
    assert result == 7, f"Expected 7, but got {result}"

# Performance test example (not to be used in every test case)
def test_large_sum():
    large_list = [i for i in range(1000000)]
    result = sum(large_list)
    assert result == 499999500000, f"Expected 499999500000, but got {result}"

# Test for an invalid input to a function
def test_invalid_input():
    with pytest.raises(TypeError):
        result = add_numbers("3", 4)

