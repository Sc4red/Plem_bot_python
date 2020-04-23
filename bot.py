import tkinter as tk
from tkinter import *

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtCore

from selenium import webdriver  # todo import webdriver
from selenium.webdriver.common.by import By  # todo import By for XPATH

import time
from selenium.webdriver.common.keys import Keys

import schedule


class PlemionaBot(QMainWindow):  # todo main class plemiona
    def __init__(self):
        super(PlemionaBot, self).__init__()
        self.main_widget = Widget(self)
        self.app()

    def app(self):
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Pleminona")

        self.setCentralWidget(self.main_widget)
        self.widget = Widget()
        self.thrend1 = MyThread1()
        if self.thrend1.isRunning():
            self.thrend1.exiting = True
            while self.thrend1.isRunning():
                time.sleep(0.01)
                continue
            #self.widget.time_Input.setText("123")
        else:
            self.thrend1.exiting = False
            self.thrend1.start()
            while not self.thrend1.isRunning():
                time.sleep(0.01)
                continue
            #self.widget.time_Input.setText("321")
        #self.thrend1.started.connect(self.printed)

    def printed(self):
        self.widget.time_Input.setText("123")


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__()
        self.time_Box = QGroupBox("TIME")
        self.time_Input = QLineEdit()
        self.bot = ParametersPlemiona()
        self.button_Wedge = QPushButton("Wedge")
        self.input_Millisecond = QLineEdit()
        self.input_Second = QLineEdit()
        self.input_Minute = QLineEdit()
        self.input_Hour = QLineEdit()
        self.wedge_Box = QGroupBox("WEDGE")
        self.button_Login = QPushButton("Login", self)
        self.world_Input = QLineEdit()
        self.password_Input = QLineEdit()
        self.username_Input = QLineEdit()
        self.login_Box = QGroupBox("LOGIN")
        self.createLeyoutLogin()
        self.createLeyoutWedge()
        self.createLeyoutTime()

        box = QGridLayout()
        box.addWidget(self.login_Box, 0, 0, 2, 12)
        box.addWidget(self.wedge_Box, 0, 12, 1, 30)
        box.addWidget(self.time_Box, 3, 0, 1, 1)

        self.setLayout(box)

    def buttonLogin(self):
        self.button_Login.setEnabled(False)
        username = self.username_Input.text()
        password = self.password_Input.text()
        world = self.world_Input.text()
        self.bot.signIn(username, password, world)
        #self.thrend1.started.connect(self.printed)
        #self.thrend1.started.connect(self.timerApp)
        # self.timerApp()
        # self.connect(self.thrend1, QtCore.SIGNAL('log1(QString)'), self.time_Input.setText)
        # self.time_Input.setText(self.bot.getTime())

    def buttonWedge(self):
        hour = self.input_Hour.text()
        minute = self.input_Minute.text()
        second = self.input_Second.text()
        millisecond = self.input_Millisecond.text()

    def timerApp(self):
        self.time_Input.clear()
        self.time_Input.setText(self.bot.getTime)
        # self.thrend1.on_source(self, self.bot.getTime)

    def createLeyoutLogin(self):
        grid_layout = QGridLayout()

        username_label = QLabel("Username")
        password_label = QLabel("Password")
        world_label = QLabel("World")

        self.password_Input.setEchoMode(2)  # Hasło zasłonięte

        # self.button_Login.setCheckable(True)
        self.button_Login.clicked.connect(self.buttonLogin)

        grid_layout.addWidget(username_label, 0, 0)
        grid_layout.addWidget(self.username_Input, 0, 1)
        grid_layout.addWidget(password_label, 1, 0)
        grid_layout.addWidget(self.password_Input, 1, 1)
        grid_layout.addWidget(world_label, 2, 0)
        grid_layout.addWidget(self.world_Input, 2, 1)
        grid_layout.addWidget(self.button_Login, 3, 1)

        self.login_Box.setLayout(grid_layout)

    def createLeyoutWedge(self):
        grid_layout = QGridLayout()

        hour_label = QLabel("HOUR(00)")
        minute_label = QLabel("MINUTE(00)")
        second_label = QLabel("SECOND(00)")
        millisecond_label = QLabel("MILLISECOND(000)")

        self.button_Wedge.setCheckable(True)
        # self.button_Wedge.clicked.connect(self.buttonStatus)

        grid_layout.addWidget(hour_label, 0, 0)
        grid_layout.addWidget(self.input_Hour, 1, 0)
        grid_layout.addWidget(minute_label, 0, 1)
        grid_layout.addWidget(self.input_Minute, 1, 1)
        grid_layout.addWidget(second_label, 0, 2)
        grid_layout.addWidget(self.input_Second, 1, 2)
        grid_layout.addWidget(millisecond_label, 0, 3)
        grid_layout.addWidget(self.input_Millisecond, 1, 3)
        grid_layout.addWidget(self.button_Wedge, 2, 3)

        self.wedge_Box.setLayout(grid_layout)

    def createLeyoutTime(self):
        grid_layout = QGridLayout()

        time_label = QLabel("Time")

        grid_layout.addWidget(time_label, 0, 0)
        grid_layout.addWidget(self.time_Input, 0, 1)

        self.time_Box.setLayout(grid_layout)


