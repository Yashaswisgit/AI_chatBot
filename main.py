import sys
from backend import Chatbot
import threading

from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()
        self.setMinimumSize(700, 500)


        #ADD CHAT AREA WIDGET
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style = 'color: #333333'> Me: {user_input} </p>")
        self.input_field.clear()
        thread = threading.Thread(target = self.get_bot_response, args = (user_input, ))
        thread.start()

    def get_bot_response(self):
        reponse = self.chatbot.get_response(user_input)
        self.chat_area.append(f" <p style = 'color: #333333'; background-color: #E9E9E9> Bot: {respponse} </p>")


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())