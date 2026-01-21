import tkinter as tk

class My_Calc():

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('380x470+750+200')
        self.window.resizable(False, False)

        self.window.title('Calculator')
        self.icon = tk.PhotoImage(file='icon.png')
        self.window.iconphoto(False, self.icon)
        self.window.configure(bg="#503b34")

        self.entry = tk.Entry(self.window, font=('', 20))
        self.entry.place(x=50, y=50, height=70, width=280)

        self.but_1 = tk.Button(self.window, bg='black', fg="#E6D3D8", text='1', font=('', 20), command= lambda : self.input_into_entry(symbol='1'))
        self.but_1.place(x=50, y=150, width=70, height=70)

        self.but_2 = tk.Button(self.window, bg='black', fg="#E6D3D8", text='2', font=('', 20), command= lambda : self.input_into_entry(symbol='2'))
        self.but_2.place(x=120, y=150, width=70, height=70)

        self.but_3 = tk.Button(self.window, bg='black', fg='#E6D3D8', text='3', font=('', 20), command= lambda : self.input_into_entry(symbol='3'))
        self.but_3.place(x=190, y=150, width=70, height=70)

        self.but_4 = tk.Button(self.window, bg='black', fg='#E6D3D8', text='4', font=('', 20), command= lambda : self.input_into_entry(symbol='4'))
        self.but_4.place(x=50, y=220, width=70, height=70)

        self.but_5 = tk.Button(self.window, bg='black', fg='#E6D3D8', text='5', font=('', 20), command= lambda : self.input_into_entry(symbol='5'))
        self.but_5.place(x=120, y=220, width=70, height=70)

        self.but_6 = tk.Button(self.window, bg='black', fg='#E6D3D8', text='6', font=('', 20), command= lambda : self.input_into_entry(symbol='6'))
        self.but_6.place(x=190, y=220, width=70, height=70)

        self.but_7 = tk.Button(self.window, bg='black', fg='#E6D3D8', text='7', font=('', 20), command= lambda : self.input_into_entry(symbol='7'))
        self.but_7.place(x=50, y=290, width=70, height=70)

        self.but_8 = tk.Button(self.window, bg='black', fg='#E6D3D8', text='8', font=('', 20), command= lambda : self.input_into_entry(symbol='8'))
        self.but_8.place(x=120, y=290, width=70, height=70)

        self.but_9 = tk.Button(self.window, bg='black', fg='#E6D3D8', text='9', font=('', 20), command= lambda : self.input_into_entry(symbol='9'))
        self.but_9.place(x=190, y=290, width=70, height=70)

        self.but_plus = tk.Button(self.window, bg='black', fg='#E6D3D8', text='+', font=('', 20), command= lambda : self.input_into_entry(symbol='+'))
        self.but_plus.place(x=260, y=150, width=70, height=70)

        self.but_minus = tk.Button(self.window, bg='black', fg='#E6D3D8', text='-', font=('', 20), command= lambda : self.input_into_entry(symbol='-'))
        self.but_minus.place(x=260, y=220, width=70, height=70)

        self.but_devide = tk.Button(self.window, bg='black', fg='#E6D3D8', text='/', font=('', 20), command= lambda : self.input_into_entry(symbol='/'))
        self.but_devide.place(x=260, y=290, width=70, height=70)

        self.but_multiply = tk.Button(self.window, bg='black', fg='#E6D3D8', text='*', font=('', 20), command= lambda : self.input_into_entry(symbol='*'))
        self.but_multiply.place(x=260, y=360, width=70, height=70)

        self.but_result = tk.Button(self.window, bg='#c33a3a', fg='#E6D3D8', text='=', font=('', 20),command=self.count_result)
        self.but_result.place(x=190, y=360, width=70, height=70)

        self.but_clear = tk.Button(self.window, bg='black', fg='#E6D3D8', text='CE', font=('', 20), command=self.clear_entry)
        self.but_clear.place(x=120, y=360, width=70, height=70)

        self.but_zero = tk.Button(self.window, bg='black', fg='#E6D3D8', text='0', font=('', 20), command= lambda : self.input_into_entry(symbol='0'))
        self.but_zero.place(x=50, y=360, width=70, height=70)

        self.window.mainloop()


    def input_into_entry(self, symbol:str):
        self.entry.insert(tk.END, symbol)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def count_result(self):
        expr = self.entry.get()
        if not expr or any(s not in "0123456789+-*/." for s in expr):
            self.clear_entry()
            self.input_into_entry('ERROR')
            return
        
        try:
            result = eval(expr)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            self.clear_entry()
            self.input_into_entry(str(result))

        except ZeroDivisionError:
            self.clear_entry()
            self.input_into_entry('DIV/0')
        
        except Exception:
            self.clear_entry()
            self.input_into_entry('ERROR')


if __name__ == '__main__':
    my_calc = My_Calc()