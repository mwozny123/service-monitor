# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs/Services.ui'
#
# Created: Tue Nov  1 23:45:45 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Services(object):
    def setupUi(self, Services):
        Services.setObjectName(_fromUtf8("Services"))
        Services.resize(588, 472)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Services)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.activeServicesLabel = QtGui.QLabel(Services)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.activeServicesLabel.sizePolicy().hasHeightForWidth())
        self.activeServicesLabel.setSizePolicy(sizePolicy)
        self.activeServicesLabel.setObjectName(_fromUtf8("activeServicesLabel"))
        self.verticalLayout_2.addWidget(self.activeServicesLabel)
        self.activeServicesList = QtGui.QListWidget(Services)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.activeServicesList.sizePolicy().hasHeightForWidth())
        self.activeServicesList.setSizePolicy(sizePolicy)
        self.activeServicesList.setObjectName(_fromUtf8("activeServicesList"))
        self.verticalLayout_2.addWidget(self.activeServicesList)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.sortTopButton = QtGui.QPushButton(Services)
        self.sortTopButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow-up-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sortTopButton.setIcon(icon)
        self.sortTopButton.setFlat(False)
        self.sortTopButton.setObjectName(_fromUtf8("sortTopButton"))
        self.horizontalLayout.addWidget(self.sortTopButton)
        self.sortUpButton = QtGui.QPushButton(Services)
        self.sortUpButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow-up")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sortUpButton.setIcon(icon1)
        self.sortUpButton.setObjectName(_fromUtf8("sortUpButton"))
        self.horizontalLayout.addWidget(self.sortUpButton)
        self.sortDownButton = QtGui.QPushButton(Services)
        self.sortDownButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow-down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sortDownButton.setIcon(icon2)
        self.sortDownButton.setObjectName(_fromUtf8("sortDownButton"))
        self.horizontalLayout.addWidget(self.sortDownButton)
        self.sortBottomButton = QtGui.QPushButton(Services)
        self.sortBottomButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow-down-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sortBottomButton.setIcon(icon3)
        self.sortBottomButton.setObjectName(_fromUtf8("sortBottomButton"))
        self.horizontalLayout.addWidget(self.sortBottomButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 78, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.activateButton = QtGui.QPushButton(Services)
        self.activateButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow-left-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.activateButton.setIcon(icon4)
        self.activateButton.setObjectName(_fromUtf8("activateButton"))
        self.verticalLayout.addWidget(self.activateButton)
        self.deactivateButton = QtGui.QPushButton(Services)
        self.deactivateButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow-right-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deactivateButton.setIcon(icon5)
        self.deactivateButton.setObjectName(_fromUtf8("deactivateButton"))
        self.verticalLayout.addWidget(self.deactivateButton)
        spacerItem1 = QtGui.QSpacerItem(20, 98, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.inactiveServicesLabel = QtGui.QLabel(Services)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.inactiveServicesLabel.sizePolicy().hasHeightForWidth())
        self.inactiveServicesLabel.setSizePolicy(sizePolicy)
        self.inactiveServicesLabel.setObjectName(_fromUtf8("inactiveServicesLabel"))
        self.verticalLayout_3.addWidget(self.inactiveServicesLabel)
        self.inactiveServicesList = QtGui.QListWidget(Services)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inactiveServicesList.sizePolicy().hasHeightForWidth())
        self.inactiveServicesList.setSizePolicy(sizePolicy)
        self.inactiveServicesList.setObjectName(_fromUtf8("inactiveServicesList"))
        self.verticalLayout_3.addWidget(self.inactiveServicesList)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(Services)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_4.addWidget(self.line)
        self.infoTextarea = QtGui.QTextEdit(Services)
        self.infoTextarea.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoTextarea.sizePolicy().hasHeightForWidth())
        self.infoTextarea.setSizePolicy(sizePolicy)
        self.infoTextarea.setStyleSheet(_fromUtf8(""))
        self.infoTextarea.setFrameShadow(QtGui.QFrame.Sunken)
        self.infoTextarea.setReadOnly(True)
        self.infoTextarea.setObjectName(_fromUtf8("infoTextarea"))
        self.verticalLayout_4.addWidget(self.infoTextarea)

        self.retranslateUi(Services)
        QtCore.QMetaObject.connectSlotsByName(Services)

    def retranslateUi(self, Services):
        Services.setWindowTitle(QtGui.QApplication.translate("Services", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.activeServicesLabel.setText(QtGui.QApplication.translate("Services", "Active Services", None, QtGui.QApplication.UnicodeUTF8))
        self.inactiveServicesLabel.setText(QtGui.QApplication.translate("Services", "Available Services", None, QtGui.QApplication.UnicodeUTF8))
        self.infoTextarea.setHtml(QtGui.QApplication.translate("Services", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nimbus Sans L\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Add the services to be monitored to the list of active services. The icons show the install status of each service.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you find some service missing, you can add it either as custom service or through a source file downloaded from the internet (see the sources tab).</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc