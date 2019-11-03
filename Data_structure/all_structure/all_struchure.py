# 链表

class Node(object):
    def __init__(self, elem):
        # _item存放数据元素
        self.elem = elem
        # _next是下一个节点的标识
        self.next = None


class SingleLinkList(object):
    def __init__(self, node=None):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next

    def add(self, item):
        # 头部添加元素
        node = Node(item)
        node.next = self._head
        self.head = node

    def append(self, item):
        # 尾部添加元素
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):

        if pos <= 0:
            self.add(item)
        elif pos >= self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            while pos > 0:
                cur = cur.next
                pos -= 1
            node.next = cur.next
            cur.next = node



# 栈
class Stack(object):
    def __init__(self):
        self.items=[]
    def is_empty(self):
        # 判断是否为空
        return self.items==[]
    def pop(self):
        # 弹出元素
        return self.items.pop()
    def push(self,items):
        # 加入元素
        return self.items.append(items)
    def peek(self):
        # 返回栈顶函数
        return self.items[len(self.items)-1]
    def size(self):
        # 反回栈的大小
        return len(self.items)

# 队列
class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# 树
class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.lchild=None
        self.rchild=None
class Tree(object):
    def __init__(self):
        self.root=None

    def add(self,item):
        node=Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild=node
                return
            else:
                queue.append(cur_node.lchild)

                if cur_node.rchild is None:
                    cur_node.rchild=node
                    return
                else:
                    queue.append(cur_node.rchild)

    def breadth_travel(self):
        # 广度遍历
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node=queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self,node):# 前序遍历
        if node is None:
            return
        print(node.elem,end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self,node): # 中序遍历
        if node is None:
            return
        self.preorder(node.lchild)
        print(node.elem,end=" ")
        self.preorder(node.rchild)
    def postorder(self,node): # 后序遍历
        if node is None:
            return
        self.preorder(node.lchild)
        self.preorder(node.rchild)
        print(node.elem,end=" ")


