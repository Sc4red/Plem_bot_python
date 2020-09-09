# import tkinter as tk
from tkinter import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.uic.properties import QtCore
from PyQt5.uic.properties import QtCore

from selenium import webdriver  # todo import webdriver
from selenium.webdriver.common.by import By  # todo import By for XPATH
from selenium.common.exceptions import NoSuchElementException, WebDriverException, NoSuchWindowException
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support import expected_conditions as EC

import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys

from QLed import QLed
from selenium.webdriver.support.wait import WebDriverWait

import pandas as pd
'''
time1 ="1:32:21"
time1 = time.strptime(time1, '%H:%M:%S')
print(time1.tm_hour)
print(time1.tm_min)
print(time1.tm_sec)
'''
class PlemionaBot(QMainWindow):  # todo klasa odpowiada za wywołąnie wszystkich elementów okna MainWindow
    def __init__(self):
        super(PlemionaBot, self).__init__()
        self.main_widget = Widget(self)
        self.app()

    def app(self):
        # self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Pleminona")
        # self.setWindowIcon(QIcon("image/plemiona_icon.png"))

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
        self.led_Wedge = QLed(shape=QLed.Circle, onColour=QLed.Red, value=True)
        self.wedge_Box = QGroupBox("WEDGE")
        self.input_Hour.setFixedSize(50, 20)
        self.input_Minute.setFixedSize(50, 20)
        self.input_Second.setFixedSize(50, 20)
        self.input_Millisecond.setFixedSize(50, 20)
        self.led_Wedge.setFixedSize(20, 20)

        self.time_Input = QLineEdit("00:00:00")
        self.time_Box = QGroupBox("TIME")

        self.button_BackArmyToBarb = QPushButton("Back army to barba")
        self.button_WriteArmyToExcel = QPushButton("Write army to excel")
        self.button_SendAutoAttackFromExcel = QPushButton("Send auto attack from EXCEL")
        self.otherbutton_Box = QGroupBox("BUTTON")

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
        self.checkbox_all_army = QCheckBox('All Army')
        # self.checkbox_all_army.stateChanged.connect(self.checkboxAllArmy)

        # self.error_dialog = QErrorMessage()
        # self.error_dialog.setWindowTitle("Error message")
        # self.error_dialog.setWindowIcon(QIcon("image/error_icon.png"))
        self.error_dialog = QMessageBox()
        self.error_dialog.setWindowIcon(QIcon("image/error_icon.png"))
        self.error_dialog.setWindowTitle("Error message")
        self.error_dialog.setIconPixmap(
            QPixmap("image/warning_icon2.png").scaled(int(QPixmap("image/warning_icon2.png").width() / 2),
                                                      int(QPixmap("image/warning_icon2.png").height() / 2)))

        self.button_FarmersAssistant = QPushButton("Farmer's assistant")
        self.farm_Box = QGroupBox("FARM")

        self.createLayoutLogin()
        self.createLayoutWedge()
        self.createLayoutTime()
        self.createLayoutOtherButton()
        self.createLayoutSendAutoAttack()
        self.createLayoutFarm()

        box = QGridLayout()
        box.addWidget(self.login_Box, 0, 0, 2, 10)
        box.addWidget(self.wedge_Box, 0, 10, 1, 8)
        box.addWidget(self.time_Box, 2, 0, 1, 10)
        box.addWidget(self.otherbutton_Box, 3, 0, 1, 10)
        box.addWidget(self.sendautoattack_Box, 2, 10, 10, 20)
        #box.addWidget(self.farm_Box, 0, 18, 2, 12)

        self.setLayout(box)

    def checkboxAllArmy(self, state):
        if Qt.Checked == state:
            print(self.checkbox_all_army.isChecked())
        else:
            print(self.checkbox_all_army.isChecked())

    def buttonLogin(self):
        bool1 = True
        username = self.username_Input.text()
        password = self.password_Input.text()
        world = self.world_Input.text()

        if username == "" or password == "" or world == "":
            # self.error_dialog.showMessage("Brak lub za mało wprowadzonych danych w ramce 'LOGIN'")
            self.error_dialog.setText("Brak lub za mało wprowadzonych danych w ramce 'LOGIN'")
            self.error_dialog.exec_()
            print("Brak lub za mało wprowadzonych danych w ramce 'LOGIN'")
            return

        bool1 = self.bot.signIn(username, password, world)

        if bool1 != False:
            self.button_Login.setEnabled(False)
            self.button_Wedge.setEnabled(True)
            self.button_BackArmyToBarb.setEnabled(True)
            self.button_WriteArmyToExcel.setEnabled(True)
            self.led_Login.setOnColour(QLed.Green)
        # self.thrend1.terminated.connect(self.printed)
        # self.thrend1.started.connect(self.timerApp)
        self.thread1 = MyThread1(self.time_Input, self.bot, self.button_Login, self.button_Wedge,
                                 self.button_BackArmyToBarb, self.button_WriteArmyToExcel, self.led_Login)
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

        if hour == "" or minute == "" or second == "" or millisecond == "":
            self.error_dialog.setText("Brak lub za mało wprowadzonych danych w ramce 'WEDGE'")
            self.error_dialog.exec_()
            print("Brak lub za mało wprowadzonych danych w ramce 'WEDGE'")
            return

        self.led_Wedge.setOnColour(QLed.Green)
        self.thrend2 = MyThread2(self.bot, hour, minute, second, millisecond, self.led_Wedge)
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
        self.thread3 = MyThread3(self.bot, self.world_Input, self.input_Numbervillage)
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

    def buttonWriteArmyToExcel(self):
        self.bot.WriteArmyToExcel(self.world_Input.text())

    def timerApp(self):
        self.time_Input.clear()
        self.time_Input.setText(self.bot.getTime())
        # self.thrend1.on_source(self, self.bot.getTime)

    def buttonSendAttack(self):
        # self.button_Login.setEnabled(False)
        hour = self.input_Hour.text()
        minute = self.input_Minute.text()
        second = self.input_Second.text()
        millisecond = self.input_Millisecond.text()

        username = self.username_Input.text()
        password = self.password_Input.text()
        world = self.world_Input.text()

        number_village = self.input_Numbervillage.text()

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
        checkboxallarmy = self.checkbox_all_army.isChecked()

        if username == "" or password == "" or world == "":
            self.error_dialog.setText("Brak lub za mało wprowadzonych danych w ramce 'LOGIN'")
            self.error_dialog.exec_()
            print("Brak lub za mało wprowadzonych danych w ramce 'LOGIN'")
            return

        if hour == "" or minute == "" or second == "" or millisecond == "":
            self.error_dialog.setText("Brak lub za mało wprowadzonych danych w ramce 'WEDGE'")
            self.error_dialog.exec_()
            print("Brak lub za mało wprowadzonych danych w ramce 'WEDGE'")
            return

        if number_village == "" or coordinateXvillage == "" or coordinateYvillage == "" or trooptraveltime_hour == "" or trooptraveltime_minute == "":
            self.error_dialog.setText("Brak lub za mało wprowadzonych danych w ramce 'SEND AUTO ATTACK'")
            self.error_dialog.exec_()
            print("Brak lub za mało wprowadzonych danych w ramce 'SEND AUTO ATTACK'")
            return

        self.thread4 = MyThread4(self.bot, username, password, world, hour, minute, second, millisecond, number_village,
                                 coordinateXvillage, coordinateYvillage, pikeman, swordfish, axeman, scout,
                                 lightcavalery, heavycavalery, ram, catapult, knight, nobleman, trooptraveltime_hour,
                                 trooptraveltime_minute, checkboxallarmy)

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

    def buttonSendAutoAttackFromExcel(self):
        excel_file = 'plemiona.xlsx'
        data_excel = pd.read_excel(excel_file, sheet_name=0)
        #print(data_excel)
        data_excel = data_excel.fillna(0)
        # print(data_excel)
        rows = data_excel.shape[0]
        columns = data_excel.shape[1]
        # movies = movies.head(5)
        # print(movies.get(key='Genres'))
        # movies1 = movies.get(key='Genres')
        # print(movies.shape[0])
        username = self.username_Input.text()
        password = self.password_Input.text()
        world = self.world_Input.text()

        if username == "" or password == "" or world == "":
            self.error_dialog.setText("Brak lub za mało wprowadzonych danych w ramce 'LOGIN'")
            self.error_dialog.exec_()
            print("Brak lub za mało wprowadzonych danych w ramce 'LOGIN'")
            return

        for i in range(rows):
            #print(i)
            # date = data_excel.at[i, 'Action date'].strftime("%m/%d/%Y, %H:%M:%S.%f")[:-3]
            # print(date)
            hour = str(data_excel.at[i, 'Action date'].strftime("%H"))
            minute = str(data_excel.at[i, 'Action date'].strftime("%M"))
            second = str(data_excel.at[i, 'Action date'].strftime("%S"))
            millisecond = str(data_excel.at[i, 'Action date'].strftime("%f")[:-3])

            number_village = str(data_excel.at[i, 'Number village'])

            coordinateXvillage = str(data_excel.at[i, 'Cordinate'])
            # print(coordinateXvillage)
            coordinateYvillage = ""
            pikeman = int(data_excel.at[i, 'spear'])
            swordfish = int(data_excel.at[i, 'sword'])
            axeman = int(data_excel.at[i, 'axe'])
            scout = int(data_excel.at[i, 'spy'])
            lightcavalery = int(data_excel.at[i, 'light'])
            heavycavalery = int(data_excel.at[i, 'heavy'])
            ram = int(data_excel.at[i, 'ram'])
            catapult = int(data_excel.at[i, 'catapult'])
            knight = int(data_excel.at[i, 'knight'])
            nobleman = int(data_excel.at[i, 'snob'])
            # print(nobleman)
            trooptraveltime_hour = str(data_excel.at[i, 'Troop travel time'].strftime("%H"))
            trooptraveltime_minute = str(data_excel.at[i, 'Troop travel time'].strftime("%M"))
            checkboxallarmy = bool(data_excel.at[i, 'All army'])
            # print(checkboxallarmy)

            self.thread4 = MyThread4(self.bot, username, password, world, hour, minute, second, millisecond,
                                     number_village,
                                     coordinateXvillage, coordinateYvillage, pikeman, swordfish, axeman, scout,
                                     lightcavalery, heavycavalery, ram, catapult, knight, nobleman,
                                     trooptraveltime_hour,
                                     trooptraveltime_minute, checkboxallarmy)

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
            time.sleep(0.5)

    def buttonFarmersAssistant(self):
        print("1")
        '''
        #settings
        max_ressources = 99999
        archers = 0
        skip_level_1 = 0

        #settings_spear
        untouchable_spear = 0
        max_unit_number_spear = 9999
        conditional_safeguard_spear = 0

        #settings_sword
        untouchable_sword = 0
        max_unit_number_sword = 9999
        conditional_safeguard_sword = 0

        #settings_axe
        untouchable_axe = 0
        max_unit_number_axe = 9999
        conditional_safeguard_axe = 0

        # settings_archer
        untouchable_archer = 0
        max_unit_number_archer = 9999
        conditional_safeguard_archer = 0
        '''
        username = self.username_Input.text()
        password = self.password_Input.text()
        world = self.world_Input.text()

        if username == "" or password == "" or world == "":
            self.error_dialog.setText("Brak lub za mało wprowadzonych danych w ramce 'LOGIN'")
            self.error_dialog.exec_()
            print("Brak lub za mało wprowadzonych danych w ramce 'LOGIN'")
            return

        self.thread5 = MyThread5(self.bot, username, password, world)

        if self.thread5.isRunning():
            self.thread5.exiting = True
            while self.thread5.isRunning():
                time.sleep(0.01)
                continue
        else:
            self.thread5.exiting = False
            self.thread5.start()
            while not self.thread5.isRunning():
                time.sleep(0.01)
                continue

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
        grid_layout.addWidget(self.led_Wedge, 2, 4, 1, 1)

        # grid_layout.addWidget(self.button_BackArmy, 0, 5, 1, 1)
        # grid_layout.addWidget(self.input_Numbervillage, 1, 0)

        self.wedge_Box.setLayout(grid_layout)

    def createLayoutTime(self):
        grid_layout = QGridLayout()

        # time_label = QLabel("Time")

        # grid_layout.addWidget(time_label, 0, 0, 1, 1)
        grid_layout.addWidget(self.time_Input, 0, 0, 1, 1)

        self.time_Box.setLayout(grid_layout)

    def createLayoutOtherButton(self):
        grid_layout = QGridLayout()

        self.button_BackArmyToBarb.setEnabled(False)
        self.button_BackArmyToBarb.clicked.connect(self.buttonBackArmy)
        self.button_WriteArmyToExcel.setEnabled(False)
        self.button_WriteArmyToExcel.clicked.connect(self.buttonWriteArmyToExcel)
        self.button_SendAutoAttackFromExcel.setEnabled(True)
        self.button_SendAutoAttackFromExcel.clicked.connect(self.buttonSendAutoAttackFromExcel)
        tips_label = QLabel("TIPS: Gdy używasz przycisku 'Send auto attack from EXCEL' to: WYPEŁNIJ POLA W RAMCJE "
                            "LOGIN INACZEJ NIE ZADZIAŁA!!! ")
        tips_label.setStyleSheet("background-color: yellow;  border: 2px solid black;")
        tips_label.setFont(QFont('Calibri', 10))
        tips_label.setWordWrap(TRUE)
        tips_label.setMaximumSize(200, 200)
        grid_layout.addWidget(self.button_BackArmyToBarb, 0, 0, 1, 1)
        grid_layout.addWidget(self.button_WriteArmyToExcel, 1, 0, 1, 1)
        grid_layout.addWidget(self.button_SendAutoAttackFromExcel, 2, 0, 1, 1)
        grid_layout.addWidget(tips_label, 3, 0, 1, 1)

        self.otherbutton_Box.setLayout(grid_layout)

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
                            "UWAGA!!! Gdy przejdziesz do Troop travel time: to ta zakładka oznacza długość podróży\n"
                            "twoich wojsk(na plemionach jest to oznaczone jako trwanie)")
        pikeman_label = QLabel(alignment=Qt.AlignRight)
        swordfish_label = QLabel(alignment=Qt.AlignRight)
        axeman_label = QLabel(alignment=Qt.AlignRight)
        scout_label = QLabel(alignment=Qt.AlignRight)
        lightcavalery_label = QLabel(alignment=Qt.AlignRight)
        heavycavalery_label = QLabel(alignment=Qt.AlignRight)
        ram_label = QLabel(alignment=Qt.AlignRight)
        catapult_label = QLabel(alignment=Qt.AlignRight)
        knight_label = QLabel(alignment=Qt.AlignRight)
        nobleman_label = QLabel(alignment=Qt.AlignRight)
        trooptraveltime_label = QLabel("Troop travel time:")
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

        grid_layout.addWidget(self.checkbox_all_army, 0, 10, 1, 1)

        grid_layout.addWidget(self.button_Sendautoattack, 5, 0, 1, 10)

        grid_layout.addWidget(tips_label, 6, 0, 1, 10)

        self.sendautoattack_Box.setLayout(grid_layout)

    def createLayoutFarm(self):
        grid_layout = QGridLayout()

        self.button_FarmersAssistant.setEnabled(True)
        self.button_FarmersAssistant.clicked.connect(self.buttonFarmersAssistant)

        grid_layout.addWidget(self.button_FarmersAssistant, 0, 0, 1, 1)

        self.farm_Box.setLayout(grid_layout)


