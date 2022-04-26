import subprocess
import sys
import time
from Worker import *
from asyncio import CancelledError
from cProfile import run
from functools import partial
import pandas as pd
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

from PyQt5.QtCore import QObject, QThread, pyqtSignal

from gui.design import Ui_MainWindow

class FormatCSV(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.account_counter = None
        self.file_path = None
        self.list = None
        self.save_list = []
        self.progressBar.hide()
        self.price = 0

        self.generate_btn.setEnabled(False)

        self.office_365_e3 = 23.00
        self.office_365_e1 = 10.00
        self.microsoft_365_business_standard = 12.50
        self.microsoft_365_business_premium = 22.00
        self.exchange_online_plan1 = 8.0
        self.power_bi_pro = 9.99

        self.update_btn.setIcon(QtGui.QIcon("img/search.ico"))
        self.filter_checkBox.setIcon(QtGui.QIcon("img/filter_import.ico"))
        self.generate_btn.setIcon(QtGui.QIcon("img/terminal_script.ico"))
        self.show_script_btn.setIcon(QtGui.QIcon("img/refresh.ico"))
        self.capture_members_btn.setIcon(QtGui.QIcon("img/refresh.ico"))

        self.filter_checkBox.clicked.connect(
            lambda: self.enable_filter_fields())
        self.update_btn.clicked.connect(
            lambda: self.list_values(self.file_path))
        self.import_file_action.triggered.connect(
            lambda: self.import_file())
        self.save_action.triggered.connect(lambda: self.save_list_file())
        self.generate_btn.clicked.connect(lambda: self.save_script())
        self.show_script_btn.clicked.connect(lambda: self.show_script())

        # Combo Box - Group Types
        self.type_group_combobox.addItem('Security')
        self.type_group_combobox.addItem('List distribuition')
        self.type_group_combobox.addItem('Office 365')

        # Combo Box - Licenses
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
                    self.price = 0
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
                    self.price = self.office_365_e3

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
                    self.price = self.office_365_e1

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
                    self.price = self.microsoft_365_business_standard

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
                    self.price = self.exchange_online_plan1

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
                    self.price = self.microsoft_365_business_premium

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
                    self.price = self.power_bi_pro

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
                    self.price = 0

            self.progressBar.setValue(self.progressBar.value() + 1)

    @staticmethod
    def report_error(msg, status):
        msgbox = QMessageBox()
        if status == 'Warning':
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setWindowTitle("Warning")
        elif status == 'Critical':
            msgbox.setIcon(QMessageBox.Critical)
            msgbox.setWindowTitle("Critical")
        msgbox.setText(msg)
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.exec()

    def list_values(self, file_path):
        if file_path is None:
            self.report_error(
                'You need to import a csv file.', 'Warning')
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
                total_price = self.account_counter * self.price
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
                        self.load_domain_combobox(line)

                    elif '#EXT#' in str(line[0]) and 'nan' not in str(line[1]):
                        self.result_table.addItem(f'{line[0]}')
                        self.account_counter = self.account_counter + 1
                        self.save_list.append(line[0])
                    self.progressBar.setValue(self.progressBar.value() + 1)
                self.qtde_accounts_label.setText(str(self.account_counter))
                resultado_total = qtde_accounts * self.price
                self.total_coast_label.setText(
                    '${:,.2f}'.format(resultado_total))

        time.sleep(0.5)
        self.progressBar.hide()
        self.progressBar.reset()

    def load_domain_combobox(self, linha):

        if "@" in linha[0]:
            account_mail = linha[0].split("@")
            if str(account_mail[1]) not in self.list_combobox:
                self.domain_combobox.addItem(str(account_mail[1]).rstrip())
                self.list_combobox.append(str(account_mail[1]))

    def save_list_file(self):
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

    def run_script_in_thread(self, filename):

        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(partial(self.worker.run, filename))
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.report_script_progress)
        # Step 6: Start the thread
        self.thread.start()

        self.generate_btn.setEnabled(False)
        self.progressBar.hide()
        self.thread.finished.connect(
            lambda: self.enable_scripts_functions()

        )

    def enable_scripts_functions(self):
        self.generate_btn.setEnabled(True)
        self.script_progressBar.hide()

    def report_script_progress(self, progress_status):
        self.script_progressBar.setValue(progress_status)

    def save_script(self):
        script_commands = self.show_script()
        if script_commands == None:
            pass
        else:
            button_clicked = QMessageBox.question(self, 'Execute', "save the file .ps1 before execute.",
                                                  QMessageBox.Yes | QMessageBox.Cancel)
            if button_clicked == QMessageBox.Yes:
                try:
                    filename, _ = QFileDialog.getSaveFileName(
                        self, "Save .ps1 file", "", "Shell Files (*.ps1)")
                    archive = open(filename, 'w')
                    archive.write(script_commands)
                    self.run_script_in_thread(filename)
                    archive.close()
                except FileNotFoundError:
                    self.progressBar.hide()
                except PermissionError:
                    pass
            elif button_clicked == QMessageBox.Cancel:
                print('tarefa cancelada.')

    def show_script(self):
        self.generate_btn.setEnabled(True)
        self.list_script.clear()
        group_name = self.name_group.text()
        type_group = self.type_group_combobox.currentText()

        if 'Security' in type_group:
            create_security_group = f'Connect-AzureAD \nNew-AzureADGroup -DisplayName "{group_name}" \
            -MailEnabled $false -SecurityEnabled $true -MailNickName "NotSet"\nDisconnect-AzureAD'
            self.list_script.appendPlainText(create_security_group)
            return create_security_group
        elif 'Distribuition list' in type_group:
            pass
        elif 'Office 365' in type_group:
            pass
