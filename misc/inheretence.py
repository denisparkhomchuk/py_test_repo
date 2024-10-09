from pyclbr import Class


class A:
    def method_1(self):
        print("1")

class B(A):
    def method_1(self):
        print("2")



def method_2(_obj: A):
    _obj.method_1()


obj = B()
method_2(obj)