from etl_functions import double_values

def test_double():
    assert double_values([1, 2, 3]) == [2, 4, 6]
