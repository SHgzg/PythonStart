class Student:
    number = 1
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.__class__.number = self.__class__.number

    def show(self):
        print("Name: {}.Score {}".format(self.name,self.score))

    #定义类方法打印学生数量
    @classmethod
    #使用 cls 获取类变量作为参数
    def total(cls):
        print("Total: {0}".format(cls.number))

student1 = Student("A",100)
student2 = Student("A",90)
student1.show()
print(Student.number)
Student.total()