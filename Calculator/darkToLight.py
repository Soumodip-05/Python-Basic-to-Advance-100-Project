class ThemeManager:
    def toggle_theme(self):
        # DARK → LIGHT
        if self.dark_mode:
            self.bg_color = "#f5f5f5"
            self.button_color = "#c2c1c1"
            self.dif_button_color = "#a8a8a8"
            self.operator_color = "#9499a3"
            self.equal_color = "#008e06"
            self.sec_text_color = "#ffffff"
            self.pre_text_color = "#000000"

            self.dark_mode = False
            self.theme_button.config(text="🌙")

        # LIGHT → DARK
        else:

            self.bg_color = "#000000"
            self.button_color = "#1e1e1e"
            self.dif_button_color = "#2e2d2d"
            self.operator_color = "#9499a3"
            self.equal_color = "#008e06"

            self.pre_text_color = "#ffffff"
            self.sec_text_color = "#000000"

            self.dark_mode = True
            self.theme_button.config(text="☀")

        # MAIN WINDOW
        self.configure(bg=self.bg_color)

        # DISPLAY
        self.display_frame.config(bg=self.bg_color)

        self.display_label.config(
            bg=self.bg_color,
            fg=self.pre_text_color
        )

        # TOP BAR
        self.top_frame.config(bg=self.bg_color)

        self.history_btn.config(
            bg=self.bg_color,
            activebackground=self.bg_color,
            fg=self.pre_text_color
        )

        self.theme_button.config(
            bg=self.bg_color,
            activebackground=self.bg_color,
            fg=self.pre_text_color
        )

        self.escape_btn.config(
            bg=self.bg_color,
            activebackground=self.bg_color
        )

        # SEPARATOR
        self.separator.config(
            bg="#aaaaaa" if not self.dark_mode else "#2a2a2a"
        )

        # BUTTON FRAME
        self.button_frame.config(bg=self.bg_color)

        # UPDATE ALL CANVAS BUTTONS
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

        for i, canvas in enumerate(self.all_buttons):

            button = buttons[i]

            # OPERATOR BUTTONS
            if button in ['÷', 'x', '-', '+']:
                bg_color = self.operator_color
                text_color = self.pre_text_color

            # TOP BUTTONS
            elif button in ['⇆', 'Rad', '√', '|x|', 'sin', 'cos', 'tan', 'π', 'ln', 'log', '1/x', 'e', 'eˣ', 'x²', 'xʸ','C', '()', '%']:
                bg_color = self.dif_button_color
                text_color = self.pre_text_color

            # EQUAL BUTTON
            elif button == "=":
                bg_color = self.equal_color
                text_color = "#ffffff"

            elif button == '  ':
                bg_color = self.bg_color

            # NORMAL BUTTONS
            else:
                bg_color = self.button_color
                text_color = self.pre_text_color

            # UPDATE CANVAS BG
            canvas.config(bg=self.bg_color)

            # UPDATE CIRCLE
            canvas.itemconfig(canvas.circle, fill=bg_color)

            # UPDATE TEXT
            canvas.itemconfig(canvas.text_item, fill=text_color)

            # ACTIVE PRESS COLORS
            if self.dark_mode:
                active_bg = "#5b5a5a"
                active_fg = "#ffffff"
            else:
                active_bg = "#eeeeee"
                active_fg = "#000000"

            # SAVE COLORS
            canvas.bg_color = bg_color
            canvas.text_color = text_color

            canvas.active_bg = active_bg
            canvas.active_fg = active_fg
            
    def __init__(self, app):
        self.app = app
