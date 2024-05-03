import main

import customtkinter
import threading

ran = main.rand()


class ctk(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x1000")
        self.title("🎲random number🎲")
        self.config(bg='#222222')

        self.reading = False

        # button
        self.run_button = customtkinter.CTkButton(
            self, command=self.run_button_click, bg_color="#222222", text='RUN')
        self.run_button.place(relx=0.5, rely=0.35, anchor="center")

        self.clear_button = customtkinter.CTkButton(
            self, command=self.clear_button_click, bg_color='#222222', text='CLEAR')
        self.clear_button.place(relx=0.5, rely=0.4, anchor='center')

        self.voice_button = customtkinter.CTkButton(
            self, fg_color="#2E8B57", bg_color="#222222", command=self.voice_button_click, hover_color="#006400")
        self.voice_button.place(relx=0.5, rely=0.65, anchor="center")
        self.voice_button.configure(text="ON")

        # label
        self.print_number = customtkinter.CTkLabel(
            self, bg_color='#222222', text_color='#FFFFFF', text='result will print in here', font=('Arial', 75))
        self.print_number.place(relx=0.5, rely=0.25, anchor='center')

        self.title_text = customtkinter.CTkLabel(
            self, bg_color='#222222', text_color='#FFFFFF', text='🎲Random Number🎲', font=('Arial', 75))
        self.title_text.place(relx=0.5, rely=0.05, anchor='center')

        self.inform = customtkinter.CTkLabel(
            self, bg_color='#222222', text_color='#FFFFFF', text='Welcome', font=('Arial', 50))
        self.inform.place(relx=0.5, rely=0.15, anchor='center')

        self.w_s = customtkinter.CTkLabel(
            self, bg_color='#222222', text_color='#FFFFFF', text='|\nset the word size')
        self.w_s.place(relx=0.5, rely=0.52, anchor='center')

        self.from_ = customtkinter.CTkLabel(
            self, bg_color='#222222', text_color='#FFFFFF', text='from:', font=('Arial', 25))
        self.from_.place(relx=0.3, rely=0.6, anchor='center')
        self.to_ = customtkinter.CTkLabel(
            self, bg_color='#222222', text_color='#FFFFFF', text='to:', font=('Arial', 25))
        self.to_.place(relx=0.51, rely=0.6, anchor='center')

        # combocox
        self.count_choose = customtkinter.CTkComboBox(self, bg_color='#222222', values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                                                      command=ran.count_change, fg_color="#4A9CDF", button_color="#4A9CDF", border_color="#4A9CDF", text_color="#FFFFFF",
                                                      dropdown_fg_color="#4A9CDF", dropdown_text_color="#FFFFFF", state='readonly')
        self.count_choose.place(relx=0.5, rely=0.45, anchor='center')
        self.count_choose.set('5')

        self.start_choose = customtkinter.CTkComboBox(self, bg_color='#222222', values=[str(i) for i in range(1, 35)],
                                                      command=self.start_change, fg_color="#4A9CDF", button_color="#4A9CDF", border_color="#4A9CDF", text_color="#FFFFFF",
                                                      dropdown_fg_color="#4A9CDF", dropdown_text_color="#FFFFFF", state='readonly')
        self.start_choose.place(relx=0.4, rely=0.6, anchor='center')
        self.start_choose.set('1')

        self.end_choose = customtkinter.CTkComboBox(self, bg_color='#222222', values=[str(i) for i in range(2, 51)],
                                                    command=self.end_change, fg_color="#4A9CDF", button_color="#4A9CDF", border_color="#4A9CDF", text_color="#FFFFFF",
                                                    dropdown_fg_color="#4A9CDF", dropdown_text_color="#FFFFFF", state='readonly')
        self.end_choose.place(relx=0.6, rely=0.6, anchor='center')
        self.end_choose.set('35')

        # slider
        self.number_size = customtkinter.CTkSlider(
            self, from_=3, to=7, command=self.number_size, bg_color="#222222")
        self.number_size.place(relx=0.5, rely=0.5, anchor='center')

    def voice_button_click(self):
        if self.voice_button.cget("text") == "ON":
            self.voice_button.configure(
                text="OFF", fg_color="#FF0000", hover_color="#800000")
            ran.read_ = False
        else:
            self.voice_button.configure(
                text="ON", fg_color="#2E8B57", hover_color="#006400")
            ran.read = True

    def start_change(self, newnumber):
        ran.startnumber_change(newnumber=newnumber)
        self.inform.configure(text='reseted')
        self.end_choose.configure(values=[str(i)
                                  for i in range(int(newnumber)+1, 51)])
        if int(self.end_choose.get())-int(newnumber) < 10:
            self.count_choose.configure(values=[str(i) for i in range(
                1, int(self.end_choose.get())-int(newnumber)+2)])
            if ran.count > int(self.end_choose.get())-int(newnumber)+1:
                self.count_choose.set(
                    str(int(self.end_choose.get())-int(newnumber)+1))
                ran.count = int(self.end_choose.get())-int(newnumber)+1
        else:
            self.count_choose.configure(values=[str(i) for i in range(1, 11)])

    def end_change(self, newnumber):
        ran.endnumber_change(newnumber=newnumber)
        self.inform.configure(text='reseted')
        self.start_choose.configure(
            values=[str(i) for i in range(1, int(newnumber))])
        if int(newnumber)-int(self.start_choose.get()) < 10:
            self.count_choose.configure(values=[str(i) for i in range(
                1, int(newnumber)-int(self.start_choose.get())+2)])
            if ran.count > int(newnumber)-int(self.start_choose.get())+1:
                self.count_choose.set(
                    str(int(newnumber)-int(self.start_choose.get())+1))
                ran.count = int(newnumber)-int(self.start_choose.get())+1
        else:
            self.count_choose.configure(values=[str(i) for i in range(1, 11)])

    def number_size(self, size_):
        self.print_number.configure(font=('Arial', size_*15))

    def run_button_click(self):
        if not self.reading:
            if ran.run():
                self.inform.configure(text='')
            else:
                self.inform.configure(text='reseted')
            self.print_number.configure(
                text=','.join(map(str, ran.randnumber)))
            if ran.read_:
                threading.Thread(target=self.read).start()
        else:
            self.inform.configure(text="it's reading now")

    def clear_button_click(self):
        ran.clear()
        self.inform.configure(text='reseted')

    def read(self):
        self.reading = True
        ran.read()
        self.reading = False
        if self.inform.cget('text') == "it's reading now":
            self.inform.configure(text='')
