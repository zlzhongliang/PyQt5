from PyQt5.Qt import *
from demo.UI_PY.login_ui import Ui_Form

class LoginPane(QWidget, Ui_Form):
    show_register_pane_signal = pyqtSignal()
    send_account_pwd_signal = pyqtSignal(str,str,bool,bool)
    def __init__(self,parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        # 加载动画
        movie = QMovie(':/login/images/login_top_bg.gif')
        movie.setScaledSize(QSize(500, 181))
        self.login_top_bg_label.setMovie(movie)
        movie.start()

    def show_register_pane(self):
        self.show_register_pane_signal.emit()

    def check_account_pwd(self):
        if self.account_cb.currentText() and self.pwd_le.text():
            self.login_btn.setEnabled(True)

    def check_autocb_pwdcb(self,check):
        if check:
            self.remmber_pwd_check.setChecked(True)

    def check_remmber_pwd(self,check):
        if not check:
            self.auto_login_check.setChecked(False)


    def send_account_pwd(self):
        account = self.account_cb.currentText()
        pwd = self.pwd_le.text()
        auto_flag = self.auto_login_check.isChecked()
        remmber_flag = self.remmber_pwd_check.isChecked()
        self.send_account_pwd_signal.emit(account,pwd,auto_flag,remmber_flag)

    def login_error(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.login_weight)
        animation.setPropertyName(b'pos')
        animation.setKeyValueAt(0,self.login_weight.pos())
        animation.setKeyValueAt(0.2,self.login_weight.pos() + QPoint(15,0))
        animation.setKeyValueAt(0.5,self.login_weight.pos())
        animation.setKeyValueAt(0.7,self.login_weight.pos() + QPoint(-15,0))
        animation.setKeyValueAt(1,self.login_weight.pos())
        animation.setDuration(100)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = LoginPane()
    window.show()
    sys.exit(app.exec_())