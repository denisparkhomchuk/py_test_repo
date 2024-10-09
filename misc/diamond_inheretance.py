class A:
    def ping(self):
        print("A")

class B(A):
    def ping(self):
        print("B")

class C(A):
    def ping(self):
        print("C")

class D(B, C):
    def ping(self):
        super().ping()
        #print("D")



obj_d = D()
obj_d.ping()