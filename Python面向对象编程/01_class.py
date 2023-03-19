class Student:
    #定义初始属性及初始化方法
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    #定义打印学生信息的方法
    def show(self):
        print("Name: {}.Score: {}".format(self.name, self.score))


student1 = Student("John",100)
student2 = Student("Lucy",99)
student1.show()
student2.show()