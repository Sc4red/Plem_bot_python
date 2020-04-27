import tkinter as tk
from tkinter import *

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtCore

from selenium import webdriver  # todo import webdriver
from selenium.webdriver.common.by import By  # todo import By for XPATH
from selenium.common.exceptions import NoSuchElementException, WebDriverException

import time
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys

from QLed import QLed


class PlemionaBot(QMainWindow):  # todo klasa odpowiada za wywołąnie wszystkich elementów okna MainWindow
    def __init__(self):
        super(PlemionaBot, self).__init__()
        self.main_widget = Widget(self)
        self.app()

    def app(self):
        #self.setGeometry(0, 0, 500, 500)
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
        self.bot = ParametersPlemiona()

        self.button_Login = QPushButton("Login")
        self.button_Checkpassword = QPushButton()
        self.button_Checkpassword.setIcon(QIcon("image/check_password.png"))
        self.password_Input = QLineEdit()
        self.username_Input = QLineEdit()
        self.world_Input = QLineEdit()
        self.led_Login = QLed(shape=QLed.Circle, onColour=QLed.Red, value=True)
        self.login_Box = QGroupBox("LOGIN")
        self.button_Checkpassword.setFixedSize(20, 20)
        self.password_Input.setFixedSize(100, 20)
        self.username_Input.setFixedSize(100, 20)
        self.world_Input.setFixedSize(100, 20)
        self.led_Login.setFixedSize(20, 20)

        self.button_Wedge = QPushButton("Wedge")
        self.input_Hour = QLineEdit()
        self.input_Minute = QLineEdit()
        self.input_Second = QLineEdit()
        self.input_Millisecond = QLineEdit()
        self.wedge_Box = QGroupBox("WEDGE")
        self.input_Hour.setFixedSize(50, 20)
        self.input_Minute.setFixedSize(50, 20)
        self.input_Second.setFixedSize(50, 20)
        self.input_Millisecond.setFixedSize(50, 20)

        self.time_Input = QLineEdit()
        self.time_Box = QGroupBox("TIME")

        self.button_BackArmy = QPushButton("Back")
        self.backarmy_Box = QGroupBox("BACK")

        self.button_Sendautoattack = QPushButton("Send auto attack")
        self.input_Numbervillage = QLineEdit()
        self.input_CoordinateXvillage = QLineEdit()
        self.input_CoordinateYvillage = QLineEdit()
        self.input_Pikeman = QLineEdit()
        self.input_Swordfish = QLineEdit()
        self.input_Axeman = QLineEdit()
        self.input_Scout = QLineEdit()
        self.input_Lightcavalery = QLineEdit()
        self.input_Heavycavalery = QLineEdit()
        self.input_Ram = QLineEdit()
        self.input_Catapult = QLineEdit()
        self.input_Knight = QLineEdit()
        self.input_Nobleman = QLineEdit()
        self.input_Trooptraveltimehour = QLineEdit()
        self.input_Trooptraveltimeminute = QLineEdit()
        self.sendautoattack_Box = QGroupBox("SEND AUTO ATTACK")
        self.input_Numbervillage.setFixedSize(50, 20)
        self.input_CoordinateXvillage.setFixedSize(50, 20)
        self.input_CoordinateYvillage.setFixedSize(50, 20)
        self.input_Pikeman.setFixedSize(50, 20)
        self.input_Swordfish.setFixedSize(50, 20)
        self.input_Axeman.setFixedSize(50, 20)
        self.input_Scout.setFixedSize(50, 20)
        self.input_Lightcavalery.setFixedSize(50, 20)
        self.input_Heavycavalery.setFixedSize(50, 20)
        self.input_Ram.setFixedSize(50, 20)
        self.input_Catapult.setFixedSize(50, 20)
        self.input_Knight.setFixedSize(50, 20)
        self.input_Nobleman.setFixedSize(50, 20)
        self.input_Trooptraveltimehour.setFixedSize(50, 20)
        self.input_Trooptraveltimeminute.setFixedSize(50, 20)

        self.createLayoutLogin()
        self.createLayoutWedge()
        self.createLayoutTime()
        self.createLayoutBackArmy()
        self.createLayoutSendAutoAttack()

        self.thread1 = MyThread1(self.time_Input, self.bot, self.button_Login, self.button_Wedge, self.button_BackArmy, self.led_Login)
        self.thread3 = MyThread3(self.bot, self.world_Input, self.input_Numbervillage)

        box = QGridLayout()
        box.addWidget(self.login_Box, 0, 0, 2, 10)
        box.addWidget(self.wedge_Box, 0, 10, 1, 8)
        box.addWidget(self.backarmy_Box, 1, 10, 1, 20)
        box.addWidget(self.time_Box, 2, 0, 1, 10)
        box.addWidget(self.sendautoattack_Box, 2, 10, 10, 20)

        self.setLayout(box)

    def buttonLogin(self):
        bool1 = True
        username = self.username_Input.text()
        password = self.password_Input.text()
        world = self.world_Input.text()
        bool1 = self.bot.signIn(username, password, world)
        if bool1 != False:
            self.button_Login.setEnabled(False)
            self.button_Wedge.setEnabled(True)
            self.button_BackArmy.setEnabled(True)
            self.led_Login.setOnColour(QLed.Green)
        # self.thrend1.terminated.connect(self.printed)
        # self.thrend1.started.connect(self.timerApp)
        if self.thread1.isRunning():
            self.thread1.exiting = True
            while self.thread1.isRunning():
                time.sleep(0.01)
                continue
        else:
            self.thread1.exiting = False
            self.thread1.start()
            while not self.thread1.isRunning():
                time.sleep(0.01)
                continue

    def buttonCheckpassword(self):
        if self.password_Input.echoMode() == QLineEdit.Password:
            self.password_Input.setEchoMode(QLineEdit.Normal)
        else:
            self.password_Input.setEchoMode(QLineEdit.Password)

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
        else:
            self.thrend2.exiting = False
            self.thrend2.start()
            while not self.thrend2.isRunning():
                time.sleep(0.01)
                continue

    def buttonBackArmy(self):
        if self.thread3.isRunning():
            self.thread3.exiting = True
            while self.thread3.isRunning():
                time.sleep(0.01)
                continue
        else:
            self.thread3.exiting = False
            self.thread3.start()
            while not self.thread3.isRunning():
                time.sleep(0.01)
                continue

    def buttonSendAttack(self):
        self.button_Login.setEnabled(False)
        hour = self.input_Hour.text()
        minute = self.input_Minute.text()
        second = self.input_Second.text()
        millisecond = self.input_Millisecond.text()

        username = self.username_Input.text()
        password = self.password_Input.text()
        world = self.world_Input.text()

        number_village = self.input_Numbervillage.text()

        world = self.world_Input.text()

        coordinateXvillage = self.input_CoordinateXvillage.text()
        coordinateYvillage = self.input_CoordinateYvillage.text()
        pikeman = self.input_Pikeman.text()
        swordfish = self.input_Swordfish.text()
        axeman = self.input_Axeman.text()
        scout = self.input_Scout.text()
        lightcavalery = self.input_Lightcavalery.text()
        heavycavalery = self.input_Heavycavalery.text()
        ram = self.input_Ram.text()
        catapult = self.input_Catapult.text()
        knight = self.input_Knight.text()
        nobleman = self.input_Nobleman.text()
        trooptraveltime_hour = self.input_Trooptraveltimehour.text()
        trooptraveltime_minute = self.input_Trooptraveltimeminute.text()

        self.thread4 = MyThread4(self.bot, username, password, world, hour, minute, second, millisecond, number_village,
                                 coordinateXvillage, coordinateYvillage, pikeman, swordfish, axeman, scout,
                                 lightcavalery, heavycavalery, ram, catapult, knight, nobleman, trooptraveltime_hour,
                                 trooptraveltime_minute)

        if self.thread4.isRunning():
            self.thread4.exiting = True
            while self.thread4.isRunning():
                time.sleep(0.01)
                continue
        else:
            self.thread4.exiting = False
            self.thread4.start()
            while not self.thread4.isRunning():
                time.sleep(0.01)
                continue

    def timerApp(self):
        self.time_Input.clear()
        self.time_Input.setText(self.bot.getTime())
        # self.thrend1.on_source(self, self.bot.getTime)

    def createLayoutLogin(self):
        grid_layout = QGridLayout()

        username_label = QLabel("Username:")
        password_label = QLabel("Password:")
        world_label = QLabel("World:")

        self.password_Input.setEchoMode(QLineEdit.Password)  # Hasło zasłonięte

        # self.button_Login.setCheckable(True)
        self.button_Login.clicked.connect(self.buttonLogin)
        self.button_Checkpassword.clicked.connect(self.buttonCheckpassword)

        grid_layout.addWidget(username_label, 0, 0, 1, 1)
        grid_layout.addWidget(self.username_Input, 0, 1, 1, 1)
        grid_layout.addWidget(password_label, 1, 0, 1, 1)
        grid_layout.addWidget(self.password_Input, 1, 1, 1, 1)
        grid_layout.addWidget(world_label, 2, 0, 1, 1)
        grid_layout.addWidget(self.world_Input, 2, 1, 1, 1)
        grid_layout.addWidget(self.button_Login, 3, 0, 1, 2)
        grid_layout.addWidget(self.led_Login, 3, 2, 1, 1)
        grid_layout.addWidget(self.button_Checkpassword, 1, 2, 1, 1)

        self.login_Box.setLayout(grid_layout)

    def createLayoutWedge(self):
        grid_layout = QGridLayout()

        hour_label = QLabel("HOUR(00)")
        minute_label = QLabel("MINUTE(00)")
        second_label = QLabel("SECOND(00)")
        millisecond_label = QLabel("MILLISECOND(000)")

        self.button_Wedge.setEnabled(False)
        self.button_Wedge.clicked.connect(self.buttonWedge)

        grid_layout.addWidget(hour_label, 0, 0, 1, 1)
        grid_layout.addWidget(self.input_Hour, 1, 0, 1, 1)
        grid_layout.addWidget(minute_label, 0, 1, 1, 1)
        grid_layout.addWidget(self.input_Minute, 1, 1, 1, 1)
        grid_layout.addWidget(second_label, 0, 2, 1, 1)
        grid_layout.addWidget(self.input_Second, 1, 2, 1, 1)
        grid_layout.addWidget(millisecond_label, 0, 3, 1, 1)
        grid_layout.addWidget(self.input_Millisecond, 1, 3, 1, 1)
        grid_layout.addWidget(self.button_Wedge, 2, 0, 1, 4)

        self.wedge_Box.setLayout(grid_layout)

    def createLayoutTime(self):
        grid_layout = QGridLayout()

        time_label = QLabel("Time")

        grid_layout.addWidget(time_label, 0, 0, 1, 1)
        grid_layout.addWidget(self.time_Input, 0, 1, 1, 1)

        self.time_Box.setLayout(grid_layout)

    def createLayoutBackArmy(self):
        grid_layout = QGridLayout()

        self.button_BackArmy.setEnabled(False)
        self.button_BackArmy.clicked.connect(self.buttonBackArmy)

        grid_layout.addWidget(self.button_BackArmy, 0, 0)
        grid_layout.addWidget(self.input_Numbervillage, 1, 0)

        self.backarmy_Box.setLayout(grid_layout)

    def createLayoutSendAutoAttack(self):
        grid_layout = QGridLayout()

        numbervillage_label = QLabel("Number village:")
        cordinateXvillage_label = QLabel("Cordinate X:")
        cordinateYvillage_label = QLabel("Cordinate Y:")
        tips_label = QLabel("TIPS: W celu użycia tej ramki należy wypełnić wszystkie pola w ramkach: LOGIN, WEDGE,\n"
                            "SEND AUTO ATTACK. Numer wioski należy odczytać z linku jak przejdziesz do konkretnej\n"
                            "wioski, ten numer jest po village=, np. 26527.\n"
                            "W polach gdzie jest podany odpowiedni format należy się do niego stosować, np. cyfrę\n"
                            "jeden zapisujemy jako dwa znaki,NIE JEDEN (00)->01,05,20 itp.\n"
                            "Gdy format jedt nie podany, nie jest konieczne usupełnienie danego pola, oprócz ramki LOGIN\n"
                            "Gdy chcemy wysłaś zautomatyzowany atak nie klikamy przycisku login, tylko Send auto attack\n"
                            "UWAGA!!! Gdy przejdziesz do Trop travel time: to ta zakładka oznacza długość podróży\n"
                            "twoich wojsk(na plemionach jest to oznaczone jako trwanie)")
        pikeman_label = QLabel()
        swordfish_label = QLabel()
        axeman_label = QLabel()
        scout_label = QLabel()
        lightcavalery_label = QLabel()
        heavycavalery_label = QLabel()
        ram_label = QLabel()
        catapult_label = QLabel()
        knight_label = QLabel()
        nobleman_label = QLabel()
        trooptraveltime_label = QLabel("Trop travel time:")
        trooptraveltimehour_label = QLabel("HOUR(00)")
        trooptraveltimeminute_label = QLabel("MIN(00)")

        pikeman_label.setPixmap(QPixmap("image/unit_spear.png"))
        swordfish_label.setPixmap(QPixmap("image/unit_sword.png"))
        axeman_label.setPixmap(QPixmap("image/unit_axe.png"))
        scout_label.setPixmap(QPixmap("image/unit_spy.png"))
        lightcavalery_label.setPixmap(QPixmap("image/unit_light.png"))
        heavycavalery_label.setPixmap(QPixmap("image/unit_heavy.png"))
        ram_label.setPixmap(QPixmap("image/unit_ram.png"))
        catapult_label.setPixmap(QPixmap("image/unit_catapult.png"))
        knight_label.setPixmap(QPixmap("image/unit_knight.png"))
        nobleman_label.setPixmap(QPixmap("image/unit_snob.png"))

        self.button_Sendautoattack.clicked.connect(self.buttonSendAttack)

        grid_layout.addWidget(numbervillage_label, 0, 0, 1, 1)
        grid_layout.addWidget(self.input_Numbervillage, 0, 1, 1, 1)
        grid_layout.addWidget(cordinateXvillage_label, 1, 0, 1, 1)
        grid_layout.addWidget(self.input_CoordinateXvillage, 1, 1, 1, 1)
        grid_layout.addWidget(cordinateYvillage_label, 2, 0, 1, 1)
        grid_layout.addWidget(self.input_CoordinateYvillage, 2, 1, 1, 1)
        grid_layout.addWidget(trooptraveltime_label, 3, 0, 1, 1)
        grid_layout.addWidget(trooptraveltimehour_label, 4, 1, 1, 1)
        grid_layout.addWidget(self.input_Trooptraveltimehour, 4, 2, 1, 2)
        grid_layout.addWidget(trooptraveltimeminute_label, 4, 5, 1, 1)
        grid_layout.addWidget(self.input_Trooptraveltimeminute, 4, 6, 1, 2)

        grid_layout.addWidget(pikeman_label, 0, 2, 1, 1)
        grid_layout.addWidget(swordfish_label, 1, 2, 1, 1)
        grid_layout.addWidget(axeman_label, 2, 2, 1, 1)
        grid_layout.addWidget(self.input_Pikeman, 0, 3, 1, 1)
        grid_layout.addWidget(self.input_Swordfish, 1, 3, 1, 1)
        grid_layout.addWidget(self.input_Axeman, 2, 3, 1, 1)

        grid_layout.addWidget(scout_label, 0, 4, 1, 1)
        grid_layout.addWidget(lightcavalery_label, 1, 4, 1, 1)
        grid_layout.addWidget(heavycavalery_label, 2, 4, 1, 1)
        grid_layout.addWidget(self.input_Scout, 0, 5, 1, 1)
        grid_layout.addWidget(self.input_Lightcavalery, 1, 5, 1, 1)
        grid_layout.addWidget(self.input_Heavycavalery, 2, 5, 1, 1)

        grid_layout.addWidget(ram_label, 0, 6, 1, 1)
        grid_layout.addWidget(catapult_label, 1, 6, 1, 1)
        grid_layout.addWidget(self.input_Ram, 0, 7, 1, 1)
        grid_layout.addWidget(self.input_Catapult, 1, 7, 1, 1)

        grid_layout.addWidget(knight_label, 0, 8, 1, 1)
        grid_layout.addWidget(nobleman_label, 1, 8, 1, 1)
        grid_layout.addWidget(self.input_Knight, 0, 9, 1, 1)
        grid_layout.addWidget(self.input_Nobleman, 1, 9, 1, 1)

        grid_layout.addWidget(self.button_Sendautoattack, 5, 0, 1, 10)

        grid_layout.addWidget(tips_label, 6, 0, 1, 10)

        self.sendautoattack_Box.setLayout(grid_layout)


