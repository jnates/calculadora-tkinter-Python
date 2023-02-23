import tkinter as tk
import unittest

class Calculator(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x250")
        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, width=30, font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        button_list = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        for button_text in button_list:
            button = tk.Button(self, text=button_text, width=5, height=2, font=('Arial', 14),
                               command=lambda text=button_text:self.button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        clear_button = tk.Button(self, text='C', width=5, height=2, font=('Arial', 14),
                                 command=self.clear_display)
        clear_button.grid(row=row, column=0, padx=5, pady=5)

    def button_click(self, text):
        if text == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = 'Error'
        elif text == 'C':
            self.expression = ""
        else:
            self.expression += text
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def clear_display(self):
        self.expression = ""
        self.display.delete(0, tk.END)

class TestCalculatorAddition(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.calculator.button_click('1')
        self.calculator.button_click('+')
        self.calculator.button_click('2')
        self.calculator.button_click('=')
        self.assertEqual(self.calculator.expression, '3')

class TestCalculatorSubtraction(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_subtraction(self):
        self.calculator.button_click('5')
        self.calculator.button_click('-')
        self.calculator.button_click('3')
        self.calculator.button_click('=')
        self.assertEqual(self.calculator.expression, '2')

class TestCalculatorMultiplication(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_multiplication(self):
        self.calculator.button_click('2')
        self.calculator.button_click('*')
        self.calculator.button_click('4')
        self.calculator.button_click('=')
        self.assertEqual(self.calculator.expression, '8')

class TestCalculatorDivision(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_division(self):
        self.calculator.button_click('9')
        self.calculator.button_click('/')
        self.calculator.button_click('3')
        self.calculator.button_click('=')
        self.assertEqual(self.calculator.expression, '3')

class TestCalculatorDecimal(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_decimal(self):
        self.calculator.button_click('1')
        self.calculator.button_click
