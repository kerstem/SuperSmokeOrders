from tkinter import *
from tkinter.ttk import *


class Scrollable(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.canvas = Canvas(self)
        self.scrollbar = Scrollbar(self, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.frame = Frame(self)
        self.window = self.canvas.create_window((0, 0), window=self.frame, anchor=NW)
        self.canvas.bind('<Configure>', self.__fill)
        self.canvas.bind('<>')
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.pack(side=LEFT, fill=Y, expand=False)
        self.bind('<Enter>', self._bound_to_mousewheel)
        self.bind('<Leave>', self._unbound_to_mousewheel)

    def __fill(self, event):
        print(event.width)
        self.canvas.itemconfigure(self.window, width=event.width)

    def __update(self):
        self.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox(self.window))

    def _bound_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def add(self):
        Label(self.frame, text='ABC').pack()
        self.__update()

    def delete(self):
        self.frame.winfo_children()[-1].destroy()
        self.__update()


class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title('SuperSmokeOrders')
        self.scr = Scrollable(self)
        self.scr.pack(side=LEFT, fill=BOTH,expand=True)
        self.right = Frame(self)
        self.right.pack(side=RIGHT,fill=Y)
        self.addbtn = Button(self.right, text='Add', command=self.scr.add)
        self.addbtn.pack(side=TOP, fill=BOTH,expand=True)
        self.deldbtn = Button(self.right, text='Del', command=self.scr.delete)
        self.deldbtn.pack(side=BOTTOM, fill=BOTH,expand=True)


if __name__ == '__main__':
    a = Gui()
    a.mainloop()
    input()
