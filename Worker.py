from PyQt5.QtCore import QObject, QThread, pyqtSignal
import subprocess

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self, filename):
        for i in range(100):
            self.progress.emit(i + 1)

        self.finished.emit()
        cmd = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe ', f'{filename}'
        try:
            completed = subprocess.run(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        except:
            print('Erro ao rodar o comando')