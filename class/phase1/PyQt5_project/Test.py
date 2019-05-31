import sys
from PyQt5 import QtWidgets


class MainUi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.main()
        self.data.close()
        self.show()

    def main(self):
        self.resize(800,800)
        show_student = QtWidgets.QPushButton(self)
        show_student.setGeometry(10,10,80,20)
        show_student.setText("显示学生")
        show_student.clicked.connect(self.show_student)

        add_student = QtWidgets.QPushButton(self)
        add_student.setGeometry(10, 40, 80, 20)
        add_student.setText("添加学生")

        self.data = QtWidgets.QFrame(self)
        self.data.setGeometry(100,10,690,780)
        self.data.setStyleSheet("backgroud-color:black;border:1px solid red")

    def show_student(self):
        self.data.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainUi()
    app.exec_()

