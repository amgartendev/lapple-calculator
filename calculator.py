import customtkinter as ctk


class Calculator(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.main_window()
        self.result_screen()
        self.buttons()
        self.__numbers_added = []

    def add_number_to_screen(self, number):
        self.decrease_font_size()

        self.__numbers_added.append(number)
        self.label_result.configure(text=''.join(self.__numbers_added))

    def all_clear_screen(self):
        self.__numbers_added = []
        self.label_result.configure(text='')

    def clear_screen(self):
        if len(self.__numbers_added) > 0:
            self.__numbers_added.pop()
            self.label_result.configure(text=''.join(self.__numbers_added))

    def decrease_font_size(self):
        if len(self.__numbers_added) >= 5:
            self.label_result.configure(font=('Century Gothic', 42))
            self.label_result.place(x=-10, y=10)

        if len(self.__numbers_added) >= 11:
            self.label_result.configure(font=('Century Gothic', 26))
            self.label_result.place(x=-10, y=20)

    def decrease_total_font_size(self, total):
        if len(str(total)) >= 5:
            self.label_result.configure(font=('Century Gothic', 42))
            self.label_result.place(x=-10, y=10)

        if len(str(total)) >= 11:
            self.label_result.configure(font=('Century Gothic', 26))
            self.label_result.place(x=-10, y=20)

    def sum(self):
        try:
            joined_numbers = ''.join(self.__numbers_added)
            eval_numbers = eval(joined_numbers)
            self.decrease_total_font_size(total=eval_numbers)
            self.label_result.configure(text=eval_numbers)
            self.__numbers_added = [str(eval_numbers)]
        except ZeroDivisionError:
            self.label_result.configure(text='Cannot Divide By Zero', font=('Century Gothic', 22))
            self.label_result.place(x=-10, y=20)
        except SyntaxError:
            self.label_result.configure(text='Leading Zeros in Decimal Integers Literals\n are not Permitted',
                                        font=('Century Gothic', 14))
            self.label_result.place(x=-10, y=20)

    def main_window(self):
        self.title('Lapple Calculator')
        self.geometry('300x380')
        self.resizable(height=False, width=False)

    def result_screen(self):
        # Result Screen
        self.frame_result = ctk.CTkFrame(master=self,
                                         height=75,
                                         width=300,
                                         fg_color='#2B2D2F')
        self.frame_result.place(x=0, y=0)

        self.label_result = ctk.CTkLabel(master=self.frame_result,
                                         width=300,
                                         anchor='e',
                                         text='0',
                                         font=('Century Gothic', 64))
        self.label_result.place(x=-10, y=-5)

    def buttons(self):
        # Buttons and Operations
        self.frame_buttons = ctk.CTkFrame(master=self, height=380, width=300)
        self.frame_buttons.grid(row=0, column=2, pady=75)

        # First Row
        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='AC',
                      font=('Century Gothic', 26),
                      fg_color='#3F4143',
                      hover_color='#797A7A',
                      command=self.all_clear_screen).grid(row=0, column=0)

        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='C',
                      font=('Century Gothic', 26),
                      fg_color='#3F4143',
                      hover_color='#797A7A',
                      command=self.clear_screen).grid(row=0, column=1, padx=1)

        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='%',
                      font=('Century Gothic', 26),
                      fg_color='#3F4143',
                      hover_color='#797A7A').grid(row=0, column=2)

        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='/',
                      font=('Century Gothic', 26),
                      fg_color='#FF9F0C',
                      hover_color='#B56D02',
                      command=lambda: self.add_number_to_screen('/')).grid(row=0, column=3, padx=1)

        # Second Row
        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='7',
                      font=('Century Gothic', 26),
                      fg_color='#3F4143',
                      hover_color='#797A7A',
                      command=lambda: self.add_number_to_screen('7')).grid(row=1, column=0, padx=1, pady=1)

        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='8',
                      font=('Century Gothic', 26),
                      fg_color='#3F4143',
                      hover_color='#797A7A',
                      command=lambda: self.add_number_to_screen('8')).grid(row=1, column=1, padx=1, pady=1)

        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='9',
                      font=('Century Gothic', 26),
                      fg_color='#3F4143',
                      hover_color='#797A7A',
                      command=lambda: self.add_number_to_screen('9')).grid(row=1, column=2, padx=1, pady=1)

        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='x',
                      font=('Century Gothic', 26),
                      fg_color='#FF9F0C',
                      hover_color='#B56D02',
                      command=lambda: self.add_number_to_screen('*')).grid(row=1, column=3, padx=1, pady=1)

        # Third Row
        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='4',
                      font=('Century Gothic', 26),
                      fg_color='#3F4143',
                      hover_color='#797A7A',
                      command=lambda: self.add_number_to_screen('4')).grid(row=2, column=0, padx=1, pady=1)

        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='5',
                      font=('Century Gothic', 26),
                      fg_color='#3F4143',
                      hover_color='#797A7A',
                      command=lambda: self.add_number_to_screen('5')).grid(row=2, column=1, padx=1, pady=1)

        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='6',
                      font=('Century Gothic', 26),
                      fg_color='#3F4143',
                      hover_color='#797A7A',
                      command=lambda: self.add_number_to_screen('6')).grid(row=2, column=2, padx=1, pady=1)

        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='-',
                      font=('Century Gothic', 26),
                      fg_color='#FF9F0C',
                      hover_color='#B56D02',
                      command=lambda: self.add_number_to_screen('-')).grid(row=2, column=3, padx=1, pady=1)

        # Fourth Row
        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='1',
                      font=('Century Gothic', 26),
                      fg_color='#3F4143',
                      hover_color='#797A7A',
                      command=lambda: self.add_number_to_screen('1')).grid(row=3, column=0, padx=1, pady=1)

        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='2',
                      font=('Century Gothic', 26),
                      fg_color='#3F4143',
                      hover_color='#797A7A',
                      command=lambda: self.add_number_to_screen('2')).grid(row=3, column=1, padx=1, pady=1)

        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='3',
                      font=('Century Gothic', 26),
                      fg_color='#3F4143',
                      hover_color='#797A7A',
                      command=lambda: self.add_number_to_screen('3')).grid(row=3, column=2, padx=1, pady=1)

        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='+',
                      font=('Century Gothic', 26),
                      fg_color='#FF9F0C',
                      hover_color='#B56D02',
                      command=lambda: self.add_number_to_screen('+')).grid(row=3, column=3, padx=1, pady=1)

        # Fifth Row
        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='',
                      fg_color='#3F4143',
                      hover_color='#797A7A').grid(row=4, column=0, padx=1, pady=1)

        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='0',
                      font=('Century Gothic', 26),
                      fg_color='#3F4143',
                      hover_color='#797A7A',
                      command=lambda: self.add_number_to_screen('0')).grid(row=4, column=1, padx=1, pady=1)

        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='.',
                      font=('Century Gothic', 26),
                      fg_color='#3F4143',
                      hover_color='#797A7A',
                      command=lambda: self.add_number_to_screen('.')).grid(row=4, column=2, padx=1, pady=1)

        ctk.CTkButton(master=self.frame_buttons,
                      height=60,
                      width=75,
                      corner_radius=0,
                      text='=',
                      font=('Century Gothic', 26),
                      fg_color='#FF9F0C',
                      hover_color='#B56D02',
                      command=self.sum).grid(row=4, column=3, padx=1, pady=1)


if __name__ == '__main__':
    calculator = Calculator()
    calculator.mainloop()
