from PyQt6 import QtWidgets, QtCore
import client_ui
import requests
from datetime import datetime

class Messenger(QtWidgets.QMainWindow, client_ui.Ui_MainWindow): #Классы некотрое объедениения функций и переменных в один единый объект.
    def __init__(self): #self=Доступ к классу.объекту, подается всегда на вход.
        super().__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.send_message)
        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)

    def show_messages(self, messages):
        for message in messages:
            dt = datetime.fromtimestamp(message['time'])
            first_line = dt.strftime('%H:%M:%S') + ' '+ message['name']
            self.textBrowser.append(first_line)
            self.textBrowser.append(message['text'])
            self.textBrowser.append('')


    def get_messages(self):
        try:
            response = requests.get(
                url='http://127.0.0.1:5000/messages',
                params={'after': self.after})
        except:
            return


        messages = response.json()['messages']
        if messages:
            self.show_messages(response.json()['messages'])
            self.after = messages[-1]['time']


    def send_message(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()
        try:
            response = requests.post(
                url='http://127.0.0.1:5000/send',
                json={'name': name, 'text': text}
            )
        except:
            self.textBrowser.append("Server error")
            self.textBrowser.append(" ")
            return


        if response.status_code != 200:
            self.textBrowser.append('Error name or text')
            self.textBrowser.append(" ")
            return


        self.textEdit.clear()


app = QtWidgets.QApplication([])
window = Messenger()
window.show()
app.exec()