class MyThread1(QThread):  # todo klasa odpowiedzialna za aktualizacje czasu w aplikacji
    def __init__(self, input, bot, buttonlogin, buttonwedge, buttonbackarmytobarb, buttonwritearmytoexcel,
                 ledlogin, parent=None):
        QThread.__init__(self, parent)
        self.input = input
        self.bot = bot
        self.buttonlogin = buttonlogin
        self.buttonwedge = buttonwedge
        self.buttonbackarmytobarb = buttonbackarmytobarb
        self.buttonwritearmytoexcel = buttonwritearmytoexcel
        self.ledlogin = ledlogin
        self.exiting = False

    def run(self):
        while self.exiting == False:
            bool1 = self.bot.getTime()
            if bool1 == True:
                self.input.setText("00:00:00")
                self.buttonlogin.setEnabled(True)
                self.buttonwedge.setEnabled(False)
                self.buttonbackarmytobarb.setEnabled(False)
                self.buttonwritearmytoexcel.setEnabled(False)
                self.ledlogin.setOnColour(QLed.Red)
                print("Przeglądarka została zakmnieta")
                self.quit()
                break
            self.input.setText(bool1)
            # sys.stdout.write('*')
            # sys.stdout.flush()
            self.sleep(1)


class MyThread2(QThread):  # todo klasa odpowiedzialna za wywołanie klina
    def __init__(self, bot, hour, minute, second, millisecond, ledwedge, parent=None):
        QThread.__init__(self, parent)
        self.bot = bot
        self.hour = hour
        self.minute = minute
        self.second = second
        self.millisecond = millisecond
        self.ledwedge = ledwedge
        self.exiting = False

    def run(self):
        # while self.exiting == False:
        self.bot.wedge(self.hour, self.minute, self.second, self.millisecond)
        self.ledwedge.setOnColour(QLed.Red)
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
        while self.exiting == False:
            if self.bot.getBackArmy() == True:
                break
            # sys.stdout.write('*')
            # sys.stdout.flush()
            self.sleep(0.03)


