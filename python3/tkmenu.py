#!/usr/bin/env python3
# ***************************************************************************
# *   tkmenu.py                                Version 20200902.193906      *
# *                                                                         *
# *   Plot with tk and matplotlib                                           *
# *   Copyright (C) 2020         by JHeine                                  *
# ***************************************************************************
#
# The MIT License
#
# Copyright (C) 2020 by JHeine
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# ***************************************************************************
# *   To contact the author, please write to:                               *
# *   JHeine                                                                *
# *   Email: jonheine@gmail.com                                             *
# *   Webpage: http://heine.wildsurf.net                                    *
# *   Phone: (**) *****-****                                                *
# ***************************************************************************/

import math
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox


class MainApplication(tk.Frame):

    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root
        self.plotversion = 0

        menubar = tk.Menu(root)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", underline=0, command=self.open)
        filemenu.add_command(label="Save", underline=0, command=self.save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=0, command=root.quit)
        menubar.add_cascade(label="File", underline=0, menu=filemenu)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cut", underline=0, command=self.cut)
        editmenu.add_command(label="Copy", underline=0, command=self.copy)
        editmenu.add_command(label="Paste", underline=0, command=self.paste)
        editmenu.add_command(label="Edit", underline=0, command=self.edit)
        menubar.add_cascade(label="Edit", underline=0, menu=editmenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", underline=0, command=self.about)
        menubar.add_cascade(label="Help", underline=0, menu=helpmenu)

        root.config(menu=menubar)

        frame = tk.Frame(root, width=500, height=300)
        self.text = tk.Text(frame, height=20, width=100)
        self.text.pack()
        frame.pack()

        self.pack()

    def hello(self):
        print("Hello called\n")

    def open(self):
        fn = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")], title="Open File")
        if fn is not None:
            print ("filename: " + fn)
            f = open(fn, "r")
            self.text.insert(tk.END, f.read())

    def save(self):
        pass

    def quit(self):
        pass

    def cut(self):
        self.text.delete('1.0', tk.END)

    def copy(self):
        pass

    def paste(self):
        pass

    def edit(self):
        pass

    def about(self):
        messagebox.showinfo("About tkmenu", "A simple menu example")


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

# vi: set ai et ts=4 sw=4 tw=0 wm=0 fo=croql : C config for Vim modeline
