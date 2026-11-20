import labsample1


def test_get_longest_workout():
    workouts = labsample1.load_csv()

    longest = labsample1.get_longest_workout(workouts)

    assert longest["duration"] == 75.0
    

def test_calc_total_duration():
    workouts = labsample1.load_csv()


def test_calc_average_duration():
    workouts = labsample1.load_csv()
