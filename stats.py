means_of_travel = {
    'Drive alone' : 153,
    'Carpool' : 22,
    'Public transportation' : 10,
    'Walk' : 5,
    'Other means' : 3,
    'Work at home' : 7
}

total = sum(means_of_travel.values())
walk = means_of_travel['Walk']/total
print(walk)