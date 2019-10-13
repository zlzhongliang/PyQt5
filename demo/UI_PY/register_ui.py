# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        Form.setStyleSheet("#Form{\n"
"    border-image: url(:/register/images/1.jpg)\n"
"}")
        self.main_menue_btn = QtWidgets.QPushButton(Form)
        self.main_menue_btn.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.main_menue_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 170, 255);\n"
"    color: rgb(170, 0, 0);\n"
"    border-radius: 25px;\n"
"    border:2px solid rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    border:4px double rgb(255, 85, 255);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: rgb(255, 85, 255);\n"
"    border:4px double rgb(255, 85, 255);\n"
"}")
        self.main_menue_btn.setCheckable(True)
        self.main_menue_btn.setObjectName("main_menue_btn")
        self.reset_menue_btn = QtWidgets.QPushButton(Form)
        self.reset_menue_btn.setGeometry(QtCore.QRect(100, 90, 50, 50))
        self.reset_menue_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 170, 255);\n"
"    color: rgb(170, 0, 0);\n"
"    border-radius: 25px;\n"
"    border:2px solid rgb(255, 0, 0);\n"
"}")
        self.reset_menue_btn.setObjectName("reset_menue_btn")
        self.about_menue_btn = QtWidgets.QPushButton(Form)
        self.about_menue_btn.setGeometry(QtCore.QRect(120, 20, 50, 50))
        self.about_menue_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 170, 255);\n"
"    color: rgb(170, 0, 0);\n"
"    border-radius: 25px;\n"
"    border:2px solid rgb(255, 0, 0);\n"
"}")
        self.about_menue_btn.setObjectName("about_menue_btn")
        self.exit_menue_btn = QtWidgets.QPushButton(Form)
        self.exit_menue_btn.setGeometry(QtCore.QRect(20, 110, 50, 50))
        self.exit_menue_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 170, 255);\n"
"    color: rgb(170, 0, 0);\n"
"    border-radius: 25px;\n"
"    border:2px solid rgb(255, 0, 0);\n"
"}")
        self.exit_menue_btn.setObjectName("exit_menue_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 220, 174, 102))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.account_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.account_le.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 0, 0);\n"
"border:none;\n"
"border-bottom: 1px solid red;")
        self.account_le.setText("")
        self.account_le.setObjectName("account_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.account_le)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_le.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 0, 0);\n"
"border:none;\n"
"border-bottom: 1px solid red;")
        self.password_le.setText("")
        self.password_le.setObjectName("password_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_le)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.confir_pwd_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.confir_pwd_le.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 0, 0);\n"
"border:none;\n"
"border-bottom: 1px solid red;")
        self.confir_pwd_le.setText("")
        self.confir_pwd_le.setObjectName("confir_pwd_le")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.confir_pwd_le)
        self.register_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.register_btn.setEnabled(False)
        self.register_btn.setMinimumSize(QtCore.QSize(0, 31))
        self.register_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 170, 255);\n"
"    color: rgb(170, 0, 0);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:disabled{\n"
"    background-color:rgb(189, 189, 189);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(255, 170, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"")
        self.register_btn.setObjectName("register_btn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.register_btn)
        self.reset_menue_btn.raise_()
        self.about_menue_btn.raise_()
        self.exit_menue_btn.raise_()
        self.layoutWidget.raise_()
        self.main_menue_btn.raise_()

        self.retranslateUi(Form)
        self.main_menue_btn.clicked['bool'].connect(Form.show_hide_menue)
        self.about_menue_btn.clicked.connect(Form.about_menue)
        self.reset_menue_btn.clicked.connect(Form.reset_menue)
        self.exit_menue_btn.clicked.connect(Form.exit_menue)
        self.register_btn.clicked.connect(Form.check_register)
        self.account_le.textChanged['QString'].connect(Form.enable_register_btn)
        self.password_le.textChanged['QString'].connect(Form.enable_register_btn)
        self.confir_pwd_le.textChanged['QString'].connect(Form.enable_register_btn)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.main_menue_btn.setText(_translate("Form", "菜单"))
        self.reset_menue_btn.setText(_translate("Form", "重置"))
        self.about_menue_btn.setText(_translate("Form", "关于"))
        self.exit_menue_btn.setText(_translate("Form", "退出"))
        self.label.setText(_translate("Form", "账   号："))
        self.label_2.setText(_translate("Form", "密   码："))
        self.label_3.setText(_translate("Form", "确认密码："))
        self.register_btn.setText(_translate("Form", "注册"))
import register_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
