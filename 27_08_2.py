class Student:
    def __init__(self,
                 student_id: str,
                 group: str,
                 year: int,
                 grade_ave: float):
        self._grade_ave = grade_ave
        self.year = year
        self.__group = group
        self.student_id = student_id
    #геттер
    @property
    def grade_ave(self):
        return self._grade_ave
    #сеттер
    @grade_ave.setter
    def grade_ave(self, value: float):
        if isinstance(value, (int, float)):
            self._grade_ave = value





st1 = Student(
    'EIF#YR*&QQ$#$@42i(34',
    'PT-302',
    5,
    4.8
)
print(f'{st1._grade_ave} = ')
print(f'{st1.grade_ave} = ')
