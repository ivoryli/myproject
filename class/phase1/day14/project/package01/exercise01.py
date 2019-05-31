import sys

print(sys.path)
#添加根目录后才能在终端导入package01,因为本身path路径只有package01里的,不包含package01
sys.path.append('/home/tarena/class/phase1/day14/project/')

from package01.m01 import test

test().class_test()