class MyThread1(QThread):  # todo klasa odpowiedzialna za aktualizacje czasu w aplikacji
    def __init__(self, input, bot, buttonlogin, buttonwedge, buttobackarmy, ledlogin, parent=None):
        QThread.__init__(self, parent)
        self.input = input
        self.bot = bot
        self.buttonlogin = buttonlogin
        self.buttonwedge = buttonwedge
        self.buttobackarmy = buttobackarmy
        self.ledlogin = ledlogin
        self.exiting = False

    def run(self):
        while self.exiting == False:
            bool1 = self.bot.getTime()
            if bool1 == True:
                self.input.setText("00:00:00")
                self.buttonlogin.setEnabled(True)
                self.buttonwedge.setEnabled(False)
                self.buttobackarmy.setEnabled(False)
                self.ledlogin.setOnColour(QLed.Red)
                break
            self.input.setText(bool1)
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
        # self.exit()


class MyThread3(QThread):  # todo klasa odpowiedzialna za aktualizacje czasu w aplikacji
    def __init__(self, bot, world, number_village, parent=None):
        QThread.__init__(self, parent)
        self.bot = bot
        self.world = world
        self.number_village = number_village
        self.exiting = False

    def run(self):
        # while self.exiting == False:
        self.bot.getBackArmy(self.world, self.number_village)
        # sys.stdout.write('*')
        # sys.stdout.flush()
        # time.sleep(0.1)


