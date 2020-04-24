import tkinter as tk
from tkinter import *

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtCore

from selenium import webdriver  # todo import webdriver
from selenium.webdriver.common.by import By  # todo import By for XPATH
from selenium.common.exceptions import NoSuchElementException

import time
from selenium.webdriver.common.keys import Keys


class PlemionaBot(QMainWindow):  # todo klasa odpowiada za wywołąnie wszystkich elementów okna MainWindow
    def __init__(self):
        super(PlemionaBot, self).__init__()
        self.main_widget = Widget(self)
        self.app()

    def app(self):
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Pleminona")

        self.setCentralWidget(self.main_widget)
        # self.widget = Widget()

        # self.widget.time_Input.setText("321")
        # self.thrend1.started.connect(self.printed)

    def printed(self):
        self.widget.time_Input.setText("123")


class Widget(QWidget):  # todo ustawianie ukąłdu widgetów oraz ich funkcji
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
        self.thread1 = MyThread1(self.time_Input, self.bot)
        # self.thread1.started.connect(self.printed)

        box = QGridLayout()
        box.addWidget(self.login_Box, 0, 0, 2, 12)
        box.addWidget(self.wedge_Box, 0, 12, 1, 30)
        box.addWidget(self.time_Box, 3, 0, 1, 1)

        self.setLayout(box)

    def printed(self):
        print(self.bot.getTime())

    def buttonLogin(self):
        self.button_Login.setEnabled(False)
        username = self.username_Input.text()
        password = self.password_Input.text()
        world = self.world_Input.text()
        self.bot.signIn(username, password, world)
        # self.thrend1.terminated.connect(self.printed)
        # self.thrend1.started.connect(self.timerApp)
        # self.timerApp()
        # self.connect(self.thrend1, QtCore.SIGNAL('log1(QString)'), self.time_Input.setText)
        # self.time_Input.setText(self.bot.getTime())
        if self.thread1.isRunning():
            self.thread1.exiting = True
            while self.thread1.isRunning():
                time.sleep(0.01)
                continue
            # self.widget.time_Input.setText("123")
        else:
            self.thread1.exiting = False
            self.thread1.start()
            while not self.thread1.isRunning():
                time.sleep(0.01)
                continue

    def buttonWedge(self):
        hour = self.input_Hour.text()
        minute = self.input_Minute.text()
        second = self.input_Second.text()
        millisecond = self.input_Millisecond.text()

        self.thrend2 = MyThread2(self.bot, hour, minute, second, millisecond)
        if self.thrend2.isRunning():
            self.thrend2.exiting = True
            while self.thrend2.isRunning():
                time.sleep(0.01)
                continue
            # self.widget.time_Input.setText("123")
        else:
            self.thrend2.exiting = False
            self.thrend2.start()
            while not self.thrend2.isRunning():
                time.sleep(0.01)
                continue

    def timerApp(self):
        self.time_Input.clear()
        self.time_Input.setText(self.bot.getTime())
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
        self.button_Wedge.clicked.connect(self.buttonWedge)

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


class MyThread1(QThread):  # todo klasa odpowiedzialna za aktualizacje czasu w aplikacji
    sig1 = pyqtSignal(str)

    def __init__(self, input, bot, parent=None):
        QThread.__init__(self, parent)
        self.input = input
        self.bot = bot
        self.exiting = False

    def run(self):
        while self.exiting == False:
            self.input.setText(self.bot.getTime())
            # sys.stdout.write('*')
            # sys.stdout.flush()
            time.sleep(1)


class MyThread2(QThread):  # todo klasa odpowiedzialna za wywołanie klina
    def __init__(self, bot, hour, minute, second, millisecond, parent=None):
        QThread.__init__(self, parent)
        self.bot = bot
        self.hour = hour
        self.minute = minute
        self.second = second
        self.millisecond = millisecond
        self.exiting = False

    def run(self):
        # while self.exiting == False:
        self.bot.wedge(self.hour, self.minute, self.second, self.millisecond)
        self.exiting = True
        #self.exit()


class ParametersPlemiona:  # todo klasa w której analizowane są parametryw  przeglądarce a następnie poddawane obróbce
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

    def getTimeAttack(self):
        timer = self.browser.find_element_by_class_name('relative_time')
        text = timer.text
        textlength = len(text)
        hour = text[textlength - 8] + text[textlength - 7] + text[textlength - 6] + text[textlength - 5] + text[textlength - 4] + text[
            textlength - 3] + text[textlength - 2] + text[textlength - 1]
        return hour

    def getTime(self):
        try:
            self.browser.find_element_by_id('serverTime')
            timer = self.browser.find_element_by_id('serverTime')
            return timer.text
        except NoSuchElementException:
            return "00:00:00"

    def wedge(self, hour, minute, second, millisecond):
        action = True
        hour2 = hour + ":" + minute + ":" + second
        mili = float(millisecond) / 1000
        while action:
            time.sleep(0.001)
            if self.getTimeAttack() == hour2:
                time.sleep(mili)
                self.browser.find_element_by_id('troop_confirm_go').click()
                action = False


# bot.signin()
app = QApplication(sys.argv)
bott = PlemionaBot()
bott.show()
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
