import tkinter as tk
from tkinter import *

from PyQt5.QtWidgets import *

from selenium import webdriver  # todo import webdriver
from selenium.webdriver.common.by import By  # todo import By for XPATH

import time
from selenium.webdriver.common.keys import Keys


class PlemionaBot(QMainWindow):  # todo main class plemiona
    def __init__(self):
        super(PlemionaBot, self).__init__()
        self.app()

    def app(self):
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Pleminona")

        self.main_widget = Widget(self)
        self.setCentralWidget(self.main_widget)
        self.show()


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__()
        self.buttonWedge = QPushButton("Wedge")
        self.inputMilisecond = QLineEdit()
        self.inputSecond = QLineEdit()
        self.inputMinute = QLineEdit()
        self.inputHour = QLineEdit()
        self.wedgeBox = QGroupBox("WEDGE")
        self.buttonLogin = QPushButton("Login", self)
        self.worldInput = QLineEdit()
        self. passwordInput = QLineEdit()
        self.usernameInput = QLineEdit()
        self.loginBox = QGroupBox("LOGIN")
        self.bot = ParametersPlemiona()
        self.createLeyoutLogin()
        self.createLeyoutWedge()
        self.createLeyoutWedge2()

        box = QGridLayout()
        box.addWidget(self.loginBox, 0, 0)
        box.addWidget(self.wedgeBox, 0, 1)
        box.addWidget(self.wedgeBox2, 1, 1)

        self.setLayout(box)

    def buttonStatus(self):
        if self.buttonLogin.pressed():
            self.buttonLogin.setEnabled(False)
            username = self.usernameInput.text()
            password = self.passwordInput.text()
            world = self.worldInput.text()
            self.bot.signIn(username, password, world)
        elif self.buttonWedge.pressed():
            print("nie klikniety")

    def createLeyoutLogin(self):
        grid_layout = QGridLayout()

        username_label = QLabel("Username")
        password_label = QLabel("Password")
        world_label = QLabel("World")

        self.passwordInput.setEchoMode(2)  # Hasło zasłonięte

        self.buttonLogin.setCheckable(True)
        self.buttonLogin.clicked.connect(self.buttonStatus)

        grid_layout.addWidget(username_label, 0, 0)
        grid_layout.addWidget(self.usernameInput, 0, 1)
        grid_layout.addWidget(password_label, 1, 0)
        grid_layout.addWidget(self.passwordInput, 1, 1)
        grid_layout.addWidget(world_label, 2, 0)
        grid_layout.addWidget(self.worldInput, 2, 1)
        grid_layout.addWidget(self.buttonLogin, 3, 1)

        self.loginBox.setLayout(grid_layout)

    def createLeyoutWedge(self):
        grid_layout = QGridLayout()

        hour_label = QLabel("HOUR(00)")
        minute_label = QLabel("MINUTE(00)")
        second_label = QLabel("SECOND(00)")
        millisecond_label = QLabel("MILLISECOND(000)")

        self.buttonWedge.clicked.connect(self.buttonStatus)

        grid_layout.addWidget(hour_label, 0, 0)
        grid_layout.addWidget(self.inputHour, 1, 0)
        grid_layout.addWidget(minute_label, 0, 1)
        grid_layout.addWidget(self.inputMinute, 1, 1)
        grid_layout.addWidget(second_label, 0, 2)
        grid_layout.addWidget(self.inputSecond, 1, 2)
        grid_layout.addWidget(millisecond_label, 0, 3)
        grid_layout.addWidget(self.inputMilisecond, 1, 3)
        grid_layout.addWidget(self.buttonWedge, 2, 3)

        self.wedgeBox.setLayout(grid_layout)

    def createLeyoutWedge2(self):
        self.wedgeBox2 = QGroupBox("Klin")
        gridlayout2 = QGridLayout()

        usernameLabel2 = QLabel("Username")
        passwordLabel2 = QLabel("Password")

        usernameInput2 = QLineEdit()
        passwordInput2 = QLineEdit()

        gridlayout2.addWidget(usernameLabel2, 0, 0)
        gridlayout2.addWidget(usernameInput2, 0, 1)
        gridlayout2.addWidget(passwordLabel2, 1, 0)
        gridlayout2.addWidget(passwordInput2, 1, 1)

        self.wedgeBox2.setLayout(gridlayout2)


class ParametersPlemiona():
    def __init__(self):
        self.browser = webdriver.Chrome()

    def signIn(self, username, password, world):
        username1 = username
        password1 = password
        world1 = world

        self.browser.get('https://www.plemiona.pl/')
        #time.sleep(1)

        usernameInput = self.browser.find_elements_by_css_selector('input')[1]
        passwordInput = self.browser.find_elements_by_css_selector('input')[3]
        buttonLogin = self.browser.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[10]/div[3]/div[2]/form/div/div/a')
        # usernameInput = self.browser.find_element_by_name("username")
        # passwordInput = self.browser.find_element_by_name("password")

        usernameInput.send_keys(username1)
        passwordInput.send_keys(password1)
        # passwordInput.send_keys(Keys.ENTER)
        buttonLogin.click()
        time.sleep(0.5)

        # worldInput = self.browser.find_element(By.XPATH,"/html/body/div[3]/div[4]/div[10]/div[3]/div[2]/div[1]/a[3]/span")
        # worldInput = self.browser.find_element(By.XPATH,"//a[@href='/page/play/pl152']")
        self.browser.get('https://www.plemiona.pl/' + 'page/play/pl' + world1)
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

# bot.signin()

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
