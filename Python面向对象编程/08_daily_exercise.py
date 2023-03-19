class Father:
    class_f = 0

    def __init__(self, proto_a, proto_b):
        self.proto_a = proto_a
        self.proto_b = proto_b
        self.__class__.class_f = self.__class__.class_f + 1

    def normalmethod(self):
        print("Proto A: {}".format(self.proto_a))

    @classmethod
    def clsmethod(cls):
        cls.class_f = cls.class_f + 1
        print("Class_f: {}".format(cls.class_f))

    @property
    def Proto_B(self):
        print("Proto B: {}".format(self.proto_b))


instance_a = Father("A属性","B属性")
instance_a.clsmethod()
Father.clsmethod()
instance_a.Proto_B