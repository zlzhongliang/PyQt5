from demo.login_pane import LoginPane
from demo.register_pane import RegisterPane
from demo.caculator_pane import CaculatorPane

from PyQt5.Qt import *
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    login_pane = LoginPane()
    caculator = CaculatorPane()

    def check_account_pass(account,pwd,auto_flag,remmber_flag):
        print('点击了登陆', account, pwd, auto_flag, remmber_flag)
        if account == '123456' and pwd == '123':
            caculator.show()
            login_pane.hide()
        else:
            login_pane.login_error()

    login_pane.send_account_pwd_signal.connect(check_account_pass)

    register_pane = RegisterPane(login_pane)
    register_pane.move(0, login_pane.height())
    register_pane.show()
    register_pane.register_account_pwd_signal.connect(lambda account,pwd:print('点击了注册',account,pwd))

    def exit_register_pane():
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b'pos')
        animation.setStartValue(register_pane.pos())
        animation.setEndValue(QPoint(0, login_pane.height()))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
    register_pane.exit_singal.connect(exit_register_pane)

    def show_register_pane():
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b'pos')
        animation.setStartValue(register_pane.pos())
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)



    login_pane.show_register_pane_signal.connect(show_register_pane)
    login_pane.show()

    sys.exit(app.exec_())