import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(
    name="DayLog",
    version="1.0",
    description="A simple application to keep a log of your daily actions.",
    author="Montblac",
    options={
        "build_exe": {
            "includes": ['tkinter', 'time', 'os'],
            "excludes": ['tcl', 'Tcl']
        }
    },
    executables=[
        Executable("main.py", base=base)
    ]
)
