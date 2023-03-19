#创建父类学校成员
class SchoolMember:
    school_number = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        SchoolMember.school_number = SchoolMember.school_number + 1

    def tell(self):
        print("Name: {}. Age: {}".format(self.name,self.age))

    #cls不能作为property参数
    # @property
    # def count(cls):
    #     print("School Member is {}".format(cls.school_number))
    #类变量咋折腾也不能作为属性？？
    # @property
    # def count(self):
    #     print("School Member is {}".format(self.__class__.school_number))
    @property
    def count(self):
        print("This man is {}".format(self.age))

#创建子类老师 Teacher
class Teacher(SchoolMember):
    teacher_number = 0

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    #方法重写
    def tell(self):
        super().tell()
        print("Salary: {}".format(self.salary))

#创建子类学生 Student
class Student(SchoolMember):
    student_member = 0

    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score
    
    #方法重写
    def tell(self): 
        super().__init__.tell()
        print("Score {}".format(self.score))

    #属性也是可以重写的
    @property
    def count(self):
        print("This man is {}".format(self.age))


teaher1 = Teacher("Mr.Zhang",40,6000)
teaher1.tell()
student1 = Student("A",19,100)
student2 = Student("B",18,89)
Teacher.teacher_number
student2.count
teaher1.count
SchoolMember.count