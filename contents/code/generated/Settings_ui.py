# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.resize(647, 512)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Settings)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(Settings)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pollingIntervalSpinbox = QtGui.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pollingIntervalSpinbox.setFont(font)
        self.pollingIntervalSpinbox.setSuffix(_fromUtf8(" sec"))
        self.pollingIntervalSpinbox.setMinimum(0.5)
        self.pollingIntervalSpinbox.setMaximum(5000000.0)
        self.pollingIntervalSpinbox.setSingleStep(0.5)
        self.pollingIntervalSpinbox.setObjectName(_fromUtf8("pollingIntervalSpinbox"))
        self.gridLayout.addWidget(self.pollingIntervalSpinbox, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.sleepTimeSpinbox = QtGui.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sleepTimeSpinbox.setFont(font)
        self.sleepTimeSpinbox.setSuffix(_fromUtf8(" sec"))
        self.sleepTimeSpinbox.setMinimum(0.0)
        self.sleepTimeSpinbox.setMaximum(5.0)
        self.sleepTimeSpinbox.setSingleStep(0.1)
        self.sleepTimeSpinbox.setProperty("value", 0.5)
        self.sleepTimeSpinbox.setObjectName(_fromUtf8("sleepTimeSpinbox"))
        self.gridLayout.addWidget(self.sleepTimeSpinbox, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.themeComboBox = QtGui.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.themeComboBox.setFont(font)
        self.themeComboBox.setObjectName(_fromUtf8("themeComboBox"))
        self.gridLayout.addWidget(self.themeComboBox, 2, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.suppressStdoutCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.suppressStdoutCheckBox.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.suppressStdoutCheckBox.setFont(font)
        self.suppressStdoutCheckBox.setObjectName(_fromUtf8("suppressStdoutCheckBox"))
        self.gridLayout.addWidget(self.suppressStdoutCheckBox, 3, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(Settings)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.sudoHelperComboBox = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sudoHelperComboBox.sizePolicy().hasHeightForWidth())
        self.sudoHelperComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sudoHelperComboBox.setFont(font)
        self.sudoHelperComboBox.setObjectName(_fromUtf8("sudoHelperComboBox"))
        self.sudoHelperComboBox.addItem(_fromUtf8(""))
        self.sudoHelperComboBox.addItem(_fromUtf8(""))
        self.sudoHelperComboBox.addItem(_fromUtf8(""))
        self.sudoHelperComboBox.addItem(_fromUtf8(""))
        self.sudoHelperComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.sudoHelperComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sudoHelperTextarea = QtGui.QPlainTextEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sudoHelperTextarea.sizePolicy().hasHeightForWidth())
        self.sudoHelperTextarea.setSizePolicy(sizePolicy)
        self.sudoHelperTextarea.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sudoHelperTextarea.setFont(font)
        self.sudoHelperTextarea.setObjectName(_fromUtf8("sudoHelperTextarea"))
        self.verticalLayout.addWidget(self.sudoHelperTextarea)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.usernameLabel = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.horizontalLayout_3.addWidget(self.usernameLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_6 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.passwordLineEdit = QtGui.QLineEdit(self.groupBox)
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.horizontalLayout_3.addWidget(self.passwordLineEdit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.checkSudoButton = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkSudoButton.setFont(font)
        self.checkSudoButton.setObjectName(_fromUtf8("checkSudoButton"))
        self.horizontalLayout_3.addWidget(self.checkSudoButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.line = QtGui.QFrame(Settings)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpTabWidget.addTab(self.help, icon, _fromUtf8(""))
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
        self.verticalLayout_2.addWidget(self.helpTabWidget)

        self.retranslateUi(Settings)
        self.helpTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Settings)
        Settings.setTabOrder(self.pollingIntervalSpinbox, self.sleepTimeSpinbox)
        Settings.setTabOrder(self.sleepTimeSpinbox, self.themeComboBox)
        Settings.setTabOrder(self.themeComboBox, self.suppressStdoutCheckBox)
        Settings.setTabOrder(self.suppressStdoutCheckBox, self.sudoHelperComboBox)
        Settings.setTabOrder(self.sudoHelperComboBox, self.sudoHelperTextarea)
        Settings.setTabOrder(self.sudoHelperTextarea, self.passwordLineEdit)
        Settings.setTabOrder(self.passwordLineEdit, self.checkSudoButton)
        Settings.setTabOrder(self.checkSudoButton, self.helpTabWidget)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QtGui.QApplication.translate("Settings", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Settings", "Service Monitor Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Settings", "Service polling interval:", None, QtGui.QApplication.UnicodeUTF8))
        self.pollingIntervalSpinbox.setToolTip(QtGui.QApplication.translate("Settings", "Update service status every x seconds.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Settings", "Start/stop command delay:", None, QtGui.QApplication.UnicodeUTF8))
        self.sleepTimeSpinbox.setToolTip(QtGui.QApplication.translate("Settings", "Wait x seconds after execution of start/stop commands before rechecking service status.\n"
"If the status immediatly flashes back to inactive when starting a service, increase this value.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Settings", "Indicator theme:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Settings", "Supress stderr when starting/stopping services:", None, QtGui.QApplication.UnicodeUTF8))
        self.suppressStdoutCheckBox.setToolTip(QtGui.QApplication.translate("Settings", "Disables warnings when start/stop commands produce error output. Check this option\n"
"if you experience annoying error output being produced by some commands.", None, QtGui.QApplication.UnicodeUTF8))
        self.suppressStdoutCheckBox.setText(QtGui.QApplication.translate("Settings", "(use with caution)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Settings", "Sudo Configuration Helper", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Settings", "Grant root access for", None, QtGui.QApplication.UnicodeUTF8))
        self.sudoHelperComboBox.setItemText(0, QtGui.QApplication.translate("Settings", "< please select an option >", None, QtGui.QApplication.UnicodeUTF8))
        self.sudoHelperComboBox.setItemText(1, QtGui.QApplication.translate("Settings", "every user in group sudoers, ask for user password", None, QtGui.QApplication.UnicodeUTF8))
        self.sudoHelperComboBox.setItemText(2, QtGui.QApplication.translate("Settings", "every user in group sudoers, ask for root password", None, QtGui.QApplication.UnicodeUTF8))
        self.sudoHelperComboBox.setItemText(3, QtGui.QApplication.translate("Settings", "only me, ask for my own password", None, QtGui.QApplication.UnicodeUTF8))
        self.sudoHelperComboBox.setItemText(4, QtGui.QApplication.translate("Settings", "only me, ask for root password", None, QtGui.QApplication.UnicodeUTF8))
        self.sudoHelperTextarea.setPlainText(QtGui.QApplication.translate("Settings", "This tool will help you configure sudo.\n"
"\n"
"It creates snippets for inclusion in the /etc/sudoers configuration file. Sudo allows fine-grained control, this tool will cover the most standard setups, but they will be sufficient. Simply choose the config that most suits your needs, append the generated snippet to your /etc/sudoers and use the button below to check your configuration.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Settings", "Current user:", None, QtGui.QApplication.UnicodeUTF8))
        self.usernameLabel.setText(QtGui.QApplication.translate("Settings", "User:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Settings", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSudoButton.setText(QtGui.QApplication.translate("Settings", "Check sudo configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Settings", "These settings influence general behavior fine-tune them to your needs.\n"
"Since Service Monitor uses \"sudo\" to gain root privileges, make sure you have a working\n"
"confiuration. If not, you can use the configuration helper to generate configuration snippets.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Settings", "Please note: sudo can be configured to work without asking for a password. As of now, Service\n"
"Monitor is *not* compatible with this setting.\n"
"Besides, it can be highly dangerous, so you shouldn\'t be using it anyway. ", None, QtGui.QApplication.UnicodeUTF8))
        self.helpTabWidget.setTabText(self.helpTabWidget.indexOf(self.tab_1), QtGui.QApplication.translate("Settings", "Sudo Configuration Helper", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
