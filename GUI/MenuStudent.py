from Facade.FcdCourses import FcdCourses
from GUI.EditScreen import *

class MenuStudent:
    def __init__(self, student, master=None):
        self.student = student
        self.mainWidget = tkinter.Frame(master)
        self.mainWidget.pack()

        self.titleLabel = tkinter.Label(self.mainWidget, text="Menu Principal do Aluno")
        self.titleLabel["font"] = ("Arial", "15", "bold")
        self.titleLabel.pack()



        self.profileInfoWidget = tkinter.Frame(master)
        self.profileInfoWidget.pack()

        self.rightProfileInfoWidget = tkinter.Frame(self.profileInfoWidget)
        self.rightProfileInfoWidget.grid(row=0, column=1,padx=(10,30))

        self.leftProfileInfoWidget = tkinter.Frame(self.profileInfoWidget)
        self.leftProfileInfoWidget.grid(row=0, column=0, padx=(30,10))


        self.nameLabel = tkinter.Label(self.leftProfileInfoWidget)
        self.nameLabel["text"] = ("Nome: {}".format(student.name))
        self.nameLabel.grid(row=0, column=0, sticky=tkinter.W)

        self.ageLabel = tkinter.Label(self.leftProfileInfoWidget)
        self.ageLabel["text"] = ("Idade: {}".format(student.age))
        self.ageLabel.grid(row=1, column=0, sticky=tkinter.W)

        self.emailLabel = tkinter.Label(self.rightProfileInfoWidget)
        self.emailLabel["text"] = ("Email: {}".format(student.email))
        self.emailLabel.grid(row=0, column=0, sticky=tkinter.W)

        self.contactLabel = tkinter.Label(self.rightProfileInfoWidget)
        self.contactLabel["text"] = ("Contato: {}".format(student.contact))
        self.contactLabel.grid(row=1, column=0, sticky=tkinter.W)



        self.optionsWidget = tkinter.Frame(master)
        self.optionsWidget.pack()

        self.openEditProfileAreaButton = tkinter.Button(self.optionsWidget, text='Modificar Perfil')
        self.openEditProfileAreaButton.pack(side=tkinter.LEFT)
        self.openEditProfileAreaButton["command"] = self.editOptionsButtons


        #Itens sem pack
        self.editNameButton = tkinter.Button(self.optionsWidget, text='Atualizar Nome')
        self.editLoginButton = tkinter.Button(self.optionsWidget, text='Atualizar Login')
        self.editPasswordButton = tkinter.Button(self.optionsWidget, text='Atualizar Senha')



        self.listCoursesWidget = tkinter.Frame(master)
        self.listCoursesWidget.pack()

        self.labelCourses = tkinter.Label(self.listCoursesWidget, text="Cursos disponíveis")
        self.labelCourses.grid(row=0, column=0, padx=(20,30), pady=(10,0))

        self.listCourses = tkinter.Listbox(self.listCoursesWidget, height=8)
        FcdCourses.takeListOfAllCoursesAndSendToGui(self.listCourses)
        self.listCourses.grid(row=1, column=0, padx=(20,30))

        self.labelYourCourses = tkinter.Label(self.listCoursesWidget, text="Cursos matriculados")
        self.labelYourCourses.grid(row=0, column=1, padx=(20,30), pady=(10,0))

        self.listYourCourses = tkinter.Listbox(self.listCoursesWidget, height=8)
        self.listYourCourses.grid(row=1, column=1, padx=(20,30))

    def editOptionsButtons(self):
        self.openEditProfileAreaButton.pack_forget()

        self.editLoginButton.pack(side=tkinter.LEFT)
        self.editLoginButton["command"] = self.editLoginScreen

        self.editPasswordButton.pack(side=tkinter.LEFT)
        self.editPasswordButton["command"] = self.editPasswordScreen

        self.editNameButton.pack(side=tkinter.LEFT)
        self.editNameButton["command"] = self.editNameScreen

    
    def editLoginScreen(self):
        EditScr = tkinter.Tk()
        EditScr.title("Modificar Login")
        EditScr.geometry('260x150')

        EditScreen(self.student, 1, EditScr)
        EditScr.mainloop()


    def editPasswordScreen(self):
        EditScr = tkinter.Tk()
        EditScr.title("Modificar Senha")
        EditScr.geometry('260x150')

        EditScreen(self.student, 2, EditScr)
        EditScr.mainloop()


    def editNameScreen(self):
        EditScr = tkinter.Tk()
        EditScr.title("Modificar Nome")
        EditScr.geometry('260x150')

        EditScreen(self.student, 3, EditScr)
        EditScr.mainloop()