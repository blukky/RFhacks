from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QImage, QPixmap


class Ui_Result(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.image = None

    def setupUi(self):
        self.setObjectName("Result")
        self.resize(640, 480)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("")
        self.label.setGeometry(0, 0, 640, 480)
        self.label.setObjectName("label")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Результат"))

    def show(self) -> None:
        super().show()
        self.label.setPixmap(QPixmap.fromImage(self.image))
