import main
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QRadioButton, QLineEdit, QFrame, QMessageBox, QButtonGroup
from PyQt5.QtGui import QPixmap


# CSS stylesheet for the application
stylesheet = """
    #fishingArea {
        background-image: url(res/fishing-net.png); 
        background-repeat: no-repeat; 
        background-position: center;
    }
    #header {
        font: 16px Segoe UI;
        font-weight: bold;
    }
    #mainButton {
        font: 14px Segoe UI;
        font-weight: bold;
        color: white;
    }
"""

# Subclass QMainWindow to customize your application's main window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # main window settings
        self.setWindowTitle("Fishing Simulator")
        self.setFixedSize(QSize(800, 600))
        main_layout = QVBoxLayout()

        # Day preparation
        day_prep_widget = QWidget()
        day_prep_layout = QHBoxLayout(day_prep_widget)

        # shop section
        shop_widget = QFrame()
        shop_widget.setFrameStyle(QFrame.Panel | QFrame.Raised)
        shop_layout = QVBoxLayout(shop_widget)
        shop_title = QLabel("Shop")
        shop_title.setAlignment(Qt.AlignCenter)
        shop_title.setObjectName("header")
        shop_layout.addWidget(shop_title)
        self.current_gold_label = QLabel("Gold: 100")
        self.current_gold_label.setStyleSheet("color: orange")
        self.current_gold_label.setAlignment(Qt.AlignCenter)
        shop_layout.addWidget(self.current_gold_label)

        # pole selection
        pole_select_widget = QWidget()
        pole_select_layout = QVBoxLayout(pole_select_widget)
        pole_select_label = QLabel("Buy a fishing pole")
        self.pole_btn_group = QButtonGroup()
        self.radio_small_pole = QRadioButton("Small Fishing Pole", self)
        self.radio_medium_pole = QRadioButton("Medium Fishing Pole", self)
        self.radio_big_pole = QRadioButton("Big Fishing Pole", self)
        self.pole_btn_group.addButton(self.radio_small_pole)
        self.pole_btn_group.addButton(self.radio_medium_pole)
        self.pole_btn_group.addButton(self.radio_big_pole)
        self.pole_btn_group.buttonToggled.connect(self.update_current_gold)
        pole_select_layout.addWidget(pole_select_label)
        pole_select_layout.addWidget(self.radio_small_pole)
        pole_select_layout.addWidget(self.radio_medium_pole)
        pole_select_layout.addWidget(self.radio_big_pole)
        pole_select_layout.addStretch()

        # bait shop
        buy_bait_widget = QWidget()
        buy_bait_layout = QVBoxLayout(buy_bait_widget)
        buy_bait_label = QLabel("Buy some baits")
        red_bait_label = QLabel("Red bait")
        red_bait_label.setStyleSheet("color: red")
        blue_bait_label = QLabel("Blue bait")
        blue_bait_label.setStyleSheet("color: blue")
        green_bait_label = QLabel("Green bait")
        green_bait_label.setStyleSheet("color: green")
        self.input_red_bait = QLineEdit("0")
        self.input_blue_bait = QLineEdit("0")
        self.input_green_bait = QLineEdit("0")
        self.input_red_bait.textChanged.connect(self.update_current_gold)
        self.input_blue_bait.textChanged.connect(self.update_current_gold)
        self.input_green_bait.textChanged.connect(self.update_current_gold)
        buy_bait_layout.addWidget(buy_bait_label)
        buy_bait_layout.addWidget(red_bait_label)
        buy_bait_layout.addWidget(self.input_red_bait)
        buy_bait_layout.addWidget(blue_bait_label)
        buy_bait_layout.addWidget(self.input_blue_bait)
        buy_bait_layout.addWidget(green_bait_label)
        buy_bait_layout.addWidget(self.input_green_bait)
        buy_bait_layout.addStretch()

        # assign to shop layout
        shop_form_widget = QWidget()
        shop_form_layout = QHBoxLayout(shop_form_widget)
        shop_form_layout.addWidget(pole_select_widget)
        shop_form_layout.addWidget(buy_bait_widget)
        shop_layout.addWidget(shop_form_widget)

        # Forecast
        forecast_widget = QFrame()
        forecast_widget.setFrameStyle(QFrame.Panel | QFrame.Raised)
        forecast_widget.setFixedWidth(400)
        forecast_layout = QVBoxLayout(forecast_widget)
        forecast_label = QLabel("Today's Forecast")
        forecast_label.setAlignment(Qt.AlignCenter)
        forecast_label.setObjectName("header")
        forecast_layout.addWidget(forecast_label)
        forecast_layout.addStretch()

        # generated forecast data
        forecast_size_label = QLabel("Today, we're seeing :")
        self.forecast_small_fish = QLabel("9 Small Fish")
        self.forecast_medium_fish = QLabel("3 Medium Fish")
        self.forecast_big_fish = QLabel("4 Big Fish")
        self.forecast_red_fish = QLabel(r"30% are red")
        self.forecast_red_fish.setStyleSheet("color: red")
        self.forecast_blue_fish = QLabel(r"40% are blue")
        self.forecast_blue_fish.setStyleSheet("color: blue")
        self.forecast_green_fish = QLabel(r"30% are green")
        self.forecast_green_fish.setStyleSheet("color: green")

        forecast_layout.addWidget(forecast_size_label)
        forecast_layout.addWidget(self.forecast_small_fish)
        forecast_layout.addWidget(self.forecast_medium_fish)
        forecast_layout.addWidget(self.forecast_big_fish)
        forecast_layout.addStretch()
        forecast_layout.addWidget(self.forecast_red_fish)
        forecast_layout.addWidget(self.forecast_blue_fish)
        forecast_layout.addWidget(self.forecast_green_fish)
        forecast_layout.addStretch()

        # day preparation layout done
        day_prep_layout.addWidget(shop_widget)
        day_prep_layout.addWidget(forecast_widget)

        # Fishing
        fishing_widget = QWidget()
        fishing_widget.setObjectName("fishingArea")
        fishing_widget.setFixedSize(QSize(800, 200))
        fishing_layout = QVBoxLayout(fishing_widget)
        self.btn_start = QPushButton("Start Fishing")
        self.btn_start.setStyleSheet("background-color: green")
        self.btn_start.setFixedWidth(600)
        self.btn_start.setObjectName("mainButton")
        self.btn_skip = QPushButton("Skip the day")
        self.btn_skip.setStyleSheet("background-color: orange")
        self.btn_skip.setObjectName("mainButton")

        # buttons layout and connect events
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout(buttons_widget)
        self.btn_start.clicked.connect(self.go_fishing)
        self.btn_skip.clicked.connect(self.generate_day)
        buttons_layout.addWidget(self.btn_start)
        buttons_layout.addWidget(self.btn_skip)

        # caught fish simulation
        self.caught_fish_widget = QWidget()
        self.caught_fish_layout = QHBoxLayout(self.caught_fish_widget)

        # assign to fishing layout
        fishing_layout.addWidget(buttons_widget)
        fishing_layout.addWidget(self.caught_fish_widget)

        # assign to main layout
        main_layout.addWidget(day_prep_widget)
        main_layout.addWidget(fishing_widget)

        # finish layout and initialize data
        self.setLayout(main_layout)
        self.generate_day()

    # generate new fishing day data and display them
    def generate_day(self):
        main.generate_day()
        self.forecast_small_fish.setText(f"{main.generated_fish_size[0]} Small Fish")
        self.forecast_medium_fish.setText(f"{main.generated_fish_size[1]} Medium Fish")
        self.forecast_big_fish.setText(f"{main.generated_fish_size[2]} Big Fish")

        color_percentaged = main.get_percentage_from_int_list(main.generated_fish_color)
        self.forecast_red_fish.setText(f"{color_percentaged[0]}% are red")
        self.forecast_blue_fish.setText(f"{color_percentaged[1]}% are blue")
        self.forecast_green_fish.setText(f"{color_percentaged[2]}% are green")

        if self.pole_btn_group.checkedButton():
            self.pole_btn_group.setExclusive(False)
            self.pole_btn_group.checkedButton().setChecked(False)
            self.pole_btn_group.setExclusive(True)
        
        self.input_red_bait.setText("0")
        self.input_blue_bait.setText("0")
        self.input_green_bait.setText("0")

        self.update_current_gold()

    # start the fishing simulation
    def go_fishing(self):
        pole = self.get_pole_selection()
        if not pole:
            return
        bait_list = [self.get_safe_bait_value(self.input_red_bait), self.get_safe_bait_value(self.input_blue_bait),\
                      self.get_safe_bait_value(self.input_green_bait)]
        self.color_to_spawn_list = main.simulate_fishing_day(main.list_fish_by_size, main.list_fish_by_color, pole.value, bait_list)
        self.start_fish_timer()

    # fish spawning timer for simulation
    def start_fish_timer(self):
        self.caught_fish_count = 0
        self.fish_to_clear = []
        self.fish_timer = QTimer(self)
        self.fish_timer.timeout.connect(self.spawn_fish)
        self.fish_timer.start(500)

    # create fish QLabel with given color
    def create_fish(self, fish_type):
        fish = QLabel()
        fish_img = QPixmap(f"res/fish-{fish_type}.png")
        fish.setPixmap(fish_img)
        return fish

    # spawn fish QLabel with given color
    def spawn_fish(self):
        self.caught_fish_count += 1
        if self.caught_fish_count <= 9: # window size limit
            fish = self.create_fish(self.color_to_spawn_list[self.caught_fish_count - 1])
            self.fish_to_clear.append(fish)
            self.caught_fish_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.caught_fish_layout.addWidget(fish)
        
        if self.caught_fish_count >= len(self.color_to_spawn_list):
            self.end_day()

    # end the fishing simulation
    def end_day(self):
        self.fish_timer.stop()
        self.color_to_spawn_list = []
        final_gold = main.current_gold + main.today_earnings
        if final_gold < main.starting_gold:
            result_text = "You lost..."
        elif final_gold == main.starting_gold:
            result_text = "You tied..."
        else:
            result_text = "You won!"
        msg = QMessageBox()
        msg.setWindowTitle("Fishing result")
        msg.setText(f"<p align='center'>{result_text}<br>Total gold at the end of the day : {final_gold}</p>")
        msg.exec_()
        self.generate_day()
        for fish in self.fish_to_clear:
            self.caught_fish_layout.removeWidget(fish)
            fish.deleteLater()
            fish = None

    # get the selected pole from the radio buttons
    def get_pole_selection(self):
        if self.radio_big_pole.isChecked():
            return main.FishSize.Big
        elif self.radio_medium_pole.isChecked():
            return main.FishSize.Medium
        elif self.radio_small_pole.isChecked():
            return main.FishSize.Small
        else:
            return None

    # get bait value from text input
    def get_safe_bait_value(self, input):
        return 0 if not input.text().isnumeric() else int(input.text())

    # update the current gold label
    def update_current_gold(self):
        gold = main.starting_gold
        pole = self.get_pole_selection()
        if pole:
            gold -= main.pole_prices[pole]

        gold -= self.get_safe_bait_value(self.input_red_bait) * main.bait_prices[main.FishColor.Red]
        gold -= self.get_safe_bait_value(self.input_blue_bait) * main.bait_prices[main.FishColor.Blue]
        gold -= self.get_safe_bait_value(self.input_green_bait) * main.bait_prices[main.FishColor.Green]

        main.current_gold = gold
        self.current_gold_label.setText(f"Gold: {gold}")

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(stylesheet)
    window = MainWindow()
    window.show()

    app.exec()