class Person:
    """
    Class: base
    constructors: __init__()
    fields: name, surname, age, gender
    dunder methods: __repr__() - returns information about fields
    """

    def __init__(self, name, surname, age, gender):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__gender = gender

    def __repr__(self):
        return f"{self.__name} {self.__surname}: {self.__gender}, {self.__age} years old."


class Student(Person):
    """
    Class: derived from Person()
    constructors: __init__(overridden from Person class)
    fields: additional fields except overridden fields- university, faculty, course, middle_score
    dunder methods: __repr__(overridden from Person class)- returns information about it's and base class' fields
    regular methods: getters with name of each field
    """

    def __init__(self, name, surname, age, gender, university, faculty, course, middle_score):
        super().__init__(name, surname, age, gender)
        self.__university = university
        self.__faculty = faculty
        self.__course = course
        self.__middle_score = middle_score

    def __repr__(self):
        print(super().__repr__())
        return f"Student of {self.get_faculty()} faculty,{self.get_university()}, {self.get_course()}-th course, middle score-{self.get_score()}."

    def get_score(self):
        return self.__middle_score

    def get_course(self):
        return self.__course

    def get_faculty(self):
        return self.__faculty

    def get_university(self):
        return self.__university


class Teacher(Person):
    """
       Class: derived from Person()
       constructors: __init__(overridden from base class)
       fields: additional fields except overridden fields- university, faculty, discipline, experience, salary
       dunder methods: __repr__(overridden from Person class)- returns information about it's and base class' fields
       regular methods: getters with name of each field
       """

    def __init__(self, name, surname, age, gender, university, faculty, discipline, experience, salary):
        super().__init__(name, surname, age, gender)
        self.__university = university
        self.__faculty = faculty
        self.__discipline = discipline
        self.__experience = experience
        self.__salary = salary

    def __repr__(self):
        print(super().__repr__())
        return f"Teacher of '{self.get_discipline()}' subject, faculty - {self.get_faculty()}, {self.get_university()}, experience-{self.get_experience()} years, salary-{self.get_salary()}."

    def get_discipline(self):
        return self.__discipline

    def get_faculty(self):
        return self.__faculty

    def get_university(self):
        return self.__university

    def get_experience(self):
        return int(self.__experience)

    def get_salary(self):
        return f"{int(self.__salary)} USD"
