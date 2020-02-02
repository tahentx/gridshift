# kata: https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
def increment_string(string: str) -> str:
    string_list = list(string)
    integers = list(filter(lambda s: s.isnumeric(),string_list))
    single_int = int("".join(map(str, integers)))
    print(single_int)
increment_string("Ju23456ice")