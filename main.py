class Person:
    def __init__(self, fullname1, age1, is_married1):
        self.fullname = fullname1
        self.age = age1
        self.is_married = is_married1


introduce_myself = Person('Bek Aidarov', 19, 'not married')
print(
    f' fullname: {introduce_myself.fullname} \n Age: {introduce_myself.age} \n Married: {introduce_myself.is_married}')


class Student(Person):

    def __init__(self, fullname1, age1, is_married1, marks1):
        super().init(fullname1, age1, is_married1)
        self.marks = marks1

    marks = {'math': 5, "history": 4, 'english': 4, "physics": 5, 'biology': 5, 'chemistry': 3, 'literature': 5,
             'drawing': 4, 'music': 3}

    def __get_ball__(self):
        return list(self.marks.values())

    res = sum(marks.values()) / len(marks)
    print(" Average: " + str(res))


def __pay__(salary, experience):
    if experience > 3:
        salary += salary / 100 * 5


class Teacher(Person):

    def __init__(self, fullname1, age1, is_married1, experience=0, salary=0):
        super().__init__(fullname1, age1, is_married1)
        self.experience = experience
        self.salary = salary

    def __zarplata__(self):
        return self.salary + ((self.salary / 100 * 5) * (self.experience - 3)) if self.experience > 3 else self.salary


get_ball = Student
print(f' marks: {get_ball.marks}')
zarplata = Teacher('olga ivanova', 43, 'married', 3, 16000)
print(f' fname: {zarplata.fullname}, age: {zarplata.age}, married: {zarplata.is_married}, '
      f'experience: {zarplata.experience}, bonus: {zarplata.salary}')