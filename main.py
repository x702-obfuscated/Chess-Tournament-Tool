

WHITE = "White"
BLACK = "Black"

WIN = 1
LOSE = 0
DRAW = 0.5





def assign_bye(list1d: Student):
    '''
    Pop and Return Student, "BYE" form list1d.

    Determines the bye student:
        Starting from the end of the list check if each student had a bye.
        If they did move to the next student. 
        If they did not set student.had_bye to True, return Student, "BYE"
    
    '''

    for student in reversed(list1d):
        if not student.had_bye:
            student.had_bye = True
            student.previous_opponents.append("BYE")

            return student, "BYE"
        


        


        