from tkinter import*
from tkinter import ttk, messagebox
class Aplicacion():
    __ventana= None
    __precio_unitario= None
    __iva= None
    __precio_con_iva= None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('290x115')
        self.__ventana.title("Calculo de IVA")
        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5")
        mainframe.grid(row=0, column=0, sticky=(N,W,E,S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__precio_unitario = StringVar()
        self.__precio_con_iva = StringVar()
        self.__iva = StringVar()
        self.__precio_unitario.trace('w', self.__precio_unitario)
        self.__iva.trace('w', self.__iva)
        self.__precio_unitario_entry = ttk.Entry(mainframe, width=7, textvariable= self.__precio_unitario)
        self.__precio_unitario_entry.grid(row= 1, column= 2, sticky= E)
        self.__iva_entry = ttk.Entry(mainframe, width=7, textvariable= self.__iva)
        self.__iva_entry.grid(row= 4, column= 2, sticky= E)
        self.__precio_con_iva_entry = ttk.Entry(mainframe, width=7, textvariable= self.__precio_con_iva)
        self.__precio_con_iva_entry.grid(row= 5, column= 2, sticky= E)
        ttk.Label(mainframe, textvariable= self.__precio_unitario).grid(row=1, column= 0, sticky= (W,E))
        ttk.Radiobutton(mainframe, text='IVA 21%', value=0, variable=self.__iva, command= self.calcular).grid(row=2, column=0, columnspan=1, sticky=W)
        ttk.Radiobutton(mainframe, text='IVA 10.5', value=0, variable=self.__iva, command= self.calcular).grid(row=3, column=0, columnspan=1, sticky=W)
        ttk.Label(mainframe, textvariable= self.__iva).grid(row= 4, column=0, sticky=(W,E))
        ttk.Label(mainframe, textvariable=self.__precio_con_iva).grid(row=5, column=0, sticky=(W,E))
        ttk.Button(mainframe, text='Calcular', command=self.calcular).grid(row=6, column=0, sticky= W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(row=6, column=2, sticky=E)
        ttk.Label(mainframe, text='Precio sin IVA').grid(row=1, column=0, sticky=W)
        ttk.Label(mainframe, text='IVA').grid(row=4, column=0, sticky=W)
        ttk.Label(mainframe, text='Precio con IVA').grid(row=5, column=0, sticky=W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
            self.__iva_entry.focus()
            self.__precio_unitario_entry.focus()
            self.__ventana.mainloop()

    def calcular(self):
        try:
            valor= float(self.__precio_unitario_entry.get())
            valor_iva = float(self.__iva_entry.get())
            if valor_iva == 10.5:
                self.__precio_con_iva.set(valor* 10.5//100)
            elif valor_iva == 21:
                self.__precio_con_iva.set(valor* 21//100)
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar un digito valido')
            self.__precio_unitario_entry.focus()
            self.__iva_entry.focus()
            self.__precio_con_iva_entry.focus()

