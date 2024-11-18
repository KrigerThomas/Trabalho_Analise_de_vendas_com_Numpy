import numpy as np

# Caminho do arquivo recebido
file_path = 'C:/Users/alunolab12/Desktop/Trabalho - Analise de vendas com Numpy/vendas.csv'

# Visualizando o conteúdo inicial do arquivo para análise
with open(file_path, 'r', encoding='utf-8') as file:
    header = file.readline()  # Lendo o cabeçalho
    sample_data = [file.readline() for _ in range(5)]  # Lendo algumas linhas de exemplo

header, sample_data

# Carregando os dados do CSV em um array NumPy
# Configurando os tipos para cada coluna: Data (str), Região (str), Produto (str), Quantidade (float), Preço Unitário (float), Valor Total (float)
data_types = [('Data', 'U10'), ('Região', 'U10'), ('Produto', 'U20'), 
              ('Quantidade Vendida', 'f8'), ('Preço Unitário', 'f8'), ('Valor Total', 'f8')]

# Usando numpy.genfromtxt para carregar e converter os dados
sales_data = np.genfromtxt(file_path, delimiter=',', dtype=data_types, skip_header=1, encoding='utf-8')

# Visualizando os primeiros registros para verificar o processamento
sales_data[:5]
