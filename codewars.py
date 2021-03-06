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
stockton = MountingType(44,44,True)
# print(stockton.tracking)

Stats = namedtuple('FinalStats', ['points','rebounds','assists'])
bradley = Stats(12,8,8)
# print(bradley.rebounds)

# kata: https://www.codewars.com/kata/5906a218dfeb0dbb52000005/train/python
def hidden(num: int) -> list:
    assert num in range(100,999999)
    from collections import namedtuple
    Variable = namedtuple('Variable',['char','int'])
    a = Variable('a',6)
    b = Variable('b',1)
    d = Variable('d',7)
    e = Variable('e',4)
    i = Variable('i',3)
    l = Variable('l',2)
    m = Variable('m',9)
    n = Variable('n',8)
    o = Variable('o',0)
    t = Variable('t',5)
    catalog = [a,b,d,e,i,l,m,n,o,t]
    num_list = [int(x) for x in str(num)]
    decoded = []
    for num in num_list:
        for item in catalog:
            if item.int == num:
                decoded.append(item.char)
    answer = "".join(decoded).lower()
    print(answer)
    
# hidden(567095)

def rolldice_sum_prob(sum, dice_amount):
    assert (dice_amount * 6) <= sum
    print("ok")
# rolldice_sum_prob(45,3)

# kata: https://www.codewars.com/kata/5e2596a9ad937f002e510435/train/python
def infected(s):
    lands = s.split('X')
    total = sum(map(len, lands))
    infected = sum(len(x) for x in lands if '1' in x)
    return infected * 100 / (total or 1)


inv = '8965RMA90009002RMA9010'

def shipment_analysis(units):
    goods = units.split('RMA')
    quality = sum(map(len,goods))
    warranty = sum(len(x) for x in goods if int(x) > 5)
    
    print(quality)
    print(warranty)
# shipment_analysis(inv)
# 
# kata: https://www.codewars.com/kata/569d488d61b812a0f7000015/train/python
def data_reverse(data):
    bit = data[::8]
    print(bit)

# data_reverse([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

# kata: https://www.codewars.com/kata/56af1a20509ce5b9b000001e/train/python
def travel(r):
    import re
    single = r.split(',')
    for x in single:
        zip_code = re.compile(r'\d{5}')
        zip_list = zip_code.findall(x)

    
    unique_zip_codes = set(zip_list)
    print(unique_zip_codes)
# travel("123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432")

# kata: https://www.codewars.com/kata/586ee462d0982081bf001f07
def fillable(stock,merch,n):
    for key,value in stock.items():
        if merch == key:
            if (value - n) >= 0: 
                return True
            else:
                return False
        else:
            return False
    
# fillable({'foo' : 5},'foo',8)


def close_compare(a,b,margin):
    if (b - a) >= 0:
        return -1
    elif margin >= abs(b - a):
        return 0
    elif (a - b) >= 0:
        return 1

# close_compare(5,3,1)

def who_is_paying(name):
    hoa = []
    if len(name) > 2:
        hoa.append(name)
        hoa.append(name[:2])
    else:
        hoa.append(name)
    return hoa
who_is_paying("Cholo")

# kata: https://www.codewars.com/kata/5738f5ea9545204cec000155/train/python

def count_letters_and_digits(s):
    s_lst = list(s)
    digs = list(map(lambda x: x.isdigit(),s_lst))
    alpha = list(map(lambda y: y.isalpha(),s_lst))
    combine = digs + alpha
    return sum(bool(x) for x in combine)

# count_letters_and_digits("55bsdf9")

def make_negative(number):
    assert number.isnumeric()
    if number < 0:
        pass
    else:
        return number * -1

def odd_one_out(s):
    s = s.split()
    unpaired = []
    paired = []
    for word in s:
        word = list(word)
        for letter in word:
            if word.count(letter) % 2 == 0:
                paired.append(letter)
                unpaired.append(' ')
            else:
                unpaired.append(letter)
    return unpaired
odd_one_out("Hello World")

# kata: https://www.codewars.com/kata/559ac78160f0be07c200005a/solutions/python
def name_shuffler(str_):
    shuffled = str_.split()
    foo = ' '.join(shuffled[::-1])
    return foo
name_shuffler("Billy Buckets")

# kata: https://www.codewars.com/kata/59c8b38423dacc7d95000008/train/python
def is_valid(formula):
    assert isinstance(formula,list)
    template = [str(i) for i in formula]
    if '1' in template and '2' in template:
        return False
    elif '3' in template and '4' in template:
        return False
    elif '5' in template and '6' not in template:
        return False
    elif '6' in template and '5' not in template:
        return False
    elif '7' not in template and '8' not in template:
        return False
    else:
        return True
    
is_valid([2,3,4])

# kata: https://www.codewars.com/kata/577e694af5db624cf30002d0/train/python
def closest_sum(ints,num):
    assert isinstance(ints,list)
    assert isinstance(num,int)
    while len(ints) > 3:
        ints.remove(max(list(map(lambda x: num - x,ints))))
    print(sum(ints))        

