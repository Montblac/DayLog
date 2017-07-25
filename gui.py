from tkinter import Tk, Label, Entry, Button, Frame, Toplevel
from time import strftime, localtime
from os import path
from settings import Settings

class AppGUI:
    """ Creates the gui for the daylog
    """
    def __init__(self):
        self.settings = Settings()

        self.bg = "#34495e"  # Midnight Blue
        self.fg = "#FFFFFF"  # White

        self.master = Tk()
        self.master.title("DayLog")
        self.master.configure(bg=self.bg)
        self.master.resizable(width=False, height=False)

        Label(self.master, text='Entry', bg=self.bg, fg=self.fg).grid(row=0)

        self.entry = Entry(self.master)
        self.entry.configure(bg=self.bg, fg=self.fg, highlightbackground=self.bg)
        self.entry.grid(row=0, column=1)
        self.entry.focus_set()
        self.entry.bind('<Return>', self.add)

        self.frame = Frame(self.master, bg=self.bg)
        self.frame.grid(row=1, column=0, columnspan=2, sticky='WE')
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)

        self.show_button = Button(self.frame, text="Show", command=self.show)
        self.show_button.configure(bg=self.bg, fg=self.bg, highlightbackground=self.bg, highlightcolor=self.bg)
        self.show_button.grid(row=0, column=0, sticky='WE')

        self.settings_button = Button(self.frame, text="Settings", command=None)
        self.settings_button.configure(bg=self.bg, fg=self.bg, highlightbackground=self.bg, highlightcolor=self.bg)
        self.settings_button.grid(row=0, column=1, sticky='WE')



    def get(self):
        """ Returns the text entry of the user
        """
        return self.entry.get()

    def add(self, event):
        """ Adds user input to text file
        """
        base = self.settings.getLocation()

        filename = strftime("%Y-%d-%m") + ".txt"
        filepath = path.join(base, filename)

        with open(filepath, 'a+') as fp:
            fp.write("[{}]  {}\n".format(strftime("%H:%M:%S", localtime()), self.get()))

        self.update()

    def remove(self):
        """ Removes user input from text file
        """
        pass

    def update(self):
        """ Updates window with a clean entry box
        """
        self.entry.delete(0, 'end')

    def show(self):
        """ Prints the logs for the day
        """
        x = self.master.winfo_x()
        y = self.master.winfo_y()
        w = self.master.winfo_width()
        h = self.master.winfo_height()

        root_h = self.master.winfo_height()
        frame_h = self.frame.winfo_height()

        toplevel = Toplevel()
        toplevel.title("Viewer")
        toplevel.configure(width=w, bg=self.bg)
        toplevel.resizable(width=False, height=False)

        base = self.settings.getLocation()
        filename = strftime("%Y-%d-%m") + ".txt"
        filepath = path.join(base, filename)

        # WIP ---
        if path.isfile(filepath):
            text = ""
            with open(filepath, 'r') as fp:
                for line in fp:
                    text += line
            print(text)
        else:
            toplevel.geometry("%dx%d%+d%+d" % (w, h, x, y + root_h + frame_h + 2))
            Label(toplevel, text="File does not exist.", bg=self.bg, fg=self.fg).grid()
            toplevel.focus_set()


    def start(self):
        """ Starts the GUI window
        """
        self.master.mainloop()



