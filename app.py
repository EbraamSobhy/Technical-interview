class A:
  def m1(self):
    print("m1 in class A")

class B(A):
  def m2(self):
    print("m2 in class B")

class C(A):
  def m3(self):
    print("m2 in class C")

class D(B, C):
  def m4(self):
    print("m2 in class D")

d = D()

d.m1()
d.m2()
d.m3()
d.m4()
