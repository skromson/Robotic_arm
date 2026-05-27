from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QSlider, QVBoxLayout
from robot import Robot
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #inicjalization of object robot
        self.robot = Robot()

        #setting window parameters
        self.setWindowTitle("Robotic arm")
        self.setGeometry(100, 100, 1024, 768)
        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)

        layout = QVBoxLayout()

        #phi slider widget
        self.phiLabel = QLabel("phi slider")
        self.phiSlider = QSlider()
        self.phiSlider.setRange(-180, 180)
        self.phiSlider.valueChanged.connect(self.phiChanged)
        layout.addWidget(self.phiLabel)
        layout.addWidget(self.phiSlider)

        #height slider widget
        self.heightLabel = QLabel("height slider")
        self.heightSlider = QSlider()
        self.heightSlider.setRange(0, 100)
        self.heightSlider.valueChanged.connect(self.heightChanged)
        layout.addWidget(self.heightLabel)
        layout.addWidget(self.heightSlider)
        

        #extension slider widget
        self.extensionLabel = QLabel("extension slider")
        self.extensionSlider = QSlider()
        self.extensionSlider.setRange(0, 100)
        self.extensionSlider.valueChanged.connect(self.extensionChanged)
        layout.addWidget(self.extensionLabel)
        layout.addWidget(self.extensionSlider)
        

        mainWidget.setLayout(layout)

    
    def phiChanged(self, angle):
        self.robot.phi = angle
        print(f"aktualny kąt robota: {self.robot.phi}, aktualna pozycja suwaka: {angle}")
    
    def heightChanged(self, height):
        self.robot.zHeight = height
        print(f"aktualna pozycja robota: {self.robot.zHeight}, aktualna pozycja suwaka: {height}")

    def extensionChanged(self, extension):
        self.robot.rExtension = extension
        print(f"aktualna pozycja robota: {self.robot.rExtension}, aktualna pozycja suwaka: {extension}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()