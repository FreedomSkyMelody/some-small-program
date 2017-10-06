#用菜单实现矩阵的加和乘
#作者：代睿

#_____________求和函数_________________
def Sum(a,b):
   #定义一个二维数组
   #c=[[0 for i in range(L1)]for i in range(H1)]
   c=[[0]*L1]*H1
   if H1==H2 and L1==L2:
      for i in range(0,H1):
         for j in range(0,L1):
            c[i][j]=int(a[i][j])+int(b[i][j])
      print ('两个矩阵和为;',c)
   else:
      print('\n这两个矩阵无法相加！\n')

#_____________求积函数__________________
def Product(a,b):
   #定义一个二维数组
   #c=[[0 for i in range(L2)]for i in range(H1)]
   c=[[0]*L2]*H1
   if L1==H2:
      k=0
      f=0
      for i in range(H1):
         for j in range(L2):
            while f<L1:
               k+=int(a[i][j])*int(b[j][i])
               f+=1
            c[i][j]=k
      print (c)
   else:
      print('\n这两个矩阵无法相乘！\n')
            
#_____________处理函数__________________
def Dealwith():
   a=[]
   f=1
   while f-1<H1:
      print('请输入第',f,'行：a',f,'=',end='')
      x=input()
      x=x.split(',')
      a=a+[x]
      f+=1
   return a


#主程序______________________________________________________________
while True:
   order='new'
   #第一个矩阵
   H1=int(input('请输入第一个矩阵的行 H1='))
   L1=int(input('请输入第一个个矩阵的列 L1='))
   a=Dealwith()
   #第二个矩阵
   H2=int(input('请输入第二个矩阵的行 H2='))
   L2=int(input('请输入第二个个矩阵的列 L2='))
   b=Dealwith()
   if order=='new':   
      while True:
         print('0.退出当前\n1.求  和\n2.求  积')
         flag=int(input('请输入命令前的代号f='))
         if flag==1:
            Sum(a,b)
         if flag==2:
            Product(a,b)
         if flag==0:
            print('\n目前的两个矩阵运算已经正常结束！\n')
            break
      print('close.关闭程序\nnew.建立新的矩阵运算')
      order=input('关闭程序还是建立新的矩阵运算？order=')
   if order=='close':
      print ('\n程序已经正常结束！')
      break
