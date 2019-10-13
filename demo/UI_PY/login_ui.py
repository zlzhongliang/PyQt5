# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(500, 450)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.login_top_bg_label = QtWidgets.QLabel(self.widget)
        self.login_top_bg_label.setText("")
        self.login_top_bg_label.setObjectName("login_top_bg_label")
        self.verticalLayout_2.addWidget(self.login_top_bg_label)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 15)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.register_btn = QtWidgets.QPushButton(self.widget_2)
        self.register_btn.setFlat(True)
        self.register_btn.setObjectName("register_btn")
        self.horizontalLayout.addWidget(self.register_btn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.login_weight = QtWidgets.QWidget(self.widget_2)
        self.login_weight.setStyleSheet("")
        self.login_weight.setObjectName("login_weight")
        self.gridLayout = QtWidgets.QGridLayout(self.login_weight)
        self.gridLayout.setObjectName("gridLayout")
        self.account_cb = QtWidgets.QComboBox(self.login_weight)
        self.account_cb.setMinimumSize(QtCore.QSize(0, 40))
        self.account_cb.setMaximumSize(QtCore.QSize(16777215, 40))
        self.account_cb.setStyleSheet("QComboBox{\n"
"    font-size: 20px;\n"
"    border: none;\n"
"    border-bottom: 1px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QComboBox:hover{\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"QComboBox:focus{\n"
"    border-bottom: 1px solid rgb(18, 183, 245);\n"
"}\n"
"QComboBox:drop-down{\n"
"    background-color: transparent;\n"
"    width: 60px;\n"
"    height: 40px;\n"
"}\n"
"QComboBox:down-arrow{\n"
"    image: url(:/login/images/login_combobox_icon.png);\n"
"    width: 60px;\n"
"    height: 40px;\n"
"}\n"
"QComboBox:QAbstractItemView{\n"
"    min-height: 60px;\n"
"}\n"
"QComboBox:QAbstractItemView:item{\n"
"    color: lightblue;\n"
"}")
        self.account_cb.setEditable(True)
        self.account_cb.setObjectName("account_cb")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/login/images/login_item_icon1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_cb.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/login/images/login_item_icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_cb.addItem(icon1, "")
        self.gridLayout.addWidget(self.account_cb, 0, 0, 1, 2)
        self.pwd_le = QtWidgets.QLineEdit(self.login_weight)
        self.pwd_le.setMinimumSize(QtCore.QSize(0, 40))
        self.pwd_le.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pwd_le.setStyleSheet("QLineEdit{\n"
"    font-size: 20px;\n"
"    border: none;\n"
"    border-bottom: 1px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QLineEdit:hover{\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"QLineEdit:focus{\n"
"    border-bottom: 1px solid rgb(18, 183, 245);\n"
"}\n"
"")
        self.pwd_le.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.pwd_le.setClearButtonEnabled(True)
        self.pwd_le.setObjectName("pwd_le")
        self.gridLayout.addWidget(self.pwd_le, 1, 0, 1, 2)
        self.auto_login_check = QtWidgets.QCheckBox(self.login_weight)
        self.auto_login_check.setObjectName("auto_login_check")
        self.gridLayout.addWidget(self.auto_login_check, 2, 0, 1, 1)
        self.remmber_pwd_check = QtWidgets.QCheckBox(self.login_weight)
        self.remmber_pwd_check.setObjectName("remmber_pwd_check")
        self.gridLayout.addWidget(self.remmber_pwd_check, 2, 1, 1, 1)
        self.login_btn = QtWidgets.QPushButton(self.login_weight)
        self.login_btn.setEnabled(False)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.login_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.login_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    spacing: 20px\n"
"}\n"
"QPushButton:disabled{\n"
"    background-color: rgb(162, 162, 162);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(72, 203, 250);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 255);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/login/images/login_btn_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon2)
        self.login_btn.setIconSize(QtCore.QSize(30, 30))
        self.login_btn.setObjectName("login_btn")
        self.gridLayout.addWidget(self.login_btn, 3, 0, 1, 2)
        self.horizontalLayout.addWidget(self.login_weight)
        self.QR_code_btn = QtWidgets.QPushButton(self.widget_2)
        self.QR_code_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.QR_code_btn.setMaximumSize(QtCore.QSize(80, 80))
        self.QR_code_btn.setStyleSheet("border-image: url(:/login/images/login_qr_code.png);")
        self.QR_code_btn.setText("")
        self.QR_code_btn.setFlat(True)
        self.QR_code_btn.setObjectName("QR_code_btn")
        self.horizontalLayout.addWidget(self.QR_code_btn, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 3)

        self.retranslateUi(Form)
        self.register_btn.clicked.connect(Form.show_register_pane)
        self.account_cb.editTextChanged['QString'].connect(Form.check_account_pwd)
        self.pwd_le.textChanged['QString'].connect(Form.check_account_pwd)
        self.auto_login_check.clicked['bool'].connect(Form.check_autocb_pwdcb)
        self.login_btn.clicked.connect(Form.send_account_pwd)
        self.remmber_pwd_check.clicked['bool'].connect(Form.check_remmber_pwd)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.register_btn.setText(_translate("Form", "注册账号"))
        self.account_cb.setItemText(0, _translate("Form", "123456"))
        self.account_cb.setItemText(1, _translate("Form", "23456"))
        self.auto_login_check.setText(_translate("Form", "自动登陆"))
        self.remmber_pwd_check.setText(_translate("Form", "记住密码"))
        self.login_btn.setText(_translate("Form", "安全登陆"))
import register_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
