import sys

# import PyQt4 QtCore and QtGui modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
import traceback

from mainwindow import MainWindow

if __name__ == '__main__':

    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('LSS-Reader')
    

    # create widget
    w = MainWindow()
    w.setWindowTitle('LSS-Reader')
    w.setWindowIcon(QIcon('logo.png'))
    w.showMaximized()

    # connection
    # app.lastWindowClosed.connect()
    # QObject.connect(app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))

    # execute application
    sys.exit(app.exec_())
