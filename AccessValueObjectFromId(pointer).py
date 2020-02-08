'''
import ctypes
str = "Komal Memane"
id = id(str)
print(id)
print(ctypes.cast(id, ctypes.py_object).value)
'''


import ctypes

str = "Komal"
strid = id(str)
str = "Akshay"
print(ctypes.cast(strid, ctypes.py_object).value)


print('^'*20)
name = "pawar"

print(ctypes.cast(id(name), ctypes.py_object).value)



