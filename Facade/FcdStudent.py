from Login import *
from EditProfile import *
import tkinter
from GUI.Errors.LoginError import LoginError

class FcdStudent:
    def __init__(self):
        pass

    @staticmethod
    def log(usuario, senha):
        student = Login.log(usuario, senha)

        return student


    @staticmethod
    def register(usuario, senha, nome, idade, email, contato):
        student = Login.register(usuario, senha, nome, idade, email, contato)

        return student

    @staticmethod
    def editPassword(student, login, senha, novaSenha):
        EditProfile.editStudentPassword(student, login, senha, novaSenha)

    @staticmethod
    def editLogin(student, login, senha, novoLogin):
        EditProfile.editStudentLogin(student, login, senha, novoLogin)

    @staticmethod
    def editName(student, login, senha, novoNome):
        EditProfile.editStudentName(student, login, senha, novoNome)

    @staticmethod
    def throwExceptionGUI(msgError):
        mainFrame = tkinter.Tk()
        mainFrame.title("Error")
        mainFrame.geometry('225x60')
        LoginError(msgError, mainFrame)