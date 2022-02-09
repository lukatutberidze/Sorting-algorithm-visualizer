from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import random
import time
import threading
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class Ui_MainWindow(QObject):
        update_required = QtCore.pyqtSignal()
        def __init__(self):
            super().__init__()
            self.update_required.connect(self.update)
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(979, 680)
                MainWindow.setStyleSheet("background-color: rgb(65, 65, 65);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(20, 20, 940, 491))
                self.label.setStyleSheet("background-color: rgb(107, 107, 107);")
                self.label.setText("")
                self.label.setObjectName("label")
                self.add10 = QtWidgets.QPushButton(self.centralwidget)
                self.add10.setGeometry(QtCore.QRect(20, 520, 241, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic Medium")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.add10.setFont(font)
                self.add10.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(108, 108, 108);")
                self.add10.setObjectName("add10")
                self.startsort = QtWidgets.QPushButton(self.centralwidget)
                self.startsort.setGeometry(QtCore.QRect(270, 590, 241, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic Medium")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.startsort.setFont(font)
                self.startsort.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(108, 108, 108);")
                self.startsort.setObjectName("startsort")
                self.algos = QtWidgets.QComboBox(self.centralwidget)
                self.algos.setGeometry(QtCore.QRect(20, 590, 241, 61))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.algos.setFont(font)
                self.algos.setStyleSheet("color: rgb(255, 255, 255);")
                self.algos.setObjectName("algos")
                self.algos.addItem("")
                self.algos.addItem("")
                self.stopsort = QtWidgets.QPushButton(self.centralwidget)
                self.stopsort.setGeometry(QtCore.QRect(270, 520, 241, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic Medium")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.stopsort.setFont(font)
                self.stopsort.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(108, 108, 108);")
                self.stopsort.setObjectName("stopsort")

                self.clear = QtWidgets.QPushButton(self.centralwidget)
                self.clear.setGeometry(QtCore.QRect(520, 520, 171, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic Medium")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.clear.setFont(font)
                self.clear.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(108, 108, 108);")
                self.clear.setObjectName("clear")
                self.info = QtWidgets.QPushButton(self.centralwidget)
                self.info.setGeometry(QtCore.QRect(520, 590, 301, 61))
                font = QtGui.QFont()
                font.setFamily("Yu Gothic Medium")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.info.setFont(font)
                self.info.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(108, 108, 108);")
                self.info.setObjectName("info")
                self.speed1 = QtWidgets.QRadioButton(self.centralwidget)
                self.speed1.setGeometry(QtCore.QRect(700, 520, 82, 17))
                self.speed1.setStyleSheet("color: rgb(255, 255, 255);")
                self.speed1.setObjectName("speed1")
                self.speed2 = QtWidgets.QRadioButton(self.centralwidget)
                self.speed2.setGeometry(QtCore.QRect(700, 540, 82, 17))
                self.speed2.setStyleSheet("color: rgb(255, 255, 255);")
                self.speed2.setObjectName("speed2")
                self.speed3 = QtWidgets.QRadioButton(self.centralwidget)
                self.speed3.setGeometry(QtCore.QRect(700, 560, 82, 17))
                self.speed3.setStyleSheet("color: rgb(255, 255, 255);")
                self.speed3.setObjectName("speed3")
                self.credits = QtWidgets.QLabel(self.centralwidget)
                self.credits.setGeometry(QtCore.QRect(880, 640, 91, 16))
                self.credits.setStyleSheet("color: rgb(255, 255, 255);")
                self.credits.setObjectName("credits")
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                self.setup()

        def setup(self):
                self.ls=[]
                self.add10.clicked.connect(self.adder)
                self.clear.clicked.connect(self.cl)
                self.startsort.clicked.connect(self.stort)
                self.stopsort.clicked.connect(self.stoprt)
                self.sortable=True
                self.started=0

        def stort(self):
                if self.speed1.isChecked()==False and self.speed2.isChecked()==False and self.speed3.isChecked()==False:
                        self.error(0)
                        return 0
                elif len(self.ls)==0:
                        self.error(1)
                        return 0
                if self.algos.currentText()=='Bubble Sort':
                        self.sortable=True
                        self.started+=1
                        t=threading.Thread(target=self.bubl)
                        t.start()
                elif self.algos.currentText()=='Selection Sort':
                        self.sortable=True
                        self.started+=1
                        t=threading.Thread(target=self.selection)
                        t.start()
        
        def getspeed(self):
                if self.speed3.isChecked()==True:
                        return 0.0001
                elif self.speed2.isChecked()==True:
                        return 0.05
                elif self.speed1.isChecked()==True:
                        return 0.1
        def stoprt(self):self.sortable=False     
        def selection(self):
                if self.started!=1:
                        return 0
                skr=sorted(self.ls,key=lambda x:x[1]['height'])
                p=self.getspeed()
                a=self.ls[0][1]['height']
                start=0
                while self.ls!=skr:
                        time.sleep(p)
                        if self.sortable==False:
                                self.started=0
                                self.sortable=True
                                return 0
                        currentminind=start
                        for i in range(len(self.ls[:start])):
                                self.ls[i][0].setStyleSheet("background-color: rgb(40, 252, 97);")
                        for i in range(start,len(self.ls)):
                                if self.ls[i][1]['height']<self.ls[currentminind][1]['height']:
                                        currentminind=i
                        if start==91:
                                self.ls[91][0].setStyleSheet("background-color: rgb(40, 252, 97);")
                                return 0
                        self.ls[start],self.ls[currentminind]=self.ls[currentminind],self.ls[start]
                        self.update_required.emit()
                        start+=1
                return 0       
                 
        def bubl(self):
                if self.started!=1:
                        return 0
                x=sorted(self.ls,key=lambda x:x[1]['height'])
                p=self.getspeed()
                a,b=0,1
                c=93
                while self.ls!=x:
                        time.sleep(p)
                        if self.sortable==False:
                                self.started=0
                                self.sortable=True
                                return 0
                        elif b in (92,c):
                                a,b=0,1
                                c-=1
                        else:   
                                if self.ls[a][1]['height']>self.ls[b][1]['height']:
                                        self.ls[a],self.ls[b]=self.ls[b],self.ls[a]
                                        self.ls[a][0].setStyleSheet("background-color: rgb(255, 30, 0);")
                                        self.ls[b][0].setStyleSheet("background-color: rgb(255, 30, 0);")
                                        self.update_required.emit()
                                        time.sleep(p)
                                        self.ls[a][0].setStyleSheet("background-color: rgb(255, 255, 255);")
                                        self.ls[b][0].setStyleSheet("background-color: rgb(255, 255, 255);")
                                else:
                                        self.ls[a][0].setStyleSheet("background-color: rgb(40, 252, 97);")
                                        self.ls[b][0].setStyleSheet("background-color: rgb(40, 252, 97);")
                                        time.sleep(p)
                                        self.ls[a][0].setStyleSheet("background-color: rgb(255, 255, 255);")
                                        self.ls[b][0].setStyleSheet("background-color: rgb(255, 255, 255);")
                                a+=1
                                b+=1
                return 0         
        def adder(self):
                if len(self.ls)!=0:
                        return 0
                x=30
                for i in range(92):
                        a=random.randrange(20,470)
                        self.label = QtWidgets.QLabel(self.centralwidget)
                        self.label.setGeometry(QtCore.QRect(x, 510-a, 4, a))
                        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
                        self.label.show()
                        self.ls.append([self.label,{'x':x,'y':510-a,'height':a}])
                        x+=10
        def update(self):
                x=30
                for i in range(len(self.ls)):
                        self.ls[i][0].setGeometry(x,self.ls[i][1]['y'],4,self.ls[i][1]['height'])
                        self.ls[i][1]['x']=x
                        x+=10
        def cl(self):
                for i in range(len(self.ls)):
                        self.ls[i][0].hide()
                self.ls=[]
                self.started=0
        def error(self,ind):
                ls=['You have to select a speed, before the sorting starts.',"You haven't inserted the cones. Insert some!"]
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText(ls[ind])
                msgBox.setWindowTitle("Speed not selected")
                msgBox.addButton('Ok', QMessageBox.YesRole)
                returnValue = msgBox.exec()


        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Sorting algorithm visualizer"))
                self.add10.setText(_translate("MainWindow", "Add cones"))
                self.startsort.setText(_translate("MainWindow", "Start sorting"))
                self.algos.setItemText(0, _translate("MainWindow", "Bubble Sort"))
                self.algos.setItemText(1, _translate("MainWindow", "Selection Sort"))
                self.stopsort.setText(_translate("MainWindow", "Stop sorting"))
                self.clear.setText(_translate("MainWindow", "Clear"))
                self.info.setText(_translate("MainWindow", "Information about the algorithm"))
                self.speed1.setText(_translate("MainWindow", "Speed 1"))
                self.speed2.setText(_translate("MainWindow", "Speed 2"))
                self.speed3.setText(_translate("MainWindow", "Speed 3"))
                self.credits.setText(_translate("MainWindow", "Luka Tutberidze"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())