# closest_sum([3,4,5,1],6)

# kata: https://www.codewars.com/kata/5547929140907378f9000039
def shortcut(s):
    s = list(s.lower())
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        if vowel in s:
            s.remove(vowel)
    s = ''.join(s)
    print(s)        
        
# shortcut("hello")

# kata: https://www.codewars.com/kata/59f7a0a77eb74bf96b00006a/train/python
def golf_score_calculator(par_string,score_string):
    assert len(par_string) == len(score_string)
    card = list(zip(par_string,score_string))
    score = [(int(x[1]) - int(x[0])) for x in card]
    return (sum(score))

# golf_score_calculator([5,4,5],[4,4,3])
# kata: https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python
def title_case(title,minor_words):
    assert isinstance(title,str)
    title = title.split()
    minor = minor_words.split()
    proper = []
    for word in title:
        if word in minor and title.index(word) != 0:
            proper.append(word.lower())
        elif word not in minor:
            proper.append(word.title())
        elif word in minor and title.index(word) == 0:
            proper.append(word.title())
    return proper
title_case("This is a test","this a")

def distribute(nodes,workload):
    entire_load = [x for x in range(workload)]
    allocation = entire_load[:nodes]
    foo = [dist for dist in enumerate(entire_load, start=1) if entire_load.index(dist) % len(allocation) == 0]
    print(foo)
    
# distribute(4,16)

# kata: https://www.codewars.com/kata/5715eaedb436cf5606000381
def positive_sum(arr):
    if not arr:
        return 0
    else:
        return sum(list(filter(lambda x: x > 0, arr)))
# positive_sum([1,-4,7,12])

# kata: https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python
def is_valid_walk(walk: list) -> bool:
    dist_to_origin = 0
    steps = []
    for step in walk:
        steps.append(step)

    dist = dist_to_origin - sum(steps)
    print(dist)
    if sum(steps) == 10:
        return True
# kata: https://www.codewars.com/kata/55ecd718f46fba02e5000029/train/python            
def between(a,b):
    return [i for i in range(a,(b+1))]

# kata: https://www.codewars.com/kata/5672682212c8ecf83e000050/train/python
def dbl_linear(n):
    a = 1
    cont = []
    for num in range(n):
        foo = a * num + 1
        cont.append(foo)
        a = a + 1
    print(cont)
    for ind,value in enumerate(cont):
        if n == ind:
            print(value)

# dbl_linear(2)

def combine(a,b):
    c = list(zip(a,b))
    print(type(c))
    print(c)
# combine([1,3,5],['a','b','c'])

# kata: https://www.codewars.com/kata/586f5808aa04285bc800009d
def modes(data):
    set_of_data = set(data)
    if len(set_of_data) == len(data):
        return []
    else:
        return max(data,key=data.count)
# modes('spoon')

def sorter(textbooks):
    return sorted(textbooks,key=str.casefold)

# kata: https://www.codewars.com/kata/5808ff71c7cfa1c6aa00006d
def letter_count(s):
    dict = {}
    for item in s:
        keys = dict.keys()
        if item in keys:
            dict[item] += 1
        else:
            dict[item] = 1
    return dict
letter_count("Walrus")

# kata: https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python
def invert(lst):
    x = list(map(lambda x: x * -1,lst))
    print(x)
# invert([4,5,32])

# kata: https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
def solution(s):
    s = list(s)
    container = []
    for letter in s:
        if letter.isupper():
            container.append(" ")
            container.append(letter)
        else:
            container.append(letter)
    lsd = ''.join([str(elem) for elem in container]) 
    return lsd
solution("blueBridge")

# kata: https://www.codewars.com/kata/55d9f257d60c5fd98d00001b/train/python
def remove_duplicates(head):
    try:
        output = list(set(head))
        output.sort(reverse=True)
        return output
    except:
        return None
# remove_duplicates(['T','i','i','nil','m','e'])

def tax_calculator(amount):
    tax_rate = {
        "AL" : .09,
        "AK" : .045,
        "AZ" : .07
    }
    amount = input("What is the amount?")
    state = input("What is the state?")
    for key,value in tax_rate.items():
        if state == key:
            tax_applied = int(amount * value) + amount
        else:
            "We do not have your state sales tax rate yet. We apologize for the inconvenience."
    print("The total is " + str(amount))
    print("The total with tax applied is " + str(tax_applied))        

# tax_calculator(55)

def exchange_with(a,b):
    zipped = zip(a,b)
    new_a = []
    new_b = []
    for x,y in zipped:
        new_b.append(x)
        new_a.append(y)
    a = new_a
    b = new_b
    return a,b
        

exchange_with(['a','b','c'],['x','y','z'])

def unpack(l):
    import itertools
    flatten = itertools.chain.from_iterable
    return list(flatten(l))
# unpack(["off",["the","chain"]])

# kata: https://www.codewars.com/kata/5601409514fc93442500010b/train/python
def better_than_average(class_points,your_points):
    avg = sum(class_points) / len(class_points)
    if your_points > avg:
        return True 
    else:
        return False
