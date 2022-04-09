import sys
import time

import pandas as pd
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

from gui.design import Ui_MainWindow


class FormatadorCSV(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.account_counter = None
        self.file_path = None
        self.list = None
        self.save_list = []

        # setting  the fixed size of window
        self.setFixedSize(950, 670)
        self.filter_checkBox.clicked.connect(
            lambda: self.enable_filter_fields())
        self.update_btn.clicked.connect(
            lambda: self.list_values(self.file_path))
        self.import_file_action.triggered.connect(
            lambda: self.import_file())
        self.save_action.triggered.connect(lambda: self.save_file())

        self.progressBar.hide()
        self.dollar_price = 5

        # Combo Box - Licenças
        self.license_combobox.addItem('Office 365 E1')
        self.license_combobox.addItem('Office 365 E3')
        self.license_combobox.addItem('Microsoft 365 Business Standard')
        self.license_combobox.addItem('Microsoft 365 Business Premium')
        self.license_combobox.addItem('Exchange Online (Plan 1)')
        self.license_combobox.addItem('Power BI Pro')
        self.license_combobox.addItem('Power BI (Free)')
        self.license_combobox.addItem('Outras')

    def enable_filter_fields(self):
        if self.filter_checkBox.isChecked():
            self.domain_combobox.setEnabled(True)
            self.license_combobox.setEnabled(True)
            self.block_radioButton.setEnabled(True)
        else:
            self.domain_combobox.setEnabled(False)
            self.license_combobox.setEnabled(False)
            self.block_radioButton.setEnabled(False)

    def import_file(self):

        try:
            self.file_path = QFileDialog.getOpenFileName(
                self.centralwidget,
                'Escolha um arquivo CSV',
                'C:\\',
                "CSV (*.csv)"
            )
            self.progressBar.show()
            self.domain_combobox.clear()
            self.list_combobox = []
            self.filter_checkBox.setChecked(False)
            self.result_table.clear()
            self.list_values(self.file_path)
        except FileNotFoundError:
            self.file_path = None
            self.progressBar.hide()

    def filter_file(self, domain, license, entry_status):
        for line in self.list:
            if license == 'Outras':
                if domain in str(line[0]) and 'nan' not in str(line[1]):
                    if not entry_status:
                        if 'False' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    elif entry_status:
                        if 'True' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    self.dollar_price = 0
            elif license == 'Office 365 E3':
                if domain in str(line[0]) and 'Office 365 E3' in str(line[1]):
                    if not entry_status:
                        if 'False' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    elif entry_status:
                        if 'True' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    self.dollar_price = 147.20

            elif license == 'Office 365 E1':
                if domain in str(line[0]) and 'Office 365 E1' in str(line[1]):
                    if not entry_status:
                        if 'False' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    elif entry_status:
                        if 'True' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    self.dollar_price = 64

            elif license == 'Microsoft 365 Business Standard':
                if domain in str(line[0]) and 'Microsoft 365 Business Standard' in str(line[1]):
                    if not entry_status:
                        if 'False' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    elif entry_status:
                        if 'True' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    self.dollar_price = 80

            elif license == 'Exchange Online (Plan 1)':
                if domain in str(line[0]) and 'Exchange Online (Plan 1)' in str(line[1]):
                    if not entry_status:
                        if 'False' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    elif entry_status:
                        if 'True' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    self.dollar_price = 25.60

            elif license == 'Microsoft 365 Business Premium':
                if domain in str(line[0]) and 'Microsoft 365 Business Premium' in str(line[1]):
                    if not entry_status:
                        if 'False' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    elif entry_status:
                        if 'True' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    self.dollar_price = 140.80

            elif license == 'Power BI Pro':
                if domain in str(line[0]) and 'Power BI Pro' in str(line[1]):
                    if not entry_status:
                        if 'False' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    elif entry_status:
                        if 'True' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    self.dollar_price = 140.80

            elif license == 'Power BI (Free)':
                if domain in str(line[0]) and 'Power BI (Free)' in str(line[1]):
                    if not entry_status:
                        if 'False' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    elif entry_status:
                        if 'True' in str(line[2]):
                            self.result_table.addItem(f'{line[0]}')
                            self.account_counter = self.account_counter + 1
                            self.save_list.append(line[0])
                    self.dollar_price = 140.80

            self.progressBar.setValue(self.progressBar.value() + 1)

    @staticmethod
    def report_error(msg, status):
        msgbox = QMessageBox()
        if status == 'Warning':
            msgbox.setIcon(QMessageBox.Warning)
        elif status == 'Critical':
            msgbox.setIcon(QMessageBox.Critical)

        msgbox.setText(msg)
        msgbox.setWindowTitle("Alerta")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.exec()

    def list_values(self, file_path):
        if file_path is None:
            self.report_error(
                'Você precisa importar um arquivo .csv', 'Warning')
        else:
            self.progressBar.show()
            self.save_list = []
            self.account_counter = 0
            self.result_table.clear()
            data = pd.read_csv(fr'{file_path[0]}', usecols=[
                               'Nome UPN', 'Licenças', 'Bloquear credencial'])
            df = pd.DataFrame(
                data, columns=['Nome UPN', 'Licenças', 'Bloquear credencial'])
            self.list = df.values.tolist()

            license_combobox = self.license_combobox.currentText()
            domain_combobox = self.domain_combobox.currentText()
            status_login = self.block_radioButton.isChecked()

            qtde_accounts = 0

            if self.filter_checkBox.isChecked():
                self.filter_file(
                    domain_combobox, license_combobox, status_login)
                self.qtde_accounts_label.setText(str(self.account_counter))
                total_price = self.account_counter * self.dollar_price
                self.total_coast_label.setText(
                    '${:,.2f}'.format(total_price))
                self.progressBar.setValue(self.progressBar.value() + 1)
            else:
                self.progressBar.show()
                for line in self.list:
                    if '#EXT' not in str(line[0]) and 'nan' not in str(line[1]):
                        self.result_table.addItem(f'{line[0]}')
                        self.account_counter = self.account_counter + 1
                        self.save_list.append(line[0])

                        self.load_combobox(line)

                    elif '#EXT#' in str(line[0]) and 'nan' not in str(line[1]):
                        self.result_table.addItem(f'{line[0]}')
                        self.account_counter = self.account_counter + 1
                        self.save_list.append(line[0])
                    self.progressBar.setValue(self.progressBar.value() + 1)
                self.qtde_accounts_label.setText(str(self.account_counter))
                resultado_total = qtde_accounts * self.dollar_price
                self.total_coast_label.setText(
                    '${:,.2f}'.format(resultado_total))

        time.sleep(0.5)
        self.progressBar.hide()
        self.progressBar.reset()

    def load_combobox(self, linha):

        if "@" in linha[0]:
            account_mail = linha[0].split("@")
            if str(account_mail[1]) not in self.list_combobox:
                self.domain_combobox.addItem(str(account_mail[1]).rstrip())
                self.list_combobox.append(str(account_mail[1]))

    def save_file(self):
        print(self.save_list)
        if self.list != None:
            try:
                filename, _ = QFileDialog.getSaveFileName(
                    self, "Save text file", "", "Text Files (*.txt)")
                archive = open(filename, 'w')
                for linha in self.save_list:
                    if linha == self.save_list[-1]:
                        archive.write(str(linha))
                    else:
                        archive.write(str(linha + ',\n'))
                archive.close()
                self.save_list = []
            except FileNotFoundError:
                self.progressBar.hide()
        else:
            self.report_error('Não existem dados para serem salvos.', 'Alert')
