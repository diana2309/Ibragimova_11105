# -*- coding: utf8 -*-
import socket
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QVBoxLayout, QLabel, QTextEdit, QTableWidget, QButtonGroup
from PyQt6 import QtCore
import threading
import random

#не подключается
serv_conn = socket.socket()
serv_conn.connect(('localhost', 4548))
events = []

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Memory Game')
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.main_table = QGridLayout(self.centralwidget)
        self.first_player_score = 0
        self.second_player_score = 0
        self.scores1 = QLabel()
        self.scores2 = QLabel()
        self.scores1.setText('1 player: ' + str(self.first_player_score))
        self.scores2.setText('2 player: ' + str(self.second_player_score))
        self.main_table.addWidget(self.scores1, 6, 0, 2, 4)
        self.main_table.addWidget(self.scores2, 9, 0, 2, 4)
        self.painted_button_row = []
        self.painted_button_column = []
        self.game_steps = []
        self.matrix = []

        self.buttonGroup = QButtonGroup(self)
        # self.pushButton = QPushButton(' \ _ /\n = ^.^ =\n (")_(")')

        row = 6
        column = 6

        for i in range(row):
            for step in range(column):
                self.pushButton = QPushButton(' \ _ /\n = ^.^ =\n (")_(")')
                self.pushButton.setFixedSize(80, 80)
                self.pushButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: #1faee9;}')
                self.buttonGroup.addButton(self.pushButton)
                # self.pushButton.clicked.connect(self.buttonClicked)
                self.main_table.addWidget(self.pushButton, step // column + i, step % column)

        self.label = QLabel()
        self.main_table.addWidget(self.label, step + 1, 0, 2, column)

#получилось менять цвет только у одной кнопки
    def buttonClicked(self):
        color_list = ['#edd19c', '#c9dc87', '#00fa9a', '#bd8644', '#8ac8ff', '#ddadaf', '#47252b', '#eba8ff', '#eee8aa', '#d4c62a', '#544f11', '#c98320', '#4d0000', '#210904', '#402335', '#61323a', '#6bdb6b', '#004220']
        rand = random.randint(0, len(color_list) - 1)
        self.pushButton.setStyleSheet('QPushButton {background-color:' + color_list[rand] + '}')

#для нескольких нерабочая
    def buttonClicked_all(self):
        color_list = ['#edd19c', '#c9dc87', '#00fa9a', '#bd8644', '#8ac8ff', '#ddadaf', '#47252b', '#eba8ff']
        used_colors = []
        for i in range(16):
            rand = random.randint(0, len(color_list) - 1)
            if any([isinstance(color_list[rand], str) or color_list[rand] is None for color_list[rand] in used_colors]):
                color_list.remove(color_list[rand])
                break
            else:
                self.pushButton[i].setStyleSheet('QPushButton {background-color:' + color_list[rand] + '}')
                rand.append(used_colors)




def listener():
    while True:
        try:
            message = serv_conn.recv(1024).decode('utf-8')
            if message:
                events.append(message)
        except:
            print("Error!")
            serv_conn.close()
            break



app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()
