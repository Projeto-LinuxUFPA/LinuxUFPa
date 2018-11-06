#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from portal2 import Ui_portal2
from windows_1252 import *
from joko import *
import sys, os


class GuiPortal(Ui_portal2):
	def __init__(self, dialog):
		Ui_portal2.__init__(self)
		self.setupUi(dialog)
		
		self.imagem.setStyleSheet("background-color: white; border: 1px solid gray; border-radius: 5px;")
		self.imagem.setScaledContents(True)
		self.imagem.setPixmap(QPixmap("foto.jpg"))

		self.noticia.setWordWrap(True)
		self.noticia.setOpenExternalLinks(True)

		self.noticia.setStyleSheet("background-color: gray; border: 1px solid white; border-radius: 3px;")

		self.atualizar.setStyleSheet("background-color: gray; border: 1px solid white; border-radius: 3px;")
		images(".loading.png", 2)
		self.atualizar.setIcon(QIcon(".loading.png"))
		os.remove(".loading.png")
		self.atualizar.setIconSize(QtCore.QSize(22,22))

		self.anterior.setStyleSheet("background-color: gray; border: 1px solid white; border-radius: 3px;")
		images(".anterior.png", 5)
		self.anterior.setIcon(QIcon(".anterior.png"))
		os.remove(".anterior.png")
		self.anterior.setIconSize(QtCore.QSize(22,22))

		self.proximo.setStyleSheet("background-color: gray; border: 1px solid white; border-radius: 3px;")
		images(".proximo.png", 6)
		self.proximo.setIcon(QIcon(".proximo.png"))
		os.remove(".proximo.png")
		self.proximo.setIconSize(QtCore.QSize(22,22))

		self.atualizar.clicked.connect(self.carregar)
		self.proximo.clicked.connect(self.posterior)
		self.anterior.clicked.connect(self.antes)

		self.carregar()


	def carregar(self):
		images(".carr.png", 0)
		self.imagem.setPixmap(QPixmap(".carr.png"))
		self.noticia.setText("Carregando notícias!")
		os.remove(".carr.png")

		global test

		dados = function()
		if type(dados) is list:
			global jlink, jtitulo, jimg
			global number

			test = True

			number = 0

			jlink = dados[0]
			jtitulo = dados[1]
			jimg = dados[2]

			save_image(jimg[0], ".img0."+jimg[0][-3:])
			self.imagem.setPixmap(QPixmap(".img0."+jimg[0][-3:]))

			self.noticia.setText(self.notice(jlink[0], restore_windows_1252_characters(jtitulo[0])))

			save_image(jimg[1], ".img1."+jimg[1][-3:])
			save_image(jimg[2], ".img2."+jimg[2][-3:])
			save_image(jimg[3], ".img3."+jimg[3][-3:])
			save_image(jimg[4], ".img4."+jimg[4][-3:])
			save_image(jimg[5], ".img5."+jimg[5][-3:])


		else:
			print (dados)
			images(".erro.png", 1)
			self.imagem.setPixmap(QPixmap(".erro.png"))
			self.noticia.setText("Erro de Conexão!")
			os.remove(".erro.png")

			test = False


	def posterior(self):
		global test

		if test == True:
			global jlink, jtitulo, jimg
			global number

			if number < 5:
				number = number + 1

				self.imagem.setPixmap(QPixmap(".img"+str(number)+"."+jimg[number][-3:]))
				self.noticia.setText(self.notice(jlink[number], restore_windows_1252_characters(jtitulo[number])))


			elif number == 5:
				number = 0

				self.imagem.setPixmap(QPixmap(".img"+str(number)+"."+jimg[number][-3:]))
				self.noticia.setText(self.notice(jlink[number], restore_windows_1252_characters(jtitulo[number])))


	def antes(self):
		global test

		if test == True:
			global jlink, jtitulo, jimg
			global number

			if number > 0:
				number = number - 1

				self.imagem.setPixmap(QPixmap(".img"+str(number)+"."+jimg[number][-3:]))
				self.noticia.setText(self.notice(jlink[number], restore_windows_1252_characters(jtitulo[number])))


			elif number == 0:
				number = 5

				self.imagem.setPixmap(QPixmap(".img"+str(number)+"."+jimg[number][-3:]))
				self.noticia.setText(self.notice(jlink[number], restore_windows_1252_characters(jtitulo[number])))


	def notice(self, link, news):
		return u"<a href=\""+link+"\"style=\"color: black;\">"+news+"</a>"


	def messagebox(self):
		msg = QMessageBox()
		msg.setWindowTitle("Portal UFPA")
		msg.setText(u"Atualizando notícias!")
#		msg.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
		msg.exec()


def funct():
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QWidget()

	prog = GuiPortal(dialog)

	dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)

	dialog.setFixedSize(dialog.size())
	images(".ufpa.png", 3)
	dialog.setWindowIcon(QIcon(".ufpa.png"))
	os.remove(".ufpa.png")

	dialog.show()
	app.exec_()


	for file in os.scandir(os.getcwd()):
		if file.name.endswith(".jpg"):
			os.unlink(file.path)

		elif file.name.endswith(".JPG"):
			os.unlink(file.path)

		elif file.name.endswith(".png"):
			os.unlink(file.path)


if __name__ == '__main__':
	sys.exit(funct())
