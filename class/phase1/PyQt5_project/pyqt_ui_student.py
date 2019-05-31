from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem

class myui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.myui_01()
        self.show()

    def myui_01(self):
        # 窗体尺寸大小
        # self.resize(600,300)
        # 设置相对位置，以及窗口大小
        self.setGeometry(200,200,520,300)
        # 设置窗口标题
        self.setWindowTitle('学生信息管理系统')
        # 窗口logo
        self.setWindowIcon(QIcon('Flap.png'))
        # 窗口样式
        self.setStyleSheet('background-color:#FFFFFF')

        # 创建按钮对象
        self.bt = QtWidgets.QPushButton(self)
        self.bt.setGeometry(10,20,90,30)
        # 设置按钮内容
        self.bt.setText('添加信息')

        # 创建学号标签
        self.lable = QtWidgets.QLabel(self)
        self.lable.setGeometry(105,20,30,30)
        self.lable.setText('学号')
        #学号输入框
        self.number_lineEdit = QtWidgets.QLineEdit(self)
        self.number_lineEdit.setGeometry(140,25,70,20)

        #创建姓名标签输入框
        self.name_lb_le_dic = {'lable_x':215,'lable_y':20,'lable_l':30,'lable_w':30,'lable_name':'姓名',
                               'lineEdit_x':240,'lineEdit_y':25,'lineEdit_l':70,'lineEdit_w':20}
        self.name = self.lb_le(**self.name_lb_le_dic)
        # 创建年龄标签输入框
        self.age_lb_le_dic = {'lable_x': 315, 'lable_y': 20, 'lable_l': 30, 'lable_w': 30, 'lable_name': '年龄',
                              'lineEdit_x': 340, 'lineEdit_y': 25, 'lineEdit_l': 70, 'lineEdit_w': 20}
        self.age = self.lb_le(**self.age_lb_le_dic)
        # 创建年龄标签输入框
        self.score_lb_le_dic = {'lable_x': 415, 'lable_y': 20, 'lable_l': 30, 'lable_w': 30, 'lable_name': '成绩',
                                'lineEdit_x': 440, 'lineEdit_y': 25, 'lineEdit_l': 70, 'lineEdit_w': 20}
        self.score = self.lb_le(**self.score_lb_le_dic)

        #生成表格
        self.table = QtWidgets.QTableWidget(self)
        self.table.setGeometry(10,60,500,230)
        #s设置表格列数
        self.table.setRowCount(7)
        # 设置表格行数
        self.table.setColumnCount(4)
        # 设置列宽自适应表格大小
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #设置垂直表头不可见
        self.table.verticalHeader().setVisible(False)
        #设置单元格选中背景色
        self.table.setStyleSheet("selection-background-color:lightblue;")
        l = ['学号', '姓名', '年龄', '成绩']
        self.table.setHorizontalHeaderLabels(l)

        # self.table.setItem(0,0 ,QTableWidgetItem('180801'))

        # 创建按钮点击事件
        self.bt.clicked.connect(self.print)



    def print(self):
        # print('我是按钮点击事件')
        # 获取输入框的值
        number = self.number_lineEdit.text()
        name = self.name.text()
        age = self.age.text()
        score = self.score.text()
        list = [number,name,age,score]
        for i in range(4):
            self.table.setItem(0,i,QTableWidgetItem(list[i]))
            self.table.item(0, i).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # print(a)



    #生成标签输入框
    def lb_le(self, lable_x,lable_y,lable_l,lable_w,lable_name,
              lineEdit_x,lineEdit_y,lineEdit_l,lineEdit_w):

        # 创建学号标签
        self.lable = QtWidgets.QLabel(self)
        self.lable.setGeometry(lable_x, lable_y, lable_l, lable_w)
        self.lable.setText(lable_name)

        # 学号输入框
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(lineEdit_x, lineEdit_y, lineEdit_l, lineEdit_w)
        return self.lineEdit

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # 实例化界面对象
    my_ui = myui()# 调用界面函数
    # my_ui.myui_01()
    # # 显示界面
    # my_ui.show()

    sys.exit(app.exec_())




# 设置列宽自适应表格大小
# self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
# # 设置标题栏样式表
# self.table.horizontalHeader().setStyleSheet("QHeaderView:section{"
#                                              "background-color:rgb(150,170,250);\
#                                               border-radius:2px solid;height:20px;}")
# # 隐藏左侧标题头
# self.table.verticalHeader().setVisible(False)
# # 设置表头内容
# l = ['学号', '姓名', '年龄', '成绩']
# self.table.setHorizontalHeaderLabels(l)
# 添加内容到指定的行跟列
# self.table.setItem(0, 0, QTableWidgetItem(str('xxx')))