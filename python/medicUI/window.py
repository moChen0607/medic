from Qt import QtWidgets, QtCore
from . import widgets
from . import model
import os


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setObjectName("medic_main_window")
        self.__makeWidgets()
        self.__setStyleSheet()

    def __setStyleSheet(self):
        qss_path = os.path.abspath(os.path.join(__file__, "../style.qss"))

        if not os.path.isfile(qss_path):
            return

        current_dir = os.path.dirname(__file__)

        style = ""
        with open(qss_path, "r") as f:
            style = f.read()
            style = style.replace('url("', 'url("%s/' % current_dir)

        self.setStyleSheet(style)

    def __makeWidgets(self):
        self.__central_widget = QtWidgets.QWidget()
        self.__central_layout = QtWidgets.QVBoxLayout()
        self.setCentralWidget(self.__central_widget)
        self.__central_widget.setLayout(self.__central_layout)

        self.__top_widget = widgets.TopBarWidget()
        self.__main_widget = widgets.MainWidget()

        self.__central_layout.addWidget(self.__top_widget)
        self.__central_layout.addWidget(self.__main_widget)
        self.__central_layout.setSpacing(0)
        self.__central_layout.setContentsMargins(0, 0, 0, 0)

        self.__top_widget.setBrowserButtonEnabled(False, False)
        self.__main_widget.ConditionChanged.connect(self.__top_widget.setBrowserButtonEnabled)
        self.__main_widget.KarteChanged.connect(self.__top_widget.setCurrentKarteName)
        self.__top_widget.BackClicked.connect(self.__back)
        self.__top_widget.NextClicked.connect(self.__next)
        self.__top_widget.reset_button.clicked.connect(self.__main_widget.reset)
        self.__top_widget.test_button.clicked.connect(self.__main_widget.test)

    def __next(self):
        self.__top_widget.next()
        self.__main_widget.next()

    def __back(self):
        self.__top_widget.back()
        self.__main_widget.back()