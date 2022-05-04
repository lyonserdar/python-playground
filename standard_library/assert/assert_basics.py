"""
assert_basics.py
"""
# Basic assert usage
countries = ["POL", "ENG", "GER", "USA", "ITA"]
is_italy_in_countries = "ITA" in countries
assert is_italy_in_countries

is_canada_in_countries = "CAN" in countries
assert is_canada_in_countries

# Check if the length of the function argument is not zero
def max_min_difference(numbers):
    assert len(numbers) != 0
    return max(numbers) - min(numbers)


max_min_difference([])

# Check if function output is correct
def area(width, height):
    return width * height


assert area(4, 10) == 40
assert area(5, 6) == 30
