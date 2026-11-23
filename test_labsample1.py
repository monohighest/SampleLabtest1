import labsample1


def test_get_longest_workout():
    workouts = labsample1.load_csv()

    longest = labsample1.get_longest_workout(workouts)

    assert longest["duration"] == 75.0
    

def test_calc_total_duration():
    workouts = labsample1.load_csv()

    total = labsample1.calc_total_duration(workouts)
    
    assert total == 853.0

def test_calc_average_duration():
    workouts = labsample1.load_csv()

    average = labsample1.calc_average_duration(workouts)

    assert average == 42.6
