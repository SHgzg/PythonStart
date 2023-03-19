class Student:
    number = 0
    def __init__(self, name, score):
        self.name = name
        self.__score = score
        self.__class__.number = self.__class__.number + 1

    def show(self):
        print("Name: {}. Score: {}".format(self.name,self.__score))

    @classmethod
    def total(cls):
        print("Total:{}".format(cls.number))

    @property
    def score(self):
        print("Name: {}.Score {}".format(self.name,self.__score))


student1 = Student("Jhon",100)
student2 = Student("Jhon2",100)
student1.score
Student.total()
