# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'portal2.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_portal2(object):
    def setupUi(self, portal2):
        portal2.setObjectName("portal2")
        portal2.resize(327, 276)
        self.imagem = QtWidgets.QLabel(portal2)
        self.imagem.setGeometry(QtCore.QRect(10, 10, 310, 150))
        self.imagem.setMinimumSize(QtCore.QSize(310, 150))
        self.imagem.setMaximumSize(QtCore.QSize(310, 150))
        self.imagem.setText("")
        self.imagem.setObjectName("imagem")
        self.noticia = QtWidgets.QLabel(portal2)
        self.noticia.setGeometry(QtCore.QRect(10, 170, 310, 60))
        self.noticia.setMinimumSize(QtCore.QSize(310, 60))
        self.noticia.setMaximumSize(QtCore.QSize(310, 60))
        self.noticia.setObjectName("noticia")
        self.widget = QtWidgets.QWidget(portal2)
        self.widget.setGeometry(QtCore.QRect(210, 230, 111, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.anterior = QtWidgets.QPushButton(self.widget)
        self.anterior.setMinimumSize(QtCore.QSize(31, 31))
        self.anterior.setMaximumSize(QtCore.QSize(31, 31))
        self.anterior.setText("")
        self.anterior.setObjectName("anterior")
        self.horizontalLayout.addWidget(self.anterior)
        self.proximo = QtWidgets.QPushButton(self.widget)
        self.proximo.setMinimumSize(QtCore.QSize(31, 31))
        self.proximo.setMaximumSize(QtCore.QSize(31, 31))
        self.proximo.setText("")
        self.proximo.setObjectName("proximo")
        self.horizontalLayout.addWidget(self.proximo)
        self.atualizar = QtWidgets.QPushButton(self.widget)
        self.atualizar.setMinimumSize(QtCore.QSize(31, 31))
        self.atualizar.setMaximumSize(QtCore.QSize(31, 31))
        self.atualizar.setText("")
        self.atualizar.setObjectName("atualizar")
        self.horizontalLayout.addWidget(self.atualizar)

        self.retranslateUi(portal2)
        QtCore.QMetaObject.connectSlotsByName(portal2)

    def retranslateUi(self, portal2):
        _translate = QtCore.QCoreApplication.translate
        portal2.setWindowTitle(_translate("portal2", "Portal UFPA"))
        self.noticia.setText(_translate("portal2", "Lola"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    portal2 = QtWidgets.QWidget()
    ui = Ui_portal2()
    ui.setupUi(portal2)
    portal2.show()
    sys.exit(app.exec_())

