import sys
import os
from PyQt6 import QtWidgets, uic

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Always find the .ui file relative to this script's location
        ui_path = os.path.join(os.path.dirname(__file__), "calculatorui.ui")
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Simple Calculator")

        self.setStyleSheet("""
    QMainWindow {
        background-color: #0a0a0a;
    }
    /* Default buttons */
    QPushButton {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 #16213e, stop:0.5 #1a237e, stop:1 #0d47a1);
        color: rgba(255, 255, 255, 0.9);
        border: 1px solid #1a237e;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-weight: 300;
    }
    QPushButton:hover {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 #1e2a4a, stop:0.5 #283593, stop:1 #1565c0);
    }
    QPushButton:pressed {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 #0d47a1, stop:1 #16213e);
    }

    /* Clear button */
    QPushButton#clearbutton {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 #00acc1, stop:1 #00838f);
        border: 1px solid #00838f;
        font-weight: 400;
    }
    QPushButton#clearbutton:hover {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 #26c6da, stop:1 #0097a7);
    }

    /* Equal button */
    QPushButton#equalbutton {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 #2962ff, stop:1 #0039cb);
        border: 1px solid #0039cb;
        font-weight: 500;
    }
    QPushButton#equalbutton:hover {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 #448aff, stop:1 #2962ff);
    }

    /* Glassy display (Qt-compatible) */
    QLineEdit#display {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 rgba(50, 50, 50, 0.9), stop:1 rgba(30, 30, 30, 0.9));
        color: rgba(255, 255, 255, 0.95);
        font-size: 24px;
        font-family: 'Segoe UI Light', Arial, sans-serif;
        border: 1px solid rgba(100, 100, 100, 0.4);
        border-radius: 8px;
        padding: 10px;
        selection-background-color: rgba(100, 150, 255, 0.4);
    }
    QLineEdit#display:focus {
        border: 1px solid rgba(100, 150, 255, 0.6);
    }
""")

        # Display
        self.display = self.findChild(QtWidgets.QLineEdit, "display")

        # Digits
        for i in range(10):
            button = self.findChild(QtWidgets.QPushButton, f"btn{i}")
            if button:
                button.clicked.connect(lambda _, b=i: self.append_text(str(b)))

        # Operators
        self.findChild(QtWidgets.QPushButton, "addbutton").clicked.connect(lambda: self.append_text("+"))
        self.findChild(QtWidgets.QPushButton, "subbutton").clicked.connect(lambda: self.append_text("-"))
        self.findChild(QtWidgets.QPushButton, "mulbutton").clicked.connect(lambda: self.append_text("*"))
        self.findChild(QtWidgets.QPushButton, "divbutton").clicked.connect(lambda: self.append_text("/"))
        self.findChild(QtWidgets.QPushButton, "modbutton").clicked.connect(lambda: self.append_text("%"))
        self.findChild(QtWidgets.QPushButton, "dotbutton").clicked.connect(lambda: self.append_text("."))

        # Functions
        self.findChild(QtWidgets.QPushButton, "equalbutton").clicked.connect(self.calculate_result)
        self.findChild(QtWidgets.QPushButton, "clearbutton").clicked.connect(self.clear_display)
        self.findChild(QtWidgets.QPushButton, "backbutton").clicked.connect(self.backspace)

    def append_text(self, char):
        self.display.setText(self.display.text() + char)

    def clear_display(self):
        self.display.clear()

    def backspace(self):
        self.display.setText(self.display.text()[:-1])

    def calculate_result(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except Exception:
            self.display.setText("Error")           

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