class MyThread1(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.exiting = False

    def run(self):
        while self.exiting == False:
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(1)


class ParametersPlemiona():
    def __init__(self):
        self.browser = None

    def signIn(self, username, password, world):
        self.browser = webdriver.Chrome()
        self.browser.get('https://www.plemiona.pl/')
        # time.sleep(1)

        usernameInput = self.browser.find_elements_by_css_selector('input')[1]
        passwordInput = self.browser.find_elements_by_css_selector('input')[3]
        buttonLogin = self.browser.find_element(By.XPATH,
                                                '/html/body/div[3]/div[4]/div[10]/div[3]/div[2]/form/div/div/a')
        # usernameInput = self.browser.find_element_by_name("username")
        # passwordInput = self.browser.find_element_by_name("password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        # passwordInput.send_keys(Keys.ENTER)
        buttonLogin.click()
        time.sleep(0.5)

        # worldInput = self.browser.find_element(By.XPATH,"/html/body/div[3]/div[4]/div[10]/div[3]/div[2]/div[1]/a[3]/span")
        # worldInput = self.browser.find_element(By.XPATH,"//a[@href='/page/play/pl152']")
        self.browser.get('https://www.plemiona.pl/' + 'page/play/pl' + world)
        '''
        # worldInput.click()
        time.sleep(2)
        self.browser.get('https://pl' + world1 + '.plemiona.pl' + '/game.php?village=&screen=barracks')
        time.sleep(1)
        # koszary = self.browser.find_element(By.XPATH,'/game.php?village=26574&screen=barracks').click()
        #axemenInput = browser1.find_element(By.XPATH, "//*[@id='axe_0']")
        #axemenInput.send_keys(10)
        #buttonRecruitment = buttonLogin = browser1.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td[2]/input')
        #buttonRecruitment.click()
        '''

    def getTime(self):
        timer = self.browser.find_element(By.XPATH, "//*[@id='serverTime']")
        text = timer.text
        return text

    def wedge(self, hour, minute, second, millisecond):
        return 0


# bot.signin()
schedule.run_pending()
app = QApplication(sys.argv)
bot = PlemionaBot()
bot.show()
app.exec_()

# window.geometry('1000x700')
'''
usernameLabel = Label(window, text="Username")
usernameLabel.grid(row=0, column=0)
usernameInput = Entry(window)
usernameInput.grid(row=0, column=1)

passwordLabel = Label(window, text="Password")
passwordLabel.pack(row=1, column=0)
passwordInput = Entry(window)
passwordInput.grid(row=1, column=1)
'''

# greeting = tk.Label(text="Hello, Tkinter")
# window.mainloop()
