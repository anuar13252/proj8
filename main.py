import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView
data = [['', -1], ['', '', '', ''], ['', -1]]

ans = ['', '', '']


class welcome(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(welcome, self).__init__()
        uic.loadUi('forms/welcome.ui', self)

        self.setWindowTitle('Окно приветсвия')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.Exit.clicked.connect(self.close)
        self.welcomeStart.clicked.connect(self.next)

    def next(self):
        self.switch_window.emit('1>2')


class chilhood(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(chilhood, self).__init__()
        uic.loadUi('forms/chilhood.ui', self)

        self.setWindowTitle('Окно Детство')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.label_img.setPixmap(QPixmap('images/kasha.jpg'))
        self.label_img.setScaledContents(True)

        if data[1][0] != '':
            self.checkBox_0.setCheckState(2)
        if data[1][1] != '':
            self.checkBox_1.setCheckState(2)
        if data[1][2] != '':
            self.checkBox_2.setCheckState(2)
        if data[1][2] != '':
            self.checkBox_2.setCheckState(2)
        self.label_3.setText(form3input(data[1]))
        self.checkBox_0.stateChanged.connect(self.cb0)
        self.checkBox_1.stateChanged.connect(self.cb1)
        self.checkBox_2.stateChanged.connect(self.cb2)
        self.checkBox_3.stateChanged.connect(self.cb3)
        self.Back.clicked.connect(self.back)
        self.Next.clicked.connect(self.next)


    def cb0(self):
        if self.checkBox_0.checkState() > 0:
            data[1][0] = self.checkBox_0.text()
        else:
            data[1][0] = ''
        self.label_3.setText(form3input(data[1]))
        


    def cb1(self):
        if self.checkBox_1.checkState() > 0:
            data[1][1] = self.checkBox_1.text()
        else:
            data[1][1] = ''
        self.label_3.setText(form3input(data[1]))


    def cb2(self):
        if self.checkBox_2.checkState() > 0:
            data[1][2] = self.checkBox_2.text()
        else:
            data[1][2] = ''
        self.label_3.setText(form3input(data[1]))


    def cb3(self):
        if self.checkBox_3.checkState() > 0:
            data[1][3] = self.checkBox_3.text()
        else:
            data[1][3] = ''
        self.label_3.setText(form3input(data[1]))
        print(data[1])

    def back(self):
        self.switch_window.emit('1<2')

    def next(self):
        self.switch_window.emit('2>3')


class boyhood(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(boyhood, self).__init__()
        uic.loadUi('forms/boyhood.ui', self)

        self.setWindowTitle('Окно Отрочество')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.label_img.setPixmap(QPixmap('images/karandash.jpg'))
        self.label_img.setScaledContents(True)

        if ans[1] is not None:
            self.boyhoodLbl1.setText('Выбрано: ' + ans[1])

        self.comboBox.activated.connect(self.handleActivated)
        self.Back.clicked.connect(self.back)
        self.Next.clicked.connect(self.next)

    def handleActivated(self, index):
        ans[1] = self.comboBox.itemText(index)
        self.boyhoodLbl1.setText('Выбрано: ' + ans[1])


    def back(self):
        self.switch_window.emit('2<3')

    def next(self):
        self.switch_window.emit('3>4')


class youth(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(youth, self).__init__()
        uic.loadUi('forms/youth.ui', self)

        self.setWindowTitle('Окно Юность')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.label_img.setPixmap(QPixmap('images/obraz.png'))
        self.label_img.setScaledContents(True)

        if ans[2] is not None:
            self.YouthLbl1.setText('Выбрано: ' + ans[2])

        self.radioButton_1.toggled.connect(
            lambda: self.onToggled(self.radioButton_1))
        self.radioButton_2.toggled.connect(
            lambda: self.onToggled(self.radioButton_2))
        self.radioButton_3.toggled.connect(
            lambda: self.onToggled(self.radioButton_3))
        self.radioButton_4.toggled.connect(
            lambda: self.onToggled(self.radioButton_4))

        self.Back.clicked.connect(self.back)
        self.Next.clicked.connect(self.next)

    def onToggled(self, radiobutton):
        if radiobutton.isChecked():
            ans[2] = radiobutton.text()
            self.YouthLbl1.setText('Выбрано: ' + ans[2])
    def back(self):
        self.switch_window.emit('3<4')

    def next(self):
        self.switch_window.emit('4>5')


class finish(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(finish, self).__init__()
        uic.loadUi('forms/finish.ui', self)

        self.setWindowTitle('Результат')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.textEdit.setText('Любимая каша: ' + ans[0] + '\n' + 'Учился: ' + ans[1] + '\n' + 'Образование: ' + ans[2])
        
        self.Back.clicked.connect(self.back)
        self.Exit.clicked.connect(self.close)

    def back(self):
        self.switch_window.emit("4<5")

class Controller:
    def __init__(self):
        pass

    def select_forms(self, text):
        if text == '1':
            self.form1 = welcome()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()

        if text == '1>2':
            self.form2 = chilhood()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
            self.form1.close()

        if text == '2>3':
            self.form3 = boyhood()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
            self.form2.close()

        if text == '3>4':
            self.form4 = youth()
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
            self.form3.close()

        if text == '4>5':
            self.form5 = finish()
            self.form5.switch_window.connect(self.select_forms)
            self.form5.show()
            self.form4.close()

        if text == '4<5':
            self.form4 = youth()
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
            self.form5.close()

        if text == '3<4':
            self.form3 = boyhood()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
            self.form4.close()

        if text == '2<3':
            self.form2 = chilhood()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
            self.form3.close()

        if text == '1<2':
            self.form1 = welcome()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()
            self.form2.close()

def form3input(array):
    tempvar = 0
    tempstr = ''
    for i in range(4):
        if array [i] != '':
            if tempvar == 0:
                tempstr += array[i]
                tempvar += 1
            else:
                tempstr += ', ' + array[i]
    return tempstr

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.select_forms("1")
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
