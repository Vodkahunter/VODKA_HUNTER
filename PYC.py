import os,sys
import py_compile
print('\033[1;93m -ENTER FILE NAME')
Z = input('\033[1;97m  ')
C = py_compile.compile(Z)
print(C)