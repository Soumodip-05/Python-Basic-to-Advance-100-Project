import math

class ButtonOperations:
    # BUTTON CLICK
    def button_click(self, value):
        operators = ['⇆', 'Rad', '√', '|x|', 'sin', 'cos', 'tan', 'π', 'ln', 'log', '1/x', 'e', 'eˣ', 'x²', 'xʸ', '+', '-', '*', '/', '%']

        # CLEAR
        if value == "C":
            self.current_expression = ""

        elif value == "⇆":
            self.toggle_second_function()
            return

        # Escape
        elif value == "⌫":
            self.current_expression = self.current_expression[:-1] if self.current_expression else ""

        # RAD / DEG TOGGLE
        elif value == "Rad":
            self.is_radian = not self.is_radian
            for canvas in self.all_buttons:
                txt = canvas.itemcget(canvas.text_item, "text")

                if txt in ["Rad", "Deg"]:
                    canvas.itemconfig(
                        canvas.text_item,
                        text="Rad" if self.is_radian else "Deg"
                    )
                    break

        # PI
        elif value == "π":
            self.current_expression += str(math.pi)

        # EULER NUMBER
        elif value == "e":
            self.current_expression += str(math.e)

        # SQUARE ROOT
        elif value == "√":
            try:
                num = float(self.current_expression)
                self.current_expression = str(math.sqrt(num))
            except:
                self.current_expression = "Error"

        # ABSOLUTE VALUE
        elif value == "|x|":
            try:
                num = float(self.current_expression)
                self.current_expression = str(abs(num))
            except:
                self.current_expression = "Error"

        # SIN
        elif value == "sin":
            try:
                num = float(self.current_expression)

                if not self.is_radian:
                    num = math.radians(num)

                self.current_expression = str(math.sin(num))
            except:
                self.current_expression = "Error"

        # COS
        elif value == "cos":
            try:
                num = float(self.current_expression)

                if not self.is_radian:
                    num = math.radians(num)

                self.current_expression = str(math.cos(num))
            except:
                self.current_expression = "Error"

        # TAN
        elif value == "tan":
            try:
                num = float(self.current_expression)

                if not self.is_radian:
                    num = math.radians(num)

                self.current_expression = str(math.tan(num))
            except:
                self.current_expression = "Error"

        # NATURAL LOG
        elif value == "ln":
            try:
                num = float(self.current_expression)
                self.current_expression = str(math.log(num))
            except:
                self.current_expression = "Error"

        # LOG BASE 10
        elif value == "log":
            try:
                num = float(self.current_expression)
                self.current_expression = str(math.log10(num))
            except:
                self.current_expression = "Error"

        # RECIPROCAL
        elif value == "1/x":
            try:
                num = float(self.current_expression)
                self.current_expression = str(1 / num)
            except:
                self.current_expression = "Error"

        # e^x
        elif value == "eˣ":
            try:
                num = float(self.current_expression)
                self.current_expression = str(math.exp(num))
            except:
                self.current_expression = "Error"

        # x²
        elif value == "x²":
            try:
                num = float(self.current_expression)
                self.current_expression = str(num ** 2)
            except:
                self.current_expression = "Error"

        # xʸ
        elif value == "xʸ":
            self.current_expression += "^"

        elif value == "∛":
            try:
                num = float(self.current_expression)
                self.current_expression = str(num ** (1/3))
            except:
                self.current_expression = "Error"

        elif value == "2ˣ":
            try:
                num = float(self.current_expression)
                self.current_expression = str(2 ** num)
            except:
                self.current_expression = "Error"    

        elif value == "sin⁻¹":
            try:
                num = float(self.current_expression)

                result = math.asin(num)

                if not self.is_radian:
                    result = math.degrees(result)

                self.current_expression = str(result)

            except:
                self.current_expression = "Error"    

        elif value == "cos⁻¹":
            try:
                num = float(self.current_expression)

                result = math.acos(num)

                if not self.is_radian:
                    result = math.degrees(result)

                self.current_expression = str(result)

            except:
                self.current_expression = "Error"

        elif value == "tan⁻¹":
            try:
                num = float(self.current_expression)

                result = math.atan(num)

                if not self.is_radian:
                    result = math.degrees(result)

                self.current_expression = str(result)

            except:
                self.current_expression = "Error"

        elif value == "x³":
            try:
                num = float(self.current_expression)
                self.current_expression = str(num ** 3)
            except:
                self.current_expression = "Error"

        elif value == "sinh":
            try:
                num = float(self.current_expression)
                self.current_expression = str(math.sinh(num))
            except:
                self.current_expression = "Error"

        elif value == "cosh":
            try:
                num = float(self.current_expression)
                self.current_expression = str(math.cosh(num))
            except:
                self.current_expression = "Error"

        elif value == "tanh":
            try:
                num = float(self.current_expression)
                self.current_expression = str(math.tanh(num))
            except:
                self.current_expression = "Error"

        elif value == "x!":
            try:
                num = int(float(self.current_expression))

                if num < 0:
                    raise ValueError

                self.current_expression = str(math.factorial(num))

            except:
                self.current_expression = "Error"

        elif value == "sinh⁻¹":
            try:
                num = float(self.current_expression)
                self.current_expression = str(math.asinh(num))
            except:
                self.current_expression = "Error"

        elif value == "cosh⁻¹":
            try:
                num = float(self.current_expression)
                self.current_expression = str(math.acosh(num))
            except:
                self.current_expression = "Error"

        elif value == "tanh⁻¹":
            try:
                num = float(self.current_expression)
                self.current_expression = str(math.atanh(num))
            except:
                self.current_expression = "Error"

        # EQUAL
        elif value == "=":
            try:
                expression = self.current_expression

                expression = expression.replace("÷", "/")
                expression = expression.replace("x", "*")
                expression = expression.replace("^", "**")

                result = eval(expression)

                # SAVE HISTORY
                history_item = f"{expression} = {result}"
                self.history.append(history_item)

                self.current_expression = str(result)

            except:
                self.current_expression = "Error"

        # BRACKET
        elif value == "()":
            open_count = self.current_expression.count("(")
            close_count = self.current_expression.count(")")

            if open_count == close_count:
                self.current_expression += "("
            else:
                self.current_expression += ")"

        # PLUS MINUS
        elif value == "+/-":
            if self.current_expression.startswith("-"):
                self.current_expression = self.current_expression[1:]
            else:
                self.current_expression = "-" + self.current_expression

        else:
            # SYMBOL CONVERSION
            if value == "x":
                value = "*"

            elif value == "÷":
                value = "/"

            elif value == "%":
                try:
                    expression = self.current_expression

                    operators_list = ['+', '-', '*', '/']

                    # FIND LAST OPERATOR
                    last_operator_index = -1
                    last_operator = ""

                    for i in range(len(expression) - 1, -1, -1):

                        if expression[i] in operators_list:
                            last_operator_index = i
                            last_operator = expression[i]
                            break

                    # NO OPERATOR
                    if last_operator_index == -1:

                        number = float(expression)

                        self.current_expression = str(
                            number / 100
                        )

                    else:

                        first_number = float(
                            expression[:last_operator_index]
                        )

                        second_number = float(
                            expression[last_operator_index + 1:]
                        )

                        # + and -
                        if last_operator in ['+', '-']:

                            percent_value = (
                                first_number * second_number / 100
                            )

                        # * and /
                        else:

                            percent_value = (
                                second_number / 100
                            )

                        new_expression = (
                            expression[:last_operator_index + 1]
                            + str(percent_value)
                        )

                        self.current_expression = new_expression
                except:
                    pass

                self.update_display()
                return

            # PREVENT DOUBLE OPERATORS
            if value in operators:
                if (self.current_expression != "" and self.current_expression[-1] in operators):
                    self.current_expression = (self.current_expression[:-1] + value)
                else:
                    self.current_expression += value
            else:
                self.current_expression += value

        # UPDATE DISPLAY
        self.update_display()


    # UPDATE DISPLAY
    def update_display(self):

        # DEFAULT DISPLAY
        if self.current_expression == "":
            display_text = "0"
        else:
            display_text = self.current_expression

        # REPLACE SYMBOLS FOR DISPLAY
        display_text = display_text.replace("*", "x")
        display_text = display_text.replace("/", "÷")
        display_text = display_text.replace("**", "^")

        # DYNAMIC FONT SIZE
        text_length = len(display_text)

        if text_length > 16:
            self.font_size = 18

        elif text_length > 12:
            self.font_size = 24

        elif text_length > 8:
            self.font_size = 32

        else:
            self.font_size = 40

        # UPDATE LABEL
        self.display_label.config(
            text=display_text,
            font=("Arial", self.font_size)
        )


    # KEYBOARD SUPPORT
    def key_press(self, event):
        key = event.char

        # NUMBERS & OPERATORS
        if key in "0123456789+-*/.%":
            self.button_click(key)

        # ENTER
        elif key == "\r":
            self.button_click("=")

        # BACKSPACE
        elif key == "\x08":
            self.current_expression = (
                self.current_expression[:-1]
            )
            self.update_display()


    # BUTTON PRESS EFFECT
    def on_press(self, event):
        canvas = event.widget
        canvas.itemconfig(canvas.circle, fill=canvas.active_bg)
        canvas.itemconfig(canvas.text_item, fill=canvas.active_fg)

    # BUTTON RELEASE EFFECT
    def on_release(self, event):
        canvas = event.widget
        canvas.itemconfig(canvas.circle, fill=canvas.bg_color)
        canvas.itemconfig(canvas.text_item, fill=canvas.text_color)
        
    def __init__(self, app):
        self.app = app
