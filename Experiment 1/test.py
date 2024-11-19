import tkinter as tk


class Calc(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = None  # 输入框
        self.title('计算器')
        self.create()

    def create(self):
        btn_list = ['7', '8', '9', '/',
                    '4', '5', '6', '*',
                    '1', '2', '3', '-',
                    'C', '0', '=', '+']

        r, c = 1, 0
        for text in btn_list:
            tk.Button(self, text=text, width=5,
                      command=(lambda x=text: self.click(x))).grid(row=r, column=c, padx=3, pady=6)

            c += 1
            if c > 3:
                c = 0
                r += 1

        self.entry = tk.Entry(self, width=24, borderwidth=2)
        self.entry.grid(row=0, column=0, columnspan=4, padx=8, pady=6)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.entry.get())
                self.entry.insert(tk.END, ' = ' + str(result))
            except Exception:
                self.entry.insert(tk.END, ' = 错误')
        elif key == 'C':
            self.entry.delete(0, tk.END)
        else:
            if '=' in self.entry.get():
                self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, key)


Calc().mainloop()
