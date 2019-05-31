# import double_list_helper as dlh
# from double_list_helper import DoubleListHelper,Vector2

import double_list_helper
print(double_list_helper.__doc__)
print(double_list_helper.__file__)
print(double_list_helper.__name__)

list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]

# 10               向右　　　　　３　　　　－－> 11 12  13
# re01 = DoubleListHelper.get_elements(list01,Vector2(1,0),Vector2.right(),3)
# print(re01)

# re02 = dlh.DoubleListHelper.get_elements(list01,dlh.Vector2(2,3),dlh.Vector2.left(),3)
# print(re02)
#
# re03 = dlh.DoubleListHelper.get_elements(list01,dlh.Vector2(0,2),dlh.Vector2.down(),2)
# print(re03)
#
# re04 = dlh.DoubleListHelper.get_elements(list01,dlh.Vector2(2,0),dlh.Vector2.up_right(),2)
# print(re04)

