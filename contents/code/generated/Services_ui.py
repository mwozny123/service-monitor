# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Services(object):
    def setupUi(self, Services):
        Services.setObjectName(_fromUtf8("Services"))
        Services.resize(604, 508)
        self.verticalLayout_8 = QtGui.QVBoxLayout(Services)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
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
        self.hideUnavailableCheckBox = QtGui.QCheckBox(Services)
        self.hideUnavailableCheckBox.setMinimumSize(QtCore.QSize(0, 25))
        self.hideUnavailableCheckBox.setMaximumSize(QtCore.QSize(16777215, 25))
        self.hideUnavailableCheckBox.setObjectName(_fromUtf8("hideUnavailableCheckBox"))
        self.verticalLayout_3.addWidget(self.hideUnavailableCheckBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(Services)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_8.addWidget(self.line)
        self.infoTextarea = QtGui.QTextEdit(Services)
        self.infoTextarea.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoTextarea.sizePolicy().hasHeightForWidth())
        self.infoTextarea.setSizePolicy(sizePolicy)
        self.infoTextarea.setMaximumSize(QtCore.QSize(16777215, 130))
        self.infoTextarea.setStyleSheet(_fromUtf8(""))
        self.infoTextarea.setFrameShadow(QtGui.QFrame.Sunken)
        self.infoTextarea.setReadOnly(True)
        self.infoTextarea.setHtml(_fromUtf8("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.infoTextarea.setObjectName(_fromUtf8("infoTextarea"))
        self.verticalLayout_8.addWidget(self.infoTextarea)
        self.line_2 = QtGui.QFrame(Services)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_8.addWidget(self.line_2)
        self.helpTabWidget = QtGui.QTabWidget(Services)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpTabWidget.sizePolicy().hasHeightForWidth())
        self.helpTabWidget.setSizePolicy(sizePolicy)
        self.helpTabWidget.setMinimumSize(QtCore.QSize(0, 110))
        self.helpTabWidget.setObjectName(_fromUtf8("helpTabWidget"))
        self.help = QtGui.QWidget()
        self.help.setObjectName(_fromUtf8("help"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.help)
        self.verticalLayout_4.setMargin(10)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_2 = QtGui.QLabel(self.help)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpTabWidget.addTab(self.help, icon6, _fromUtf8(""))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_1)
        self.verticalLayout_5.setMargin(10)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label = QtGui.QLabel(self.tab_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_5.addWidget(self.label)
        self.helpTabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setMargin(10)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_6.addWidget(self.label_3)
        self.helpTabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_8.addWidget(self.helpTabWidget)

        self.retranslateUi(Services)
        self.helpTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Services)
        Services.setTabOrder(self.activeServicesList, self.inactiveServicesList)
        Services.setTabOrder(self.inactiveServicesList, self.activateButton)
        Services.setTabOrder(self.activateButton, self.deactivateButton)
        Services.setTabOrder(self.deactivateButton, self.sortTopButton)
        Services.setTabOrder(self.sortTopButton, self.sortUpButton)
        Services.setTabOrder(self.sortUpButton, self.sortDownButton)
        Services.setTabOrder(self.sortDownButton, self.sortBottomButton)
        Services.setTabOrder(self.sortBottomButton, self.hideUnavailableCheckBox)
        Services.setTabOrder(self.hideUnavailableCheckBox, self.infoTextarea)
        Services.setTabOrder(self.infoTextarea, self.helpTabWidget)

    def retranslateUi(self, Services):
        Services.setWindowTitle(QtGui.QApplication.translate("Services", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.activeServicesLabel.setText(QtGui.QApplication.translate("Services", "Active Services", None, QtGui.QApplication.UnicodeUTF8))
        self.inactiveServicesLabel.setText(QtGui.QApplication.translate("Services", "Available Services", None, QtGui.QApplication.UnicodeUTF8))
        self.hideUnavailableCheckBox.setText(QtGui.QApplication.translate("Services", "Hide unavailable services", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Services", "Add the services to be monitored to the list of active services. The icons show the install\n"
"status of each service. If you find some service missing, you can add it either as custom\n"
"service or through a source file downloaded from the internet (see the sources tab).", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Services", "This list shows all services to be monitored. Add items from the right-hand list and reorder\n"
"them to your needs. Be aware that only services marked with a green dot will work.\n"
"A red dot means the install check has failed, so the definition will not work.", None, QtGui.QApplication.UnicodeUTF8))
        self.helpTabWidget.setTabText(self.helpTabWidget.indexOf(self.tab_1), QtGui.QApplication.translate("Services", "Active services", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Services", "The list of available services is loaded from your definition source files, which you can\n"
"manage under the \"Sources\" tab. If a specific service is missing here, try looking for it\n"
"in the sources tab or define it yourself under \"Custom Services\".", None, QtGui.QApplication.UnicodeUTF8))
        self.helpTabWidget.setTabText(self.helpTabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Services", "Available services", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
