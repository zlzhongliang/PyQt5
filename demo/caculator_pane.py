from PyQt5.Qt import *
from demo.UI_PY.caculator_ui import Ui_Form

class Caculator(QObject):
    show_content = pyqtSignal(str)
    def __init__(self,parent):
        super().__init__(parent)
        # 数字键位 num 运算符 operator
        self.key_models = []
        self.flag = 0

    def parse_key_model(self, key_model):
        # print(key_model)
        if key_model['role'] == 'clear':
            self.key_models = []
            self.show_content.emit('0.0')
            return

        if key_model['role'] == 'calulate':
            if len(self.key_models) == 0:
                return
            if self.key_models[-1]['role'] != 'num':
                self.key_models.pop()

            expression = ''
            for i in self.key_models:
                expression += i['title']

            try:
                title = str(eval(expression))
                self.show_content.emit(title)
            except Exception as f:
                self.show_content.emit('错误')
                return
            self.key_models = [{'title': title, 'role': 'num'}]
            self.flag = title
            self.key_models =[]
            return

        if len(self.key_models) == 0:
            if key_model['role'] == 'num':
                if key_model['title'] == '%':
                    return
                self.key_models.append(key_model)
                if key_model['title'] == '+/-':
                    self.key_models[-1]['title'] = '-'
                    self.show_content.emit(self.key_models[-1]['title'])
                    return

                if key_model['title'] == '.':
                    self.key_models[-1]['title'] = '0.'
                    self.show_content.emit(self.key_models[-1]['title'])
                    return
                self.show_content.emit(self.key_models[-1]['title'])
                return
            else:
                return
        if key_model['role'] == self.key_models[-1]['role']:
            if key_model['role'] == 'num':
                if key_model['title'] == '.' and ('.' in self.key_models[-1]['title']):
                    self.show_content.emit(self.key_models[-1]['title'])
                    return

                if key_model['title'] == '+/-':
                    if self.key_models[-1]['title'] == '-':
                        self.key_models.pop()
                        self.show_content.emit(self.key_models[-1]['title'])
                    else:
                        title = self.key_models[-1]['title']
                        if ('.' in title):
                            self.key_models[-1]['title'] = str(float(self.key_models[-1]['title']) * -1)
                        else:
                            self.key_models[-1]['title'] = str(int(self.key_models[-1]['title']) * -1)
                        self.show_content.emit(self.key_models[-1]['title'])
                    return

                if key_model['title'] == '%':
                    self.key_models[-1]['title'] = str(float(self.key_models[-1]['title']) / 100)
                    self.show_content.emit(self.key_models[-1]['title'])
                    return

                if self.key_models[-1]['title'] == '0':
                    if key_model['title'] == '.':
                        self.key_models[-1]['title'] += key_model['title']
                    else:
                        self.key_models[-1]['title'] = key_model['title']
                else:
                    self.key_models[-1]['title'] += key_model['title']
            else:

                self.key_models[-1] = key_model
        else:
            if key_model['role'] == 'num':
                if key_model['title'] == '%':
                    self.show_content.emit(self.key_models[-1]['title'])
                    return
                self.key_models.append(key_model)
                if key_model['title'] == '+/-':
                    self.key_models[-1]['title'] = '-'
                    self.show_content.emit(self.key_models[-1]['title'])
                    return

                if key_model['title'] == '.':
                    self.key_models[-1]['title'] = '0.'
                    self.show_content.emit(self.key_models[-1]['title'])
                    return
                self.show_content.emit(self.key_models[-1]['title'])
            else:
                self.key_models.append(key_model)



        self.show_content.emit(self.key_models[-1]['title'])



class CaculatorPane(QWidget, Ui_Form):

    def __init__(self,parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.caculator = Caculator(self)
        self.caculator.show_content.connect(self.show_content)

    def show_content(self,content):
        self.lineEdit.setText(content)

    def get_key(self,title,role):
        self.caculator.parse_key_model({'title':title,'role':role})



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = CaculatorPane()
    window.show()
    sys.exit(app.exec_())