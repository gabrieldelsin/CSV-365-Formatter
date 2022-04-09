# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1011, 642)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon.fromTheme("office")
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_importar_arquivo = QtWidgets.QFrame(self.centralwidget)
        self.frame_importar_arquivo.setGeometry(QtCore.QRect(0, 0, 1011, 621))
        self.frame_importar_arquivo.setStyleSheet("background-color: rgba(255, 0, 0, 241);")
        self.frame_importar_arquivo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_importar_arquivo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_importar_arquivo.setObjectName("frame_importar_arquivo")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_importar_arquivo)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 60, 991, 551))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"border-radius: 5px;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.result_table = QtWidgets.QListWidget(self.groupBox_2)
        self.result_table.setGeometry(QtCore.QRect(10, 10, 971, 471))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.result_table.setFont(font)
        self.result_table.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.result_table.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.result_table.setStyleSheet("QAbstractScrollArea {\n"
"    border: 1px solid;\n"
"    \n"
"}")
        self.result_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.result_table.setLineWidth(0)
        self.result_table.setMidLineWidth(0)
        self.result_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.result_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.result_table.setTabKeyNavigation(True)
        self.result_table.setProperty("showDropIndicator", True)
        self.result_table.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.result_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.result_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.result_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.result_table.setMovement(QtWidgets.QListView.Static)
        self.result_table.setResizeMode(QtWidgets.QListView.Fixed)
        self.result_table.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.result_table.setViewMode(QtWidgets.QListView.ListMode)
        self.result_table.setModelColumn(0)
        self.result_table.setUniformItemSizes(False)
        self.result_table.setBatchSize(100000)
        self.result_table.setSelectionRectVisible(True)
        self.result_table.setObjectName("result_table")
        self.groupBox = QtWidgets.QGroupBox(self.frame_importar_arquivo)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 991, 41))
        self.groupBox.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(244, 244, 244);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.domain_label = QtWidgets.QLabel(self.groupBox)
        self.domain_label.setEnabled(True)
        self.domain_label.setGeometry(QtCore.QRect(90, 10, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.domain_label.setFont(font)
        self.domain_label.setObjectName("domain_label")
        self.domain_combobox = QtWidgets.QComboBox(self.groupBox)
        self.domain_combobox.setEnabled(False)
        self.domain_combobox.setGeometry(QtCore.QRect(145, 11, 231, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setKerning(True)
        self.domain_combobox.setFont(font)
        self.domain_combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.domain_combobox.setAcceptDrops(False)
        self.domain_combobox.setStyleSheet("border-style: solid;\n"
"border-width: 1px;")
        self.domain_combobox.setMinimumContentsLength(0)
        self.domain_combobox.setIconSize(QtCore.QSize(0, 16))
        self.domain_combobox.setDuplicatesEnabled(False)
        self.domain_combobox.setFrame(True)
        self.domain_combobox.setModelColumn(0)
        self.domain_combobox.setObjectName("domain_combobox")
        self.filter_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.filter_checkBox.setEnabled(True)
        self.filter_checkBox.setGeometry(QtCore.QRect(10, 10, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.filter_checkBox.setFont(font)
        self.filter_checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filter_checkBox.setObjectName("filter_checkBox")
        self.license_label = QtWidgets.QLabel(self.groupBox)
        self.license_label.setEnabled(True)
        self.license_label.setGeometry(QtCore.QRect(394, 9, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.license_label.setFont(font)
        self.license_label.setObjectName("license_label")
        self.license_combobox = QtWidgets.QComboBox(self.groupBox)
        self.license_combobox.setEnabled(False)
        self.license_combobox.setGeometry(QtCore.QRect(450, 10, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.license_combobox.setFont(font)
        self.license_combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.license_combobox.setStyleSheet("border-style: solid;\n"
"border-width: 1px;")
        self.license_combobox.setMaxVisibleItems(25)
        self.license_combobox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.license_combobox.setDuplicatesEnabled(False)
        self.license_combobox.setFrame(False)
        self.license_combobox.setObjectName("license_combobox")
        self.block_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.block_radioButton.setEnabled(False)
        self.block_radioButton.setGeometry(QtCore.QRect(770, 9, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.block_radioButton.setFont(font)
        self.block_radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.block_radioButton.setObjectName("block_radioButton")
        self.login_label = QtWidgets.QLabel(self.groupBox)
        self.login_label.setGeometry(QtCore.QRect(720, 10, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.login_label.setFont(font)
        self.login_label.setObjectName("login_label")
        self.update_btn = QtWidgets.QPushButton(self.groupBox)
        self.update_btn.setGeometry(QtCore.QRect(880, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setKerning(True)
        self.update_btn.setFont(font)
        self.update_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.update_btn.setStyleSheet("QPushButton{\n"
"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"}")
        self.update_btn.setCheckable(False)
        self.update_btn.setAutoDefault(False)
        self.update_btn.setDefault(False)
        self.update_btn.setFlat(True)
        self.update_btn.setObjectName("update_btn")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_importar_arquivo)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 550, 971, 51))
        self.groupBox_3.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(244, 244, 244);\n"
"    border-radius: 5px;\n"
"    border: 1px solid;\n"
"}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.total_accounts_label = QtWidgets.QLabel(self.groupBox_3)
        self.total_accounts_label.setEnabled(True)
        self.total_accounts_label.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.total_accounts_label.setFont(font)
        self.total_accounts_label.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.total_accounts_label.setObjectName("total_accounts_label")
        self.qtde_accounts_label = QtWidgets.QLabel(self.groupBox_3)
        self.qtde_accounts_label.setEnabled(True)
        self.qtde_accounts_label.setGeometry(QtCore.QRect(100, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.qtde_accounts_label.setFont(font)
        self.qtde_accounts_label.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.qtde_accounts_label.setText("")
        self.qtde_accounts_label.setObjectName("qtde_accounts_label")
        self.coast_label = QtWidgets.QLabel(self.groupBox_3)
        self.coast_label.setEnabled(True)
        self.coast_label.setGeometry(QtCore.QRect(711, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.coast_label.setFont(font)
        self.coast_label.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.coast_label.setObjectName("coast_label")
        self.total_coast_label = QtWidgets.QLabel(self.groupBox_3)
        self.total_coast_label.setEnabled(True)
        self.total_coast_label.setGeometry(QtCore.QRect(781, 12, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.total_coast_label.setFont(font)
        self.total_coast_label.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.total_coast_label.setText("")
        self.total_coast_label.setObjectName("total_coast_label")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar.setGeometry(QtCore.QRect(710, 14, 251, 21))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.menubar.setFont(font)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        MainWindow.setMenuBar(self.menubar)
        self.save_action = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.save_action.setFont(font)
        self.save_action.setObjectName("save_action")
        self.actionGerar_script = QtWidgets.QAction(MainWindow)
        self.actionGerar_script.setObjectName("actionGerar_script")
        self.actionSair = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.actionSair.setFont(font)
        self.actionSair.setObjectName("actionSair")
        self.actionPowershell = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.actionPowershell.setFont(font)
        self.actionPowershell.setObjectName("actionPowershell")
        self.import_file_action = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.import_file_action.setFont(font)
        self.import_file_action.setObjectName("import_file_action")
        self.arquivo_importado_action = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.arquivo_importado_action.setFont(font)
        self.arquivo_importado_action.setObjectName("arquivo_importado_action")
        self.menuArquivo.addAction(self.import_file_action)
        self.menuArquivo.addAction(self.save_action)
        self.menuArquivo.addAction(self.actionSair)
        self.menubar.addAction(self.menuArquivo.menuAction())

        self.retranslateUi(MainWindow)
        self.result_table.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CSV 365"))
        self.domain_label.setText(_translate("MainWindow", "Domain.:"))
        self.filter_checkBox.setText(_translate("MainWindow", "Filter"))
        self.license_label.setText(_translate("MainWindow", "License.:"))
        self.block_radioButton.setText(_translate("MainWindow", "Blocked"))
        self.login_label.setText(_translate("MainWindow", "Login.:"))
        self.update_btn.setText(_translate("MainWindow", "Update"))
        self.total_accounts_label.setText(_translate("MainWindow", "Total accounts.:"))
        self.coast_label.setText(_translate("MainWindow", "Total cost.: "))
        self.menuArquivo.setTitle(_translate("MainWindow", "File"))
        self.save_action.setText(_translate("MainWindow", "Save"))
        self.actionGerar_script.setText(_translate("MainWindow", "Gerar script"))
        self.actionSair.setText(_translate("MainWindow", "Exit"))
        self.actionPowershell.setText(_translate("MainWindow", "Gerar script"))
        self.import_file_action.setText(_translate("MainWindow", "Import File"))
        self.arquivo_importado_action.setText(_translate("MainWindow", "Arquivo importado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
