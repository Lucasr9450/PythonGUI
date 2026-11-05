import tkinter as tk

def digitar(numero):
    visor.insert(tk.END, numero)
    
def limpar():
    visor.delete(0, tk.END)
    
def retirar():
    visor.delete(len(visor.get()) - 1, tk.END)
    
janela = tk.Tk()
janela.title("Calculadora")

visor = tk.Entry(janela, width=35, justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=6, pady=6, ipady=8)

botao_c = tk.Button(janela, text="C", width=6, height=2, command=limpar)
botao_c.grid(row=1, column=0, padx=2, pady=2)

botao_r = tk.Button(janela, text="<--", width=6, height=2, command=retirar)
botao_r.grid(row=1, column=1, padx=2, pady=2)

botao_di = tk.Button(janela, text="÷", width=6, height=2)
botao_di.grid(row=1, column=2, padx=2, pady=2)

botao_mu = tk.Button(janela, text="x", width=6, height=2)
botao_mu.grid(row=1, column=3, padx=2, pady=2)

botao_7 = tk.Button(janela, text="1", width=6, height=2, command=lambda: digitar("7"))
botao_7.grid(row=2, column=0, padx=2, pady=2)

botao_8 = tk.Button(janela, text="2", width=6, height=2, command=lambda: digitar("8"))
botao_8.grid(row=2, column=1, padx=2, pady=2)

botao_9 = tk.Button(janela, text="3", width=6, height=2, command=lambda: digitar("9"))
botao_9.grid(row=2, column=2, padx=2, pady=2)

botao_me = tk.Button(janela, text="-", width=6,  height=2)
botao_me.grid(row=2, column=3, padx=2, pady=2)

botao_4 = tk.Button(janela, text="4", width=6, height=2, command=lambda: digitar("4"))
botao_4.grid(row=3, column=0, padx=2, pady=2)

botao_5 = tk.Button(janela, text="5", width=6, height=2, command=lambda: digitar("5"))
botao_5.grid(row=3, column=1, padx=2, pady=2)

botao_6 = tk.Button(janela, text="6", width=6, height=2, command=lambda: digitar("6"))
botao_6.grid(row=3, column=2, padx=2, pady=2)

botao_ma = tk.Button(janela, text="+", width=6, height=2)
botao_ma.grid(row=3, column=3, padx=2, pady=2)

botao_1 = tk.Button(janela, text="7", width=6, height=2, command=lambda: digitar("1"))
botao_1.grid(row=4, column=0, padx=2, pady=2)

botao_2 = tk.Button(janela, text="8", width=6, height=2, command=lambda: digitar("2"))
botao_2.grid(row=4, column=1, padx=2, pady=2)

botao_3 = tk.Button(janela, text="9", width=6, height=2, command=lambda: digitar("3"))
botao_3.grid(row=4, column=2, padx=2, pady=2)

botao_0 = tk.Button(janela, text="0", width=14, height=2, command=lambda: digitar("0"))
botao_0.grid(row=5, column=0, columnspan=2, padx=2, pady=2)

botao_p = tk.Button(janela, text=".", width=6, height=2, command=lambda: digitar("."))
botao_p.grid(row=5, column=2, padx=2, pady=2)

botao_ig = tk.Button(janela, text="=", width=6, height=5, command=limpar )
botao_ig.grid(row=4, column=3, rowspan=2, padx=2, pady=2)

janela.mainloop()