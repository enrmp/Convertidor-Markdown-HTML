
import imp
import sys

from PySide6.QtWidgets import QApplication
import PySide6.QtCore as QtCore
from controllers.main import MainWindowForm


if __name__ == '__main__':
    app = QApplication()

    window = MainWindowForm()
    
    window.show()

    sys.exit(app.exec())