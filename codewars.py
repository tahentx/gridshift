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
import random
player = input("Rock,paper or scissors: ")
def rock_paper(player, options = ['Rock','Paper','Scissors']):
    assert player in options
    comp = random.choice(options)
    tally = {}
    if player == 'Rock' and comp == 'Scissors':
        print("You win!")
        tally['Player'] = 1
    elif player == 'Rock' and comp == 'Rock':
        print("Draw!")
    elif player == 'Rock' and comp == 'Paper':
        print("Awww, computer wins!")
        tally['Computer'] = 1
    print(tally)
rock_paper("Rock")