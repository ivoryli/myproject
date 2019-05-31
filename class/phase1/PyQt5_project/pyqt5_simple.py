
import sys
from PyQt5 import QtWidgets
app=QtWidgets.QApplication(sys.argv)
widget=QtWidgets.QWidget()
widget.resize(400,400)
widget.setWindowTitle("hello mt")
widget.show()
sys.exit(app.exec_())