# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs/Settings.ui'
#
# Created: Thu Nov  3 19:04:38 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.resize(564, 487)
        self.verticalLayout = QtGui.QVBoxLayout(Settings)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Settings)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.variableTable = QtGui.QTableWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.variableTable.sizePolicy().hasHeightForWidth())
        self.variableTable.setSizePolicy(sizePolicy)
        self.variableTable.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.variableTable.setRowCount(0)
        self.variableTable.setObjectName(_fromUtf8("variableTable"))
        self.variableTable.setColumnCount(2)
        self.variableTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.variableTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.variableTable.setHorizontalHeaderItem(1, item)
        self.variableTable.horizontalHeader().setCascadingSectionResizes(False)
        self.variableTable.horizontalHeader().setDefaultSectionSize(130)
        self.variableTable.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.variableTable, 0, 0, 3, 1)
        self.addButton = QtGui.QPushButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
        self.removeButton = QtGui.QPushButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeButton.setIcon(icon1)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.gridLayout.addWidget(self.removeButton, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Settings)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.pollingIntervalSpinbox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.pollingIntervalSpinbox.setSuffix(_fromUtf8(" sec"))
        self.pollingIntervalSpinbox.setMinimum(0.5)
        self.pollingIntervalSpinbox.setMaximum(5000000.0)
        self.pollingIntervalSpinbox.setSingleStep(0.5)
        self.pollingIntervalSpinbox.setObjectName(_fromUtf8("pollingIntervalSpinbox"))
        self.gridLayout_2.addWidget(self.pollingIntervalSpinbox, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.sleepTimeSpinbox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.sleepTimeSpinbox.setSuffix(_fromUtf8(" sec"))
        self.sleepTimeSpinbox.setMinimum(0.0)
        self.sleepTimeSpinbox.setMaximum(5.0)
        self.sleepTimeSpinbox.setSingleStep(0.1)
        self.sleepTimeSpinbox.setProperty(_fromUtf8("value"), 0.5)
        self.sleepTimeSpinbox.setObjectName(_fromUtf8("sleepTimeSpinbox"))
        self.gridLayout_2.addWidget(self.sleepTimeSpinbox, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.line_2 = QtGui.QFrame(Settings)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.helpTabWidget = QtGui.QTabWidget(Settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpTabWidget.sizePolicy().hasHeightForWidth())
        self.helpTabWidget.setSizePolicy(sizePolicy)
        self.helpTabWidget.setMinimumSize(QtCore.QSize(0, 110))
        self.helpTabWidget.setObjectName(_fromUtf8("helpTabWidget"))
        self.help = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help.sizePolicy().hasHeightForWidth())
        self.help.setSizePolicy(sizePolicy)
        self.help.setObjectName(_fromUtf8("help"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.help)
        self.verticalLayout_4.setMargin(10)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(self.help)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpTabWidget.addTab(self.help, icon2, _fromUtf8(""))
        self.tab_1 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_1.sizePolicy().hasHeightForWidth())
        self.tab_1.setSizePolicy(sizePolicy)
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_1)
        self.verticalLayout_5.setMargin(10)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_5 = QtGui.QLabel(self.tab_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.helpTabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.verticalLayout.addWidget(self.helpTabWidget)

        self.retranslateUi(Settings)
        self.helpTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QtGui.QApplication.translate("Settings", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Settings", "Environment Variables", None, QtGui.QApplication.UnicodeUTF8))
        self.variableTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Settings", "Variable name", None, QtGui.QApplication.UnicodeUTF8))
        self.variableTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Settings", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("Settings", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setText(QtGui.QApplication.translate("Settings", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Settings", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Settings", "Polling interval:", None, QtGui.QApplication.UnicodeUTF8))
        self.pollingIntervalSpinbox.setToolTip(QtGui.QApplication.translate("Settings", "Update service status every x seconds.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Settings", "Append sleep to start/stop command:", None, QtGui.QApplication.UnicodeUTF8))
        self.sleepTimeSpinbox.setToolTip(QtGui.QApplication.translate("Settings", "Wait x seconds after execution of start/stop commands before rechecking service status.\n"
"If the status immediatly flashes back to inactive when starting a service, increase this value.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Settings", "These settings influence behavior of the start stop commands. Use environment\n"
"variables to customize paths and tools.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Settings", "Environment variables are available in start/stop commands. Default variables are\n"
"$SUDO for the sudo command to use (e.g. kdesudo or gksudo) and $INITDIR for\n"
"the path to your init-scripts (usually /etc/init.d).", None, QtGui.QApplication.UnicodeUTF8))
        self.helpTabWidget.setTabText(self.helpTabWidget.indexOf(self.tab_1), QtGui.QApplication.translate("Settings", "environment variables", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
