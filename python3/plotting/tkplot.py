#!/usr/bin/env python3
# ***************************************************************************
# *   tkplot.py                                Version 20200902.193906      *
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
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2TkAgg)


class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.plotversion = 0

        fig = Figure(figsize=(5, 5), dpi=100)

        y = [math.cos(i / 10) for i in range(101)]

        # adding the subplot
        self.plot1 = fig.add_subplot(111)

        # plotting the graph
        self.plot1.plot(y)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(fig, master=parent)
        self.canvas.draw()

        # placing the canvas on the Tkinter parent
        self.canvas.get_tk_widget().pack(side=tk.TOP)

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2TkAgg(self.canvas, parent)

        toolbar.update()

        # placing the toolbar on the Tkinter parent
        # self.canvas.get_tk_widget().pack()

        plot_button = tk.Button(master=parent, command=self.replot, height=2,
                                width=10, text="Plot")
        plot_button.pack(side=tk.RIGHT)

        plot_button = tk.Button(master=parent, command=self.replot, height=2,
                                width=10, text="Plot")

        self.clear = tk.IntVar()
        clear_button = tk.Checkbutton(master=parent, text="clear", variable=self.clear)
        clear_button.pack(side=tk.RIGHT)

    def replot(self):
        # list of squares
        self.plotversion += 1

        if self.plotversion == 1:
            y = [math.sin(i / 10) for i in range(101)]
        elif self.plotversion == 2:
            y = [math.sin(i / 10) * math.cos(3 * i / 10) for i in range(101)]
        elif self.plotversion == 3:
            y = [math.sin(2 * i / 10) * math.cos(3 * i / 10) for i in range(101)]
        elif self.plotversion == 4:
            y = [math.sin(3 * i / 10) * math.cos(3 * i / 10) for i in range(101)]
        elif self.plotversion == 5:
            y = [math.sin(4 * i / 10) * math.cos(3 * i / 10) for i in range(101)]
        else:
            y = [math.sin(2 * i / 10) + math.cos(4 * i / 10) for i in range(101)]
            self.plotversion = 0

        if self.clear.get():
            self.plot1.clear()

        self.plot1.plot(y)
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

# vi: set ai et ts=4 sw=4 tw=0 wm=0 fo=croql : C config for Vim modeline
