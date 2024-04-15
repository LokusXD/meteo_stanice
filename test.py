from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])

# QComboBox - políčko pro výběr z několika možností
box = QtWidgets.QComboBox()
box.addItem('First Option')
box.addItem('Second Option')

# Základní varianta napojí na activated[int]
box.activated.connect(print)

# Výběr varianty signálu pomocí hranatých závorek
box.activated[str].connect(print)
box.activated[int].connect(print)

box.show()

app.exec()