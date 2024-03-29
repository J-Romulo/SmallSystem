from tkinter import messagebox


class DuplicatePrimaryKeyError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Login já existente.\nTente outro para completar o registro"

    def throwGUI(self):
        messagebox.showerror("Error", "{}".format(self.__str__()))
