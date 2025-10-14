"""This module serves as a basis for your project. You can either use NiceGUI
or Pyside to start.

The project assumes that your main entrypoint is the function run() of this file
(see pyproject.toml scripts)
"""

import numpy as np
from {{ cookiecutter.package_name }}.my_module import typed_function
from PySide6.QtWidgets import QApplication, QWidget
import sys


def run():
    app = QApplication(sys.argv)

    widget = QWidget()
    widget.setWindowTitle("Hello World")
    widget.show()

    app.exec()
    typed_function(np.zeros(10), "")
    """This is the main function that gets run"""
