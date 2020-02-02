# kata: https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
def increment_string(string: str) -> str:
    string_list = list(string)
    if string_list[-1].isnumeric:
        integers = list(filter(lambda s: s.isnumeric(),string_list))
        list_to_int = ''.join([str(elem) for elem in integers])
        plus_one = int(list_to_int) + 1
        print(plus_one) 
    else:
        string_list[-1] = 1
        print(str(string_list))
increment_string("Juice55")