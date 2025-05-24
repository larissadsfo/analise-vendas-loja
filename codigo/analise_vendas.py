import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Gerar base de dados fictícia
np.random.seed(0)
data = {
    'Data': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Produto': np.random.choice(['Camisa', 'Calça', 'Sapato', 'Bolsa'], size=100),
    'Quantidade': np.random.randint(1, 5, size=100),
    'Preço Unitário': np.random.uniform(50, 200, size=100).round(2)
}
df = pd.DataFrame(data)
df['Total'] = df['Quantidade'] * df['Preço Unitário']

# Exibir primeiras linhas
print("\nPrimeiras entradas:")
print(df.head())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(df.describe())

# Produtos mais vendidos
print("\nQuantidade de vendas por produto:")
print(df['Produto'].value_counts())

# Receita total por produto
print("\nReceita total por produto:")
print(df.groupby('Produto')['Total'].sum())

# Visualização: Receita por Produto
plt.figure(figsize=(8, 5))
sns.barplot(x='Produto', y='Total', data=df, estimator=sum, ci=None)
plt.title('Receita por Produto')
plt.ylabel('Receita Total (R$)')
plt.xlabel('Produto')
plt.tight_layout()
plt.savefig('imagens/receita_por_produto.png')
plt.show()
