import tkinter as tk

class HistoryPanel:
    # SHOW HISTORY
    def show_history(self):
        if self.history_visible:

            self.history_frame.destroy()

            self.history_visible = False

            return

        self.history_frame = tk.Frame(
            self,
            bg=self.bg_color
        )

        self.history_frame.place(
            relx=0.02,
            rely=0.30,
            relwidth=0.72,
            relheight=0.60
        )

        # History entries
        history_text = tk.Text(
            self.history_frame,
            bg=self.bg_color,
            fg="white",
            bd=0,
            font=("Arial",12)
        )

        history_text.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(10,60)   # leave space for button
        )

        for item in reversed(self.history):
            history_text.insert("end", item + "\n\n")

        history_text.config(state="disabled")

        # Clear button
        clear_btn = tk.Button(
            self.history_frame,
            text="Clear History",
            bg="#090909",
            fg="white",
            bd=0,
            font=("Arial",12),
            command=self.clear_history
        )

        clear_btn.place(
            relx=0.5,
            rely=0.95,
            anchor="s",
            width=180,
            height=45
        )

        self.history_visible = True
    
    def clear_history(self):
        self.history.clear()
        if self.history_visible:
            self.history_frame.destroy()
            self.history_visible = False
            self.show_history()
            
    def __init__(self, app):
        self.app = app
