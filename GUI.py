from PyQt4 import QtGui
import sys

def buildGUI(list,croppedImage):
    i=0
    app=QtGui.QApplication(sys.argv)
    w=QtGui.QWidget()
    label=QtGui.QLabel(w)
    w.setGeometry(100,100,200,200)
    label.setText("HELLLLOOOOO")
    label.move(50,50)
    w.show()


    print("hellll")