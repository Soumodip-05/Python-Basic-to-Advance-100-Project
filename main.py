import tkinter as tk
import os
from button_operation import ButtonOperations
from history_panel import HistoryPanel
from darkToLight import ThemeManager

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # ICON
        try:
            if os.path.exists("calculator.ico"):
                self.iconbitmap("calculator.ico")
            elif os.path.exists("Calculator/calculator.ico"):
                self.iconbitmap("Calculator/calculator.ico")
        except:
            pass

        # COLORS
        self.bg_color = "#000000"
        self.button_color = "#1e1e1e"
        self.dif_button_color = "#2e2d2d"
        self.operator_color = "#9499a3"
        self.equal_color = "#008e06"

        self.pre_text_color = "#ffffff"
        self.sec_text_color = "#000000"

        # WINDOW SETTINGS
        self.geometry("430x750")
        self.title("Scientific Calculator")
        self.configure(bg=self.bg_color)
        self.resizable(False, False)

        # VARIABLES
        self.current_expression = ""
        self.font_size = 40
        self.dark_mode = True

        self.second_function = False

        # CREATE UI
        self.create_widgets()

        # History
        self.history = []
        self.history_visible = False

        # KEYBOARD SUPPORT
        self.bind("<Key>", lambda event: ButtonOperations.key_press(self, event))

        self.is_radian = True

        # INITIAL DISPLAY
        ButtonOperations.update_display(self)

    # ==================
    # CREATE WIDGETS
    # ==================
    def create_widgets(self):
        # DISPLAY FRAME
        self.display_frame = tk.Frame(self, bg=self.bg_color)
        self.display_frame.pack(fill="x", padx=20, pady=(40, 10))

        # DISPLAY LABEL
        self.display_label = tk.Label(
            self.display_frame, 
            text="0", 
            bg=self.bg_color, 
            fg=self.pre_text_color, 
            font=("Arial", self.font_size),
            anchor="e", 
            justify="right", 
            padx=20)
        
        self.display_label.pack(fill="both", expand=True, pady=20)


        # =========================
        # TOP ICON BAR
        # =========================
        self.top_frame = tk.Frame(self,bg=self.bg_color)
        self.top_frame.pack(fill="x",padx=25,pady=(15, 5))


        # HISTORY BUTTON
        self.history_btn = tk.Button(
            self.top_frame,
            text="🕘",
            font=("Arial", 18),
            bg=self.bg_color,
            fg=self.pre_text_color,
            bd=0, 
            activebackground=self.bg_color, 
            command=lambda: HistoryPanel.show_history(self)
        )

        self.history_btn.pack(side="left", padx=(0, 10))


        # Theme Change Button
        self.theme_button = tk.Button(
            self.top_frame,
            text="☀",
            font=("Arial", 16),
            bg=self.bg_color,
            fg=self.pre_text_color,
            bd=0,
            activebackground=self.bg_color,
            command=lambda: ThemeManager.toggle_theme(self)
        )

        self.theme_button.pack(side="left")


        # BACKSPACE BUTTON
        self.escape_btn = tk.Button(
            self.top_frame,
            text="⌫",
            font=("Arial", 16),
            bg=self.bg_color,
            fg="#02bd0b",
            bd=0,
            activebackground=self.bg_color,
            command=lambda: ButtonOperations.button_click(self, "⌫")
        )

        self.escape_btn.pack(side="right")


        # HORIZONTAL SEPARATOR LINE
        self.separator = tk.Frame(self, bg="#2a2a2a", height=1)
        self.separator.pack(fill="x", padx=20, pady=(5, 10))


        # ==================
        # BUTTON FRAME
        # ==================
        self.button_frame = tk.Frame(self, bg=self.bg_color)
        self.button_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # BUTTONS
        self.primary_buttons = [
            '⇆', 'Rad', '√', '|x|', 
            'sin', 'cos', 'tan', 'π',
            'ln', 'log', '1/x', 'e',
            'eˣ', 'x²', 'xʸ', '  '
        ]

        self.secondary_buttons = [
            '⇆', 'Rad', '∛', '2ˣ', 
            'sin⁻¹', 'cos⁻¹', 'tan⁻¹', 'x³',
            'sinh', 'cosh', 'tanh', 'x!',
            'sinh⁻¹', 'cosh⁻¹', 'tanh⁻¹', '  '
        ]

        buttons = [
            '⇆', 'Rad', '√', '|x|',
            'sin', 'cos', 'tan', 'π',
            'ln', 'log', '1/x', 'e',
            'eˣ', 'x²', 'xʸ', '  ',
            'C', '()', '%', '÷',
            '7', '8', '9', 'x',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '+/-', '0', '.', '='
        ]

        self.scientific_canvases = []
        row = 0
        col = 0
        self.all_buttons = []

        # CREATE BUTTONS
        for button in buttons:
            # OPERATOR BUTTONS
            if button in ['÷', 'x', '-', '+']:
                btn_bg_color = self.operator_color
                text_color = self.sec_text_color
                active_bg = "#bdbfc3"
                active_fg = self.sec_text_color

            # TOP BUTTONS
            elif button in ['⇆', 'Rad', '√', '|x|', 'sin', 'cos', 'tan', 'π', 'ln', 'log', '1/x', 'e', 'eˣ', 'x²', 'xʸ','C', '()', '%']:
                btn_bg_color = self.dif_button_color
                text_color = self.pre_text_color
                active_bg = "#5b5a5a"
                active_fg = self.pre_text_color

            # EQUAL BUTTON
            elif button == "=":
                btn_bg_color = self.equal_color
                text_color = self.pre_text_color
                active_bg = "#00b50a"
                active_fg = self.pre_text_color

            elif button == '  ':
                btn_bg_color = self.bg_color

            # NORMAL BUTTONS
            else:
                btn_bg_color = self.button_color
                text_color = self.pre_text_color
                active_bg = self.dif_button_color
                active_fg = self.pre_text_color

            canvas = tk.Canvas(
                self.button_frame,
                width=95,
                height=62,
                bg=self.bg_color,
                highlightthickness=0,
                bd=0
            )

            canvas.grid(
                row=row,
                column=col,
                padx=6,
                pady=6
            )

            rect = self.create_rounded_rect(
                canvas,
                2, 2,
                80, 40,
                radius=20,
                fill=btn_bg_color,
                outline=""
            )

            text = canvas.create_text(
                40,
                20,
                text=button,
                fill=text_color,
                font=("Segoe UI", 16)
            )


            # STORE VALUES
            canvas.circle = rect
            canvas.text_item = text

            button_text = canvas.itemcget(
                canvas.text_item,
                "text"
            )

            if button_text in self.primary_buttons:
                self.scientific_canvases.append(canvas)

            canvas.bg_color = btn_bg_color
            canvas.text_color = text_color

            canvas.active_bg = active_bg
            canvas.active_fg = active_fg

            # PRESS EFFECT
            canvas.bind("<ButtonPress-1>", ButtonOperations.on_press)

            def release(event):
                ButtonOperations.on_release(self, event)

                current_text = event.widget.itemcget(
                    event.widget.text_item,
                    "text"
                )

                ButtonOperations.button_click(self, current_text)

            # RELEASE EFFECT + BUTTON CLICK
            canvas.bind("<ButtonRelease-1>", release)


            self.all_buttons.append(canvas)

            col += 1

            # NEXT ROW
            if col > 3:
                col = 0
                row += 1

        # GRID EXPANSION
        for i in range(9):
            self.button_frame.grid_rowconfigure(i, weight=1)

        for i in range(4):
            self.button_frame.grid_columnconfigure(i, weight=1)

    def create_rounded_rect(self, canvas, x1, y1, x2, y2, radius=20, **kwargs):
        points = [
            x1 + radius, y1,
            x2 - radius, y1,

            x2, y1,
            x2, y1 + radius,

            x2, y2 - radius,
            x2, y2,

            x2 - radius, y2,

            x1 + radius, y2,

            x1, y2,
            x1, y2 - radius,

            x1, y1 + radius,
            x1, y1
        ]

        return canvas.create_polygon(
            points,
            smooth=True,
            **kwargs
        )

    def toggle_second_function(self):
        self.second_function = not self.second_function

        for i, canvas in enumerate(self.scientific_canvases):

            if self.second_function:

                canvas.itemconfig(
                    canvas.text_item,
                    text=self.secondary_buttons[i]
                )

            else:

                canvas.itemconfig(
                    canvas.text_item,
                    text=self.primary_buttons[i]
                )

    def button_click(self, value):
        ButtonOperations.button_click(self, value)

    def update_display(self):
        ButtonOperations.update_display(self)

    def key_press(self, event):
        ButtonOperations.key_press(self, event)

    def on_press(self, event):
        ButtonOperations.on_press(self, event)

    def on_release(self, event):
        ButtonOperations.on_release(self, event)

    def show_history(self):
        HistoryPanel.show_history(self)

    def clear_history(self):
        HistoryPanel.clear_history(self)

    def toggle_theme(self):
        ThemeManager.toggle_theme(self)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
