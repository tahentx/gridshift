# kata: https://www.codewars.com/kata/544bdc2ec29fb3456e00064a/train/python
def service(score):
    score = list(score)
    first,second = int(score[0]),int(score[2])
    
    while True:
        counter = 0
        first = True
        if (score[0] + score[2]) % 5 == 0:
            if first = True:
                first = False
            elif first = False:
                first = True
        if score[0] >= 21:
            break
        elif score[2] >=21:
            break
        counter += 1

service("3:4")
    