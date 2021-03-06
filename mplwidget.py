from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import Qt
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg \
 import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class MplCanvas(FigureCanvas):
	def __init__(self):
		self.fig = Figure()
		self.ax = self.fig.add_subplot(111)
		FigureCanvas.__init__(self, self.fig)
		FigureCanvas.setSizePolicy(self, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)

class MplWidget(QtWidgets.QWidget):
	def __init__(self, parent = None):
		QtWidgets.QWidget.__init__(self, parent)
		self.canvas = MplCanvas()
		self.toolbar = NavigationToolbar(self.canvas, parent)
		self.vbl = QtWidgets.QVBoxLayout()
		self.vbl.addWidget(self.canvas)
		self.vbl.addWidget(self.toolbar)
		self.setLayout(self.vbl)

