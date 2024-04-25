import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

sea = 0
lvl = 0
mastery_new_lvl = 70
master = 0
mastery_now_lvl = 68
mob_boss = 0
mastery_mob_kill = {"gelley_captain": 0,
                    "royal_soldier": 0,
                    "royal_squa": 0}
kill_info = {"gelley_captain": 0,
            "royal_soldier": 0,
            "royal_squa": 0}
lvl_kill = {}

mob_sea_1 = {"gelley captain": random.randint(22000,25000),
             "royal_soldier": random.randint(20000,25000),
             "royal_squa": random.randint(17000,22000)
             }
boss_sea_1 = {"cyborg": random.randint(150000,180000),
              "thunder_god": random.randint(100000,150000),
              "wysper": random.randint(85000,90000)
             }

class FourWindow(QWidget):
    def __init__(self):
        super().__init__()
        global mob_sea_1
        global lvl
        global sea
        global mob_boss
        global mastery_new_lvl
        
        def now_lvl(): 
            global lvl
            global mastery_now_lvl 
            if int(lvl) >= 1 and int(lvl) <= 99:
                for i in range(int(lvl)):
                    mastery_now_lvl += i*16
            elif int(lvl) >=100 and int(lvl) <= 199:
                mastery_now_lvl = 80000
                for i in range(int(lvl)-10):
                    mastery_now_lvl += i*2
            elif int(lvl) >=200 and int(lvl) <= 299:
                mastery_now_lvl = 260000
                for i in range(int(lvl)-100):
                    mastery_now_lvl += i*4           
            elif int(lvl) >=300 and int(lvl) <= 399:
                mastery_now_lvl = 320000
                for i in range(int(lvl)-100):
                    mastery_now_lvl += i*5
            elif int(lvl) >=400 and int(lvl) <= 499:
                mastery_now_lvl = 541265
                for i in range(int(lvl)-100):
                    mastery_now_lvl += i*6         
            elif int(lvl) >=500 and int(lvl) <= 599:
                mastery_now_lvl = 1015283
                for i in range(int(lvl)-100):
                    mastery_now_lvl += i*7            
            elif int(lvl) >=600 and int(lvl) <= 700:
                mastery_now_lvl = 1881554
                for i in range(int(lvl)-100):
                    mastery_now_lvl += i*8
            return mastery_now_lvl

        def mastery_lvl_sea_1():
            global mastery_mob_kill
            global lvl
            global lvl_kill
            global mob_sea_1
            global kill_info

            lvl_kill["gelley_captain"] = int(lvl)
            lvl_kill["royal_soldier"] = int(lvl)
            lvl_kill["royal_squa"] = int(lvl)

            while int(lvl_kill["gelley_captain"]) <= 700:

                if int(mastery_mob_kill["gelley_captain"]) < now_lvl():
                    mastery_mob_kill["gelley_captain"] += mob_sea_1["gelley captain"]
                    kill_info["gelley_captain"] += 1

                    if int(mastery_mob_kill["gelley_captain"]) >= now_lvl():
                        mastery_mob_kill["gelley_captain"] -= now_lvl()
                        lvl_kill["gelley_captain"] += 1

            while int(lvl_kill["royal_soldier"]) <= 700:
                if int(mastery_mob_kill["royal_soldier"]) < now_lvl():
                    mastery_mob_kill["royal_soldier"] += mob_sea_1["royal_soldier"]
                    kill_info["royal_soldier"] += 1

                    if int(mastery_mob_kill["royal_soldier"]) >= now_lvl():
                        mastery_mob_kill["royal_soldier"] -= now_lvl()
                        lvl_kill["royal_soldier"] += 1

            while int(lvl_kill["royal_squa"]) <= 700:
                if int(mastery_mob_kill["royal_squa"]) < now_lvl():
                    mastery_mob_kill["royal_squa"] += mob_sea_1["royal_squa"]
                    kill_info["royal_squa"] += 1

                    if int(mastery_mob_kill["royal_squa"]) >= now_lvl():
                        mastery_mob_kill["royal_squa"] -= now_lvl()
                        lvl_kill["royal_squa"] += 1

        if sea == 1:
            if mob_boss == 1:
                for i in mob_sea_1.keys():
                    mastery_lvl_sea_1()
                    self.setWindowTitle("результаты")
                    layout = QVBoxLayout()
                    self.setLayout(layout)
                    self.text = QLabel(f"Gelley Captain - {kill_info['gelley_captain']} \nRoyal Soldier - {kill_info['royal_soldier']} \nRoyal Squa - {kill_info['royal_squa']}")
                    self.text.setFont(QFont('Arial', 10)) 
                    layout.addWidget(self.text)


            if mob_boss == 2:
                for i in boss_sea_1.keys():
                    print(i,"-", boss_sea_1[i])



class ThreeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("На ком вы качаетесь")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.main_window = QWidget()
        self.stacked_widget.addWidget(self.main_window)

        layout = QVBoxLayout()
        self.main_window.setLayout(layout)
        self.text = QLabel("             На ком вы качаетесь?")
        layout.addWidget(self.text)

        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        self.button1 = QPushButton("Мобы")
        self.button1.clicked.connect(self.mob)
        self.button1.clicked.connect(self.open_four_window) 
        self.button2 = QPushButton("боссы")
        self.button2.clicked.connect(self.boss)
        self.button2.clicked.connect(self.open_four_window)

        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)

    def mob(self):
        global mob_boss
        mob_boss = 1
    def boss(self):
        global mob_boss
        mob_boss = 2

    def open_four_window(self):
        self.four_window = FourWindow()
        self.stacked_widget.addWidget(self.four_window)
        self.stacked_widget.setCurrentIndex(1)


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("сколько у вас mastery")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.text = QLabel("                        какой лвл mastery?")
        self.LE = QLineEdit()

        self.LE.textChanged.connect(self.mastery_lvl)

        layout.addWidget(self.text)
        layout.addWidget(self.LE)

        self.button = QPushButton("kill", self)
        self.button.clicked.connect(self.open_three_window)
        layout.addWidget(self.button)

    def mastery_lvl(self, text):
        global lvl
        lvl = text

    def open_three_window(self):
        global  main_window
        self.close()
        main_window.close()
        main_window = ThreeWindow()
        main_window.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("выбор что вы хотите качать")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.main_window = QWidget()
        self.stacked_widget.addWidget(self.main_window)

        layout = QVBoxLayout()
        self.main_window.setLayout(layout)
        self.text = QLabel("                         Где вы качаетесь?")
        layout.addWidget(self.text)

        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        self.button1 = QPushButton("1е море")
        self.button1.clicked.connect(self.open_second_window)
        self.button1.clicked.connect(self.sea_one)
        self.button2 = QPushButton("2е море")
        self.button2.clicked.connect(self.open_second_window)
        self.button2.clicked.connect(self.sea_two)
        self.button3 = QPushButton("3е море")
        self.button3.clicked.connect(self.open_second_window)
        self.button3.clicked.connect(self.sea_three)

        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)

    def sea_one(self):
        global sea
        sea = 1
    def sea_two(self):
        global sea
        sea = 2
    def sea_three(self):
        global sea
        sea = 3

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.stacked_widget.addWidget(self.second_window)
        self.stacked_widget.setCurrentIndex(1)
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())