class MyThread4(QThread):  # todo klasa odpowiedzialna za automatyczne wybranie wioski i jej zaatakowanie
    def __init__(self, bot, username, password, world, hour, minute, second, millisecond, number_village,
                 coordinateXvillage, coordinateYvillage, pikeman, swordfish, axeman, scout, lightcavalery,
                 heavycavalery, ram, catapult, knight, nobleman, trooptraveltime_hour, trooptraveltime_minute,
                 checkboxallarmy, parent=None):
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
        self.checkboxallarmy = checkboxallarmy

    def run(self):
        # while self.exiting == False:
        # print().time().strftime("%H:%M:%S")
        h = int(self.hour) - int(self.trooptraveltime_hour)
        m = int(self.minute) - int(self.trooptraveltime_minute) - 2
        if m < 0:
            m = 60 + m
            h = h - 1
        while h < 0:
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
        print("Zaplanowano zalogowanie sie na:", hour, "oraz wysłanie ataku do wioski", self.coordinateXvillage, "|",
              self.coordinateYvillage, "z wioski numer:", self.number_village)
        while hour != datetime.now().strftime("%H:%M"):
            self.sleep(60)
        self.bot.signIn(self.username, self.password, self.world)
        self.bot.sendAutoAttack(self.world, self.number_village, self.coordinateXvillage, self.coordinateYvillage,
                                self.pikeman, self.swordfish, self.axeman, self.scout, self.lightcavalery,
                                self.heavycavalery, self.ram, self.catapult, self.knight, self.nobleman,
                                self.checkboxallarmy)
        booll = self.bot.wedge(self.hour, self.minute, self.second, self.millisecond)
        if booll:
            print("Atak został wysłany do wioski:", self.coordinateXvillage, self.coordinateYvillage)
            print("*************************************************************")
        self.bot.closeWebDriver()
        self.bot.browser = None

    #def __del__(self):
    #    self.exiting = True
     #   self.wait()
        #self.stop()
        #self.quit()
        #self.terminate()

