from all_structure.all_struchure import Queue, Tree

q = Queue()
q.enqueue("hello")
q.enqueue("world")
q.enqueue("itcast")
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print("=" * 40)

t = Tree()
t.add("1")
t.add("2")
t.add("3")
t.add("4")

print(t.breadth_travel())
print("=" * 40)
