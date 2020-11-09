class A():
    def foo(self):
        print('A')
        
class B(A):
    def foo(self):
        print('B')
        
class C(A):
    def foo(self):
        print('C')
        
class D(B, C):
    def otherfoo(self):
        super(B, self).foo()
        A.foo(self)

d = D()
d.otherfoo()
