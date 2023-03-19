class Student:
    number = 0
    def __init__(self, name, score):
        self.name = name
        self.score = score

        Student.number = Student.number + 1

    def show(self):
        print("Name: {}. Score: {}".format(self.name, self.score))

    #静态方法无法使用 cls 和 self 参数访问实例的变量
    @staticmethod
    def func1():
        print("This is a static function")


student = Student("A",100)
student.func1()
