def test(name, expected, actual):
    passed = True
    if isinstance(expected, list) and isinstance(actual, list):
        if sorted(expected) != sorted(actual): passed = False
    else:
        if expected != actual: passed = False

    
    if passed:
        print("Test '" + name + "' passed.")
    else:
        print("Test '" + name + "' FAILED.")