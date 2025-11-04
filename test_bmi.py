import bmi

print("Test_bmi")

def test_calculate_bmi():
    input_height = 1.70
    input_weight = 75
    test_bmi = 1

    result = bmi.calculate_bmi(input_height, input_weight)

    assert (result == test_bmi)