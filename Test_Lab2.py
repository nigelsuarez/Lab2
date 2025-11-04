import Lab2

print("Test_Lab2")

def test_find_min_max():

    result = []
    test_input = [1,2,3,4,5]
    
    result = Lab2.find_min_max(test_input)

    assert result == [1,5]
    

def test_calc_average():

    result = []
    test_input = [1,2,3,4,5]

    result = Lab2.calc_average_temperature(test_input)

    assert result == 3

def test_calc_median_temperature():

    result = []
    test_input = [1,2,3,4,5]

    result = Lab2.calc_median_temperature(test_input)

    assert result == 3
