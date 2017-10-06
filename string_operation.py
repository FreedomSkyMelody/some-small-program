#使用菜单实现串的常用操作
#python3.4
#作者：代*

string=input('请输入字符串 string=')
while True:
   print('\nstartend.字符串的截取\nfind.查找字符串\nsplit.分离字符串\njoin.',
         '字符串的联接\ninsert.在末尾加入字符串\nreplace.查找和替换\nlower.转换为小写',
         '\nupper.转换为大写\nclose.退出')
   order=input('请输入命令 order=')
   if order=='startend':
      print('取出位置为 x 到位置为 y 的字符：')
      x=input('x=')
      y=input('y=')
      if x!='' and y!='':
         x=int(x)
         y=int(y)
      elif x!='' and y=='':
         x=int(x)
         y=None
      elif x=='' and y!='':
         x=None
         y=int(y)
      else:
         x=None
         y=None
      string=string[x:y]
      print ('结果为：',string)
   elif order=='find':
      print('请输入要查找的字符串：')
      f=input('find=')
      c=string.find(f)
      print('字符串的位置为：',c)
   elif order=='split':
      print('请输入一个字符，根据该字符能把字符串分离成多个子串：')
      char=input('字符为char=')
      splitstring=string.split(char)
      string=splitstring
      print('分离后的字符串为：',splitstring)
   elif order=='join':
      print('把分离后的字符串用输入的字符联结起来！')
      char=input('char=')
      sep=char
      sepstring=sep.join(string)
      string=sepstring
      print('联结后的字符串为：',sepstring)
   elif order=='insert':
      print('请输入要插入的字符串！')
      insertstring=input('string=')
      string+=insertstring
      print('结果为：',string)
   elif order=='replace':
      print('请输入要替换的旧字符和顶替的新字符：')
      oldstring=input('oldstring=')
      newstring=input('newstring=')
      if oldstring!='' and newstring!='':
         replacestring=string.replace(oldstring,newstring)
         string=replacestring
      else:
         replacestring='请输入字符串！'
      print('替换的结果为：',replacestring)
   elif order=='lower':
      print('把大写字母转换为小写字母！')
      string=string.lower()
      print('转换为小写结果为：',string)
   elif order=='upper':
      print('把小写字母转换为大写字母！')
      string=string.upper()
      print('转换为大写结果为：',string)
   elif order=='close':
      print('程序已正常结束！！\n')
      break
   else:
      print('请输入正确的命令！')
