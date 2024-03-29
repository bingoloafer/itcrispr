# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../ui/mainwindow.ui'
#
# Created: Fri Sep 28 14:49:44 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(589, 383)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.keyLabel = QtGui.QLabel(self.groupBox)
        self.keyLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.keyLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.keyLabel.setLineWidth(0)
        self.keyLabel.setText(_fromUtf8(""))
        self.keyLabel.setObjectName(_fromUtf8("keyLabel"))
        self.horizontalLayout_2.addWidget(self.keyLabel)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_2.addWidget(self.line)
        self.label_2 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.experLabel = QtGui.QLabel(self.groupBox)
        self.experLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.experLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.experLabel.setLineWidth(0)
        self.experLabel.setText(_fromUtf8(""))
        self.experLabel.setObjectName(_fromUtf8("experLabel"))
        self.horizontalLayout_2.addWidget(self.experLabel)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.exportButton = QtGui.QPushButton(self.groupBox)
        self.exportButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/document-export-table.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportButton.setIcon(icon1)
        self.exportButton.setDefault(False)
        self.exportButton.setFlat(False)
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.horizontalLayout_5.addWidget(self.exportButton)
        self.horizontalLayout_6.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.hintLabel = QtGui.QLabel(self.centralwidget)
        self.hintLabel.setStyleSheet(_fromUtf8("QLabel{\n"
"    background-color: rgb(255, 255, 0);\n"
"    border-radius: 3px;\n"
"    padding: 2px;\n"
"}"))
        self.hintLabel.setObjectName(_fromUtf8("hintLabel"))
        self.horizontalLayout_3.addWidget(self.hintLabel)
        self.hintText = QtGui.QLabel(self.centralwidget)
        self.hintText.setObjectName(_fromUtf8("hintText"))
        self.horizontalLayout_3.addWidget(self.hintText)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.selectAllButton = QtGui.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit-select-all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectAllButton.setIcon(icon2)
        self.selectAllButton.setObjectName(_fromUtf8("selectAllButton"))
        self.horizontalLayout_3.addWidget(self.selectAllButton)
        self.selectNoneButton = QtGui.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit-clear-list.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectNoneButton.setIcon(icon3)
        self.selectNoneButton.setObjectName(_fromUtf8("selectNoneButton"))
        self.horizontalLayout_3.addWidget(self.selectNoneButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet(_fromUtf8(" QListWidget::item {\n"
"     padding: 5px;\n"
" }\n"
"\n"
"QListWidget {\n"
"     show-decoration-selected: 0; \n"
" }\n"
"\n"
" QListWidget::item:selected {\n"
"   /* background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);*/\n"
"   color: #000;\n"
"    background-color: #bfd9ff;\n"
" }\n"
"\n"
""))
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.recalculateButton = QtGui.QPushButton(self.groupBox_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/task-recurring.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recalculateButton.setIcon(icon4)
        self.recalculateButton.setObjectName(_fromUtf8("recalculateButton"))
        self.horizontalLayout.addWidget(self.recalculateButton)
        self.finishedButton = QtGui.QPushButton(self.groupBox_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/task-complete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.finishedButton.setIcon(icon5)
        self.finishedButton.setObjectName(_fromUtf8("finishedButton"))
        self.horizontalLayout.addWidget(self.finishedButton)
        self.unfinishedButton = QtGui.QPushButton(self.groupBox_2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/task-ongoing.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unfinishedButton.setIcon(icon6)
        self.unfinishedButton.setObjectName(_fromUtf8("unfinishedButton"))
        self.horizontalLayout.addWidget(self.unfinishedButton)
        self.line_2 = QtGui.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        self.skipButton = QtGui.QPushButton(self.groupBox_2)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow-right-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.skipButton.setIcon(icon7)
        self.skipButton.setObjectName(_fromUtf8("skipButton"))
        self.horizontalLayout.addWidget(self.skipButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.stopButton = QtGui.QPushButton(self.groupBox_2)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/application-exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon8)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout.addWidget(self.stopButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.selectAllButton, self.selectNoneButton)
        MainWindow.setTabOrder(self.selectNoneButton, self.listWidget)
        MainWindow.setTabOrder(self.listWidget, self.recalculateButton)
        MainWindow.setTabOrder(self.recalculateButton, self.finishedButton)
        MainWindow.setTabOrder(self.finishedButton, self.unfinishedButton)
        MainWindow.setTabOrder(self.unfinishedButton, self.skipButton)
        MainWindow.setTabOrder(self.skipButton, self.stopButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Iterate CRISPR", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Key: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Experiment: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Export Database", None, QtGui.QApplication.UnicodeUTF8))
        self.exportButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Export entire traces database (CSV format)", None, QtGui.QApplication.UnicodeUTF8))
        self.hintLabel.setText(QtGui.QApplication.translate("MainWindow", "Hint:", None, QtGui.QApplication.UnicodeUTF8))
        self.hintText.setText(QtGui.QApplication.translate("MainWindow", "Double click primer to select in assembler", None, QtGui.QApplication.UnicodeUTF8))
        self.selectAllButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Select all primers", None, QtGui.QApplication.UnicodeUTF8))
        self.selectAllButton.setText(QtGui.QApplication.translate("MainWindow", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.selectNoneButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Clear Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.selectNoneButton.setText(QtGui.QApplication.translate("MainWindow", "Select None", None, QtGui.QApplication.UnicodeUTF8))
        self.recalculateButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Redo the assembly", None, QtGui.QApplication.UnicodeUTF8))
        self.recalculateButton.setText(QtGui.QApplication.translate("MainWindow", "Recalculate", None, QtGui.QApplication.UnicodeUTF8))
        self.finishedButton.setText(QtGui.QApplication.translate("MainWindow", "Save as Finished", None, QtGui.QApplication.UnicodeUTF8))
        self.unfinishedButton.setText(QtGui.QApplication.translate("MainWindow", "Save as Unfinished", None, QtGui.QApplication.UnicodeUTF8))
        self.skipButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Skip this entry", None, QtGui.QApplication.UnicodeUTF8))
        self.skipButton.setText(QtGui.QApplication.translate("MainWindow", "Skip", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Stop the program", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
