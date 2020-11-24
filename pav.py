"""
Notes:
Universal fonts for program = Arial

"""
from tkinter import *
import os
import time
import getpass
from tkinter import messagebox
from datetime import date
import subprocess
import webbrowser

def mainmenu(fileentry = ['No files'], fileentryload=[],filetypes=[" ",".sh",".txt",".py",".pdf",".java"],Projname='pav.py', autoauthorsave=[]):
    def editor():
        def loadconfig():
            def LDdestry():
                LD.destroy()
            def recentcon():
                recentcon1 = subprocess.run('ls', capture_output=True, text=True)
                reccongig = recentcon1.stdout
                recentfilestxt.insert(END, reccongig)


            def LDcon():
                lname1 = LName_of_fileent.get()
                #checks if the program is the source file
                if lname1 == Projname:
                    messagebox.showwarning("Be careful!","You are opening Pavilions source code file, feel free to edit anything you want. Just be careful not to break anything. Happy editing :D")

                #checks if input is vaild
                if lname1 == "":
                    LD.destroy()
                    messagebox.showwarning("No input found","Please enter the name of the file")
                    fileentry.remove("")
                editortxt.delete('1.0', END)
                fileentry.clear()
                fileentry.append(lname1)
                LD.destroy()
                #open the chosen file
                ldp = open(lname1,"r")
                #paste contents of file on to editor window
                editortxt.insert(END, ldp.read())
                #close and reopen the file a editable.
                ldp.close()

            LD = Tk()
            LD.title("Load Project")
            LD.geometry("500x200")

            LDframe = LabelFrame(LD)
            LDframe.pack()
            LTitlenw = Label(LDframe, text="Load Project", font=("Arial Black", 12), padx=2,pady=5, height=1)
            LTitlenw.grid(row=0,column=0)
            LName_of_file = Label(LDframe, text="Name of project:", font=("Arial", 12),padx=10)
            LName_of_file.grid(row=1,column=0)
            LName_of_fileent = Entry(LDframe, width=30)
            LName_of_fileent.grid(row=1,column=1)
            Lfilelocationbtn = Button(LDframe,text="Next",width=10,command=LDcon)
            Lfilelocationbtn.grid(row=1, column=3)
            Lfilelocationbtn1 = Button(LDframe,text="back",width=10,command=LDdestry)
            Lfilelocationbtn1.grid(row=0, column=3)

            #Text box that displays the recent files opened
            LDrecframe = LabelFrame(LD, text="Documents in path")
            LDrecframe.pack()
            recentfilestxt = Text(LDrecframe, width=60, height=5)
            recentfilestxt.pack()

            recentcon()
            LD.mainloop()

        def Ineditornewproject():
            messagebox.showwarning("Warning!","Creating a new project will erase any unsaved work currently open.")
            def NPback1():
                Nw1.destroy()
            def saving1():
                name1 = Name_of_fileent1.get()
                editorname1 = editortxt.get("1.0","end-1c")
                if name1 == "":
                    Nw1.destroy()
                    messagebox.showwarning("No input found","Please enter the name of the file")

                #create a file using the data from the last windows
                fileentry.clear()
                filenamecon1 = name1 + variable1.get()
                fileentry.append(filenamecon1)
                file1 = open(name1 + variable1.get(),"w")
                #add autoauthor
                todayx = date.today()
                usernamex = getpass.getuser()
                Namex = Name_of_fileent1.get()
                Authorx = usernamex
                Datex = todayx.strftime("%d/%m/%Y")
                pathx = __file__
                autocomepletex = """

#============================================================================
# Name of Project: {0}
# Path:            {3}
# Author:          {1}
# Date created:    {2}
# Copyright: (c) <Yourname> <Year>
# Licence: <Your Licence>
# Description:
#
# Notes:
#============================================================================

                """.format(Namex, Authorx, Datex, pathx)
                #clear the textbox
                editortxt.delete('1.0', END)
                #insert the autoauthor in
                editortxt.insert(END,autocomepletex)
                #write autoauthor into the file1
                file1.write(autocomepletex)
                file1.close()
                Nw1.destroy()


            #Startup preperation for editor
            Nw1 = Tk()
            Nw1.title('Start New Project')
            Nw1.geometry('500x100')
            Titlenw1 = Label(Nw1, text="New project", font=("Arial Black", 12), padx=2,pady=5, height=1)
            Titlenw1.grid(row=0,column=0)
            #ask user for the name of the file
            Name_of_file1 = Label(Nw1, text="Name of project:", font=("Arial", 12),padx=10)
            Name_of_file1.grid(row=1,column=0)
            Name_of_fileent1 = Entry(Nw1, width=30)
            Name_of_fileent1.grid(row=1,column=1)
            #ask for a file type
            variable1 = StringVar(Nw1) #this sets up the combobox
            variable1.set(filetypes[0])
            Name_of_fileopt1 = OptionMenu(Nw1, variable1,*filetypes)
            Name_of_fileopt1.config(width=8, )
            Name_of_fileopt1.grid(row=1,column=3)
            #ask for a saving location
            filelocationbtn1 = Button(Nw1,text="Next",width=10,command=saving1)
            filelocationbtn1.grid(row=2, column=3)
            exitbtn = Button(Nw1,text="back",width=10,command=NPback1)
            exitbtn.grid(row=2, column=0)
            Nw1.mainloop()


        #Only used for key binds
        def savekey(event):
            filenameimport1 = ''.join(fileentry)
            if filenameimport1 == "No files":
                def NOPdestry1():
                    NOP1.destroy1()
                def NOPsaving1():
                    fileentry.clear()
                    Nname1 = NName_of_fileent1.get()
                    #create a file using the data from the last windows
                    file1 = open(Nname1 + Nvariable1.get(),"w")
                    contentN1 = editortxt.get("1.0","end-1c")
                    #clears text box
                    editortxt.delete('1.0', END)
                    file1.write(contentN1)
                    file1.close()
                    messagebox.showinfo("Saved","Your file has been saved :D.")
                    NOP1.destroy()

                messagebox.showwarning("Warning","Editor will be cleared after save. If your not sure that your done, just exit from the saving prompt")
                NOP1 = Tk()
                NOP1.title('Save as a new project')
                NOP1.geometry('500x100')
                NTitlenw1 = Label(NOP1, text="New project", font=("Arial Black", 12), padx=2,pady=5, height=1)
                NTitlenw1.grid(row=0,column=0)

                NName_of_file1 = Label(NOP1, text="Name of project:", font=("Arial", 12),padx=10)
                NName_of_file1.grid(row=1,column=0)
                NName_of_fileent1 = Entry(NOP1, width=30)
                NName_of_fileent1.grid(row=1,column=1)
                NName_of_filebtn1 = Button(NOP1,text="next",width=10,command=NOPsaving1)
                NName_of_filebtn1.grid(row=3,column=3)
                NName_of_filebtn2 = Button(NOP1,text="back",width=10,command=NOPdestry1)
                NName_of_filebtn2.grid(row=3,column=0)

                Nvariable1 = StringVar(NOP1)
                Nvariable1.set(filetypes[0])
                NName_of_fileopt1 = OptionMenu(NOP1, Nvariable1,*filetypes)
                NName_of_fileopt1.config(width=8)
                NName_of_fileopt1.grid(row=1,column=3)

                NOP1.mainloop()
            else:
                #create a file using the data from the last windows
                file1 = open(filenameimport1,"w")
                contentN1 = editortxt.get("1.0","end-1c")
                #clears text box
                file1.write(contentN1)
                file1.close()
                messagebox.showinfo("Saved","Your file has been saved :D.")

        def save():
            filenameimport = ''.join(fileentry)
            if filenameimport == "No files":
                def NOPdestry():
                    NOP.destroy()
                def NOPsaving():
                    fileentry.clear()
                    Nname = NName_of_fileent.get()
                    #create a file using the data from the last windows
                    file = open(Nname + Nvariable.get(),"w")
                    contentN = editortxt.get("1.0","end-1c")
                    #clears text box
                    editortxt.delete('1.0', END)
                    file.write(contentN)
                    file.close()
                    messagebox.showinfo("Saved","file has been saved.")
                    NOP.destroy()

                messagebox.showwarning("Warning","Editor will be cleared after save. If your not sure that your done, just exit from the saving prompt")
                NOP = Tk()
                NOP.title('Save as a new project')
                NOP.geometry('500x100')
                NTitlenw = Label(NOP, text="New project", font=("Arial Black", 12), padx=2,pady=5, height=1)
                NTitlenw.grid(row=0,column=0)

                NName_of_file = Label(NOP, text="Name of project:", font=("Arial", 12),padx=10)
                NName_of_file.grid(row=1,column=0)
                NName_of_fileent = Entry(NOP, width=30)
                NName_of_fileent.grid(row=1,column=1)
                NName_of_filebtn = Button(NOP,text="next",width=10,command=NOPsaving)
                NName_of_filebtn.grid(row=3,column=3)
                NName_of_filebtn1 = Button(NOP,text="back",width=10,command=NOPdestry)
                NName_of_filebtn1.grid(row=3,column=0)

                Nvariable = StringVar(NOP)
                Nvariable.set(filetypes[0])
                NName_of_fileopt = OptionMenu(NOP, Nvariable,*filetypes)
                NName_of_fileopt.config(width=8, )
                NName_of_fileopt.grid(row=1,column=3)

                NOP.mainloop()

                #switch to editor
            #grabs the name of the file from fileentry
            fileedit = open(filenameimport,'w')
            content = editortxt.get("1.0","end-1c")
            fileedit.write(content)
            fileedit.close()
            messagebox.showinfo("Saved","Your file has been saved :)")

        #create the window for the editor
        def donothing():
            pass

        def pipetoshell():
            def pipeaction():
                #Get content of Entry
                PP = PEntry.get()
                #Get command for webbrowser and plug in the details
                webbrowser.open(PP)
            PipeT = Tk()
            PipeT.title('Pipe to shell')
            PipeT.geometry('500x200')
            Ptitle = Label(PipeT, text="Pipe shell",font=("Arial", 15),padx=10)
            Ptitle.pack()

            Pframe = LabelFrame(PipeT)
            Pframe.pack()
            PEntry = Entry(Pframe,width=30)
            PEntry.grid(row=1,column=0)
            PBTN = Button(Pframe, text="Run", width=5, command=pipeaction)
            PBTN.grid(row=1,column=1)

            conTT = """ In order to pipe this program to shell, type name of file in the box above and copy and paste this command:
            python3 <filename with extension>
            for copy & P: python3
            """
            PframeT = LabelFrame(PipeT)
            PframeT.pack()
            PcontextT = Label(PframeT, text="Run command",font=("Arial", 12))
            PcontextT.pack()
            Pcontext = Text(PframeT,width=50,height=50,padx=10)
            Pcontext.pack()
            Pcontext.insert(END, conTT)
            PipeT.mainloop()


        ED = Tk()
        ED.title('E D I T O R')
        ED.geometry('1500x600')
        menubar = Menu(ED)

        filemenu = Menu(menubar, tearoff=0)

        filemenu.add_command(label="New", command=Ineditornewproject)
        filemenu.add_command(label="Open", command=loadconfig)
        filemenu.add_command(label="Save", command=save)

        filemenu.add_separator()

        filemenu.add_command(label="New window", command=editor)

        filemenu.add_separator()


        filemenu.add_command(label="Exit Program", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        toolmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tool", menu=toolmenu)
        toolmenu.add_command(label="Pipe to shell", command=pipetoshell)

        ED.config(menu=menubar)

        #below

        frameed = LabelFrame(ED,text=fileentry)
        frameed.pack()
        editortxt = Text(frameed, width=500, height=47, bg="black") #this is our editor window
        editortxt.delete('1.0', END)
        editortxt.grid(row=0,column=0)
        editortxt.insert(END, autoauthorsave)
        autoauthorsave.clear()

        #keybinds
        ED.bind('<F1>', savekey)

        ED.mainloop()

    def Newproject():

        def NPback():
            Nw.destroy()
            mainmenu()
        def saving(today = date.today(), username = getpass.getuser()):

            name = Name_of_fileent.get()
            #create a file using the data from the last windows
            file = open(name + variable.get(),"w")
            filenamecon = name + variable.get()
            #logging the file name
            fileentry.clear()
            fileentry.append(filenamecon)
            #add autoauthor
            NameO = Name_of_fileent.get()
            Author0 = username
            Date0 = today.strftime("%d/%m/%Y")
            path0 = __file__
            autocomeplete0 = """

#============================================================================
# Name of Project: {0}
# Path:            {3}
# Author:          {1}
# Date created:    {2}
# Copyright: (c) <Yourname> <Year>
# Licence: <Your Licence>
# Description:
#
# Notes:
#============================================================================

            """.format(NameO, Author0, Date0, path0)
            #write to file
            file.write(autocomeplete0)
            #append contents to editor
            autoauthorsave.append(autocomeplete0)
            file.close()
            Nw.destroy()
            editor()


        #Startup preperation for editor
        Nw = Tk()
        Nw.title('Start New Project')
        Nw.geometry('500x100')
        Titlenw = Label(Nw, text="New project", font=("Arial Black", 12), padx=2,pady=5, height=1)
        Titlenw.grid(row=0,column=0)
        #ask user for the name of the file
        Name_of_file = Label(Nw, text="Name of project:", font=("Arial", 12),padx=10)
        Name_of_file.grid(row=1,column=0)
        Name_of_fileent = Entry(Nw, width=30)
        Name_of_fileent.grid(row=1,column=1)
        #ask for a file type
        variable = StringVar(Nw) #this sets up the combobox
        variable.set(filetypes[0])
        Name_of_fileopt = OptionMenu(Nw, variable,*filetypes)
        Name_of_fileopt.config(width=8, )
        Name_of_fileopt.grid(row=1,column=3)
        #ask for a saving location
        filelocationbtn = Button(Nw,text="Next",width=10,command=saving)
        filelocationbtn.grid(row=2, column=3)
        exitbtn = Button(Nw,text="back",width=10,command=NPback)
        exitbtn.grid(row=2, column=0)
        Nw.mainloop()
        #save and close the program
        #switch to editor

    def exit():
        fileentry.clear()
        fileentry = []
        quit()

    def closewindow():
        #closes the main window
        root.destroy()

    root = Tk()
    root.title('P A V')
    root.geometry('250x345')

    title = Label(text="P A V I L I O N",width=13,height=6,fg='white', font=("Arial Black", 20))
    title.pack()

    #button for a new project
    newbtn = Button(text="Start new project", width=20,height=1, command=lambda: [closewindow(),
                                                                                    Newproject()])
    newbtn.pack()


    #button for editor launch
    editorbtn = Button(text="Open editor", width = 20, height=1, command=lambda: [closewindow(),
                                                                                    editor()])
    editorbtn.pack()

    exitbtn = Button(text="Exit", width=20,height=1, command=quit)
    exitbtn.pack()
    root.mainloop()

if __name__ == "__main__":
    mainmenu()
