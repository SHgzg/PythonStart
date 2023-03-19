class Student:
    #number属于类变量,定义外在方法,不属于具体实例
    number = 0
    #定义学生属性，初始化方法
    #name和score属于实例变量，定义在方法里
    def __init__(self, name, score):
        self.name = name
        self.score = score
        #错误示范：
        # number=number+1

        #正确示范
        # Student.number = Student.number + 1
        self.__class__.number = self.__class__.number + 1

    #定义打印学生成绩的方法
    def show(self):
        print("Name: {}. Score: {}".format(self.name,self.score))


student1 = Student("A",100)
print(Student.number)
student2 = Student("B",99)
print(Student.number)