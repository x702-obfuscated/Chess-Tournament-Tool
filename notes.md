

Notes for chess pairing program

Players 
Stores all players in the tournament

Student object, with:
    Name
    school
    grade
    score
    previous_opponents
    previous_color
    had_bye  


pair()
'''Pairs players based on score, school, previous opponents, and previous color'''
first check score
then school

if len of unpaired list is odd:
    assign_bye


Start with top player check for the next top from a different school who is not a previous opponenent, add the pair as a tuple to the pairings list remove from the unpaired list. 
continue with next top player in the unpaired list

return a list of pairings.








assign_bye(list):
    '''pop and return student with bye'''


    for student in reversed(list):
        if student.had_bye == False:
            return student, "BYE"

        Check last player in list, if they have not recieved a bye
            set had_bye to True
            return student, bye

        if had_bye:
            check next player up in the list (-1, -2, -3)
    




assign_color(student1, student2):
    '''If both students played the same color in the last round randomize, else flip colors"

    return tuple(color of s1, color of s2)



pair students from non identical school based on top scores, and previous opponent to a board 
don't pair students from identical school

pairings based on score and school. 

determine byes based on low score, and odd nums of students. Byes can only be given to a student once. 


sep board nums based on grade
board nums for Sr. High
board nums for Jr. High



3/4 5/6 7/8/9 -Jr.High 10/11/12 Sr. High

when executed it returns pairings, who plays black, who plays white, and board number in an ordered list. 


handle duplicate student names



buying trophies(First, Second, Third), medles(gold, silver, bronze) 