class MyThread4(QThread):  # todo klasa odpowiedzialna za automatyczne wybranie wioski i jej zaatakowanie
    def __init__(self, bot, username, password, world, hour, minute, second, millisecond, number_village,
                 coordinateXvillage, coordinateYvillage, pikeman, swordfish, axeman, scout, lightcavalery,
                 heavycavalery, ram, catapult, knight, nobleman, trooptraveltime_hour, trooptraveltime_minute, parent=None):
        QThread.__init__(self, parent)
        self.exiting = False
        self.bot = bot
        self.username = username
        self.password = password
        self.world = world
        self.hour = hour
        self.minute = minute
        self.second = second
        self.millisecond = millisecond
        self.number_village = number_village
        self.coordinateXvillage = coordinateXvillage
        self.coordinateYvillage = coordinateYvillage
        self.pikeman = pikeman
        self.swordfish = swordfish
        self.axeman = axeman
        self.scout = scout
        self.lightcavalery = lightcavalery
        self.heavycavalery = heavycavalery
        self.ram = ram
        self.catapult = catapult
        self.knight = knight
        self.nobleman = nobleman
        self.trooptraveltime_hour = trooptraveltime_hour
        self.trooptraveltime_minute = trooptraveltime_minute


    def run(self):
        # while self.exiting == False:
        #print().time().strftime("%H:%M:%S")
        h = int(self.hour) - int(self.trooptraveltime_hour)
        m = int(self.minute) - int(self.trooptraveltime_minute) - 2
        if m < 0:
            m = 60 + m
            h = h - 1
        if h < 0:
            h = 24 + h

        if len(str(h)) < 2:
            h = "0" + str(h)
        else:
            h = str(h)

        if len(str(m)) < 2:
            m = "0" + str(m)
        else:
            m = str(m)
        hour = str(h) + ":" + str(m)
        print(hour)
        while hour != datetime.now().strftime("%H:%M"):
            time.sleep(60)

        self.bot.signIn(self.username, self.password, self.world)
        self.bot.sendAutoAttack(self.world, self.number_village, self.coordinateXvillage, self.coordinateYvillage,
                                self.pikeman, self.swordfish, self.axeman, self.scout, self.lightcavalery,
                                self.heavycavalery, self.ram, self.catapult, self.knight, self.nobleman)
        self.bot.wedge(self.hour, self.minute, self.second, self.millisecond)
        self.bot.browser = None


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
        time.sleep(1)

        # worldInput = self.browser.find_element(By.XPATH,"/html/body/div[3]/div[4]/div[10]/div[3]/div[2]/div[1]/a[3]/span")
        # worldInput = self.browser.find_element(By.XPATH,"//a[@href='/page/play/pl152']")
        self.browser.get('https://www.plemiona.pl/' + 'page/play/pl' + world)
        try:
            self.browser.find_element_by_id('serverTime')
        except NoSuchElementException:
            print("Błąd w danych od logowania zresetuj przeglądarke i wprowadź poprawnie dane")
            return False
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

    def sendAutoAttack(self, world, number_village, coordinateXvillage, coordinateYvillage, pikeman, swordfish, axeman,
                       scout, lightcavalery, heavycavalery, ram, catapult, knight, nobleman):
        try:
            self.browser.get('https://pl' + world + '.plemiona.pl' + '/game.php?village=n' + number_village + '&screen=place')
            time.sleep(1)
            self.browser.find_element_by_name('input').send_keys(coordinateXvillage + coordinateYvillage)
            self.browser.find_element_by_id('unit_input_spear').send_keys(pikeman)
            self.browser.find_element_by_id('unit_input_sword').send_keys(swordfish)
            self.browser.find_element_by_id('unit_input_axe').send_keys(axeman)
            self.browser.find_element_by_id('unit_input_spy').send_keys(scout)
            self.browser.find_element_by_id('unit_input_light').send_keys(lightcavalery)
            self.browser.find_element_by_id('unit_input_heavy').send_keys(heavycavalery)
            self.browser.find_element_by_id('unit_input_ram').send_keys(ram)
            self.browser.find_element_by_id('unit_input_catapult').send_keys(catapult)
            self.browser.find_element_by_id('unit_input_knight').send_keys(knight)
            self.browser.find_element_by_id('unit_input_snob').send_keys(nobleman)
            self.browser.find_element_by_id('target_attack').click()
        except NoSuchElementException:
            print("Brak elementu, wprowadź dane poprawnie")

    def getBackArmy(self, world, number_village):
        self.browser.get('https://pl' + world + '.plemiona.pl' + '/game.php?village=n' + number_village + '&screen=place')

    def getTimeAttack(self):
        timer = self.browser.find_element_by_class_name('relative_time')
        text = timer.text
        textlength = len(text)
        hour = text[textlength - 8] + text[textlength - 7] + text[textlength - 6] + text[textlength - 5] + text[
            textlength - 4] + text[
                   textlength - 3] + text[textlength - 2] + text[textlength - 1]
        return hour

    def getTime(self):
        try:
            self.browser.find_element_by_id('serverTime')
            timer = self.browser.find_element_by_id('serverTime')
            return timer.text
        except NoSuchElementException:
            return "00:00:00"
        except WebDriverException:
            self.browser = None
            return True


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
