# # kata: https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
# def increment_string(string: str) -> str:
#     string_list = list(string)
#     if string_list[-1].isnumeric:
#         integers = list(filter(lambda s: s.isnumeric(),string_list))
#         list_to_int = ''.join([str(elem) for elem in integers])
#         plus_one = int(list_to_int) + 1
#         string_list.append(str(plus_one))
#         print(string_list) 
#     else:
#         string_list[-1] = 1
#         print(str(string_list))
# increment_string("Juice55")

# kata: https://www.codewars.com/kata/56170e844da7c6f647000063/train/python
def people_with_age_drink(age):
    assert isinstance(age, (int, float)) and not isinstance(age, bool)
    if age < 14:
        return "drink toddy"
    elif age >= 14 and age < 18:
        return "drink coke"
    elif age >= 18 and age < 21:
        return "drink beer"
    elif age >= 21:
        return "drink whisky"
# people_with_age_drink(5)

# kata: https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python
def sum_mix(arr: list) -> int:
    integers = list(filter(lambda x: isinstance(x,int), arr))
    strs = [int(x) for x in arr if isinstance(x,str)]
    answer = integers + strs
    return sum(answer)

def odd_or_even(arr):
    assert isinstance(arr, list)
    if sum(arr) % 2 == 0:
       return "even" 
    else: 
        return "odd"
# odd_or_even([4,6,2,3])

# kata: https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
def square_sum(numbers):
    assert isinstance(numbers, list)
    return sum(list(map(lambda x: x**2, numbers)))

# kata: https://www.codewars.com/kata/5e0baea9d772160032022e8c/train/python

def compute_ranks(number, games):
    # create team list
    num_teams = range(number)
    teams = list(map(lambda x: "Team" + str(x + 1), list(num_teams)))
    points = {}

    # calculate goals scored 'for'
    for team in teams:
        if team == games[0]:
            points.update({team + " - for": games[2]})
            points.update({team + " - against": games[3]})
        elif team == games[1]:
            points.update({team + " - for": games[3]})
            points.update({team + " - against": games[2]})
    print(points)
        
# compute_ranks(5,['Team1','Team2',2,5])

# kata: https://www.codewars.com/kata/5583090cbe83f4fd8c000051/solutions/python
def digitize(n):
    x = list(str(n))
    y = [int(i) for i in x]
    y.reverse()
    return y

# kata: https://www.codewars.com/kata/537529f42993de0e0b00181f/train/python
def count_inversions(array):
    proper = [x for x in array if array[x + 1] - array[x] == 1]
    print(proper)
# count_inversions([4,5,9,10,3])

def min_taxis(requests):
    requests.sort(key=lambda tup: tup[0])
    for index, item in enumerate(requests):
        next_ride = index + 1
        print(item, item[next_ride])
   

# min_taxis([(9,11),(12,3),[10,11]])

def alternate_sort(l):
    absolute = sorted(l,key=abs)
    negs = list(filter(lambda x: x < 0, absolute))
    pos = list(filter(lambda x: x > 0, absolute))
    merged = list(zip(negs,pos))
    final = [y for x in merged for y in x]
    return final

# alternate_sort([-5,3,6,-13,-2,4])

# kata: https://www.codewars.com/kata/5da558c930187300114d874e/train/python
from collections import namedtuple

MountingType = namedtuple('MountingType', ['tilt','azimuth','tracking'])
aberdeen = MountingType(145,150,False)
print(aberdeen.azimuth)
print(aberdeen[1])