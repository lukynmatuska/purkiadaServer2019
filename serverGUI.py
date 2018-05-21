from PyQt5 import QtWidgets
import random

app = QtWidgets.QApplication([])

# Hlavní okno
main = QtWidgets.QWidget()
main.setWindowTitle('Server GUI')

# Layout pro hlavní okno
layout = QtWidgets.QHBoxLayout()
main.setLayout(layout)

# Tlačítko
buttonStart = QtWidgets.QPushButton('Start')
layout.addWidget(buttonStart)

# Tlačítko
buttonStop = QtWidgets.QPushButton('Stop!')
layout.addWidget(buttonStop)

# Nápis
label = QtWidgets.QLabel('Click the button to change me')
# Přidáním do layoutu se nápis automaticky stane potomkem hlavního okna
layout.addWidget(label)


def myPrint(a):
	print("{} - AHOJKY".format(a))

buttonStart.clicked.connect(lambda: myPrint("Start"))
buttonStop.clicked.connect(exit)

# Spuštění
main.show()
app.exec()