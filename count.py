def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    

assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("AA") == 2, "Two upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("aBcDeFgHiJkL") == 6, "Multiple upper case"
assert count_upper_case("£$%^&") == 0, "Special characters"
assert count_upper_case("£15$%B^Ca&T") == 3, "Mix of numbers, special characters, lower and upper case"

print("All tests passed")