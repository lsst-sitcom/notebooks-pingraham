def example_method(input_value, multiplier=10):
    """An example method that can be imported and called in a notebook.
    This method will return the input value multiplied by 10."""

    if not isinstance(input_value, float):
        raise IOError("Input value of {input_value} is not a float.")

    return input_value*multiplier