# better_than_average([98,78,80],86)
def no_boring_zeroes(n):
    n_two = list(str(n))
    n_len = len(n_two)-1
    for index,x in enumerate(n_two):
        if index == n_len:
            if x == '0':
                foo = n_two[:int(index)]
                blah = int(''.join(foo))
                return blah
        else:
            pass
# no_boring_zeroes(150430)

# kata: https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
def second_solution(string,ending):
    chunk = -(len(ending))
    x = str(string[chunk:])
    if ending == x:
        print("True")
    else:
        print("False")
# second_solution("testing","bing")

# kata: https://www.codewars.com/kata/5832db03d5bafb7d96000107/train/python
def lottery(s):
    s = list(s)
    z = []
    for char in s:
        if char.isdigit():
            z.append(char)
        else:
            pass
    
    answer = list(set(z))
    if answer == []:
        return "One more run!"
    else:
        boo = ''.join(answer)
        return boo
lottery("blah")


# kata: https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python
def parts_sum(ls):
    assert isinstance(ls,list)
    cont = []
    while len(ls) > 0:
        x = sum(ls)
        cont.append(x)
        del ls[0]
    print(cont)        
# parts_sum([5,6,9,10])

# kata: https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/python
def clean_string(s):
    s = list(s)
    z = s[:]
    pieces = []
    for x,y in enumerate(z):
        if y == '#':
            chunk_one = z[:x]
            chunk_two = z[x:]
            del chunk_one[-1]
            pieces.append(chunk_one)
            pieces.append(chunk_two)
        else:
            pass
    
    print(pieces)
# clean_string("Balu#ga")

# kata: https://www.codewars.com/kata/598ee7b6ec6cb90dd6000061/train/python
def count_repeats(txt):
    from itertools import groupby
    x = list(txt)
    count_dups = [sum(1 for _ in group) for _, group in groupby(x)]
    y = list(filter(lambda x: x > 1, count_dups))
    return len(y)
count_repeats("Balling")

from itertools import tee
# kata: https://www.codewars.com/kata/58afa8185eb02ea2a7000094/train/python
def pairwise(arr,a,b):
    a, b = tee(arr)
    next(b, None)
    x = zip(a, b)
    for i in x:
        print(sum(i))
# pairwise([3,5,23],5,6)

# kata: https://www.codewars.com/kata/59706036f6e5d1e22d000016/train/python
import string
def words_to_marks(s):
    s = list(s)
    x = list(string.ascii_lowercase)
    values = []
    for idx,item in enumerate(x):
        if item in s:
            values.append(idx)
    summed = sum(values)
    return summed    

# words_to_marks("blue")

# kata: https://www.codewars.com/kata/56414fdc6488ee99db00002c/train/python
def absent_vowel(x):
    x = x.upper()
    vowels = ["A","E","I","O","U"]
    answer = [i for i, item in enumerate(vowels) if item not in list(x)]
    return int(answer[0])
    
# absent_vowel("Bb Smith sent us six neatly arranged range bicycles")

# kata: https://www.codewars.com/kata/5b7176768adeae9bc9000056/train/python
def index_equals_value(arr):
    result = [idx if idx else None for idx,val in enumerate(arr) if idx == val]
    return min(result)

# kata: https://www.codewars.com/kata/5ac6932b2f317b96980000ca/train/python
def min_value(digits):
    from itertools import permutations
    one = str(digits)
    two = list(one)
    three = set(two)
    x = permutations(three,len(three))
    clean = []
    for value in x:
        string = ''.join(value)
        num = int(string)
        clean.append(num)
    answer = min(clean)
    return answer
# min_value(5523)

def up_array(arr):
    for char in arr:
        if isinstance(char,int):
            pass
        else: 
            return None
    foo = list(filter(lambda x: 10 > x > 0, arr))
    lst_foo = int(''.join([str(elem) for elem in foo]))
    plus_one = lst_foo + 1
    final = list(str(plus_one))
    vibe = [int(x) for x in final]
    return vibe
          
# up_array([2,35,3,-3])

# kata: https://www.codewars.com/kata/5a4bdd73d8e145f17d000035/train/python
def sort_nested_list(A):
    import itertools
    merged = list(itertools.chain(*A))
    new_list = []
    for pair in merged:
        x = sorted(pair)
        new_list.append(x)
    final_list = []
    final_list.append(new_list)
    return final_list
sort_nested_list([[[2, 1], [4, 3]], [[6, 5], [8, 7]]])

# kata: https://www.codewars.com/kata/5868b2de442e3fb2bb000119/train/python
def closest(strng):
    lst = strng.split()
    for item in lst:
        item = [value for value in set(item)]
        intgr = [int(z) for z in item]
        print(type(intgr))
# closest("444 820 742")

# kata: https://www.codewars.com/kata/55de6173a8fbe814ee000061/train/python
def unused_digits(intake):
    base = [x for x in list(range(0,10))]
    intake = list(set(intake))
    output = [value for value in base if value not in intake]
    return output
unused_digits([5,3,2,9,3])