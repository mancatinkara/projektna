from tkinter import *
from datetime import *

class ITM():
    
    def __init__(self, master):

        menu = Menu(master)
        master.config(menu=menu)

  
        Label(master, fg="purple", font=('arial', 12, 'bold'), text = "Izračun indeksa telesne teže pri moških in ženskah.").grid(row = 0, columnspan = 4)

        self.a = IntVar()
        Label(master, fg="purple", font=('arial', 11, 'bold'), text = "Izberi spol:",).grid(row = 1, column = 0)
        self.gumb_zenska = Radiobutton(master,variable = self.a, value = 1, fg="pink", font=('arial', 10, 'bold'), text = "ženska")
        self.gumb_zenska.grid(row = 1, column=1)
        self.gumb_moski = Radiobutton(master,variable = self.a, value = 2, fg="light blue", font=('arial', 10, 'bold'), text = "moški")
        self.gumb_moski.grid(row = 1, column=2)
        
#===============================================================================================================================================================
        
        Label(master, fg="pink", font=('arial', 10, 'bold'), text = "TEŽA [kg] ").grid(row = 2, column = 1)
        Label(master, fg="pink", font=('arial', 10, 'bold'), text = "VIŠINA [m] ").grid(row = 2, column = 0)

        gumb_izracunaj = Button(master, fg="purple", font=('arial', 10, 'bold'), text="Izračunaj!", bg="pink", command=self.izracunaj)
        gumb_izracunaj.grid(row = 2, rowspan = 2, column = 2)
        
        Label(master, fg="pink", font=('arial', 10, 'bold'), text = "ITM").grid(row = 2, column = 3)
        
#===============================================================================================================================================================
        
        self.lista = Listbox(master,selectmode=SINGLE)
        self.lista.grid(row = 4,rowspan = 2, column = 0, columnspan = 4, sticky=E+W+N+S)

        self.teza = DoubleVar(master, value = 0)
        self.visina = DoubleVar(master, value=0)
        self.itm = DoubleVar(master, value=0)

        polje_teza = Entry(master, textvariable = self.teza)
        polje_teza.grid(row = 3, column = 1)

        polje_visina = Entry(master, textvariable = self.visina)
        polje_visina.grid(row = 3, column = 0)

        polje_itm = Entry(master, textvariable=self.itm)
        polje_itm.grid(row = 3, column = 3)

#===============================================================================================================================================================

        self.sez_liste =[]

        self.stanje = StringVar(value = "Niste izpolnili vseh obveznih podatkov.")
        Label(master, fg="purple", font=('arial', 11, 'bold'), text =  "REZULTAT:").grid(row = 6, column = 0)
        napis_stanje = Label(master, textvariable = self.stanje)
        napis_stanje.grid(row = 6, column = 1, columnspan = 3)

#================================================================================================================================================================

    def izracunaj(self):
        self.itm.set(self.teza.get() / (self.visina.get() * self.visina.get()))    
        self.lista.insert(0, str(date.today()) + " ~ " + str(self.itm.get()) + "  [ " + str(self.teza.get()) + " kg ... " + str(self.visina.get()) + " m ]")
        self.sez_liste += [str(date.today()) + " ~ " + str(self.itm.get()) + "  [ " + str(self.teza.get()) + " kg ... " + str(self.visina.get()) + " m ]"]
        
        if self.a.get() == 1: # 1 so ženske 
            if self.itm.get() <= 18.4:
                self.stanje.set("prenizka telesna teža")
            elif self.itm.get() >= 18.5 and self.itm.get() <= 24.9:
                self.stanje.set("normalno")
            elif self.itm.get() >= 25 and self.itm.get() <= 29.9:
                self.stanje.set("prekomerna telesna teža")
            elif self.itm.get() >= 20:
                self.stanje.set( "debelost")
        elif self.a.get() == 2: # 2 so moški
            if self.itm.get() <= 17.9:
                self.stanje.set("prenizka telesna teža")
            elif self.itm.get() >= 18 and self.itm.get() <= 24.8:
                self.stanje.set("normalno")
            elif self.itm.get() >= 24.9 and self.itm.get() <= 29.2:
                self.stanje.set("prekomerna telesna teža")
            elif self.itm.get() >= 29.3:
                self.stanje.set("debelost")

#===============================================================================================================================================================

root = Tk()

aplikacija = ITM(root)
root.title("ITM kalkulator")
root.mainloop()
