def add_numbers(a=5, b=10):
    """
    Adds two numbers with default values of 5 and 10.

    Parameters:
        a (int or float): The first number. Default is 5.
        b (int or float): The second number. Default is 10.

    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b

# Using default values
result_default = add_numbers()
print(f"Sum with default inputs: {result_default}")

# Providing custom values
result_custom = add_numbers(15, 20)
print(f"Sum with custom inputs: {result_custom}")
