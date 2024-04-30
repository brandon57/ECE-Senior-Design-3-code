import customtkinter as ctk

class NumericEntry(ctk.CTkFrame):
    def __init__(self, parent, controller, input_type, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        self.input_type = input_type
        self.parent = parent

        self.grid_columnconfigure((0, 7), weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure((4, 5, 6), weight=2)
        self.grid_rowconfigure(0, weight=1)
        for i in range(1, 6):
            self.grid_rowconfigure(i, weight=1, uniform='row')
        self.grid_rowconfigure(6, weight=1)

        self.top_spacer = ctk.CTkFrame(self, height=20, width=60)
        self.top_spacer.grid(row=0, column=0) 
        self.top_spacer.lower()

        self.display_label = ctk.CTkLabel(self, text="Set fixed " + input_type, font=("default_font", 24))
        self.display_label.grid(row=1, column=1, sticky="ews", padx=10, pady=10)

        self.text_box = ctk.CTkEntry(self, font=("default_font", 28), width=300)
        self.text_box.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

        self.save_button = ctk.CTkButton(self, text="Save", font=("default_font", 20), fg_color="green", hover=False)
        self.save_button.grid(row=4, column=1, sticky="nsew", padx=10, pady=5)
        
        self.discard_button = ctk.CTkButton(self, text="Discard", font=("default_font", 20), fg_color="darkred", hover=False)
        self.discard_button.grid(row=5, column=1, sticky="nsew", padx=10, pady=5)

        self.middle_spacer = ctk.CTkFrame(self, height=20, width=60)
        self.middle_spacer.grid(row=0, column=2)
        self.middle_spacer.lower()

        keypad_buttons = [
            ('Clear', 1, 4), ('Backspace', 1, 5, 2), 
            ('7', 2, 4), ('8', 2, 5), ('9', 2, 6),
            ('4', 3, 4), ('5', 3, 5), ('6', 3, 6),
            ('1', 4, 4), ('2', 4, 5), ('3', 4, 6),
            ('0', 5, 5), ('.', 5, 4), ('-', 5, 6),
        ]

        for button_details in keypad_buttons:
            text = button_details[0]
            row = button_details[1]
            col = button_details[2]
            colspan = button_details[3] if len(button_details) > 3 else 1
            rowspan = button_details[4] if len(button_details) > 4 else 1

            button = ctk.CTkButton(self, text=text, font=("default_font", 24), hover=False, command=lambda b=text: self.controller.on_button_press(b))
            button.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan, sticky="nsew", padx=5, pady=5)

        self.bottom_spacer = ctk.CTkFrame(self, height=20, width=60)
        self.bottom_spacer.grid(row=6, column=7)
        self.bottom_spacer.lower()
