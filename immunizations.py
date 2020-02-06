# kata: https://www.codewars.com/kata/577d0a117a3dbd36170001c2/train/python
fiveInOne = ['8 weeks', '12 weeks', '16 weeks']
# //Protects against: diphtheria, tetanus, whooping cough, polio and Hib (Haemophilus influenzae type b)
pneumococcal : ['8 weeks', '16 weeks']
# //Protects against: some types of pneumococcal infection
rotavirus : ['8 weeks', '12 weeks']
# //Protects against: rotavirus infection, a common cause of childhood diarrhoea and sickness
meningitisB : ['8 weeks', '16 weeks', '12 months']
# //Protects against: meningitis caused by meningococcal type B bacteria
hibMenC : ['12 months']
# //Protects against: Haemophilus influenzae type b (Hib), meningitis caused by meningococcal group C bacteria    
measlesMumpsRubella : ['12 months', '40 months']
# //Protects against: measles, mumps and rubella
fluVaccine : ['september','october','november']
# //Given at: annually in Sept/Oct
preSchoolBooster : ['40 months']
# //Protects against: diphtheria, tetanus, whooping cough and polio

def deliver(shot):
    # shots_due = []
    # convert_to_weeks = lambda x: x * 52
    # age = convert_to_weeks(age)
    # if status == 'up-to-date':
    #     pass
    # else:

    # fall = ['september','october','november'] 
    
    # if month in fall:
    #     shots_due.append('offer fluVaccine')
    
    for data in shot:
        parsed = data.split()
        print(parsed)

deliver(fiveInOne)