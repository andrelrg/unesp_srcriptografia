from tkinter import *
from criptograpy import Criptograpy


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Programa de criptografia")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nameLabel = Label(self.segundoContainer,text="Texto", font=self.fontePadrao)
        self.nameLabel.pack(side=LEFT)

        self.text = Entry(self.segundoContainer)
        self.text["width"] = 70
        self.text["font"] = self.fontePadrao
        self.text.pack(side=LEFT)

        self.criptografar = Button(self.quartoContainer)
        self.criptografar["text"] = "Criptografar"
        self.criptografar["font"] = ("Calibri", "8")
        self.criptografar["width"] = 12
        self.criptografar["command"] = self.createCrypto
        self.criptografar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        self.cripted = False
  
    def createCrypto(self):
        text = self.text.get()
        if not hasattr("self", "c"):
            self.c = Criptograpy(text)
        if not self.cripted:
            cripted = self.c.create_hash()
            self.mensagem["text"] = cripted
            self.criptografar["text"] = "Descriptografar"
            self.cripted = True
        else:
            self.mensagem["text"] = self.c.decrypt(self.mensagem["text"])
            self.criptografar["text"] = "Criptografar"
            self.cripted = False
        