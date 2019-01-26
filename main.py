# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QFileDialog, QAbstractItemView
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from PyQt5.QtGui import QFileDialog
import pandas as pd 
import numpy as np
import evaluation
import _thread
import time
import datetime
from final import DEAP
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        ##DATA
        
        self.Liquidity = pd.DataFrame(columns=['bucket', 'LDD','LSD','LTD','LB'])
        self.Liquidity['bucket'] = self.Liquidity['bucket'].astype(int)
        self.Liquidity.set_index('bucket')
        self.Cost = pd.DataFrame(columns=['bucket', 'CLDD','CLSD','CLTD','CLB'])
        self.Cost.bucket.astype(int)
        self.Cost.set_index('bucket')
        self.Return = pd.DataFrame(columns=['bucket', 'RABCB','RABOB','RAGS','RADB','RAA'])
        self.Return.bucket.astype(int)
        self.Return.set_index('bucket')

        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        # self.MainWindow.showMaximized()
        MainWindow.resize(1448,800)
        self.width = self.MainWindow.width()
        self.height = self.MainWindow.height()
        self.MainWindow.setFixedSize(self.width, self.height)
        
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, self.width, self.height))
        self.tabWidget.setObjectName("tabWidget")
        self.data_tab = QtWidgets.QWidget()
        self.data_tab.setObjectName("data_tab")

        #DATA LABEL
        #Label Geometry 
        # X =((self.width/3)*l)-((self.width/3)/2)
        #List Geometry (padding 10)
        # X =((self.width/3)*(l-1))+10
        #Width =(self.width/3)-20
        self.return_label = QtWidgets.QLabel(self.data_tab)
        self.return_label.setGeometry(QtCore.QRect(((self.width/3)*3)-((self.width/3)/2)-59/2, 20, 59, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.return_label.setFont(font)
        self.return_label.setAlignment(QtCore.Qt.AlignCenter)
        self.return_label.setObjectName("return_label")
        self.liquidity_label = QtWidgets.QLabel(self.data_tab)
        self.liquidity_label.setGeometry(QtCore.QRect(((self.width/3)*1)-((self.width/3)/2)-59/2, 20, 59, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.liquidity_label.setFont(font)
        self.liquidity_label.setObjectName("liquidity_label")

        ##Liquidity List
        self.liquidity_list = QtWidgets.QTableWidget(8,3,self.data_tab)
        self.liquidity_list.setColumnCount(5)
        self.liquidity_list.setRowCount(0)
        self.liquidity_list.setGeometry(QtCore.QRect(((self.width/3)*(1-1))+10, 40, (self.width/3)-20, 321))
        self.liquidity_list.setObjectName("liquidity_list")
        self.liquidity_list.setHorizontalHeaderLabels(['Bucket','LDD','LSD','LTD','LB'])
        self.liquidity_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.liquidity_list.clicked.connect(self.rowClick)
        header = self.liquidity_list.horizontalHeader()
        for col in range(0,self.liquidity_list.columnCount()):
            header.setSectionResizeMode(int(col), QtWidgets.QHeaderView.Stretch)
        self.liquidity_list.verticalHeader().setVisible(False)
        self.liquidity_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cost_label = QtWidgets.QLabel(self.data_tab)
        self.cost_label.setGeometry(QtCore.QRect(((self.width/3)*2)-((self.width/3)/2)-59/2, 20, 59, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cost_label.setFont(font)
        self.cost_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cost_label.setObjectName("cost_label")
        self.next_button = QtWidgets.QPushButton(self.data_tab)
        self.next_button.setGeometry(QtCore.QRect(self.width/2-114/2, 590, 114, 32))
        self.next_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.next_button.setAutoFillBackground(False)
        self.next_button.setObjectName("next_button")
        self.next_button.clicked.connect(self.nextTab)
        self.next_button.setEnabled(False)

        #Need add excel file status
        self.status_label = QtWidgets.QLabel(self.data_tab)
        self.status_label.setGeometry(QtCore.QRect(((self.width/3)*2)-((self.width/3)/2)-59/2-60, 530, 200, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.status_label.setFont(font)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName("status_label")
        # Cost List
        self.cost_list = QtWidgets.QTableWidget(8,5,self.data_tab)
        self.cost_list.setGeometry(QtCore.QRect(((self.width/3)*(2-1))+10, 40, (self.width/3)-20, 321))
        self.cost_list.setObjectName("cost_list")
        self.cost_list.setColumnCount(5)
        self.cost_list.setRowCount(0)
        self.cost_list.setHorizontalHeaderLabels(['Bucket','CLDD','CLSD','CLTD','CLB'])
        self.cost_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cost_list.clicked.connect(self.rowClick)
        self.cost_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        header = self.cost_list.horizontalHeader()
        for col in range(0,self.cost_list.columnCount()):
            header.setSectionResizeMode(int(col), QtWidgets.QHeaderView.Stretch)
        self.cost_list.verticalHeader().setVisible(False)
        # Return List
        self.return_list = QtWidgets.QTableWidget(8,6,self.data_tab)
        self.return_list.setGeometry(QtCore.QRect(((self.width/3)*(3-1))+10, 40, (self.width/3)-20, 321))
        self.return_list.setObjectName("return_list")
        self.return_list.setColumnCount(6)
        self.return_list.setRowCount(0)
        self.return_list.setHorizontalHeaderLabels(['Bucket','RABCB','RABOB','RAGS','RADB','RAA'])
        self.return_list.clicked.connect(self.rowClick)
        self.return_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.return_list.verticalHeader().setVisible(False)
        self.return_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        header = self.return_list.horizontalHeader()
        for col in range(0,self.return_list.columnCount()):
            header.setSectionResizeMode(int(col), QtWidgets.QHeaderView.Stretch)

        #Frame Size
        frameWidth = (self.width/3)-20
        frameHeight = 121
        
        #Liquidity Frame
        #Text edit geometry
        #Padding 5
        #Budget X: 5
        #Other: (((frameWidth - (5+21))/4)*(1-1))+31
        #Text edit size
        #Bugdet:21
        #Other: ((frameWidth - (5+21))/4)-10
        self.frame = QtWidgets.QFrame(self.data_tab)
        self.frame.setGeometry(QtCore.QRect((self.width/3)*(1-1)+10, 370, (self.width/3)-20, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.liquidityAdd = QtWidgets.QPushButton(self.frame)
        self.liquidityAdd.setGeometry(QtCore.QRect(30, 90, 80, 32))
        self.liquidityAdd.setObjectName("liquidityAdd")
        self.liquidityAdd.clicked.connect(self.addRow)
        self.liquidityAdd.setEnabled(False)
        # self.liquidityRemove = QtWidgets.QPushButton(self.frame)
        # self.liquidityRemove.setGeometry(QtCore.QRect(170, 90, 81, 32))
        # self.liquidityRemove.setObjectName("liquidityRemove")
        # self.liquidityRemove.clicked.connect(self.removeRow)
        self.liquidityModify = QtWidgets.QPushButton(self.frame)
        self.liquidityModify.setGeometry(QtCore.QRect(100, 90, 81, 32))
        self.liquidityModify.setObjectName("liquidityModify")
        self.liquidityModify.clicked.connect(self.modifyRow)
        self.liquidityModify.setEnabled(False)
        self.Lbudget = QtWidgets.QTextEdit(self.frame)
        self.Lbudget.setGeometry(QtCore.QRect(5, 60, 21, 31))
        self.Lbudget.setObjectName("Bucket")
        self.LDD = QtWidgets.QTextEdit(self.frame)
        self.LDD.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(1-1))+31, 60, ((frameWidth - (5+21))/4)-10, 31))
        self.LDD.setObjectName("LDD")
        self.LSD = QtWidgets.QTextEdit(self.frame)
        self.LSD.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(2-1))+31, 60, ((frameWidth - (5+21))/4)-10, 31))
        self.LSD.setObjectName("LSD")
        self.LTD = QtWidgets.QTextEdit(self.frame)
        self.LTD.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(3-1))+31, 60, ((frameWidth - (5+21))/4)-10, 31))
        self.LTD.setObjectName("LTD")
        self.LB = QtWidgets.QTextEdit(self.frame)
        self.LB.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(4-1))+31, 60, ((frameWidth - (5+21))/4)-10, 31))
        self.LB.setObjectName("LB")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(1-1))+31, 10, ((frameWidth - (5+21))/4)-10, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(2-1))+31, 10, ((frameWidth - (5+21))/4)-10, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(3-1))+31, 10, ((frameWidth - (5+21))/4)-10, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        
        self.LB_label = QtWidgets.QLabel(self.frame)
        self.LB_label.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(4-1))+31, 10, ((frameWidth - (5+21))/4)-10, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LB_label.setFont(font)
        self.LB_label.setAlignment(QtCore.Qt.AlignCenter)
        self.LB_label.setWordWrap(True)
        self.LB_label.setObjectName("LB_label")
        
        #Cost frame
        #Text edit geometry
        #Padding 5
        #Budget X: 5
        #Other: (((frameWidth - (5+21))/4)*(1-1))+31
        #Text edit size
        #Bugdet:21
        #Other: ((frameWidth - (5+21))/4)-10
        self.frame_2 = QtWidgets.QFrame(self.data_tab)
        self.frame_2.setGeometry(QtCore.QRect((self.width/3)*(2-1)+10, 370, (self.width/3)-20, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Cbudget = QtWidgets.QTextEdit(self.frame_2)
        self.Cbudget.setGeometry(QtCore.QRect(5, 60, 21, 31))
        self.Cbudget.setObjectName("Bucket")
        self.costAdd = QtWidgets.QPushButton(self.frame_2)
        self.costAdd.setGeometry(QtCore.QRect(30, 90, 80, 32))
        self.costAdd.setObjectName("costAdd")
        self.costAdd.clicked.connect(self.addRow)
        self.costAdd.setEnabled(False)
        # self.costRemove = QtWidgets.QPushButton(self.frame_2)
        # self.costRemove.setGeometry(QtCore.QRect(170, 90, 81, 32))
        # self.costRemove.setObjectName("costRemove")
        # self.costRemove.clicked.connect(self.removeRow)
        self.costModify = QtWidgets.QPushButton(self.frame_2)
        self.costModify.setGeometry(QtCore.QRect(100, 90, 81, 32))
        self.costModify.setObjectName("costModify")
        self.costModify.clicked.connect(self.modifyRow)
        self.costModify.setEnabled(False)
        self.CLDD = QtWidgets.QTextEdit(self.frame_2)
        self.CLDD.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(1-1))+31, 60, ((frameWidth - (5+21))/4)-10, 31))
        self.CLDD.setObjectName("CLDD")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(1-1))+31, 10, ((frameWidth - (5+21))/4)-10, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(2-1))+31, 10, ((frameWidth - (5+21))/4)-10, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.CLSD = QtWidgets.QTextEdit(self.frame_2)
        self.CLSD.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(2-1))+31, 60, ((frameWidth - (5+21))/4)-10, 31))
        self.CLSD.setObjectName("CLSD")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(3-1))+31, 10, ((frameWidth - (5+21))/4)-10, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.CLTD = QtWidgets.QTextEdit(self.frame_2)
        self.CLTD.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(3-1))+31, 60, ((frameWidth - (5+21))/4)-10, 31))
        self.CLTD.setObjectName("CLTD")
        self.label_19 = QtWidgets.QLabel(self.frame_2)
        self.label_19.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(4-1))+31, 10, ((frameWidth - (5+21))/4)-10, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName("label_19")
        self.CLB = QtWidgets.QTextEdit(self.frame_2)
        self.CLB.setGeometry(QtCore.QRect((((frameWidth - (5+21))/4)*(4-1))+31, 60, ((frameWidth - (5+21))/4)-10, 31))
        self.CLB.setObjectName("CLB")

        #Return frame
        #Text edit geometry
        #Padding 5
        #Budget X: 5
        #Other: (((frameWidth - (5+21))/5)*(1-1))+31
        #Text edit size
        #Bugdet:21
        #Other: ((frameWidth - (5+21))/5)-10
        self.frame_3 = QtWidgets.QFrame(self.data_tab)
        self.frame_3.setGeometry(QtCore.QRect((self.width/3)*(3-1)+10, 370, (self.width/3)-20, 121))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.returnAdd = QtWidgets.QPushButton(self.frame_3)
        self.returnAdd.setGeometry(QtCore.QRect(80, 90, 80, 32))
        self.returnAdd.setObjectName("returnAdd")
        self.returnAdd.clicked.connect(self.addRow)
        self.returnAdd.setEnabled(False)
        # self.returnRemove = QtWidgets.QPushButton(self.frame_3)
        # self.returnRemove.setGeometry(QtCore.QRect(220, 90, 81, 32))
        # self.returnRemove.setObjectName("returnRemove")
        # self.returnRemove.clicked.connect(self.removeRow)
        self.returnModify = QtWidgets.QPushButton(self.frame_3)
        self.returnModify.setGeometry(QtCore.QRect(150, 90, 81, 32))
        self.returnModify.setObjectName("returnModify")
        self.returnModify.clicked.connect(self.modifyRow)
        self.returnModify.setEnabled(False)
        self.Rbudget = QtWidgets.QTextEdit(self.frame_3)
        self.Rbudget.setGeometry(QtCore.QRect(5, 60, 21, 31))
        self.Rbudget.setObjectName("Bucket")
        self.RABCB = QtWidgets.QTextEdit(self.frame_3)
        self.RABCB.setGeometry(QtCore.QRect((((frameWidth - (5+21))/5)*(1-1))+31, 60, ((frameWidth - (5+21))/5)-10, 31))
        self.RABCB.setObjectName("RABCB")
        self.label_21 = QtWidgets.QLabel(self.frame_3)
        self.label_21.setGeometry(QtCore.QRect((((frameWidth - (5+21))/5)*(1-1))+31, 10, ((frameWidth - (5+21))/5)-10, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_3)
        self.label_22.setGeometry(QtCore.QRect((((frameWidth - (5+21))/5)*(2-1))+31, 10, ((frameWidth - (5+21))/5)-10, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setWordWrap(True)
        self.label_22.setObjectName("label_22")
        self.RABOB = QtWidgets.QTextEdit(self.frame_3)
        self.RABOB.setGeometry(QtCore.QRect((((frameWidth - (5+21))/5)*(2-1))+31, 60, ((frameWidth - (5+21))/5)-10, 31))
        self.RABOB.setObjectName("RABOB")
        self.label_23 = QtWidgets.QLabel(self.frame_3)
        self.label_23.setGeometry(QtCore.QRect((((frameWidth - (5+21))/5)*(3-1))+31, 10, ((frameWidth - (5+21))/5)-10, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.RAGS = QtWidgets.QTextEdit(self.frame_3)
        self.RAGS.setGeometry(QtCore.QRect((((frameWidth - (5+21))/5)*(3-1))+31, 60, ((frameWidth - (5+21))/5)-10, 31))
        self.RAGS.setObjectName("RAGS")
        self.label_24 = QtWidgets.QLabel(self.frame_3)
        self.label_24.setGeometry(QtCore.QRect((((frameWidth - (5+21))/5)*(4-1))+31, 10, ((frameWidth - (5+21))/5)-10, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.RADB = QtWidgets.QTextEdit(self.frame_3)
        self.RADB.setGeometry(QtCore.QRect((((frameWidth - (5+21))/5)*(4-1))+31, 60, ((frameWidth - (5+21))/5)-10, 31))
        self.RADB.setObjectName("RADB")
        self.label_25 = QtWidgets.QLabel(self.frame_3)
        self.label_25.setGeometry(QtCore.QRect((((frameWidth - (5+21))/5)*(5-1))+31, 10, ((frameWidth - (5+21))/5)-10, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setWordWrap(True)
        self.label_25.setObjectName("label_25")
        self.RAA = QtWidgets.QTextEdit(self.frame_3)
        self.RAA.setGeometry(QtCore.QRect((((frameWidth - (5+21))/5)*(5-1))+31, 60, ((frameWidth - (5+21))/5)-10, 31))
        self.RAA.setObjectName("RAA")
        self.tabWidget.addTab(self.data_tab, "")
        # self.contraint_tab = QtWidgets.QWidget()
        # self.contraint_tab.setObjectName("contraint_tab")
        # self.calculate_button = QtWidgets.QPushButton(self.contraint_tab)
        # self.calculate_button.setGeometry(QtCore.QRect(400, 500, 114, 32))
        # self.calculate_button.setObjectName("calculate_button")
        # self.calculate_button.clicked.connect(self.calculate)
        # self.contraint_table = QtWidgets.QTableWidget(self.contraint_tab)
        # self.contraint_table.setGeometry(QtCore.QRect(10, 10, 891, 411))
        # self.contraint_table.setObjectName("contraint_table")
        # self.contraint_table.setColumnCount(0)
        # self.contraint_table.setRowCount(0)
        # self.tabWidget.addTab(self.contraint_tab, "")
        self.result_tab = QtWidgets.QWidget()
        self.result_tab.setObjectName("result_tab")

        self.result_printOut  = QtWidgets.QTextEdit(self.result_tab)
        # self.result_printOut.setGeometry(QtCore.QRect(((self.width/3)*(3-1))+10, 40, (self.width/3)-20, 321))
        self.result_printOut.setGeometry(QtCore.QRect(10, 10, (self.width-20)/4, 411))
        self.result_printOut.moveCursor(QtGui.QTextCursor.Start)
        self.result_printOut.ensureCursorVisible()
        self.result_printOut.setLineWrapColumnOrWidth((self.width-20)/4)
        self.result_printOut.setLineWrapMode(int((self.width-20)/4))
        
        self.result_printOut.setObjectName("result_printOut")

        # Cost List
        self.result_list = QtWidgets.QTableWidget(8,7,self.result_tab)
        self.result_list.setGeometry(QtCore.QRect((self.width-20)/4+20, 10, (self.width-20)/4*3-10, 411))
        self.result_list.setObjectName("result_list")
        self.result_list.setColumnCount(7)
        self.result_list.setRowCount(0)
        self.result_list.setHorizontalHeaderLabels(['Bucket','Borrowings\nLB','Balance with\nCentral Bank\nABCB','Balance with\nother banks\nABOB','Invest. in\ngovernment and sec.\nAGS','Investment in\ndebentures and bonds\nADB','Advances\nAA'])
        self.result_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.result_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.result_list.clicked.connect(self.rowClick)
        header = self.result_list.horizontalHeader()
        header.setSectionResizeMode(int(0), QtWidgets.QHeaderView.ResizeToContents)
        for col in range(1,self.result_list.columnCount()):
            header.setSectionResizeMode(int(col), QtWidgets.QHeaderView.Stretch)
        self.result_list.verticalHeader().setVisible(False)
        self.timer_label = QtWidgets.QLabel(self.result_tab)
        self.timer_label.setGeometry(QtCore.QRect(310, 440, 200, 20))
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_label.setObjectName("timer_label")

        self.objectiveFuntion_label = QtWidgets.QLabel(self.result_tab)
        self.objectiveFuntion_label.setGeometry(QtCore.QRect(310, 480, 131, 20))
        self.objectiveFuntion_label.setAlignment(QtCore.Qt.AlignCenter)
        self.objectiveFuntion_label.setObjectName("objectiveFuntion_label")
        self.objectiveFuntion_label_2 = QtWidgets.QLabel(self.result_tab)
        self.objectiveFuntion_label_2.setGeometry(QtCore.QRect(440, 480, 200, 20))
        self.objectiveFuntion_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.objectiveFuntion_label_2.setObjectName("objectiveFuntion_label_2")

        self.satisfiedConstraint_label = QtWidgets.QLabel(self.result_tab)
        self.satisfiedConstraint_label.setGeometry(QtCore.QRect(245, 520, 200, 20))
        self.satisfiedConstraint_label.setAlignment(QtCore.Qt.AlignCenter)
        self.satisfiedConstraint_label.setObjectName("satisfiedConstraint_label")
        self.satisfiedConstraint_label2 = QtWidgets.QLabel(self.result_tab)
        self.satisfiedConstraint_label2.setGeometry(QtCore.QRect(440, 520, 200, 20))
        self.satisfiedConstraint_label2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.satisfiedConstraint_label2.setObjectName("satisfiedConstraint_label")

        self.tabWidget.addTab(self.result_tab, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 915, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFiles = QtWidgets.QMenu(self.menuBar)
        self.menuFiles.setObjectName("menuFiles")
        # self.menuFiles.triggered.connect(self.browseFile)
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionAdd_Excel_file = QtWidgets.QAction(MainWindow)
        self.actionAdd_Excel_file.setObjectName("actionAdd_Excel_file")
        self.actionAdd_Excel_file.triggered.connect(self.browseFile)
        self.menuFiles.addAction(self.actionAdd_Excel_file)
        self.menuBar.addAction(self.menuFiles.menuAction())

        self.GenerationField = QtWidgets.QTextEdit(self.data_tab)
        self.GenerationField.setGeometry(QtCore.QRect(((self.width/3)*(2-1))+10+100, 550, 50, 25))
        self.GenerationField.setObjectName("GenerationField")
        self.GenerationLabel = QtWidgets.QLabel(self.data_tab)
        self.GenerationLabel.setGeometry(QtCore.QRect(((self.width/3)*(2-1))+10-70+100, 550, 70, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GenerationLabel.setFont(font)
        self.GenerationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GenerationLabel.setWordWrap(True)
        self.GenerationLabel.setObjectName("GenerationLabel")

        self.PopulationField = QtWidgets.QTextEdit(self.data_tab)
        self.PopulationField.setGeometry(QtCore.QRect(((self.width/3)*(2-1))+10+140+100, 550, 50, 25))
        self.PopulationField.setObjectName("PopulationField")
        self.PopulationLabel = QtWidgets.QLabel(self.data_tab)
        self.PopulationLabel.setGeometry(QtCore.QRect(((self.width/3)*(2-1))+10+70+100, 550, 70, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.PopulationLabel.setFont(font)
        self.PopulationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PopulationLabel.setWordWrap(True)
        self.PopulationLabel.setObjectName("GenerationLabel")


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.return_label.setText(_translate("MainWindow", "Return"))
        self.liquidity_label.setText(_translate("MainWindow", "Liquidity"))
        self.cost_label.setText(_translate("MainWindow", "Cost"))
        self.status_label.setText(_translate("MainWindow", "You need to add an excel file"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.liquidityAdd.setText(_translate("MainWindow", "Change"))
        # self.liquidityRemove.setText(_translate("MainWindow", "Remove"))
        self.liquidityModify.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", "LDD \n"
"Demand Deposit"))
        self.label_2.setText(_translate("MainWindow", "LSD \n"
"Saving Deposit"))
        self.label_3.setText(_translate("MainWindow", "LTD \n"
"Term Deposit"))
        self.LB_label.setText(_translate("MainWindow", "LB \n"
"Borrowings"))
        self.costAdd.setText(_translate("MainWindow", "Change"))
        # self.costRemove.setText(_translate("MainWindow", "Remove"))
        self.costModify.setText(_translate("MainWindow", "Clear"))
        self.label_10.setText(_translate("MainWindow", "CLDD \n"
"Demand Deposit"))
        self.label_11.setText(_translate("MainWindow", "CLSD \n"
"Saving Deposit"))
        self.label_12.setText(_translate("MainWindow", "CLTD \n"
"Term Deposit"))
        self.label_19.setText(_translate("MainWindow", "Borrowing\n"
"CLB"))
        self.returnAdd.setText(_translate("MainWindow", "Change"))
        # self.returnRemove.setText(_translate("MainWindow", "Remove"))
        self.returnModify.setText(_translate("MainWindow", "Clear"))
        self.label_21.setText(_translate("MainWindow", "central bank\n"
"RABCB"))
        self.label_22.setText(_translate("MainWindow", "other banks\n"
"RABOB"))
        self.label_23.setText(_translate("MainWindow", "RAGS"))
        self.label_24.setText(_translate("MainWindow", "RADB"))
        self.label_25.setText(_translate("MainWindow", "Advances \n"
"RAA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data_tab), _translate("MainWindow", "Data"))
        # self.calculate_button.setText(_translate("MainWindow", "Calculate"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.contraint_tab), _translate("MainWindow", "Constraints"))
        self.objectiveFuntion_label.setText(_translate("MainWindow", "Objective Function: "))
        self.objectiveFuntion_label_2.setText(_translate("MainWindow", "Number"))

        self.satisfiedConstraint_label.setText(_translate("MainWindow", "Number of satified contraints: "))
        self.satisfiedConstraint_label2.setText(_translate("MainWindow", "Number"))

        self.timer_label.setText(_translate("MainWindow", "0:00"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.result_tab), _translate("MainWindow", "Result"))
        self.menuFiles.setTitle(_translate("MainWindow", "File"))
        self.actionAdd_Excel_file.setText(_translate("MainWindow", "Add Excel file"))

        self.GenerationLabel.setText("Generation: ")
        self.PopulationLabel.setText("Population: ")
        self.GenerationField.setText("50")
        self.PopulationField.setText("100")
        # self.GenerationField.setText("1")
        # self.PopulationField.setText("1")
        sys.stdout = Stream(newText=self.onUpdateText)
        file = open("cond.dat","w") 
        file.write("")
        file.close()
    def __del__(self):
            sys.stdout = sys.__stdout__
    def addRow(self):
        # print("Add Row")
        #Specify table
        senderBtn = self.MainWindow.sender()
        if(senderBtn == self.liquidityAdd):
            data = self.composeData(0)
            if(data!=None):
                self.Liquidity.loc[data[0]] = data
            # print("Liquidity")
            # print(self.Liquidity)
        elif(senderBtn == self.costAdd):
            data = self.composeData(1)
            if(data!=None):
                self.Cost.loc[data[0]] = data
            # print("Cost")
            # print(self.Cost)
        elif(senderBtn == self.returnAdd ):
            data = self.composeData(2)
            if(data!=None):
                self.Return.loc[data[0]] = data
            # print("Return")
            # print(self.Return)
        else:
            print("Error")
            return
        self.refreshTable()
    def addExelRow(self,table,data):
        # table
        # Liquidity = 1
        # Cost = 2
        # Return = 3
        # print(data)
        if(table==1):
            if(data!=None):
                self.Liquidity.loc[data[0]] = data
        elif (table==2):
            if(data!=None):
                self.Cost.loc[data[0]] = data
        elif(table ==3):
            if(data!=None):
                self.Return.loc[data[0]] = data
        else: 
            print("AddExcelRow errror")
            return
        self.refreshTable()
    def modifyRow(self):
        # print("Modify Row")
        #Specify table
        senderBtn = self.MainWindow.sender()
        if(senderBtn == self.liquidityAdd or senderBtn == self.liquidityModify):
            self.Lbudget.clear()
            self.LDD.clear()
            self.LSD.clear()
            self.LTD.clear()

            # print(self.Liquidity)
        elif(senderBtn == self.costAdd or senderBtn == self.costModify):
            self.Cbudget.clear()
            self.CLDD.clear()
            self.CLSD.clear()
            self.CLTD.clear()
            self.CLB.clear()
        elif(senderBtn == self.returnAdd or senderBtn == self.returnModify):
            self.Rbudget.clear()
            self.RABCB.clear()
            self.RABOB.clear()
            self.RAGS.clear()
            self.RADB.clear()
            self.RAA.clear()
        else:
            print("Error")
            return
        self.refreshTable()

    def removeRow(self):
        # print("Remove Row")
        #Specify table
        senderBtn = self.MainWindow.sender()
        if(senderBtn == self.liquidityAdd or senderBtn == self.liquidityRemove):
            b_id = self.Lbudget.toPlainText()
            # print("Liquid ")
        elif(senderBtn == self.costAdd or senderBtn == self.costRemove):
            b_id = self.Cbudget.toPlainText()
            # print("Cost")
        elif(senderBtn == self.returnAdd or senderBtn == self.returnRemove):
            b_id = self.Rbudget.toPlainText()
            # print("Return")
        else:
            print("Error")
            return
        try:
            a = int(b_id)
        except:
            self.showdialog("Budget must be in int")
            return
        b_id = [int(b_id)]
        print(b_id)
        try:
            if(senderBtn == self.liquidityAdd or senderBtn == self.liquidityRemove):
                self.Liquidity.drop(b_id,inplace=True)
                # print("Liquidity")
                # print(self.Liquidity)
            elif(senderBtn == self.costAdd or senderBtn == self.costRemove):
                self.Cost.drop(b_id,inplace=True)
                # print("Cost")
                # print("Cost")
                # print(self.Cost)
            elif(senderBtn == self.returnAdd or senderBtn == self.returnRemove):
                self.Return.drop(b_id,inplace=True)
                # print("Return")
                # print("Return")
                # print(self.Return)
        except:
            self.showdialog("Budget not found")
            return
        self.refreshTable()

    def refreshTable(self):
        tableList = [self.liquidity_list,self.cost_list, self.return_list]
        dataList = [self.Liquidity,self.Cost,self.Return]
        for i in range(0,len(tableList)):
            table = tableList[i]
            data = dataList[i]
            data = data.sort_values(by=['bucket'], ascending=True)
            #For Liquidity
            table.setRowCount(0)
            rawData = []
            for index in data.index.values:
                rowPosition = table.rowCount()
                table.insertRow(rowPosition)
                col = 0
                for colData in data.loc[ index , : ]:
                    if(col==0):
                        colData = index
                    # print(type(colData))
                    colData = str(colData)
                    table.setItem(rowPosition,col,QTableWidgetItem(colData))
                    col += 1
    def composeData(self,table):
        # #Liquidity
        data = []
        if(table==0):
            #Append data
            data.append(self.Lbudget.toPlainText())
            data.append(self.LDD.toPlainText())
            data.append(self.LSD.toPlainText())
            data.append(self.LTD.toPlainText())
            data.append("0")
        #Cost
        elif(table==1):
            #Append data
            data.append(self.Cbudget.toPlainText())
            data.append(self.CLDD.toPlainText())
            data.append(self.CLSD.toPlainText())
            data.append(self.CLTD.toPlainText())
            data.append(self.CLB.toPlainText())
        # Return
        elif(table==2):
            #Append data
            data.append(self.Rbudget.toPlainText())
            data.append(self.RABCB.toPlainText())
            data.append(self.RABOB.toPlainText())
            data.append(self.RAGS.toPlainText())
            data.append(self.RADB.toPlainText())
            data.append(self.RAA.toPlainText())
        else:
            self.showdialog("No table found")
            return
        ##Check Null
        for i in data:
            if(str(i) == ""):
                self.showdialog("Please fill all the field")
                return
            #Check is Number
            try:
                a = float(i)
            except:
                self.showdialog("Number only")
                return
        #check Budget is int
        try:
                a = int(data[0])
        except:
            self.showdialog("Bucket must be in int")
            return
        for i in range(0,len(data)):
            if(i==0):
                data[i] = int(data[i])
            else:
                data[i] = float(data[i])
        # print(data)
        return data
        
    def checkData(self,data):
        # return null if erorr
        
         ##Check Null
        for i in data:
            if(str(i) == ""):
                self.showdialog("Please fill all the field")
                return
            #Check is Number
            try:
                a = float(i)
            except:
                self.showdialog("Number only: "+i )
                return
        #check Budget is int
        try:
                a = int(data[0])
        except:
            self.showdialog("Bucket must be in int")
            return
        for i in range(0,len(data)):
            if(i==0):
                data[i] = int(data[i])
            else:
                data[i] = float(data[i])
        # print(data)
        return data
            
        # print(table)
    def showdialog(self,text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("Error")
        msg.setInformativeText(text)
        msg.setWindowTitle("Error")
        # msg.setDetailedText(detail)
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # msg.buttonClicked.connect(msgbtn)

        retval = msg.exec_()

    def nextTab(self):
        self.tabWidget.setCurrentIndex(1)
        # ]self.Liquidity = pd.DataFrame(columns=['budget', 'LDD','LSD','LTD','LB'])
        # data = pd.DataFrame(columns=['Liquidity','Cost','Return'])
        self.data['Liquidity'] = self.Liquidity
        self.data['Cost'] = self.Cost
        self.data['Return']= self.Return
        import threading
        self.counting = True
        thread = threading.Thread(target=self.startCounting)
        thread.start()
        
        self.eva = Evaluation(self.data,int(self.PopulationField.toPlainText()),int(self.GenerationField.toPlainText()))
        self.eva.finished.connect(self.finishedEva)
        self.eva.start()

        
        # print(evaluation.evalALM(individual,self.data))
    # def calculate(self):
    #     self.tabWidget.setCurrentIndex(2)
    def finishedEva(self):
        self.counting=False
        data = self.eva.hof[-1]
        self.objectiveFuntion_label_2.setText(str(data.fitness.values[0]))
        self.satisfiedConstraint_label2.setText(str(int(data.fitness.values[1]))+"/8")
        table = self.result_list

        ABCB = [None]*8
        ABOB = [None]*8
        AGS  = [None]*8
        ADB = [None]*8
        AA  = [None]*8
        LB  = [None]*8

        #ABCB[0], ABOB[0], AGS[0], ADB[0], AA[0], LB[0] = individual[0:6]
        
        start = 0 
        for i in range(8):        
            ABCB[i], ABOB[i], AGS[i], ADB[i], AA[i], LB[i] = data[start+0:start+6]
            start += 6
        #For Add to result_list table
        table.setRowCount(0)
        rawData = []
        for i in range(8):
            rowPosition = table.rowCount()
            table.insertRow(rowPosition)
            table.setItem(rowPosition,0,QTableWidgetItem(str(i+1)))
            table.setItem(rowPosition,1,QTableWidgetItem(str(LB[i])))
            table.setItem(rowPosition,2,QTableWidgetItem(str(ABCB[i])))
            table.setItem(rowPosition,3,QTableWidgetItem(str(ABOB[i])))
            table.setItem(rowPosition,4,QTableWidgetItem(str(AGS[i])))
            table.setItem(rowPosition,5,QTableWidgetItem(str(ADB[i])))
            table.setItem(rowPosition,6,QTableWidgetItem(str(AA[i])))
            
            
            
                
                


    def browseFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(MainWindow,"Open data Excel file", "","All Files (*);;Excel Files (*.xlsx)", options=options)
        if fileName:
            self.readExcel(fileName)
        # self.folderPath = QtWidgets.QFileDialog.getExistingDirectory(MainWindow, 'Select folder')
        # print(self.folderPath)
    
    def composeExcel(self,table,sheet):
        for index in sheet.index.values:
            composedData = []
            col = 0
            for colData in sheet.loc[ index , : ]:
                # print(type(colData))
                colData = str(colData)
                if(col == 0):
                    try:
                        colData = colData.replace("Bucket ","")
                        colData = int(colData)
                        # print(colData)
                    except:
                        print("Replace bucket error")
                    # print(colData)
                composedData.append(colData)
                col += 1
            if(self.checkData(composedData) is not None):
                self.addExelRow(table,composedData)
    
    def readExcel(self,filename):
        try:
            self.data = pd.read_excel(filename, None)  # Load all sheets
            #Liquidity
            self.composeExcel(1,self.data['Liquidity'])
            self.composeExcel(2,self.data['Cost'])
            self.composeExcel(3,self.data['Return'])

            self.EnableButtonAfterAddExcel(True)
        except:
            self.showdialog("Error Excel file")
            self.EnableButtonAfterAddExcel(False)
    def EnableButtonAfterAddExcel(self,command):
        #Enable button
        self.next_button.setEnabled(command)
        #Liquidity button
        self.liquidityAdd.setEnabled(command)
        self.liquidityModify.setEnabled(command)
        #Cost
        self.costAdd.setEnabled(command)
        self.costModify.setEnabled(command)
        #Return
        self.returnAdd.setEnabled(command)
        self.returnModify.setEnabled(command)
        #Turn off status
        if(command):
            self.status_label.hide()
        else:
            self.status_label.show()
    def rowClick(self,item):
        senderTlb = self.MainWindow.sender()
        budget = int(item.row())+1
        if(senderTlb == self.liquidity_list):
            # print("Liquidity list")
            data = self.Liquidity.loc[budget]
            self.Lbudget.setText(str(int(data['bucket'])))
            self.LDD.setText(str(float(data['LDD'])))
            self.LSD.setText(str(float(data['LSD'])))
            self.LTD.setText(str(float(data['LTD'])))
            self.LB.setText(str(float(data['LB'])))
        elif(senderTlb == self.cost_list):
            data = self.Cost.loc[budget]
            self.Cbudget.setText(str(int(data['bucket'])))
            self.CLB.setText(str(float(data['CLB'])))
            self.CLDD.setText(str(float(data['CLDD'])))
            self.CLSD.setText(str(float(data['CLSD'])))
            self.CLTD.setText(str(float(data['CLTD'])))
        elif(senderTlb == self.return_list):
            data = self.Return.loc[budget]
            self.Rbudget.setText(str(int(data['bucket'])))
            self.RAA.setText(str(float(data['RAA'])))
            self.RABCB.setText(str(float(data['RABCB'])))
            self.RABOB.setText(str(float(data['RABOB'])))
            self.RADB.setText(str(float(data['RADB'])))
            self.RAGS.setText(str(float(data['RAGS'])))
        # cellContent = item.data()
        # print(cellContent)  # test
        # sf = "You clicked on {0}x{1}".format(item.column(), item.row())
        # print(sf)
    def onUpdateText(self, text):
        cursor = self.result_printOut.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.result_printOut.setTextCursor(cursor)
        self.result_printOut.ensureCursorVisible()
    def startCounting(self):
        countingtime = 0
        while self.counting:
            self.timer_label.setText("Evaluation time: "+str(datetime.timedelta(seconds=countingtime)))
            time.sleep(1)
            
            countingtime+=1


   
class Stream(QtCore.QObject):
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))

class Evaluation(QThread):

    def __init__(self,data,population,generation):
        QThread.__init__(self)
        self.data = data
        self.population = population
        self.generation = generation
    def __del__(self):
        self.wait()

    def run(self):
        result = DEAP(self.data,self.population,self.generation)
        self.pop, self.stats, self.hof = result.main()
        
    
        # self.counting = False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    if app is None:
        app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())