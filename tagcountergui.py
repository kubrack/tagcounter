
import tkinter
from tkinter import ttk
import aliases
import tagcounterlib as tlib
from tagcounterdb import DB
import logging

aliases = aliases.AliasDB()

class TagCounterGui(tkinter.Frame):
    def __init__(self, master=tkinter.Tk()):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.logger = logging.getLogger('tagcounter')

    def create_widgets(self):
        self.t1 = tkinter.Label(self, text = 'Please select URI alias: ')
        self.t1.pack(side="top")

        self.aliases = tkinter.ttk.Combobox(self, width = 20)
        self.aliases['values'] = aliases.list()
        self.aliases.pack(side="top")

        self.bt_select = tkinter.Button(self, text = 'Select')
        self.bt_select["command"] = lambda: self.uri_text.set(aliases.get(self.aliases.get()))
        self.bt_select.pack(side="top")

        self.t2 = tkinter.Label(self, text = 'or enter URI here: ')
        self.t2.pack(side="top")

        self.uri_text = tkinter.StringVar()
        self.uri = tkinter.Entry(self, textvariable = self.uri_text, width = 20)
        self.uri.pack(side="top")

        self.bt_load = tkinter.Button(self, text = 'Load')
        self.bt_load["command"] = self.load
        self.bt_load.pack(side="top")

        self.bt_get = tkinter.Button(self, text = 'Get from DB')
        self.bt_get["command"] = self.get_from_db
        self.bt_get.pack(side="top")

        self.l_result_text = tkinter.StringVar()
        self.l_result = tkinter.Message(self, textvariable = self.l_result_text, width=400, aspect=1000)
        self.l_result.pack(side="top")

    def load(self):
        uri = self.uri.get()
        if not uri: return
        try:
            c = tlib.process_uri(uri)
            DB.set(uri, c)
            self.logger.info(uri)
            self.l_result_text.set('uri ' + uri + ' ' + str(c))
        except Exception as err:
            self.l_result_text.set('Error processing "'+ uri +'": '+ str(err))
    
    def get_from_db(self):
        uri = self.uri.get()
        if not uri: return
        c = DB.get(uri)
        self.l_result_text.set('db ' + uri + ' ' + str(c))
    
