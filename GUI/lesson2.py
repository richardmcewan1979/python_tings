#lesson 2

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

class window(QMainWindow):

	def __init__(self):
		super(window, self).__init__()
		self.setGeometry(250,250,500,300)
		self.setWindowTitle('pyqt5 tut')
		self.setWindowIcon(QIcon('strikepic4.png'))
		self.show()

app = QApplication(sys.argv)
Gui = window()
sys.exit(app.exec_())