class MyThread5(QThread):  # todo klasa odpowiedzialna za wywołanie klina
    def __init__(self, bot, username, password, world, parent=None):
        QThread.__init__(self, parent)
        self.bot = bot
        self.username = username
        self.password = password
        self.world = world
        self.exiting = False

    def run(self):
        while not self.exiting:
            self.bot.signIn(self.username, self.password, self.world)
            self.bot.farm(self.world)
            self.sleep(1)
            time1 = self.bot.closeWebDriver()
            print("Program zasypia na:", time1)
            time1 = time.strptime(time1, '%H:%M:%S')
            time1 = time1.tm_hour * 3600 + time1.tm_min * 60 + time1.tm_sec + 10
            #time.sleep(time1)
            self.sleep(time1)
        self.exiting = True
        # self.exit()


class ParametersPlemiona:  # todo klasa w której analizowane są parametry w  przeglądarce a następnie poddawane obróbce
    def __init__(self):
        self.browser = None

    def signIn(self, username, password, world):
        options = webdriver.ChromeOptions()
        options.add_argument('window-position=2500,100')
        self.browser = webdriver.Chrome(options=options)
        #self.browser.set_window_position(2000, 200)
        self.browser.get('https://www.plemiona.pl/')
        # self.browser.execute_script("window.open()")

        # print(self.browser.current_window_handle)
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
        time.sleep(1)
        # self.browser.execute_script("javascript: $(document).ready(function(){setInterval(function(){const e=new Date(Math.round(Timing.getCurrentServerTime()));var t=e.toLocaleTimeString()+':'+Math.floor(e.getMilliseconds()/100);e<10&&(t=0),$('#serverDate').text(t),$('#serverDate').attr('style','font-size: 10px;')},50)});")
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
                       scout, lightcavalery, heavycavalery, ram, catapult, knight, nobleman, checkboxallarmy):
        try:
            self.browser.get(
                'https://pl' + world + '.plemiona.pl' + '/game.php?village=' + number_village + '&screen=place')
            time.sleep(1)
            self.browser.find_element_by_name('input').send_keys(coordinateXvillage + coordinateYvillage)
            if (checkboxallarmy == False):
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
            else:
                self.browser.find_element_by_id('selectAllUnits').click()

            self.browser.find_element_by_id('target_attack').click()
            #print("Atak został wysłany do wioski:", coordinateXvillage, coordinateYvillage)

        except NoSuchElementException:
            print("Brak elementu, wprowadź dane poprawnie")

    def getBackArmy(self):
        # self.browser.get('https://pl' + world + '.plemiona.pl' + '/game.php?village=n' + number_village + '&screen=place')
        try:
            button_napad = self.browser.find_element_by_id('target_attack')
            button_napad.click()
            # time.sleep(0.03)
        except NoSuchElementException:
            time.sleep(0.05)
            self.browser.find_element_by_id('troop_confirm_go').click()
            return True
            # time.sleep(1)
        # self.browser.find_element_by_id('troop_confirm_go').click()

    def getTimeAttack(self):
        try:
            timer = self.browser.find_element_by_class_name('relative_time')
            if timer is not None:
                text = timer.text
                if text is not None:
                    textlength = len(text)
                    hour = text[textlength - 8] + text[textlength - 7] + text[textlength - 6] + text[textlength - 5] + text[
                        textlength - 4] + text[textlength - 3] + text[textlength - 2] + text[textlength - 1]
                    return hour
                else:
                    print("Brak elementu - relative_time")
                    return
        except NoSuchElementException or WebDriverException:
            print("Przeglądarka zamknięta")
            return False

    def getTime(self):
        try:
            # self.browser.find_element_by_id('serverTime')
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
                print("Wysłano atak", hour2, millisecond)
                action = False
                return True
            if not self.getTimeAttack():
                action = False

    def writeArmyToExcel(self, world):
        self.browser.get('https://pl' + world + '.plemiona.pl' + '/game.php?screen=ally&mode=members_defense')
        time.sleep(0.1)
        select = Select(self.browser.find_element_by_name("player_id")).options
        # select1 = Select(self.browser.find_element_by_name("player_id"))
        # select = self.browser.find_element_by_name("player_id")
        select.pop(0)
        # print(select1)
        tab_nick = []
        for i in select:
            # print(i.text, i.get_attribute("value"))
            tab_nick.append(i.get_attribute("value"))
            # Select(self.browser.find_element_by_name("player_id")).select_by_value(i.get_attribute("value"))
            time.sleep(0.05)
        print(tab_nick)
        time.sleep(1)

        for i in tab_nick:
            Select(self.browser.find_element_by_name("player_id")).select_by_value(i)
            time.sleep(1)
            # print(self.browser.find_element_by_class_name("table-responsive").text)
            # self.browser.find_element_by_class_name("table-responsive").text
            time.sleep(1)

    def closeWebDriver(self):
        try:
            self.browser.close()
            self.browser.quit()
        except NoSuchWindowException or WebDriverException:
            print("Przeglądarka została zamknięta przez użytkownika")

    def farm(self, world):
        try:
            self.browser.get('https://pl' + world + '.plemiona.pl' + '/game.php?screen=place&mode=scavenge')
            spear = int(self.browser.find_elements_by_css_selector('a')[97].text[1:-1])
            sword = int(self.browser.find_elements_by_css_selector('a')[98].text[1:-1])
            axe = int(self.browser.find_elements_by_css_selector('a')[99].text[1:-1])
            archer = int(self.browser.find_elements_by_css_selector('a')[100].text[1:-1])
            light = int(self.browser.find_elements_by_css_selector('a')[101].text[1:-1])
            marcher = int(self.browser.find_elements_by_css_selector('a')[102].text[1:-1])
            heavy = int(self.browser.find_elements_by_css_selector('a')[103].text[1:-1])
            print(spear, sword, axe, archer, light, marcher, heavy)

            carry_max = spear * 25 + sword * 15 + axe * 10 + archer * 10 + light * 80 + marcher * 50 + heavy * 50

            carry_max_all = [carry_max * 0.557, carry_max * 0.231, carry_max * 0.115, carry_max * 0.077]

            timee = ""
            x = 106
            y = 54
            for i in range(4):
                if spear > 0:
                    carry_max_all[i] /= 25
                    if spear >= carry_max_all[i]:
                        self.browser.find_element_by_name('spear').send_keys(int(carry_max_all[i]))
                        spear -= carry_max_all[i]
                        carry_max_all[i] = 0
                    else:
                        spear1 = carry_max_all[i] - spear
                        carry_max_all[i] = spear1 * 25
                        self.browser.find_element_by_name('spear').send_keys(int(spear))

                if sword > 0 and carry_max_all[i] > 0:
                    carry_max_all[i] /= 15
                    if sword >= carry_max_all[i]:
                        self.browser.find_element_by_name('sword').send_keys(int(carry_max_all[i]))
                        sword -= carry_max_all[i]
                        carry_max_all[i] = 0
                    else:
                        sword1 = carry_max_all[i] - sword
                        carry_max_all[i] = sword1 * 15
                        self.browser.find_element_by_name('sword').send_keys(int(sword))

                if axe > 0 and carry_max_all[i] > 0:
                    carry_max_all[i] /= 10
                    if axe >= carry_max_all[i]:
                        self.browser.find_element_by_name('axe').send_keys(int(carry_max_all[i]))
                        axe -= carry_max_all[i]
                        carry_max_all[i] = 0
                    else:
                        axe1 = carry_max_all[i] - axe
                        carry_max_all[i] = axe1 * 15
                        self.browser.find_element_by_name('axe').send_keys(int(axe))

                if archer > 0 and carry_max_all[i] > 0:
                    carry_max_all[i] /= 10
                    if archer >= carry_max_all[i]:
                        self.browser.find_element_by_name('archer').send_keys(int(carry_max_all[i]))
                        archer -= carry_max_all[i]
                        carry_max_all[i] = 0
                    else:
                        archer1 = carry_max_all[i] - archer
                        carry_max_all[i] = archer1 * 15
                        self.browser.find_element_by_name('archer').send_keys(int(archer))

                if light > 0 and carry_max_all[i] > 0:
                    carry_max_all[i] /= 80
                    if light >= carry_max_all[i]:
                        self.browser.find_element_by_name('light').send_keys(int(carry_max_all[i]))
                        light -= carry_max_all[i]
                        carry_max_all[i] = 0
                    else:
                        light1 = carry_max_all[i] - light
                        carry_max_all[i] = light1 * 15
                        self.browser.find_element_by_name('light').send_keys(int(light))

                if marcher > 0 and carry_max_all[i] > 0:
                    carry_max_all[i] /= 50
                    if marcher >= carry_max_all[i]:
                        self.browser.find_element_by_name('marcher').send_keys(int(carry_max_all[i]))
                        marcher -= carry_max_all[i]
                        carry_max_all[i] = 0
                    else:
                        marcher1 = carry_max_all[i] - marcher
                        carry_max_all[i] = marcher1 * 15
                        self.browser.find_element_by_name('marcher').send_keys(int(marcher))

                if heavy > 0 and carry_max_all[i] > 0:
                    carry_max_all[i] /= 50
                    if heavy >= carry_max_all[i]:
                        self.browser.find_element_by_name('heavy').send_keys(int(carry_max_all[i]))
                        heavy -= carry_max_all[i]
                        carry_max_all[i] = 0
                    else:
                        heavy1 = carry_max_all[i] - heavy
                        carry_max_all[i] = heavy1 * 15
                        self.browser.find_element_by_name('heavy').send_keys(int(heavy))
                if timee < self.browser.find_elements_by_css_selector('a')[y].text:
                    timee = self.browser.find_elements_by_css_selector('a')[y].text
                print(timee)
                time.sleep(5)

                self.browser.find_elements_by_css_selector('a')[x].click()
                x += 2
                y += 11
                time.sleep(5)
            return str(timee)
                # //*[@id="scavenge_screen"]/div/div[2]/div[1]/div[3]/div/div[2]/a[1]
                # //*[@id="scavenge_screen"]/div/div[2]/div[2]/div[3]/div/div[2]/a[1]
                # //*[@id="scavenge_screen"]/div/div[2]/div[3]/div[3]/div/div[2]/a[1]
                # //*[@id="scavenge_screen"]/div/div[2]/div[4]/div[3]/div/div[2]/a[1]
        except NoSuchElementException:
            print("Brak przeglądu placu")
            return "Brak zalogowania"
        
        '''
        # 0,557 0,231 0,115 0,077
        for i in tab_nick:
            self.browser.find_element_by_name("player_id").
            #i+=1
            #time.sleep(1)
       # self.browser.find_element_by_name("player_id").select_by_value('699865715')
        try:
            print('1')
        except:
            print("text")
        '''


# game.php?village=7124&screen=am_farm

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
