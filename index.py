import numpy as np
from datetime import datetime

# 1. Leitura e preparação dos dados:

# Caminho do arquivo recebido
file_path = 'D:/Vscode/Python/Trabalho_Analise_de_vendas_com_Numpy-main/vendas.csv'

# Carregando os dados do CSV em um array NumPy
# Configurando os tipos para cada coluna: Data (str), Região (str), Produto (str), Quantidade (float), Preço Unitário (float), Valor Total (float)
data_types = [('Data', 'U10'), ('Região', 'U10'), ('Produto', 'U20'), 
              ('Quantidade Vendida', 'f8'), ('Preço Unitário', 'f8'), ('Valor Total', 'f8')]

# Usando numpy.genfromtxt para carregar e converter os dados
sales_data = np.genfromtxt(file_path, delimiter=',', dtype=data_types, skip_header=1, encoding='utf-8')

# Recalculando o valor total (se necessário, para evitar inconsistências)
sales_data['Valor_Total'] = sales_data['Quantidade_Vendida'] * sales_data['Preço_Unitário']

# Visualizando os primeiros registros para verificar o processamento
sales_data[:5]


# 2. Análise Estatística:
 
#Estatísticas básicas do "Valor Total"
valor_total = sales_data['Valor_Total']

# Calculando a média, mediana e desvio padrão do "Valor Total"
media_valor_total = np.mean(valor_total) #.mean calcula a média
mediana_valor_total = np.median(valor_total) #.median retorna a mediana
desvio_valor_total = np.std(valor_total) #.std = standard deviation (retorna o desvio padrão)

print(f"Média do Valor Total: {media_valor_total}")
print(f"Mediana do Valor Total: {mediana_valor_total}")
print(f"Desvio Padrão do Valor Total: {desvio_valor_total}")

# Produto com maior quantidade vendida e maior valor total
produtos, soma_quantidade = np.unique(sales_data['Produto'], return_counts=True)

# Produto mais vendido
idx_mais_vendido = soma_quantidade.argmax()
produto_mais_vendido = produtos[idx_mais_vendido]
print(f"Produto mais vendido: {produto_mais_vendido} (Quantidade: {soma_quantidade[idx_mais_vendido]})")

# Produto com maior valor total de vendas
produto_valor_total = {produto: sales_data['Valor_Total'][sales_data['Produto'] == produto].sum() for produto in produtos}
produto_maior_valor = max(produto_valor_total, key=produto_valor_total.get)
print(f"Produto com maior valor total: {produto_maior_valor} (Valor Total: {produto_valor_total[produto_maior_valor]:.2f})")



# 3. Análise Temporal:

# Convertendo as datas para o formato datetime
datas = np.array([datetime.strptime(data, '%Y-%m-%d') for data in sales_data['Data']])

# Adicionando dia da semana
dias_semana = np.array([data.strftime('%A') for data in datas])

# Encontrando o dia da semana com mais vendas
dias_unicos, contagem_dias = np.unique(dias_semana, return_counts=True)
dia_mais_vendido_idx = contagem_dias.argmax()
dia_mais_vendas = dias_unicos[dia_mais_vendido_idx]
print(f"Dia da semana com mais vendas: {dia_mais_vendas} (Total de vendas: {contagem_dias[dia_mais_vendido_idx]})")

# Cálculo da variação diária do valor total
vendas_por_dia = {data: valor_total[sales_data['Data'] == data].sum() for data in np.unique(sales_data['Data'])}
datas_ordenadas = sorted(vendas_por_dia.keys())
variacao_diaria = np.diff([vendas_por_dia[data] for data in datas_ordenadas])

print(f"Variação diária no valor total de vendas: {variacao_diaria}")
