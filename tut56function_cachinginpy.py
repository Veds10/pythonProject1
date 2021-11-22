# import time
# from functools import lru_cache
#
# @lru_cache(maxsize=32) # its nothing but the decorators which stores/saves the value
# def some_work(n):
#     #Some task taking n seconds
#     time.sleep(n)
#     return n
#
# if _name_ == '_main_':
#     print("Now running some work")
#     some_work(3)
#     some_work(1)
#     some_work(6)
#     some_work(2)
#     input()#     print("Done... Calling again")
#     some_work(3)
#     print("Called again")

# @functools.lru_cache(maxsize=4)
# def myfunc(x):
#     time.sleep(2)
#     return x
#
# myfunc(1)
# # myfunc(1) takes 2 seconds and results for myfunc(1) are now cached
# myfunc(1)
# myfunc(2)
# myfunc(3)
# myfunc(4)
# myfunc(5)

