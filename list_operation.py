#用一个主菜单，对链表进行操作
#python3.4
#作者：代睿

#输出函数
def printnode(pnode):
    while pnode!=None:
        print(pnode.elem,'，',end='')
        pnode=pnode.next

#插入在其他位置函数
def insertnode(head):
    print ('请输入结点数据和要插入的位置：')
    data=int(input('data='))
    address=int(input('address='))
    data=LNode(data)
    address=LNode(address)
    while head is not None:
       if address.elem is head.elem:
           f=head.next
           head.next=data
           data.next=f
       head=head.next
   
#插入在表首
def insertnode1(head):
    print ('请输入结点数据：')
    data=input('data=')
    data=LNode(data)
    data.next=head
    head=data     
    return data
    
       
#删除函数
def deletenode(head):
    print ('请输入要删除的结点数据：')
    data=int(input('data='))
    data=LNode(data)
    #下面进行删除
    while head is not None:
        if head.elem is data.elem-1:
            head.next=head.next.next
        head=head.next
   
#删除表首结点
def deletenode1(head):
    head=head.next
    return head

#类
class LNode:  #只定义初始化操作
    def __init__(self,elm,next_=None):
        self.elem=elm
        self.next=next_


#_______________________主程序__________________________________
list1=LNode(1)
pnode=list1
for i in range(2,11):
    pnode.next=LNode(i)
    pnode=pnode.next
#遍历    
pnode=list1 #list1是表头变量
#输出每个结点
print('现有结点：')
while pnode!=None:
    print(pnode.elem,'，',end='')
    pnode=pnode.next #把下一个结点的地址再送给pnode，
                     #这样pnode就能遍历所有的结点
#________________________________________________________________
while True:
    print('\n菜单：\n1--删除在 其他 位置的结点\n2--删除在 表首 位置的结点',
          '\n3--插入在 其他 位置结点\n4--插入 表首 位置结点\n5--输出链表',
          '\n6--结束程序')
    order=int(input('\n请输入命令编号order='))
    if order==1:#删除其他结点
        deletenode(list1)
    elif order==2:#删除表首结点
        list1=deletenode1(list1)
    elif order==3:#插入其他位置结点
        insertnode(list1)
    elif order==4:#插入表首位置结点
        list1=insertnode1(list1)
    elif order==5:#输出链表
        printnode(list1)
    elif order==6:#结束程序
        print('程序以正常结束！')
        break

