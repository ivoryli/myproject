import sys
sys.path.append('/home/tarena/class/')

from phase1.day13.Student_project.Student_project_bll import StudentManagerController
from phase1.day13.Student_project.Student_project_model import StudentModel

from PyQt5 import QtWidgets

class DisplayWindow(QtWidgets.QWidget):
    def __init__(self, style = None,parent=None):
        super(DisplayWindow, self).__init__(parent)
        self.resize(1000, 600)
        self.setStyleSheet("background-color:rgb(255,255,255)")
        self.Student_Object = StudentManagerController()
        self.style =style

    def handle_click(self):
        if not self.isVisible():
            if self.style == "display":
                self.show_student()
            elif self.style == "add":
                self.add_student()
            self.show()

    def handle_close(self):
        self.close()

    def show_student(self):
        listFile = QtWidgets.QListWidget()
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(listFile, 0, 0, 1, 1)

        for item in self.Student_Object.list_stu:
            print("学生编号为%d的%d岁%s同学成绩是%d"%(item.id,item.age,item.name,item.score))
        for item in self.Student_Object.list_stu:
            str_message="编号:%d的%d岁,学生%s的成绩是%d\n"%(item.id,item.age,item.name,item.score)
            listFile.addItem(str_message)

    def add_student(self):
        self.input_frame = self.frame(QtWidgets.QTextEdit(self),
                                      177, 60, 628, 252,
                                      "border:none;background-color:#F0F0F5"
                                      )
        add_button = self.frame(QtWidgets.QPushButton(self.input_frame),
                                450, 212, 80, 28,
                                "QPushButton{background-color:#F23A3A;border-radius:5px;color:#FFFFFF;}"
                                "QPushButton:hover{background-color:#F75454;}"
                                "QPushButton:pressed{background-color:#6F2424;}")

        add_button.setText("添   加")

        add_button.clicked.connect(self.add_function)


    def add_function(self):
        # input_data = self.input_frame.toPlainText()
        # L = input_data.split(" ")
        # print(L)
        # age = int(L[1])
        # score = int(L[2])
        stu = StudentModel("zs",20,30)
        self.Student_Object.add_student(stu)
        for item in self.Student_Object.list_stu:
            print("学生编号为%d的%d岁%s同学成绩是%d"%(item.id,item.age,item.name,item.score))
        print("-----------------------------------------------------------------")



    def frame(self, qtype, x, y, width, height, style):
        # 框架
        _frame = qtype
        # 参数填:x,y,宽，高
        _frame.setGeometry(x, y, width, height)
        _frame.setStyleSheet(style)
        return _frame
        # self.Student_Object.add_student()
        #无法换行显示
        # def show_student(self):
        #     display = QtWidgets.QLineEdit(self)
        #     display.setGeometry(450,212,440,200)
        #     data = self.bll()
        #     display.setText(data)
        # def bll(self):
        #     L = []
        #     for item in self.Student_Object.list_stu:
        #         L.append("编号:%d的%d岁,学生%s的成绩是%d\n"%(item.id,item.age,item.name,item.score))
        #     s = "".join(L)
        #     return s


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(1000, 600)
        self.setStyleSheet("background-color:rgb(255,255,255)")
        self.display_button = None

    def main(self):
        #border-radius 四边圆角设置
        self.display_button = self.frame(QtWidgets.QPushButton(self),450, 150, 100, 32,
                                    "QPushButton{background-color:#DBB9B9;border-rius:5px;color:#FFFFFF;}")
        self.display_button.setText("显示学生信息")

        self.add_button = self.frame(QtWidgets.QPushButton(self),450, 190 , 100, 32,
                                    "QPushButton{background-color:#DBB9B9;border-rius:5px;color:#FFFFFF;}")
        self.add_button.setText("添加学生信息")

    def frame(self, qtype, x, y, width, height, style):
        # 框架
        _frame = qtype
        # 参数填:x,y,宽，高
        _frame.setGeometry(x, y, width, height)
        _frame.setStyleSheet(style)
        return _frame

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    StudentMainUi = MainWindow()
    displayWindow = DisplayWindow("display")
    addWindow = DisplayWindow("add")
    StudentMainUi.main()
    StudentMainUi.display_button.clicked.connect(displayWindow.handle_click)
    StudentMainUi.add_button.clicked.connect(addWindow.handle_click)
    StudentMainUi.show()
    app.exec_()
