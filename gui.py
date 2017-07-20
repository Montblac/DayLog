from tkinter import Tk, mainloop, Label, Entry
from time import strftime
from os import getcwd, path

# Remove after
from os import listdir

class AppGUI:
    """ Creates the gui for the daylog
    """
    def __init__(self):
        self.bg = "#34495e"  # Midnight Blue
        self.fg = "#FFFFFF"  # White

        self.master = Tk()
        self.master.title("DayLog")
        self.master.configure(bg=self.bg)

        Label(self.master, text='Entry', bg=self.bg, fg=self.fg).grid(row=0)

        self.entry = Entry(self.master)
        self.entry.grid(row=0, column=1)
        self.entry.configure(bg=self.bg, fg=self.fg, highlightbackground=self.bg)
        self.entry.focus_set()

        self.entry.bind('<Return>', self.add)


    def get(self, event):
        """ Returns the text entry of the user
        """
        return event.widget.get()

    def add(self, event):
        """ Adds user input to text file
        """
        # Current date in format month-day-year with leading zeros
        file = strftime("%m-%d-%Y")
        current_dir = getcwd()
        result = current_dir + '\\' + file

        print(listdir(current_dir))
        print(path.isfile(result))
        print(getcwd())
        print(result)


    def remove(self):
        """ Removes user input from text file
        """
        pass

    def update(self):
        """ Updates window with a clean entry box
        """
        pass

    def start(self):
        """ Starts the GUI window
        """
        self.master.mainloop()



