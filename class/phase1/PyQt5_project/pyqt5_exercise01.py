
import sys

from PyQt5 import QtWidgets
# from PyQt5.QtCore import Qt

import phase1.PyQt5_project.youdao_api


class MainWindow(QtWidgets.QWidget):
    # 主函数用来控制主界面的控件以及事件
    def main(self):
        # 参数填:宽，高
        self.resize(822, 600)
        self.setStyleSheet("background-color:rgb(255,255,255)")
        # 设置窗口无边框
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # 左侧框架
        left_frame = self.frame(QtWidgets.QFrame(self),
                                0, 0, 160, 600,
                                "background-image:url(/home/tarena/PyQt-image/youdao/youdao_left.png)")



        # 上边框
        top_frame = self.frame(QtWidgets.QFrame(self),
                               160, 0, 662, 60,
                               "background-image:url(/home/tarena/PyQt-image/youdao/youdao_top.png)")

        # 输入框
        self.input_frame = self.frame(QtWidgets.QTextEdit(self),
                                 177, 60, 628, 252,
                                 "border:none;background-color:#F0F0F5"
                                 )

        # 翻译按钮
        translate_button = self.frame(QtWidgets.QPushButton(self.input_frame),
                                      450, 212, 80, 28,
                                      "QPushButton{background-color:#F23A3A;border-radius:5px;color:#FFFFFF;}"
                                      "QPushButton:hover{background-color:#F75454;}"
                                      "QPushButton:pressed{background-color:#6F2424;}")

        translate_button.setText("翻   译")

        translate_button.clicked.connect(self.translate_function)

        # 输入框
        self.output_frame = self.frame(QtWidgets.QTextBrowser(self),
                                  177, 332, 628, 252,
                                  "border:none;"
                                  "background-color:#F0F0F5"
                                  )

    def frame(self, qtype, x, y, width, height, style):
        # 框架
        _frame = qtype
        # 参数填:x,y,宽，高
        _frame.setGeometry(x, y, width, height)
        _frame.setStyleSheet(style)
        return _frame

    def translate_function(self):
        input_data = self.input_frame.toPlainText()
        print(input_data)
        result = PyQt5_project.youdao_api.api(input_data)
        self.output_frame.append(result)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    youdao = MainWindow()
    youdao.main()
    youdao.show()
    app.exec_()
