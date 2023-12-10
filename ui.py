import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from fordFulkerson import Graph

def criar_rede():
    if hasattr(window, 'label_result'):
        window.label_result.destroy()

    try:
        routes_amount = int(input_amount.get())
        if routes_amount > 0:
            criar_matriz(routes_amount)
        else:
            messagebox.showerror("Erro", "Insira um valor maior que zero para a quantidade de roteadores.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

def criar_matriz(n):
    for widget in matriz_frame.winfo_children():
        widget.destroy()

    label_description = tk.Label(matriz_frame, text="Insira na matriz de adjacência a largura de banda de cada cabo conectado aos roteadores:")
    label_description.grid(row=0, column=0, columnspan=n + 1, pady=10)

    for j in range(n + 1):
        if j == 0:
            label_column = tk.Label(matriz_frame, text="", width=5)
        else:
            label_column = tk.Label(matriz_frame, text=str(j-1) + ".", width=5)
        label_column.grid(row=1, column=j, padx=5, pady=5)

    matrix_inputs = []
    for i in range(n):
        label_row = tk.Label(matriz_frame, text=str(i) + ".", padx=10)
        label_row.grid(row=i + 2, column=0, padx=5, pady=5)

        row_input = []
        for j in range(n):
            value = tk.Entry(matriz_frame, width=5)
            value.insert(0, "0")
            value.grid(row=i + 2, column=j + 1, padx=5, pady=5)
            row_input.append(value)
        matrix_inputs.append(row_input)

    botao_run = ttk.Button(matriz_frame, text="Calcular fluxo máximo", command=lambda: run(matrix_inputs))
    botao_run.grid(row=n + 2, columnspan=n + 1, pady=10)

def run(matrix_inputs):
    matrix_values = []
    for row_input in matrix_inputs:
        row_values = []
        for entrada in row_input:
            try:
                value = int(entrada.get())
                if value < 0:
                    raise ValueError("Insira valores inteiros acima de zero.")
                row_values.append(value)
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira valores inteiros acima de zero.")
                return
        matrix_values.append(row_values)

    graph = matrix_values
    
    # to test
    # graph = [[0, 11, 12, 0, 0, 0], 
    #          [0, 0, 0, 12, 0, 0], 
    #          [0, 1, 0, 0, 11, 0], 
    #          [0, 0, 0, 0, 0, 19], 
    #          [0, 0, 0, 7, 0, 4],
    #          [0, 0, 0, 0, 0, 0]]
    # result is 23

    # to test
    # graph = [[0, 8, 0, 0, 3, 0],
    #         [0, 0, 9, 0, 0, 0],
    #         [0, 0, 0, 0, 7, 2],
    #         [0, 0, 0, 0, 0, 5],
    #         [0, 0, 7, 4, 0, 0],
    #         [0, 0, 0, 0, 0, 0]]
    # result is 6

    g = Graph(graph)
    source = 0; dest = int(input_amount.get())-1
    result = "O fluxo máximo é %d " % g.FordFulkerson(source, dest)

    if hasattr(window, 'label_result'):
        window.label_result.destroy()

    window.label_result = tk.Label(window, text=result)
    window.label_result.pack(pady=10)


window = tk.Tk()
window.title("Problema do Fluxo Máximo")

style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', foreground='white', background='#fcba03', font=('poppins', 12))

label_amount = tk.Label(window, text="Quantidade de Roteadores")
input_amount = tk.Entry(window, width=10)
create_network_button = ttk.Button(window, text="Criar Rede", command=criar_rede)

label_amount.pack(pady=10)
input_amount.pack(pady=10)
create_network_button.pack(pady=10)

width = 600
height = 500
window.geometry(f"{width}x{height}")

matriz_frame = tk.Frame(window)
matriz_frame.pack()

window.mainloop()
