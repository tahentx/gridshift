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
odd_or_even([4,6,2,3])