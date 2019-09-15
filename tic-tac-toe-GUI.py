from tkinter import *
from threading import Thread
from tkinter import messagebox
import time

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Tic Tac Toe')
        self.geometry('400x250')
        self.is_won = True

        # game frame
        self.game_frame = Frame(self)
        self.game_frame.place(relx=.0, rely=.0, relwidth=.5, relheight=1)

        #button

        self.btn1 = Button(self.game_frame, text='', command=lambda :self.onclick(1), height=2, width=3, font='time 20 bold')
        self.btn1.grid(column=0, row=0)

        self.btn2 = Button(self.game_frame, text='',  command=lambda :self.onclick(2),  height=2, width=3, font='time 20 bold')
        self.btn2.grid(column=1, row=0)

        self.btn3 = Button(self.game_frame, text='',  command=lambda :self.onclick(3), height=2, width=3, font='time 20 bold')
        self.btn3.grid(column=2, row=0)

        self.btn4 = Button(self.game_frame, text='',  command=lambda :self.onclick(4), height=2, width=3, font='time 20 bold')
        self.btn4.grid(column=0, row=1)

        self.btn5 = Button(self.game_frame, text='',  command=lambda :self.onclick(5), height=2, width=3, font='time 20 bold')
        self.btn5.grid(column=1, row=1)

        self.btn6 = Button(self.game_frame, text='',  command=lambda :self.onclick(6), height=2, width=3, font='time 20 bold')
        self.btn6.grid(column=2, row=1)

        self.btn7 = Button(self.game_frame, text='',  command=lambda :self.onclick(7), height=2, width=3, font='time 20 bold')
        self.btn7.grid(column=0, row=2)

        self.btn8 = Button(self.game_frame, text='',  command=lambda :self.onclick(8), height=2, width=3, font='time 20 bold')
        self.btn8.grid(column=1, row=2)

        self.btn9 = Button(self.game_frame, text='',  command=lambda :self.onclick(9), height=2, width=3, font='time 20 bold')
        self.btn9.grid(column=2, row=2)

        #turn label x
        self.check_box1 = IntVar()
        self.x_label = Checkbutton(self, variable=self.check_box1, text='X-player')
        self.x_label.place(relx=.5)
        #turn label o
        self.check_box2 = IntVar()
        self.o_label = Checkbutton(self, variable=self.check_box2, text='O-player')
        self.o_label.place(relx=.7)

        #output frame
        self.output = Frame(self, bg='black')
        self.output.place(relx=.5, rely=.1, relwidth=.5, relheight=.9)

        #response of turn check box
        self.turn_box = Label(self.output, bg='black', fg='white', anchor='nw', justify=CENTER)
        self.turn_box.place(relx=.1, rely=.0, relwidth=.9, relheight=.1)

    def onclick(self, args):
        if self.is_won:
            turn = ''
            if self.check_box2.get() == 1 and self.check_box1.get() == 1:
                self.turn_box['text']='Select one player!'
                def rub(text):
                    time.sleep(2)
                    self.turn_box['text'] = text
                Thread(target=rub, args=('',)).start()

            elif self.check_box1.get() == 1: turn = 'X'
            elif self.check_box2.get() == 1: turn = 'O'


            if self.btn1['text'] is '' and args==1: self.btn1['text'] = turn
            elif self.btn2['text'] is '' and args==2: self.btn2['text'] = turn
            elif self.btn3['text'] is '' and args==3: self.btn3['text'] = turn
            elif self.btn4['text'] is '' and args==4: self.btn4['text'] = turn
            elif self.btn5['text'] is '' and args==5: self.btn5['text'] = turn
            elif self.btn6['text'] is '' and args==6: self.btn6['text'] = turn
            elif self.btn7['text'] is '' and args == 7: self.btn7['text'] = turn
            elif self.btn8['text'] is '' and args == 8: self.btn8['text'] = turn
            elif self.btn9['text'] is '' and args == 9: self.btn9['text'] = turn
            self.win_checker_call()
            self.tie_checker()

    def win_checker_call(self):
        thread1 = Thread(target=self.winner_checker, args=(self.turn_box,))
        thread1.start()

    def winner_checker(self, turn_box):
        check1 = self.btn1['text'] == self.btn2['text'] == self.btn3['text'] != ''
        check2 = self.btn4['text'] == self.btn5['text'] == self.btn6['text'] != ''
        check3 = self.btn7['text'] == self.btn8['text'] == self.btn9['text'] != ''

        check4 = self.btn1['text'] == self.btn4['text'] == self.btn7['text'] != ''
        check5 = self.btn2['text'] == self.btn5['text'] == self.btn8['text'] != ''
        check6 = self.btn3['text'] == self.btn6['text'] == self.btn9['text'] != ''

        check7 = self.btn1['text'] == self.btn5['text'] == self.btn9['text'] != ''
        check8 = self.btn3['text'] == self.btn5['text'] == self.btn7['text'] != ''

        if self.is_won:
            if check1:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                self.is_won = False
            elif check2:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                self.is_won = False
            elif check3:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                self.is_won = False
            elif check4:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                self.is_won = False
            elif check5:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                self.is_won = False
            elif check6:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                self.is_won = False
            elif check7:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                self.is_won = False
            elif check8:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                self.is_won = False

    def tie_checker(self):
        if self.is_won:
            if ('x', 'o') in self.btn1['text'] != self.btn2['text'] != self.btn3['text'] != self.btn4['text'] != self.btn5['text'] != self.btn6['text'] != self.btn7['text'] != self.btn8['text'] != self.btn9['text'] != self.btn1['text'] != self.btn4['text'] != self.btn7['text'] != self.btn2['text'] != self.btn5['text'] != self.btn8['text'] != self.btn3['text'] != self.btn6['text'] != self.btn9['text'] != self.btn1['text'] != self.btn5['text'] != self.btn9['text'] != self.btn3['text'] != self.btn5['text'] != self.btn7['text'] != '' == True:
                messagebox.showinfo('Tic-Tac-Toe', 'Tie!')






if __name__ == '__main__':
    app = App()
    app.mainloop()