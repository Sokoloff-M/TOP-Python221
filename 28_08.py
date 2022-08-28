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

    def ipdate_grade_ave(self, value: float):
        self._grade_ave = value

    def load_from_db(self):
        pass


st1 = Student(
    '32412234rwqfgsfg.'
    'PT-301',
    4,
    4.4)
print(f'\nпространство имён{st1.__dict__ =}')
scope = [name for name in dir(st1) if not name.startswith(('__'))]
print(f'\nпространство имён{st1.__dict__ =}')

st1.update_grade_ave(4.5)
print(f'\nпространство имён{st1.__dict__ =}')


# скрытые объекты в классе "_" и "__"


