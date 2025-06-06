import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, LEFT
import math
import random
import operator
import time
import threading
import asyncio
import webbrowser
import os

class CalculatorApp(toga.App):
    def show_result_slide(self, message, return_callback):
        self.result_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#D1FFD6"))
        self.result_label = toga.Label(message, style=Pack(padding=10, font_size=18))
        back_btn = toga.Button("Back", on_press=return_callback, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.result_box.add(self.result_label)
        self.result_box.add(back_btn)
        self._switch_view(self.result_box)

    def show_menu(self, widget=None):
        self._switch_view(self.main_menu)

    def show_basic(self, widget=None):
        self._switch_view(self.basic_ops_box)

    def show_advanced(self, widget=None):
        self._switch_view(self.advanced_ops_box)

    def show_abacus(self, widget=None):
        self._switch_view(self.abacus_box)

    def show_abacus_ii(self, widget=None):
        self._switch_view(self.abacus_ii_box)

    def show_square_root(self, widget=None):
        self._switch_view(self.sqrt_box)

    def show_square_root_practice(self, widget=None):
        self._switch_view(self.sqrt_prac_box)

    def show_square(self, widget=None):
        self._switch_view(self.square_box)

    def show_square_practice(self, widget=None):
        self._switch_view(self.square_prac_box)
    
    def show_abacus_learning(self, widget=None):
        self._switch_view(self.abacus_learning_box)

    def show_cube(self, widget=None):
        self._switch_view(self.cube_box)

    def show_cube_practice(self, widget=None):
        self._switch_view(self.cube_prac_box)

    def show_cube_root(self, widget=None):
        self._switch_view(self.cube_root_box)

    def show_cube_root_practice(self, widget=None):
        self._switch_view(self.cube_root_prac_box)
    
    def show_decimal_study(self, widget=None):
        self._switch_view(self.decimal_study_box)


    def open_tutorial(self, widget):
        try:
           # Try using Toga's native browser (works on mobile)
           toga.App.app.browser.open("https://youtu.be/X9hXwfFk0Jw?si=BfZkfkWHh2igU-N9")
        except Exception:
        # Fallback for desktop environments
            webbrowser.open("https://youtu.be/X9hXwfFk0Jw?si=BfZkfkWHh2igU-N9")

    def _switch_view(self, view):
        for child in list(self.main_box.children):
            self.main_box.remove(child)
        self.main_box.add(view)
    
    def startup(self):
        self.history = []
        self.main_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1))

        self.create_basic_operations()
        self.create_advanced_operations()
        self.create_menu_content()
        self.create_abacus_practice()
        self.create_abacus_ii()
        self.create_abacus_learning()
        self.create_square_root()
        self.create_square_root_practice()
        self.create_square()
        self.create_square_practice()
        self.create_cube()
        self.create_cube_practice()
        self.create_cube_root()             
        self.create_cube_root_practice()
        self.create_decimal_study()

        self.main_box.add(self.main_menu)

        self.main_window = toga.MainWindow(title=self.formal_name, size=(360, 640))
        self.main_window.content = self.main_box
        self.main_window.show()

    
    
    def create_menu_content(self):
        self.main_menu = toga.ScrollContainer(horizontal=False, style=Pack(flex=1))
        self.menu_content = toga.Box(style=Pack(direction=COLUMN, padding=10, background_color="#8DFFE2"))

        label = toga.Label(
            "Welcome To MyMathshelper!!",
            style=Pack(font_size=14, padding=10, font_family="Comic Sans MS", font_weight="bold", background_color="#8DFFE2", text_align="center"),
        )
        self.menu_content.add(label)

        tile_grid = toga.Box(style=Pack(direction=COLUMN, padding=5))

        tile_data = [
            ("🧮", "Calculator", self.show_basic),
            ("🔬", "Scientific+Math", self.show_advanced),
            ("🧠", "Abacus Practice", self.show_abacus),
            ("➕", "Abacus II", self.show_abacus_ii),
            ("📘", "Abacus Learn", self.show_abacus_learning),
            ("√", "√x", self.show_square_root),
            ("🧩", "√x Practice", self.show_square_root_practice),
            ("²", "x²", self.show_square),
            ("🎯", "x² Practice", self.show_square_practice),
            ("³", "x³", self.show_cube),
            ("🧪", "x³ Practice", self.show_cube_practice),
            ("🧿", "³√x", self.show_cube_root),
            ("📐", "³√x Practice", self.show_cube_root_practice),
            ("🔢", "Decimal Study", self.show_decimal_study),
            ("🎥", "App Tutorial", self.open_tutorial)
        ]

        row_box = None
        for idx, (emoji, title, action) in enumerate(tile_data):
            if idx % 2 == 0:
                row_box = toga.Box(style=Pack(direction=ROW, padding=5))
                tile_grid.add(row_box)

            emoji_label = toga.Label(emoji, style=Pack(font_size=36, padding=5))
            button_box = toga.Box(style=Pack(direction=COLUMN, width=120, height=100, padding=5, alignment="center"))
            btn = toga.Button(
                title,
                on_press=action,
                style=Pack(width=100, height=50, font_size=10, background_color="#5CFD84", text_align="center")
            )
            button_box.add(emoji_label)
            button_box.add(btn)
            row_box.add(button_box)

        self.menu_content.add(tile_grid)

        footer_label = toga.Label(
            "© 2025 MyMathHelper — All Rights Reserved",
            style=Pack(padding=10, font_size=6, color="Black", text_align="center"),
        )
        self.menu_content.add(footer_label)

        self.main_menu.content = self.menu_content

    def create_basic_operations(self):
        self.basic_ops_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#5CFD84"))
        label = toga.Label("Calculator", style=Pack(font_size=20, font_family="Segoe Print", padding=10))
        self.basic_display = toga.TextInput(readonly=True, style=Pack(padding=10, font_size=18))
        self.basic_ops_box.add(label)
        self.basic_ops_box.add(self.basic_display)

        for row_vals in [["7", "8", "9", "/"], ["4", "5", "6", "*"], ["1", "2", "3", "-"], ["0", ".", "C", "+"], ["="]]:
            row = toga.Box(style=Pack(direction=ROW, padding=5, background_color="MediumSeaGreen"))
            for val in row_vals:
                btn = toga.Button(val, on_press=self.basic_button_press, style=Pack(flex=1, padding=5))
                row.add(btn)
            self.basic_ops_box.add(row)

        back_btn = toga.Button("Back", on_press=self.show_menu, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.basic_ops_box.add(back_btn)

    def basic_button_press(self, widget):
        label = widget.text
        current = self.basic_display.value or ""
        if label == "C":
            self.basic_display.value = ""
        elif label == "=":
            try:
                result = eval(current)
                self.basic_display.value = str(result)
            except Exception:
                self.basic_display.value = "Error"
        else:
            self.basic_display.value = current + label

    def create_advanced_operations(self):
        self.advanced_ops_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#5CFD84"))
        label = toga.Label("Scientific Math", style=Pack(font_size=20, font_family="Segoe Print", padding=10))
        self.adv_display = toga.TextInput(readonly=True, style=Pack(padding=10, font_size=18))
        self.advanced_ops_box.add(label)
        self.advanced_ops_box.add(self.adv_display)

        adv_funcs = [
            ["sin", "cos", "tan", "log"],
            ["sqrt", "abs", "(", ")"],
            ["pi", "e", "^", "C"],
        ]
        for row_vals in adv_funcs:
            row = toga.Box(style=Pack(direction=ROW, padding=5))
            for val in row_vals:
                btn = toga.Button(val, on_press=self.advanced_button_press, style=Pack(flex=1, padding=5, background_color="MediumSeaGreen"))
                row.add(btn)
            self.advanced_ops_box.add(row)

        numpad = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]
        for row_vals in numpad:
            row = toga.Box(style=Pack(direction=ROW, padding=5))
            for val in row_vals:
                btn = toga.Button(val, on_press=self.advanced_button_press, style=Pack(flex=1, padding=5, background_color="MediumSeaGreen"))
                row.add(btn)
            self.advanced_ops_box.add(row)

        back_btn = toga.Button("Back", on_press=self.show_menu, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.advanced_ops_box.add(back_btn)

    def advanced_button_press(self, widget):
        label = widget.text
        if label == "C":
            self.adv_display.value = ""
            return
        if label == "=":
            try:
                expression = self.adv_display.value.replace("^", "**")
                # Replace constants
                expression = expression.replace("pi", str(math.pi)).replace("e", str(math.e))
                # Replace functions with math module equivalents
                for func in ["sin", "cos", "tan", "log", "sqrt", "abs"]:
                    if func in expression:
                        expression = expression.replace(func, f"math.{func}")
                result = eval(expression)
                self.adv_display.value = str(result)
            except Exception:
                self.adv_display.value = "Error"
            return
        else:
            self.adv_display.value += label

    def create_abacus_practice(self):
        self.abacus_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#5CFD84"))

        label = toga.Label("Abacus Practice Setup", style=Pack(font_size=20, padding=10))
        self.abacus_box.add(label)

        self.op_select = toga.Selection(items=["Addition", "Subtraction", "Multiplication", "Division"], style=Pack(padding=5, background_color="MediumSeaGreen"))
        self.abacus_box.add(toga.Label("Select Operation:", style=Pack(padding=(10, 5, 0, 5))))
        self.abacus_box.add(self.op_select)

        self.digits_input = toga.TextInput(placeholder="Enter number of digits", style=Pack(padding=5))
        self.abacus_box.add(toga.Label("Number of Digits:", style=Pack(padding=(10, 5, 0, 5))))
        self.abacus_box.add(self.digits_input)

        self.rows_input = toga.TextInput(placeholder="Enter number of rows", style=Pack(padding=5))
        self.abacus_box.add(toga.Label("Number of Rows:", style=Pack(padding=(10, 5, 0, 5))))
        self.abacus_box.add(self.rows_input)

        self.time_input = toga.TextInput(placeholder="Enter time limit in seconds", style=Pack(padding=5))
        self.abacus_box.add(toga.Label("Time Limit (seconds):", style=Pack(padding=(10, 5, 0, 5))))
        self.abacus_box.add(self.time_input)

        start_btn = toga.Button("Start Practice", on_press=self.start_abacus_practice, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.abacus_box.add(start_btn)

        self.result_label = toga.Label("", style=Pack(padding=10, font_size=16, color="blue"))
        self.abacus_box.add(self.result_label)

        back_btn = toga.Button("Back", on_press=self.show_menu, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.abacus_box.add(back_btn)

    def start_abacus_practice(self, widget):
        operation = self.op_select.value
        digits = self.digits_input.value
        rows = self.rows_input.value
        time_limit = self.time_input.value

        # Validation
        if not operation:
            self.show_error("Please select an operation.")
            return
        if not digits or not digits.isdigit():
            self.show_error("Please enter a valid number of digits.")
            return
        if not rows or not rows.isdigit():
            self.show_error("Please enter a valid number of rows.")
            return
        if not time_limit or not time_limit.isdigit():
            self.show_error("Please enter a valid time limit in seconds.")
            return

        digits = int(digits)
        rows = int(rows)
        time_limit = int(time_limit)

        def generate_number(d):
            start = 10 ** (d - 1)
            end = (10 ** d) - 1
            return random.randint(start, end)

        numbers = [generate_number(digits) for _ in range(rows)]

        try:
            if operation == "Addition":
                result = sum(numbers)
            elif operation == "Subtraction":
                result = numbers[0]
                for n in numbers[1:]:
                    result -= n
            elif operation == "Multiplication":
                result = 1
                for n in numbers:
                    result *= n
            elif operation == "Division":
                result = numbers[0]
                for n in numbers[1:]:
                    if n == 0:
                        self.show_error("Division by zero encountered.")
                        return
                    result /= n
            else:
                self.show_error("Unsupported operation.")
                return
        except Exception as e:
            self.show_error(f"Error during calculation: {e}")
            return

        # Show only final result
        msg = f"Operation: {operation}\nResult: {result}\nDigits: {digits} | Rows: {rows} | Time Limit: {time_limit}s"
        self.show_result_slide(msg, self.show_abacus)

    def show_error(self, message):
        self.main_window.error_dialog("Input Error", message)

    def create_abacus_ii(self):
        self.abacus_ii_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#5CFD84"))

        label = toga.Label("Abacus II", style=Pack(font_size=20, font_family="Segoe Print", padding=10))
        self.abacus_ii_box.add(label)

        self.ab2_digits = toga.TextInput(placeholder="Number of digits", style=Pack(padding=5))
        self.ab2_rows = toga.TextInput(placeholder="Number of rows", style=Pack(padding=5))
        self.ab2_sums = toga.TextInput(placeholder="Number of sums", style=Pack(padding=5))

        self.abacus_ii_box.add(self.ab2_digits)
        self.abacus_ii_box.add(self.ab2_rows)
        self.abacus_ii_box.add(self.ab2_sums)

        add_sub_btn = toga.Button("Add/Sub", on_press=self.abacus_ii_add_sub, style=Pack(padding=5, background_color="MediumSeaGreen"))
        mul_div_btn = toga.Button("Mul/Div", on_press=self.abacus_ii_mul_div, style=Pack(padding=5, background_color="MediumSeaGreen"))

        self.abacus_ii_box.add(add_sub_btn)
        self.abacus_ii_box.add(mul_div_btn)

        self.ab2_result_label = toga.Label("", style=Pack(padding=10, font_size=16, color="green"))
        self.abacus_ii_box.add(self.ab2_result_label)

        back_btn = toga.Button("Back", on_press=self.show_menu, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.abacus_ii_box.add(back_btn)

    def abacus_ii_add_sub(self, widget):
        self.ab2_result_label.text = self._abacus_ii_calc(["+", "-"])

    def abacus_ii_mul_div(self, widget):
        self.ab2_result_label.text = self._abacus_ii_calc(["*", "/"])

    def _abacus_ii_calc(self, ops):
        try:
            digits = int(self.ab2_digits.value)
            rows = int(self.ab2_rows.value)
            sums = int(self.ab2_sums.value)
            numbers = [random.randint(10 ** (digits - 1), 10 ** digits - 1) for _ in range(sums)]
            result = numbers[0]
            expression = str(numbers[0])

            for n in numbers[1:]:
                op = random.choice(ops)
                expression += f" {op} {n}"
                if op == "+":
                    result += n
                elif op == "-":
                    result -= n
                elif op == "*":
                    result *= n
                elif op == "/":
                    result = result / n if n != 0 else result  # avoid div by zero

            return f"Result: {result}"
        except Exception as e:
            return f"Error: {e}"

    def create_square_root(self):
        self.sqrt_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#5CFD84"))
        label = toga.Label("Square Root Calculator", style=Pack(font_size=20, font_family="Segoe Print", padding=10))
        self.sqrt_box.add(label)

        self.sqrt_input = toga.TextInput(placeholder="Enter number", style=Pack(padding=5))
        self.sqrt_box.add(self.sqrt_input)

        btn_calc = toga.Button("Calculate Square Root", on_press=self.sqrt_calculate, style=Pack(padding=10, background_color="MediumSeaGreen"))
        back_btn = toga.Button("Back", on_press=self.show_menu, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.sqrt_box.add(btn_calc)
        self.sqrt_box.add(back_btn)

        self.sqrt_result_label = toga.Label("", style=Pack(padding=10))
        self.sqrt_box.add(self.sqrt_result_label)

    
    def sqrt_calculate(self, widget):
        try:
            val = float(self.sqrt_input.value)
            if val < 0:
                msg = "Cannot calculate square root of a negative number."
            else:
                result = math.sqrt(val)
                msg = f"Square root of {val} is {result:.6f}"
        except Exception:
            msg = "Please enter a valid number."
        self.show_result_slide(msg, self.show_square_root)
    def create_square_root_practice(self):
        self.sqrt_prac_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#5CFD84"))
        label = toga.Label("Square Root Practice", style=Pack(font_size=20, padding=10))
        self.sqrt_prac_box.add(label)

        self.sqrt_prac_num_questions = toga.TextInput(placeholder="Number of questions", style=Pack(padding=5))
        self.sqrt_prac_box.add(toga.Label("Number of questions:", style=Pack(padding=5)))
        self.sqrt_prac_box.add(self.sqrt_prac_num_questions)

        self.sqrt_prac_digits = toga.TextInput(placeholder="Number of digits", style=Pack(padding=5))
        self.sqrt_prac_box.add(toga.Label("Number of digits (for numbers):", style=Pack(padding=5)))
        self.sqrt_prac_box.add(self.sqrt_prac_digits)

        btn_start = toga.Button("Start Practice", on_press=self.sqrt_practice_start, style=Pack(padding=10, background_color="MediumSeaGreen"))
        back_btn = toga.Button("Back", on_press=self.show_menu, style=Pack(padding=10))
        self.sqrt_prac_box.add(btn_start)
        self.sqrt_prac_box.add(back_btn)

        # Practice state UI elements
        self.sqrt_question_label = toga.Label("", style=Pack(padding=10))
        self.sqrt_prac_box.add(self.sqrt_question_label)
        self.sqrt_answer_input = toga.TextInput(placeholder="Enter your answer", style=Pack(padding=5))
        self.sqrt_prac_box.add(self.sqrt_answer_input)
        self.sqrt_submit_btn = toga.Button("Submit Answer", on_press=self.sqrt_practice_submit, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.sqrt_prac_box.add(self.sqrt_submit_btn)

        self.sqrt_feedback_label = toga.Label("", style=Pack(padding=10))
        self.sqrt_prac_box.add(self.sqrt_feedback_label)

        self.sqrt_prac_state = None

        # Initially hide question & answer controls
        self.sqrt_question_label.visible = False
        self.sqrt_answer_input.visible = False
        self.sqrt_submit_btn.visible = False
        self.sqrt_feedback_label.visible = False

    def sqrt_practice_start(self, widget):
        try:
            num_q = int(self.sqrt_prac_num_questions.value)
            digits = int(self.sqrt_prac_digits.value)
            if num_q <= 0 or digits <= 0:
                raise ValueError
        except Exception:
            self.sqrt_feedback_label.text = "Please enter valid positive integers for number of questions and digits."
            self.sqrt_feedback_label.visible = True
            return

        self.sqrt_prac_state = {
            "num_questions": num_q,
            "digits": digits,
            "current": 0,
            "correct": 0,
            "wrong": 0,
            "questions": [],
        }
        # Generate questions - numbers to take sqrt of
        self.sqrt_prac_state["questions"] = [random.randint(10 ** (digits - 1), 10 ** digits - 1) for _ in range(num_q)]

        self.sqrt_feedback_label.text = ""
        self.sqrt_feedback_label.visible = False
        self.sqrt_answer_input.value = ""

        # Show question and input UI
        self.sqrt_question_label.visible = True
        self.sqrt_answer_input.visible = True
        self.sqrt_submit_btn.visible = True
        self.show_next_sqrt_question()

    def show_next_sqrt_question(self):
        state = self.sqrt_prac_state
        if state["current"] >= state["num_questions"]:
            # Practice finished
            correct = state["correct"]
            wrong = state["wrong"]
            self.sqrt_question_label.text = "Practice Complete."
            self.sqrt_feedback_label.text = f"Correct: {correct}, Wrong: {wrong}"
            self.sqrt_feedback_label.visible = True
            self.sqrt_answer_input.visible = False
            self.sqrt_submit_btn.visible = False
            return

        current_num = state["questions"][state["current"]]
        self.sqrt_question_label.text = f"Question {state['current'] + 1}: What is the square root of {current_num} (rounded to 4 decimals)?"
        self.sqrt_answer_input.value = ""
        self.sqrt_feedback_label.text = ""

    def sqrt_practice_submit(self, widget):
        state = self.sqrt_prac_state
        if not state:
            return

        current_num = state["questions"][state["current"]]
        try:
            user_ans = float(self.sqrt_answer_input.value)
        except Exception:
            self.sqrt_feedback_label.text = "Please enter a valid number."
            self.sqrt_feedback_label.visible = True
            return

        correct_ans = round(math.sqrt(current_num), 4)
        if abs(user_ans - correct_ans) < 0.0001:
            self.sqrt_feedback_label.text = "Correct!"
            state["correct"] += 1
        else:
            self.sqrt_feedback_label.text = f"Wrong. Correct answer is {correct_ans}"
            state["wrong"] += 1
        self.sqrt_feedback_label.visible = True
        state["current"] += 1

        # Move to next question
        self.show_next_sqrt_question()

    def create_square(self):
        self.square_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#5CFD84"))
        label = toga.Label("Square Calculator", style=Pack(font_size=20, font_family="Segoe Print", padding=10))
        self.square_box.add(label)

        self.square_input = toga.TextInput(placeholder="Enter number", style=Pack(padding=5))
        self.square_box.add(self.square_input)

        btn_calc = toga.Button("Calculate Square", on_press=self.square_calculate, style=Pack(padding=10, background_color="MediumSeaGreen"))
        back_btn = toga.Button("Back", on_press=self.show_menu, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.square_box.add(btn_calc)
        self.square_box.add(back_btn)

        self.square_result_label = toga.Label("", style=Pack(padding=10))
        self.square_box.add(self.square_result_label)

    
    def square_calculate(self, widget):
        try:
            val = float(self.square_input.value)
            result = val * val
            msg = f"Square of {val} is {result}"
        except Exception:
            msg = "Please enter a valid number."
        self.show_result_slide(msg, self.show_square)
    def create_square_practice(self):
        self.square_prac_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="olive"))
        label = toga.Label("Square Practice", style=Pack(font_size=20, font_family="Segoe Print", padding=10))
        self.square_prac_box.add(label)

        self.square_prac_num_questions = toga.TextInput(placeholder="Number of questions", style=Pack(padding=5))
        self.square_prac_box.add(toga.Label("Number of questions:", style=Pack(padding=5)))
        self.square_prac_box.add(self.square_prac_num_questions)

        self.square_prac_digits = toga.TextInput(placeholder="Number of digits", style=Pack(padding=5))
        self.square_prac_box.add(toga.Label("Number of digits (for numbers):", style=Pack(padding=5)))
        self.square_prac_box.add(self.square_prac_digits)

        btn_start = toga.Button("Start Practice", on_press=self.square_practice_start, style=Pack(padding=10, background_color="MediumSeaGreen"))
        back_btn = toga.Button("Back", on_press=self.show_menu, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.square_prac_box.add(btn_start)
        self.square_prac_box.add(back_btn)

        # Practice state UI elements
        self.square_question_label = toga.Label("", style=Pack(padding=10))
        self.square_prac_box.add(self.square_question_label)
        self.square_answer_input = toga.TextInput(placeholder="Enter your answer", style=Pack(padding=5))
        self.square_prac_box.add(self.square_answer_input)
        self.square_submit_btn = toga.Button("Submit Answer", on_press=self.square_practice_submit, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.square_prac_box.add(self.square_submit_btn)

        self.square_feedback_label = toga.Label("", style=Pack(padding=10))
        self.square_prac_box.add(self.square_feedback_label)

        self.square_prac_state = None

        # Initially hide question & answer controls
        self.square_question_label.visible = False
        self.square_answer_input.visible = False
        self.square_submit_btn.visible = False
        self.square_feedback_label.visible = False

    def square_practice_start(self, widget):
        try:
            num_q = int(self.square_prac_num_questions.value)
            digits = int(self.square_prac_digits.value)
            if num_q <= 0 or digits <= 0:
                raise ValueError
        except Exception:
            self.square_feedback_label.text = "Please enter valid positive integers for number of questions and digits."
            self.square_feedback_label.visible = True
            return

        self.square_prac_state = {
            "num_questions": num_q,
            "digits": digits,
            "current": 0,
            "correct": 0,
            "wrong": 0,
            "questions": [],
        }
        # Generate questions - numbers to square
        self.square_prac_state["questions"] = [random.randint(10 ** (digits - 1), 10 ** digits - 1) for _ in range(num_q)]

        self.square_feedback_label.text = ""
        self.square_feedback_label.visible = False
        self.square_answer_input.value = ""

        # Show question and input UI
        self.square_question_label.visible = True
        self.square_answer_input.visible = True
        self.square_submit_btn.visible = True
        self.show_next_square_question()

    def show_next_square_question(self):
        state = self.square_prac_state
        if state["current"] >= state["num_questions"]:
            # Practice finished
            correct = state["correct"]
            wrong = state["wrong"]
            self.square_question_label.text = "Practice Complete."
            self.square_feedback_label.text = f"Correct: {correct}, Wrong: {wrong}"
            self.square_feedback_label.visible = True
            self.square_answer_input.visible = False
            self.square_submit_btn.visible = False
            return

        current_num = state["questions"][state["current"]]
        self.square_question_label.text = f"Question {state['current'] + 1}: What is the square of {current_num}?"
        self.square_answer_input.value = ""
        self.square_feedback_label.text = ""

    def square_practice_submit(self, widget):
        state = self.square_prac_state
        if not state:
            return

        current_num = state["questions"][state["current"]]
        try:
            user_ans = float(self.square_answer_input.value)
        except Exception:
            self.square_feedback_label.text = "Please enter a valid number."
            self.square_feedback_label.visible = True
            return

        correct_ans = current_num * current_num
        if abs(user_ans - correct_ans) < 0.0001:
            self.square_feedback_label.text = "Correct!"
            state["correct"] += 1
        else:
            self.square_feedback_label.text = f"Wrong. Correct answer is {correct_ans}"
            state["wrong"] += 1
        self.square_feedback_label.visible = True
        state["current"] += 1

        self.show_next_square_question()

    def create_abacus_learning(self):
        self.abacus_learning_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#5CFD84"))
        label = toga.Label("Abacus Learning", style=Pack(font_size=20, font_family="Segoe Print", padding=10))
        self.abacus_learning_box.add(label)

        btn_learning = toga.Button("Learning (Tutorial)", on_press=self.abacus_learning_tutorial, style=Pack(padding=10, background_color="MediumSeaGreen"))
        btn_practice = toga.Button("Practice", on_press=self.abacus_learning_practice, style=Pack(padding=10, background_color="MediumSeaGreen"))
        btn_test = toga.Button("Test", on_press=self.abacus_learning_test, style=Pack(padding=10, background_color="MediumSeaGreen"))
        back_btn = toga.Button("Back to Main Menu", on_press=self.show_menu, style=Pack(padding=10, background_color="MediumSeaGreen"))

        for btn in [btn_learning, btn_practice, btn_test, back_btn]:
            self.abacus_learning_box.add(btn)

    def abacus_learning_tutorial(self, widget):
        self.tutorial_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#5CFD84"))

        tutorial_text = (
            "Abacus Tutorial:\n\n"
            "The abacus is a simple tool for arithmetic calculations.\n"
            "It consists of rods with beads that can represent numbers.\n"
            "You can perform addition and subtraction by moving beads.\n"
            "This tutorial will teach you the basic principles of using an abacus.\n\n"
            "1. Understand the place values (ones, tens, hundreds...)\n"
            "2. Practice moving beads to represent numbers.\n"
            "3. Learn addition by combining beads.\n"
            "4. Learn subtraction by removing beads.\n\n"
            "5. Using the abacus calculator you can calculate things at a really good speed.\n"
            "Try the Practice mode to apply these concepts."
        )
        tutorial_label = toga.MultilineTextInput(readonly=True, style=Pack(flex=1, padding=10))
        tutorial_label.value = tutorial_text

        back_btn = toga.Button("Back to Abacus Learning Menu", on_press=self.show_abacus_learning, style=Pack(padding=10, background_color="MediumSeaGreen"))

        self.tutorial_box.add(tutorial_label)
        self.tutorial_box.add(back_btn)

        self._switch_view(self.tutorial_box)

    def abacus_learning_practice(self, widget):
        self.practice_setup_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#5CFD84"))
        label = toga.Label("Practice Mode Setup", style=Pack(font_size=20, font_family="Segoe Print", padding=10))

        self.practice_digit_input = toga.TextInput(placeholder="Enter number of digits", style=Pack(padding=10))
        self.practice_time_input = toga.TextInput(placeholder="Enter time limit (seconds)", style=Pack(padding=10))
        btn_start = toga.Button("Start Practice", on_press=self.start_practice_session, style=Pack(padding=10, background_color="MediumSeaGreen"))
        btn_back = toga.Button("Back to Abacus Learning Menu", on_press=self.show_abacus_learning, style=Pack(padding=10, background_color="MediumSeaGreen"))

        self.practice_setup_box.add(label)
        self.practice_setup_box.add(self.practice_digit_input)
        self.practice_setup_box.add(self.practice_time_input)
        self.practice_setup_box.add(btn_start)
        self.practice_setup_box.add(btn_back)

        self._switch_view(self.practice_setup_box)

    def start_practice_session(self, widget):
        try:
            self.practice_digits = int(self.practice_digit_input.value)
            self.practice_time_limit = int(self.practice_time_input.value)
        except ValueError:
            self.main_window.info_dialog("Input Error", "Please enter valid integers.")
            return

        self.practice_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1))

        self.practice_question_label = toga.Label("", style=Pack(font_size=18, padding=10))
        self.practice_input = toga.TextInput(style=Pack(padding=10))
        self.practice_feedback = toga.Label("", style=Pack(padding=10))
        btn_check = toga.Button("Check Answer", on_press=self.check_practice_answer, style=Pack(padding=10, background_color="MediumSeaGreen"))
        btn_back = toga.Button("Back to Abacus Learning Menu", on_press=self.show_abacus_learning, style=Pack(padding=10, background_color="MediumSeaGreen"))

        self.practice_box.add(self.practice_question_label)
        self.practice_box.add(self.practice_input)
        self.practice_box.add(btn_check)
        self.practice_box.add(self.practice_feedback)
        self.practice_box.add(btn_back)

        self._switch_view(self.practice_box)
        self.generate_practice_question()

        def time_up():
            self.practice_feedback.text = "Time's up!"
            self.practice_input.enabled = False

        threading.Timer(self.practice_time_limit, time_up).start()

    def generate_practice_question(self):
        expr, self.practice_answer = self.generate_expression(self.practice_digits)
        self.practice_question_label.text = f"What is {expr}?"
        self.practice_input.value = ""
        self.practice_feedback.text = ""

    def check_practice_answer(self, widget):
        user_input = self.practice_input.value.strip()
        try:
            if abs(float(user_input) - self.practice_answer) < 0.01:
                self.practice_feedback.text = "Correct!"
            else:
                self.practice_feedback.text = f"Incorrect. Answer was {self.practice_answer}"
        except ValueError:
            self.practice_feedback.text = "Please enter a valid number."
        asyncio.create_task(self._next_practice_question())

    async def _next_practice_question(self):
        await asyncio.sleep(2)
        self.generate_practice_question()

    def abacus_learning_test(self, widget):
        self.test_setup_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#5CFD84"))
        label = toga.Label("Test Mode Setup", style=Pack(font_size=20, font_family="Segoe Print", padding=10))

        self.test_digit_input = toga.TextInput(placeholder="Enter number of digits", style=Pack(padding=10))
        self.test_time_input = toga.TextInput(placeholder="Enter time limit (seconds)", style=Pack(padding=10))
        btn_start = toga.Button("Start Test", on_press=self.start_test_session, style=Pack(padding=10, background_color="MediumSeaGreen"))
        btn_back = toga.Button("Back to Abacus Learning Menu", on_press=self.show_abacus_learning, style=Pack(padding=10, background_color="MediumSeaGreen"))

        self.test_setup_box.add(label)
        self.test_setup_box.add(self.test_digit_input)
        self.test_setup_box.add(self.test_time_input)
        self.test_setup_box.add(btn_start)
        self.test_setup_box.add(btn_back)

        self._switch_view(self.test_setup_box)

    def start_test_session(self, widget):
        try:
            self.test_digits = int(self.test_digit_input.value)
            self.test_time_limit = int(self.test_time_input.value)
        except ValueError:
            self.main_window.info_dialog("Input Error", "Please enter valid integers.")
            return

        self.test_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#5CFD84"))

        self.test_question_label = toga.Label("", style=Pack(font_size=18, padding=10))
        self.test_input = toga.TextInput(style=Pack(padding=10))
        self.test_feedback = toga.Label("", style=Pack(padding=10))
        btn_submit = toga.Button("Submit Answer", on_press=self.submit_test_answer, style=Pack(padding=10))
        btn_back = toga.Button("Back to Abacus Learning Menu", on_press=self.show_abacus_learning, style=Pack(padding=10))

        self.test_box.add(self.test_question_label)
        self.test_box.add(self.test_input)
        self.test_box.add(btn_submit)
        self.test_box.add(self.test_feedback)
        self.test_box.add(btn_back)

        self._switch_view(self.test_box)

        self.test_score = 0
        self.test_current = 0
        self.test_total = 5

        def time_up():
            self.test_input.enabled = False
            btn_submit.enabled = False
            self.test_feedback.text = f"Time's up! Final Score: {self.test_score}/{self.test_total}"

        threading.Timer(self.test_time_limit, time_up).start()
        self.generate_test_question()

    def generate_test_question(self):
        expr, self.test_answer = self.generate_expression(self.test_digits)
        self.test_question_label.text = f"Q{self.test_current + 1}: {expr}?"
        self.test_input.value = ""
        self.test_feedback.text = ""

    def submit_test_answer(self, widget):
        try:
            user_input = float(self.test_input.value.strip())
        except ValueError:
            self.test_feedback.text = "Invalid input."
            return

        if abs(user_input - self.test_answer) < 0.01:
            self.test_score += 1

        self.test_current += 1
        if self.test_current >= self.test_total:
            self.test_feedback.text = f"Test Complete! Score: {self.test_score}/{self.test_total}"
            self.test_input.enabled = False
            widget.enabled = False
        else:
            self.generate_test_question()

    def generate_expression(self, num_digits, num_operands=4):
        ops = ["+", "-", "*", "/"]
        expression = ""
        for i in range(num_operands):
            num = random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)
            expression += str(num)
            if i < num_operands - 1:
                expression += f" {random.choice(ops)} "
        try:
            result = round(eval(expression), 2)
        except ZeroDivisionError:
            return self.generate_expression(num_digits, num_operands)
        return expression, result

    def create_cube(self):
        self.cube_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1,background_color="#5CFD84"))
        label = toga.Label("Cube Calculator", style=Pack(font_size=20, font_family="Segoe Print", padding=10))
        self.cube_box.add(label)

        self.cube_input = toga.TextInput(placeholder="Enter number", style=Pack(padding=5))
        self.cube_box.add(self.cube_input)

        calc_btn = toga.Button("Calculate Cube", on_press=self.calculate_cube, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.cube_box.add(calc_btn)

        self.cube_result = toga.Label("", style=Pack(padding=10, font_size=16, color="blue"))
        self.cube_box.add(self.cube_result)

        back_btn = toga.Button("Back", on_press=self.show_menu, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.cube_box.add(back_btn)

    
    def calculate_cube(self, widget):
        try:
            num = float(self.cube_input.value)
            result = num ** 3
            msg = f"Cube of {num} = {result}"
        except Exception:
            msg = "Invalid input. Please enter a valid number."
        self.show_result_slide(msg, self.show_cube)
    def create_cube_practice(self):
        self.cube_prac_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1))
        label = toga.Label("Cube Practice", style=Pack(font_size=20, font_family="Segoe Print", padding=10))
        self.cube_prac_box.add(label)

        self.cube_prac_num_questions = toga.NumberInput(style=Pack(padding=5))
        self.cube_prac_num_digits = toga.NumberInput(style=Pack(padding=5))

        self.cube_prac_box.add(toga.Label("Number of Questions:", style=Pack(padding=(10, 5, 0, 5))))
        self.cube_prac_box.add(self.cube_prac_num_questions)
        self.cube_prac_box.add(toga.Label("Digits of number:", style=Pack(padding=(10, 5, 0, 5))))
        self.cube_prac_box.add(self.cube_prac_num_digits)

        start_btn = toga.Button("Start Practice", on_press=self.start_cube_practice, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.cube_prac_box.add(start_btn)

        self.cube_prac_question = toga.Label("", style=Pack(padding=10, font_size=18))
        self.cube_prac_box.add(self.cube_prac_question)

        self.cube_prac_answer_input = toga.TextInput(placeholder="Enter your answer", style=Pack(padding=5))
        self.cube_prac_box.add(self.cube_prac_answer_input)

        submit_btn = toga.Button("Submit Answer", on_press=self.check_cube_answer, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.cube_prac_box.add(submit_btn)

        self.cube_prac_feedback = toga.Label("", style=Pack(padding=10, font_size=16))
        self.cube_prac_box.add(self.cube_prac_feedback)

        self.cube_prac_score = toga.Label("", style=Pack(padding=10, font_size=16))
        self.cube_prac_box.add(self.cube_prac_score)

        back_btn = toga.Button("Back", on_press=self.show_menu, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.cube_prac_box.add(back_btn)

        self.cube_prac_current = 0
        self.cube_prac_correct = 0
        self.cube_prac_wrong = 0
        self.cube_prac_questions = []

    def start_cube_practice(self, widget):
        try:
            num_questions = int(self.cube_prac_num_questions.value)
            digits = int(self.cube_prac_num_digits.value)
            if num_questions <= 0 or digits <= 0:
                self.cube_prac_feedback.text = "Enter positive integers."
                return
        except Exception:
            self.cube_prac_feedback.text = "Please enter valid integers."
            return

        self.cube_prac_questions = []
        lower = 10 ** (digits - 1)
        upper = 10 ** digits - 1

        for _ in range(num_questions):
            number = random.randint(lower, upper)
            self.cube_prac_questions.append(number)

        self.cube_prac_current = 0
        self.cube_prac_correct = 0
        self.cube_prac_wrong = 0
        self.cube_prac_feedback.text = ""
        self.cube_prac_score.text = f"Correct: 0 | Wrong: 0"

        self.show_cube_prac_question()

    def show_cube_prac_question(self):
        if self.cube_prac_current < len(self.cube_prac_questions):
            question = self.cube_prac_questions[self.cube_prac_current]
            self.cube_prac_question.text = f"What is the cube of {question}?"
            self.cube_prac_answer_input.value = ""
            self.cube_prac_feedback.text = ""
        else:
            self.cube_prac_question.text = "Practice complete!"
            self.cube_prac_answer_input.value = ""
            self.cube_prac_feedback.text = f"Final Score - Correct: {self.cube_prac_correct} | Wrong: {self.cube_prac_wrong}"

    def check_cube_answer(self, widget):
        if self.cube_prac_current >= len(self.cube_prac_questions):
            return

        try:
            user_answer = int(self.cube_prac_answer_input.value)
        except Exception:
            self.cube_prac_feedback.text = "Please enter a valid integer."
            return

        number = self.cube_prac_questions[self.cube_prac_current]
        correct_answer = number ** 3

        if user_answer == correct_answer:
            self.cube_prac_feedback.text = "Correct!"
            self.cube_prac_correct += 1
        else:
            self.cube_prac_feedback.text = f"Wrong! Correct answer is {correct_answer}."
            self.cube_prac_wrong += 1

        self.cube_prac_current += 1
        self.cube_prac_score.text = f"Correct: {self.cube_prac_correct} | Wrong: {self.cube_prac_wrong}"
        self.show_cube_prac_question()

    def create_cube_root(self):
        self.cube_root_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#5CFD84"))
        label = toga.Label("Cube Root Calculator", style=Pack(font_size=20, font_family="Segoe Print", padding=10))
        self.cube_root_box.add(label)

        self.cube_root_input = toga.TextInput(placeholder="Enter number", style=Pack(padding=5))
        self.cube_root_box.add(self.cube_root_input)

        calc_btn = toga.Button("Calculate Cube Root", on_press=self.calculate_cube_root, style=Pack(padding=10, background_color="MediumSeaGreen"))
        back_btn = toga.Button("Back", on_press=self.show_menu, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.cube_root_box.add(calc_btn)
        self.cube_root_box.add(back_btn)

        self.cube_root_result = toga.Label("", style=Pack(padding=10, font_size=16, color="blue"))
        self.cube_root_box.add(self.cube_root_result)

    
    def calculate_cube_root(self, widget):
        try:
            num = float(self.cube_root_input.value)
            result = round(num ** (1 / 3), 6)
            msg = f"Cube root of {num} = {result}"
        except Exception:
            msg = "Invalid input. Please enter a valid number."
        self.show_result_slide(msg, self.show_cube_root)
    def create_cube_root_practice(self):
        self.cube_root_prac_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#5CFD84"))
        label = toga.Label("Cube Root Practice", style=Pack(font_size=20, font_family="Segoe Print", padding=10))
        self.cube_root_prac_box.add(label)

        self.cube_root_prac_num_questions = toga.NumberInput(style=Pack(padding=5))
        self.cube_root_prac_num_digits = toga.NumberInput(style=Pack(padding=5))

        self.cube_root_prac_box.add(toga.Label("Number of Questions:", style=Pack(padding=(10, 5, 0, 5))))
        self.cube_root_prac_box.add(self.cube_root_prac_num_questions)
        self.cube_root_prac_box.add(toga.Label("Digits of cube roots:", style=Pack(padding=(10, 5, 0, 5))))
        self.cube_root_prac_box.add(self.cube_root_prac_num_digits)

        start_btn = toga.Button("Start Practice", on_press=self.start_cube_root_practice, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.cube_root_prac_box.add(start_btn)

        self.cube_root_question = toga.Label("", style=Pack(padding=10, font_size=18))
        self.cube_root_prac_box.add(self.cube_root_question)

        self.cube_root_answer_input = toga.TextInput(placeholder="Enter your answer", style=Pack(padding=5))
        self.cube_root_prac_box.add(self.cube_root_answer_input)

        submit_btn = toga.Button("Submit Answer", on_press=self.check_cube_root_answer, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.cube_root_prac_box.add(submit_btn)

        self.cube_root_feedback = toga.Label("", style=Pack(padding=10, font_size=16))
        self.cube_root_prac_box.add(self.cube_root_feedback)

        self.cube_root_score = toga.Label("", style=Pack(padding=10, font_size=16))
        self.cube_root_prac_box.add(self.cube_root_score)

        back_btn = toga.Button("Back", on_press=self.show_menu, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.cube_root_prac_box.add(back_btn)

        self.cube_root_current = 0
        self.cube_root_correct = 0
        self.cube_root_wrong = 0
        self.cube_root_questions = []

    def start_cube_root_practice(self, widget):
        try:
            num_q = int(self.cube_root_prac_num_questions.value)
            digits = int(self.cube_root_prac_num_digits.value)
            if num_q <= 0 or digits <= 0:
                self.cube_root_feedback.text = "Enter valid positive numbers."
                return
        except Exception:
            self.cube_root_feedback.text = "Invalid input."
            return

        self.cube_root_questions = []

        # Generate all cube roots whose cubes have the desired number of digits
        roots = []
        n = 1
        while True:
            cube = n ** 3
            length = len(str(cube))
            if length < digits:
                n += 1
                continue
            elif length == digits:
                roots.append((cube, n))
            else:
                break
            n += 1

        if len(roots) < num_q:
            self.cube_root_feedback.text = f"Only {len(roots)} perfect cubes found with {digits} digits."
            return

        self.cube_root_questions = random.sample(roots, num_q)

        self.cube_root_current = 0
        self.cube_root_correct = 0
        self.cube_root_wrong = 0
        self.cube_root_score.text = "Correct: 0 | Wrong: 0"
        self.show_cube_root_question()

    def show_cube_root_question(self):
        if self.cube_root_current < len(self.cube_root_questions):
            cube, _ = self.cube_root_questions[self.cube_root_current]
            self.cube_root_question.text = f"What is the cube root of {cube}?"
            self.cube_root_answer_input.value = ""
            self.cube_root_feedback.text = ""
        else:
            self.cube_root_question.text = "Practice complete!"
            self.cube_root_answer_input.value = ""
            self.cube_root_feedback.text = f"Final Score - Correct: {self.cube_root_correct} | Wrong: {self.cube_root_wrong}"

    def check_cube_root_answer(self, widget):
        if self.cube_root_current >= len(self.cube_root_questions):
            return

        try:
            user_answer = int(self.cube_root_answer_input.value)
        except Exception:
            self.cube_root_feedback.text = "Please enter a valid integer."
            return

        cube, correct_root = self.cube_root_questions[self.cube_root_current]
        if user_answer == correct_root:
            self.cube_root_feedback.text = "Correct!"
            self.cube_root_correct += 1
        else:
            self.cube_root_feedback.text = f"Wrong! Correct answer is {correct_root}."
            self.cube_root_wrong += 1

        self.cube_root_current += 1
        self.cube_root_score.text = f"Correct: {self.cube_root_correct} | Wrong: {self.cube_root_wrong}"
        self.show_cube_root_question()

    def create_decimal_study(self):
        self.decimal_study_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#5CFD84"))
        label = toga.Label("Decimal Study Setup", style=Pack(font_size=20, font_family="Segoe Print", padding=10))
        self.decimal_study_box.add(label)

        self.decimal_op_select = toga.Selection(items=["Addition", "Subtraction", "Multiplication", "Division"], style=Pack(padding=5))
        self.decimal_study_box.add(toga.Label("Select Operation:", style=Pack(padding=(10, 5, 0, 5))))
        self.decimal_study_box.add(self.decimal_op_select)

        self.decimal_digits_input = toga.TextInput(placeholder="Enter number of digits", style=Pack(padding=5))
        self.decimal_study_box.add(toga.Label("Number of Digits:", style=Pack(padding=(10, 5, 0, 5))))
        self.decimal_study_box.add(self.decimal_digits_input)

        self.decimal_rows_input = toga.TextInput(placeholder="Enter number of rows", style=Pack(padding=5))
        self.decimal_study_box.add(toga.Label("Number of Rows:", style=Pack(padding=(10, 5, 0, 5))))
        self.decimal_study_box.add(self.decimal_rows_input)

        self.decimal_time_input = toga.TextInput(placeholder="Enter time limit in seconds", style=Pack(padding=5))
        self.decimal_study_box.add(toga.Label("Time Limit (seconds):", style=Pack(padding=(10, 5, 0, 5))))
        self.decimal_study_box.add(self.decimal_time_input)

        start_btn = toga.Button("Start Decimal Study", on_press=self.start_decimal_study, style=Pack(padding=10, background_color="MediumSeaGreen"))
        back_btn = toga.Button("Back", on_press=self.show_menu, style=Pack(padding=10, background_color="MediumSeaGreen"))
        self.decimal_study_box.add(start_btn)
        self.decimal_study_box.add(back_btn)

        self.decimal_study_result = toga.Label("", style=Pack(padding=10))
        self.decimal_study_box.add(self.decimal_study_result)

    def start_decimal_study(self, widget):
        op = self.decimal_op_select.value
        digits = self.decimal_digits_input.value
        rows = self.decimal_rows_input.value
        time_limit = self.decimal_time_input.value

        try:
            digits = int(digits)
            rows = int(rows)
            time_limit = int(time_limit)
            if digits <= 0 or rows <= 0 or time_limit <= 0:
                raise ValueError
        except Exception:
            self.decimal_study_result.text = "Please enter valid positive integers."
            return

        ops = {
            "Addition": ('+', lambda a, b: a + b),
            "Subtraction": ('-', lambda a, b: a - b if a >= b else b - a),
            "Multiplication": ('*', lambda a, b: a * b),
            "Division": ('/', lambda a, b: round(a / b, 4) if b != 0 else 0),
        }

        symbol, func = ops[op]
        problems = []
        answers = []

        for _ in range(rows):
            a = round(random.uniform(10 ** (digits - 1), 10 ** digits - 1), 2)
            b = round(random.uniform(1, 10 ** digits - 1), 2)  # avoid zero division
            if symbol == '-':
                a, b = max(a, b), min(a, b)
            result = func(a, b)
            problems.append(f"{a} {symbol} {b}")
            answers.append(result)

        result_text = f"{op} Results:\n"
        for a in answers:
            result_text += f"{a}\n"
        self.show_result_slide(result_text.strip(), self.show_decimal_study)


def main():
    return CalculatorApp("MYMATHSHELPER", "org.example.calculator")


if __name__ == "__main__":
    app = main()
    app.main_loop()
