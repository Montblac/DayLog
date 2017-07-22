from tkinter import Tk, Label, Entry
from time import strftime, localtime
from os import getcwd, path

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


    def get(self):
        """ Returns the text entry of the user
        """
        return self.entry.get()

    def add(self, event):
        """ Adds user input to text file
        """
        base = getcwd()
        filename = strftime("%Y-%d-%m") + ".txt"
        filepath = path.join(base, filename)

        with open(filepath, 'a+') as fp:
            fp.write("[{}]\t{}".format(strftime("%H:%M:%S", localtime()), self.get()))

        self.update()
        self.show()

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
        base = getcwd()
        filename = strftime("%m-%d-%Y")
        filepath = path.join(base, filename)

        with open(filepath, 'r') as fp:
            for line in fp:
                print(line)

    def start(self):
        """ Starts the GUI window
        """
        self.master.mainloop()



