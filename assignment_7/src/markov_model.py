states = ('Fair', 'Loaded')

observations = ('1', '2', '3', '4', '5', '6')

start_probability = {'Fair': 1.0, 'Loaded': 1.0} # Could be 0.5 each, but my professor said this will be negligible...

transition_probability = {
    'Fair': {'Fair': .95, 'Loaded': .05},
    'Loaded': {'Fair': .1, 'Loaded': .9}
}

emission_probability = {
    'Fair': {'1': 1.0/6.0, '2': 1.0/6.0, '3': 1.0/6.0, '4': 1.0/6.0, '5': 1.0/6.0, '6': 1.0/6.0},
    'Loaded': {'1': .1, '2': .1, '3': .1, '4': .1, '5': .1, '6': .5}
}
