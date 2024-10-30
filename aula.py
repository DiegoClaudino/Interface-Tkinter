import tkinter as tk
from tkinter import ttk

# Função para buscar a cotação
def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f'Cotação do {moeda_preenchida} é de R$ {cotacao_moeda}'
    else:
        mensagem_cotacao["text"] = "Cotação não encontrada"

def buscar_cotacoes():
    texto = caixa_texto.get("1.0", tk.END)
    lista_moedas = texto.split('\n')
    mensagem_cotacoes = []
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item.strip())
        if cotacao:
            mensagem_cotacoes.append(f'{item.strip()}: R$ {cotacao}')
    mensagem4["text"] = '\n'.join(mensagem_cotacoes)

# Dicionário com as cotações
dicionario_cotacoes = {
    'Dólar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000
}

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cotação de Moedas")

# Mensagem de cabeçalho
mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2)

# Seleção de moeda
mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

moedas = list(dicionario_cotacoes.keys())
moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)

# Botão de busca de cotação
botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

# Mensagem para mostrar a cotação
mensagem_cotacao = tk.Label(text="")
mensagem_cotacao.grid(row=3, column=0, columnspan=2)

# Caixa de texto para múltiplas moedas
mensagem3 = tk.Label(text="Caso você queira pegar várias cotações, digite uma em cada linha:")
mensagem3.grid(row=4, column=0, columnspan=2)

caixa_texto = tk.Text(janela, width=30, height=5)
caixa_texto.grid(row=5, column=0, columnspan=2)

# Botão para buscar múltiplas cotações
botao_multiplas_cotacoes = tk.Button(text="Buscar Cotações", command=buscar_cotacoes)
botao_multiplas_cotacoes.grid(row=6, column=1)

# Mensagem para mostrar as cotações múltiplas
mensagem4 = tk.Label(text="")
mensagem4.grid(row=7, column=0, columnspan=2)

# Checkbox para receber promoções
var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(janela, text="Deseja receber e-mails promocionais?", variable=var_promocoes)
checkbox_promocoes.grid(row=8, column=0, columnspan=2)

# Botão para enviar
def enviar():
    print(var_promocoes.get())

botao_enviar = tk.Button(janela, text="Enviar", command=enviar)
botao_enviar.grid(row=9, column=0, columnspan=2)

# Executar a aplicação
janela.mainloop()
