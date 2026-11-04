from tkinter import * # Importando o tktinter

class Application:
    # define que a janela não tem um pai especifico
    #associado a janela padrão (root)
    def __init__(self, master = None):
        self.widget1 = Frame(master)
        self.widget1["bg"] = ("blue")
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro Widget")
        self.msg["fg"] = ("white")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg["bg"] = ("blue")
        self.msg.pack()
        self.sair = Button(self.widget1, bg = "lightblue")
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack()

    def mudarTexto(self, event):
        if self.msg["text"] == "Primeiro Widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro Widget"
        
root = Tk()
root.geometry("680x400")
root["bg"] = "blue"
Application(root)
root = mainloop()