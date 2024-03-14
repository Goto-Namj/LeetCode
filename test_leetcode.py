def test(func, params):
    for i, param in enumerate(params):
        result = func(*param[:-1])
        assert result == param[-1], f"Test case {i} failed: expected {param[-1]}, got {result}"
    print("All test cases passed")