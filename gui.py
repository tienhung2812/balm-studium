# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 619)
        
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 911, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.data_tab = QtWidgets.QWidget()
        self.data_tab.setObjectName("data_tab")
        self.return_label = QtWidgets.QLabel(self.data_tab)
        self.return_label.setGeometry(QtCore.QRect(720, 20, 59, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.return_label.setFont(font)
        self.return_label.setAlignment(QtCore.Qt.AlignCenter)
        self.return_label.setObjectName("return_label")
        self.liquidity_label = QtWidgets.QLabel(self.data_tab)
        self.liquidity_label.setGeometry(QtCore.QRect(120, 20, 59, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.liquidity_label.setFont(font)
        self.liquidity_label.setObjectName("liquidity_label")
        self.liquidity_list = QtWidgets.QTableWidget(self.data_tab)
        self.liquidity_list.setGeometry(QtCore.QRect(20, 40, 256, 321))
        self.liquidity_list.setObjectName("liquidity_list")
        self.liquidity_list.setColumnCount(0)
        self.liquidity_list.setRowCount(0)
        self.cost_label = QtWidgets.QLabel(self.data_tab)
        self.cost_label.setGeometry(QtCore.QRect(400, 20, 59, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cost_label.setFont(font)
        self.cost_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cost_label.setObjectName("cost_label")
        self.next_button = QtWidgets.QPushButton(self.data_tab)
        self.next_button.setGeometry(QtCore.QRect(400, 500, 114, 32))
        self.next_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.next_button.setAutoFillBackground(False)
        self.next_button.setObjectName("next_button")
        self.cost_list = QtWidgets.QTableWidget(self.data_tab)
        self.cost_list.setGeometry(QtCore.QRect(300, 40, 256, 321))
        self.cost_list.setObjectName("cost_list")
        self.cost_list.setColumnCount(0)
        self.cost_list.setRowCount(0)
        self.return_list = QtWidgets.QTableWidget(self.data_tab)
        self.return_list.setGeometry(QtCore.QRect(580, 40, 311, 321))
        self.return_list.setObjectName("return_list")
        self.return_list.setColumnCount(0)
        self.return_list.setRowCount(0)
        self.frame = QtWidgets.QFrame(self.data_tab)
        self.frame.setGeometry(QtCore.QRect(20, 370, 256, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.liquidityAdd = QtWidgets.QPushButton(self.frame)
        self.liquidityAdd.setGeometry(QtCore.QRect(50, 90, 61, 32))
        self.liquidityAdd.setObjectName("liquidityAdd")
        self.liquidityRemove = QtWidgets.QPushButton(self.frame)
        self.liquidityRemove.setGeometry(QtCore.QRect(170, 90, 81, 32))
        self.liquidityRemove.setObjectName("liquidityRemove")
        self.liquidityModify = QtWidgets.QPushButton(self.frame)
        self.liquidityModify.setGeometry(QtCore.QRect(100, 90, 81, 32))
        self.liquidityModify.setObjectName("liquidityModify")
        self.LDD = QtWidgets.QTextEdit(self.frame)
        self.LDD.setGeometry(QtCore.QRect(10, 60, 71, 31))
        self.LDD.setObjectName("LDD")
        self.LSD = QtWidgets.QTextEdit(self.frame)
        self.LSD.setGeometry(QtCore.QRect(90, 60, 71, 31))
        self.LSD.setObjectName("LSD")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_3.setGeometry(QtCore.QRect(170, 60, 71, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(170, 10, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(self.data_tab)
        self.frame_2.setGeometry(QtCore.QRect(300, 370, 256, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.costAdd = QtWidgets.QPushButton(self.frame_2)
        self.costAdd.setGeometry(QtCore.QRect(50, 90, 61, 32))
        self.costAdd.setObjectName("costAdd")
        self.costRemove = QtWidgets.QPushButton(self.frame_2)
        self.costRemove.setGeometry(QtCore.QRect(170, 90, 81, 32))
        self.costRemove.setObjectName("costRemove")
        self.costModify = QtWidgets.QPushButton(self.frame_2)
        self.costModify.setGeometry(QtCore.QRect(100, 90, 81, 32))
        self.costModify.setObjectName("costModify")
        self.CLDD = QtWidgets.QTextEdit(self.frame_2)
        self.CLDD.setGeometry(QtCore.QRect(10, 60, 51, 31))
        self.CLDD.setObjectName("CLDD")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(70, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.CLSD = QtWidgets.QTextEdit(self.frame_2)
        self.CLSD.setGeometry(QtCore.QRect(70, 60, 51, 31))
        self.CLSD.setObjectName("CLSD")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(130, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.CLTD = QtWidgets.QTextEdit(self.frame_2)
        self.CLTD.setGeometry(QtCore.QRect(130, 60, 51, 31))
        self.CLTD.setObjectName("CLTD")
        self.label_19 = QtWidgets.QLabel(self.frame_2)
        self.label_19.setGeometry(QtCore.QRect(185, 10, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName("label_19")
        self.CLB = QtWidgets.QTextEdit(self.frame_2)
        self.CLB.setGeometry(QtCore.QRect(190, 60, 51, 31))
        self.CLB.setObjectName("CLB")
        self.frame_3 = QtWidgets.QFrame(self.data_tab)
        self.frame_3.setGeometry(QtCore.QRect(580, 370, 311, 121))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.returnAdd = QtWidgets.QPushButton(self.frame_3)
        self.returnAdd.setGeometry(QtCore.QRect(100, 90, 61, 32))
        self.returnAdd.setObjectName("returnAdd")
        self.returnRemove_2 = QtWidgets.QPushButton(self.frame_3)
        self.returnRemove_2.setGeometry(QtCore.QRect(220, 90, 81, 32))
        self.returnRemove_2.setObjectName("returnRemove_2")
        self.ModifyRemove = QtWidgets.QPushButton(self.frame_3)
        self.ModifyRemove.setGeometry(QtCore.QRect(150, 90, 81, 32))
        self.ModifyRemove.setObjectName("ModifyRemove")
        self.RABCB = QtWidgets.QTextEdit(self.frame_3)
        self.RABCB.setGeometry(QtCore.QRect(10, 60, 51, 31))
        self.RABCB.setObjectName("RABCB")
        self.label_21 = QtWidgets.QLabel(self.frame_3)
        self.label_21.setGeometry(QtCore.QRect(10, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_3)
        self.label_22.setGeometry(QtCore.QRect(70, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setWordWrap(True)
        self.label_22.setObjectName("label_22")
        self.RABOB = QtWidgets.QTextEdit(self.frame_3)
        self.RABOB.setGeometry(QtCore.QRect(70, 60, 51, 31))
        self.RABOB.setObjectName("RABOB")
        self.label_23 = QtWidgets.QLabel(self.frame_3)
        self.label_23.setGeometry(QtCore.QRect(130, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.RAGS = QtWidgets.QTextEdit(self.frame_3)
        self.RAGS.setGeometry(QtCore.QRect(130, 60, 51, 31))
        self.RAGS.setObjectName("RAGS")
        self.label_24 = QtWidgets.QLabel(self.frame_3)
        self.label_24.setGeometry(QtCore.QRect(185, 10, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.RADB = QtWidgets.QTextEdit(self.frame_3)
        self.RADB.setGeometry(QtCore.QRect(190, 60, 51, 31))
        self.RADB.setObjectName("RADB")
        self.label_25 = QtWidgets.QLabel(self.frame_3)
        self.label_25.setGeometry(QtCore.QRect(245, 10, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setWordWrap(True)
        self.label_25.setObjectName("label_25")
        self.RAA = QtWidgets.QTextEdit(self.frame_3)
        self.RAA.setGeometry(QtCore.QRect(250, 60, 51, 31))
        self.RAA.setObjectName("RAA")
        self.tabWidget.addTab(self.data_tab, "")
        self.contraint_tab = QtWidgets.QWidget()
        self.contraint_tab.setObjectName("contraint_tab")
        self.calculate_button = QtWidgets.QPushButton(self.contraint_tab)
        self.calculate_button.setGeometry(QtCore.QRect(400, 500, 114, 32))
        self.calculate_button.setObjectName("calculate_button")
        self.contraint_table = QtWidgets.QTableWidget(self.contraint_tab)
        self.contraint_table.setGeometry(QtCore.QRect(10, 10, 891, 411))
        self.contraint_table.setObjectName("contraint_table")
        self.contraint_table.setColumnCount(0)
        self.contraint_table.setRowCount(0)
        self.tabWidget.addTab(self.contraint_tab, "")
        self.result_tab = QtWidgets.QWidget()
        self.result_tab.setObjectName("result_tab")
        self.result_list = QtWidgets.QTableWidget(self.result_tab)
        self.result_list.setGeometry(QtCore.QRect(10, 10, 891, 411))
        self.result_list.setObjectName("result_list")
        self.result_list.setColumnCount(0)
        self.result_list.setRowCount(0)
        self.objectiveFuntion_label = QtWidgets.QLabel(self.result_tab)
        self.objectiveFuntion_label.setGeometry(QtCore.QRect(310, 440, 131, 20))
        self.objectiveFuntion_label.setAlignment(QtCore.Qt.AlignCenter)
        self.objectiveFuntion_label.setObjectName("objectiveFuntion_label")
        self.objectiveFuntion_label_2 = QtWidgets.QLabel(self.result_tab)
        self.objectiveFuntion_label_2.setGeometry(QtCore.QRect(440, 440, 101, 20))
        self.objectiveFuntion_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.objectiveFuntion_label_2.setObjectName("objectiveFuntion_label_2")
        self.tabWidget.addTab(self.result_tab, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 915, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFiles = QtWidgets.QMenu(self.menuBar)
        self.menuFiles.setObjectName("menuFiles")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionAdd_Excel_file = QtWidgets.QAction(MainWindow)
        self.actionAdd_Excel_file.setObjectName("actionAdd_Excel_file")
        self.menuFiles.addAction(self.actionAdd_Excel_file)
        self.menuBar.addAction(self.menuFiles.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.return_label.setText(_translate("MainWindow", "Return"))
        self.liquidity_label.setText(_translate("MainWindow", "Liquidity"))
        self.cost_label.setText(_translate("MainWindow", "Cost"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.liquidityAdd.setText(_translate("MainWindow", "Add"))
        self.liquidityRemove.setText(_translate("MainWindow", "Remove"))
        self.liquidityModify.setText(_translate("MainWindow", "Modify"))
        self.label.setText(_translate("MainWindow", "LDD \n"
"Demand Deposit"))
        self.label_2.setText(_translate("MainWindow", "LSD \n"
"Saving Deposit"))
        self.label_3.setText(_translate("MainWindow", "LTD \n"
"Term Deposit"))
        self.costAdd.setText(_translate("MainWindow", "Add"))
        self.costRemove.setText(_translate("MainWindow", "Remove"))
        self.costModify.setText(_translate("MainWindow", "Modify"))
        self.label_10.setText(_translate("MainWindow", "CLDD \n"
"Demand Deposit"))
        self.label_11.setText(_translate("MainWindow", "CLSD \n"
"Saving Deposit"))
        self.label_12.setText(_translate("MainWindow", "CLTD \n"
"Term Deposit"))
        self.label_19.setText(_translate("MainWindow", "Borrowing\n"
"CLB"))
        self.returnAdd.setText(_translate("MainWindow", "Add"))
        self.returnRemove_2.setText(_translate("MainWindow", "Remove"))
        self.ModifyRemove.setText(_translate("MainWindow", "Modify"))
        self.label_21.setText(_translate("MainWindow", "central bank\n"
"RABCB"))
        self.label_22.setText(_translate("MainWindow", "other banks\n"
"RABOB"))
        self.label_23.setText(_translate("MainWindow", "RAGS"))
        self.label_24.setText(_translate("MainWindow", "RADB"))
        self.label_25.setText(_translate("MainWindow", "Advances \n"
"RAA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data_tab), _translate("MainWindow", "Data"))
        self.calculate_button.setText(_translate("MainWindow", "Calculate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contraint_tab), _translate("MainWindow", "Constraints"))
        self.objectiveFuntion_label.setText(_translate("MainWindow", "Objective Function: "))
        self.objectiveFuntion_label_2.setText(_translate("MainWindow", "Number"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.result_tab), _translate("MainWindow", "Result"))
        self.menuFiles.setTitle(_translate("MainWindow", "File"))
        self.actionAdd_Excel_file.setText(_translate("MainWindow", "Add Excel file"))

