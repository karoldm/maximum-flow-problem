import tkinter as tk
from tkinter import messagebox
from fordFulkerson import Graph

def criar_rede():
    try:
        quantidade_roteadores = int(entrada_quantidade.get())
        if quantidade_roteadores > 0:
            criar_matriz(quantidade_roteadores)
        else:
            messagebox.showerror("Erro", "Insira um valor maior que zero para a quantidade de roteadores.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

def criar_matriz(n):
    # Limpar widgets antigos (se existirem)
    for widget in matriz_frame.winfo_children():
        widget.destroy()

    rotulo_instrucao = tk.Label(matriz_frame, text="Insira na matriz de adjacência a largura de banda de cada cabo conectado aos roteadores:")
    rotulo_instrucao.grid(row=0, column=0, columnspan=n + 1, pady=10)

    # Criar rótulos para índices de coluna
    for j in range(n + 1):
        if j == 0:
            rotulo_coluna = tk.Label(matriz_frame, text="", width=5)
        else:
            rotulo_coluna = tk.Label(matriz_frame, text=str(j-1) + ".", width=5)
        rotulo_coluna.grid(row=1, column=j, padx=5, pady=5)

    # Criar uma matriz de entradas com rótulos de linha
    entradas_matriz = []
    for i in range(n):
        rotulo_linha = tk.Label(matriz_frame, text=str(i) + ".", padx=10)
        rotulo_linha.grid(row=i + 2, column=0, padx=5, pady=5)

        linha_entradas = []
        for j in range(n):
            entrada = tk.Entry(matriz_frame, width=5)
            entrada.insert(0, "0")
            entrada.grid(row=i + 2, column=j + 1, padx=5, pady=5)
            linha_entradas.append(entrada)
        entradas_matriz.append(linha_entradas)

    botao_run = tk.Button(matriz_frame, text="Calcular fluxo máximo", command=lambda: run(entradas_matriz))
    botao_run.grid(row=n + 2, columnspan=n + 1, pady=10)

def run(entradas_matriz):
    # Recuperar os valores da matriz
    valores_matriz = []
    for linha_entradas in entradas_matriz:
        linha_valores = []
        for entrada in linha_entradas:
            try:
                valor = int(entrada.get())
                if valor < 0:
                    raise ValueError("Insira valores inteiros acima de zero.")
                linha_valores.append(valor)
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira valores inteiros acima de zero.")
                return
        valores_matriz.append(linha_valores)

    graph = valores_matriz
    g = Graph(graph)
    source = 0; dest = int(entrada_quantidade.get())
      
    print ("The maximum possible flow is %d " % g.FordFulkerson(source, dest))

def init():
  # Criar a janela principal
  janela = tk.Tk()
  janela.title("Criador de Rede")

  # Criar widgets
  rotulo_quantidade = tk.Label(janela, text="Quantidade de Roteadores")
  entrada_quantidade = tk.Entry(janela, width=10)
  botao_criar_rede = tk.Button(janela, text="Criar Rede", command=criar_rede)

  # Organizar os widgets na janela
  rotulo_quantidade.pack(pady=10)
  entrada_quantidade.pack(pady=10)
  botao_criar_rede.pack(pady=10)

  # Definir o tamanho padrão da janela
  largura_padrao = 600
  altura_padrao = 550
  janela.geometry(f"{largura_padrao}x{altura_padrao}")

  # Frame para a matriz de entradas
  matriz_frame = tk.Frame(janela)
  matriz_frame.pack()

  # Iniciar o loop principal da janela
  janela.mainloop()
