import tkinter as tk

def somar():
    n1 = float(entrada1.get())
    n2 = float(entrada2.get())
    
    resultado = n1 + n2
    
    lbl_resultado.config(text=f"Resultado: {resultado}")

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("350x250")

lbl_numero1 = tk.Label(janela, text = "Primeiro número:")
lbl_numero1.pack()

entrada1 = tk.Entry(janela)
entrada1.pack()

lbl_numero2 = tk.Label(janela, text = "Segundo número:")
lbl_numero2.pack()

entrada2 = tk.Entry(janela)
entrada2.pack()

botao_somar = tk.Button(
    janela,
    text="Somar",
    command=somar
)
botao_somar.pack(pady=15)

lbl_resultado = tk.Label(janela, text="Resultado: ")
lbl_resultado.pack()

janela.mainloop()