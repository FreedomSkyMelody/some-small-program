#写一个类实现复数的加减乘除
#python3.4
#作者：代睿

class Rational:
   def __init__(self,m=1,n=1):
      self.m=m
      self.n=n
   #加法运算符重载
   def __add__(self,k):
      F=Rational()
      F.m=self.m+k.m
      F.n=self.n+k.n
      return F
   #减法运算符重载
   def __sub__(self,k):
      F=Rational()
      F.m=self.m-k.m
      F.n=self.n-k.n
      return F
   #乘法运算符的重载
   def __mul__(self,k):
      F=Rational()
      F.m=self.m*k.m-self.n*k.n
      F.n=self.m*k.n+self.n*k.m
      return F
   #除法运算符的重载
   def __truediv__(self,k):
      F=Rational()
      F.m=(self.m*self.n+self.n*k.n)/(self.n*self.n+k.n*k.n)
      F.n=(self.n*self.n-self.m*k.n)/(self.n*self.n+k.n*k.n)
      return F
         
#_____________________主程序________________________
f1=input('请输入第一个复数:a+bi=')
if f1.find('+')>=0:
     L=f1.split('+')
     a=int(L[0])#实部
     b=int(L[1].split('i')[0])#虚部
else:
   L=f1.split('-')
   a=-int(L[1])#实部
   b=-int(L[2].split('i')[0])#虚部
x=Rational(a,b)


f2=input('请输入第二个复数:a+bi=')
if f2.find('+')>=0:
     L=f2.split('+')
     c=int(L[0])#实部
     d=int(L[1].split('i')[0])#虚部
else:
   L=f2.split('-')
   c=-int(L[1])#实部
   d=-int(L[2].split('i')[0])#虚部
y=Rational(c,d)


#加法_________
z=x+y
if z.n<0:
   print("加：",z.m,z.n,"i")
else:
   print ("加：",z.m,"+",z.n,"i")
#减法_________
z=x-y
if z.n<0:
   print("减：",z.m,z.n,"i")
else:
   print ("减：",z.m,"+",z.n,"i")
#乘法_________
z=x*y
if z.n<0:
   print("乘：",z.m,z.n,"i")
else:
   print ("乘：",z.m,"+",z.n,"i")
#除法_________
z=x/y
if z.n<0:
   print("除：",z.m,z.n,"i")
else:
   print ("除：",z.m,"+",z.n,"i")


