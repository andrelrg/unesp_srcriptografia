from criptograpy import Criptograpy
from application import Application
from tkinter import *
import os

def main():
    os.environ["SECRETKEY"] = "TESTKEY"
    root = Tk()
    Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()