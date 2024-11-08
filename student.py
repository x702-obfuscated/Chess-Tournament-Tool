

class Student():
    '''Defines a student playing in a simple chess tournament'''

    all: dict[str:object] = {}

    @classmethod
    def get_student(cls,name):
        name = name.upper()
        try:
            return Student.all[name]
        except KeyError as e:

            return f"STUDENT '{name}' NOT FOUND." 

    def __init__(
        self,
        name: str = None, 
        school: str = None,
        grade: int = None,
        score: float = 0.0,
        opponents: dict[str:object] = [],
        prev_colors: list[str] = [], 
        had_bye:bool = False
    ):
        self.name = name.upper()
        self.school = school.upper()
        self.grade = grade
        self.score = score
        self.opponents = opponents
        self.prev_colors = prev_colors
        self.had_bye = had_bye

        self.check_duplicates()
        Student.all[self.name] = self


    def __str__(self):
        return self.name
    
    def check_duplicates(self):
        i = 0
        while self.name in Student.all:
            i += 1
            if i > 1 :
                self.name = self.name[0:-1] + str(i)
            else:
                self.name += " " + str(i)
                

if __name__ == "__main__":
    #testing

    Student("John Smith", "This HS", 10)
    Student("John Smith", "That HS", 11)
    Student("John Smith", "Another HS", 12)

    for key, value in Student.all.items():
        print(key, vars(value))
    
    print(Student.get_student("john smith"))
    print(Student.get_student("jill smith"))

    


    

    
