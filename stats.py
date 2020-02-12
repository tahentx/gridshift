means_of_travel = {
    'Drive alone' : 153,
    'Carpool' : 22,
    'Public transportation' : 10,
    'Walk' : 5,
    'Other means' : 3,
    'Work at home' : 7
}

# khan academy exercise : https://www.khanacademy.org/math/statistics-probability/probability-library/basic-theoretical-probability/v/probability-1-module-examples?modal=1

def prob_multiple(lst):
    denom = len(lst)
    numer = [x for x in lst if x % 5 == 0]
    answer = len(numer)/denom
    print(str(answer))
prob_multiple([32,49,55,30,56,28,50,40,40,45,3,25])