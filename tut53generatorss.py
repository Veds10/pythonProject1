# def getNum (x):
#     for i in range(x):
#         yield i
#
# seq = getNum (2)
# print(seq._next_())
# print(seq._next_())
# print(seq._next_())
#
# output
#
# 0
# 1
# Traceback (most recent call last):
# File "<stdin>", line 7, in <module>
#  print(seq._next_())
# StopIteration


"""
Iterable - _iter() or __getitem_() # to access one by one unlike for loop,loop displays every single element where as iter displays one by one
Iterator - _next_()
Iteration -

"""

# generators

def gen(n):
    for i in range(n):
        yield i # same as for loop just use yield instead of return we use gen when we have to fetch all val but iterate one by one using iterator

g = gen(3)
# print(g._next_())
# print(g._next_())
# print(g._next_())
# print(g._next_())


# for i in g:
#     print(i)

h = 546546
ier = iter(h)
print(ier._next_())
print(ier._next_())
print(ier._next_())
# for c in h:
#     print(c)