'''
    程序入口
'''
# 可以不用下面两句
# from Student_project_model import StudentModel
# from Student_project_bll import StudentManagerController

from Student_project_ui import StudentManagerView

if __name__ == '__main__':
    view = StudentManagerView()
    view.main()