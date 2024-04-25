from Views.numericentry import NumericEntry

class NumericEntryController:
    def __init__(self, parent, model, input_type, settings):
        self.model = model
        self.input_type = input_type
        self.view = NumericEntry(parent, self, input_type)
        self.settings = settings

        self.view.save_button.configure(command=self.save_input)
        self.view.discard_button.configure(command=self.discard_input)

        if self.input_type == 'latitude':
            current_text = self.settings.frame.base_latitude_button.cget('text')
            self.view.text_box.delete(0, 'end')
            self.view.text_box.insert(0, current_text)
        elif self.input_type == 'longitude':
            current_text = self.settings.frame.base_longitude_button.cget('text')
            self.view.text_box.delete(0, 'end')
            self.view.text_box.insert(0, current_text)

    def save_input(self):
        raw_value = self.view.text_box.get()
        try:
            value = float(raw_value)
        except ValueError:
            value = 0

        formatted_value = f"{value:.8f}"

        if self.input_type == 'latitude':
            self.settings.frame.base_latitude_button.configure(text=formatted_value)
        elif self.input_type == 'longitude':
            self.settings.frame.base_longitude_button.configure(text=formatted_value)
        
        self.view.destroy()

    def discard_input(self):
        self.view.destroy()

    def on_button_press(self, b):
        current = self.view.text_box.get()
        new_text = current 

        if b == "Clear":
            new_text = ""
        elif b == "Backspace":
            new_text = current[:-1] 
        elif b == "-":
            if current.startswith('-'):
                new_text = current[1:]
            else:
                new_text = '-' + current
        elif b == ".":
            if "." not in current:
                if current == "" or current == "-": 
                    new_text = current + "0."
                else:
                    new_text = current + "."
        elif b.isdigit() or b == ".":
            if current == "0" or current == "-0":
                if b == "0":
                    return
                else:
                    new_text = current[:-1] + b 
            else:
                new_text = current + b

        if self.is_valid_input(new_text):
            self.view.text_box.delete(0, 'end')
            self.view.text_box.insert(0, new_text)
        else:
            pass

    def is_valid_input(self, text):
        if text in ["", "-"]:
            return True
        try:
            value = float(text)
            if self.input_type == 'latitude' and not (-90 <= value <= 90):
                return False
            elif self.input_type == 'longitude' and not (-180 <= value <= 180):
                return False
            if '.' in text:
                parts = text.split('.')
                if len(parts) > 1 and len(parts[1]) > 8:
                    return False
        except ValueError:
            return False
        return True
