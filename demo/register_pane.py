from PyQt5.Qt import *
from demo.UI_PY.register_ui import Ui_Form

class RegisterPane(QWidget, Ui_Form):
    exit_singal = pyqtSignal()
    register_account_pwd_signal = pyqtSignal(str,str)
    def __init__(self,parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)

        self.animation_targets = [self.about_menue_btn, self.reset_menue_btn, self.exit_menue_btn]
        self.animation_target_pos = [target.pos() for target in self.animation_targets]

    def show_hide_menue(self,checked):
        print('显示和隐藏',checked)
        # 创建动画组
        animation_group = QSequentialAnimationGroup(self)
        for idx, target in enumerate(self.animation_targets):
            animation = QPropertyAnimation()
            animation.setTargetObject(target)
            animation.setPropertyName(b'pos')
            animation.setStartValue(self.main_menue_btn.pos())
            animation.setEndValue(self.animation_target_pos[idx])
            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.OutBounce)
            animation_group.addAnimation(animation)
        if not checked:
            # 正顺序
            animation_group.setDirection(QAbstractAnimation.Forward)
        else:
            # 反顺序
            animation_group.setDirection(QAbstractAnimation.Backward)
        # 动画结束即删除动画
        animation_group.start(QAbstractAnimation.DeleteWhenStopped)


    def about_menue(self):
        QMessageBox.about(self,'这是标题','这是内容')

    def reset_menue(self):
        self.account_le.clear()
        self.password_le.clear()
        self.confir_pwd_le.clear()

    def enable_register_btn(self):
        if self.account_le.text():
            if (self.password_le.text()) and (self.password_le.text() == self.confir_pwd_le.text()):
                self.register_btn.setEnabled(True)
                return 0
        self.register_btn.setEnabled(False)

    def exit_menue(self):
        print('退出')
        self.exit_singal.emit()

    def check_register(self):
        account = str(self.account_le.text())
        password = str(self.confir_pwd_le.text())
        self.register_account_pwd_signal.emit(account,password)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = RegisterPane()
    window.show()
    window.exit_singal.connect(lambda :print('点击了推出'))
    window.register_account_pwd_signal.connect(lambda account,pwd:print('点击了注册',account,pwd))
    sys.exit(app.exec_())