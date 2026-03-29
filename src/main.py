import sys
from PySide6 import QtUiTools
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLCDNumber

from .components.lexica import MyLexer
from .components.parsers import MyParser
from .components.memory import Memory
from .components.ui import Ui_MainWindow

# Main window class for the propositional logic evaluator GUI
class MainWindow(QMainWindow):

    # Type hints for UI elements (for IntelliSense and clarity)
    # button_1:QPushButton
    # button_2:QPushButton
    # button_plus:QPushButton
    # button_equal:QPushButton

    button_1:QPushButton
    button_2:QPushButton
    button_and:QPushButton
    button_or:QPushButton
    button_equal:QPushButton
    input_text:QLineEdit
    output_lcd:QLCDNumber

    def __init__(self):
        # Initialize the main window with PySide6 QMainWindow
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #### Binding button to function ####
        # Method 1: Direct function binding
        # self.ui.button_1.clicked.connect(self.push_1)
        # # Method 2: Lambda for dynamic text
        # self.ui.button_2.clicked.connect(lambda: self.push("2"))
        # self.ui.button_plus.clicked.connect(lambda: self.push("+"))

        # Bind buttons to append specific characters to input
        self.ui.button_1.clicked.connect(lambda: self.push("t"))  # True
        self.ui.button_2.clicked.connect(lambda: self.push("f"))  # False
        self.ui.button_and.clicked.connect(lambda: self.push("^"))  # AND operator
        self.ui.button_or.clicked.connect(lambda: self.push("v"))   # OR operator

        # Bind equal button to evaluate the expression
        self.ui.button_equal.clicked.connect(self.push_equal)

    # def push_1(self):
    #     current_text:str = self.ui.input_text.text()
    #     self.ui.input_text.setText(f"{current_text}1")
    
    # Append a character to the input text field
    def push(self, text:str):
        current_text:str = self.ui.input_text.text()
        self.ui.input_text.setText(f"{current_text}{text}")
    
    # Evaluate the propositional logic expression when "=" is pressed
    def push_equal(self):
        print("Calculate")  # Debug message
        # Initialize components
        lexer = MyLexer()
        parser = MyParser()
        memory = Memory()  # Not used in current logic evaluator
        input_text = self.ui.input_text.text()

        # Tokenize and parse the input expression
        value, prefix = parser.parse(lexer.tokenize(input_text))
        print(type(value), type(prefix))  # Debug: types of result
        print(f"Value: {value}")  # Debug: boolean result
        print(f"Prefix: {prefix}")  # Debug: prefix notation

        # Convert boolean to TRUE/FALSE string
        result_text = "TRUE" if value else "FALSE"

        # Update the label with out_put label and show the result in T and F with prefix
        self.ui.output_label.setText(f"Result: {result_text}\nPrefix: {prefix}")
        # Output bool value
        self.ui.output_lcd.display(int(value))  # True -> 1, False -> 0

        # for debug
        print(memory)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())