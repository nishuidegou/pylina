import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
label = QtWidgets.QLabel("<p style='color: red; margin-left: 20px'><b>hell world</b></p>")  # qt支持html标签，强大吧
# 有了实例，就需要用show()让他显示
label.show()

sys.exit(app.exec_())