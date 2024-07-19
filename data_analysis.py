import os
import glob
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

#Criando uma lista com todos os csv files

file_path='C:/Users/Corrigirerro/OneDrive/Área de Trabalho/Project/'
arquivo_csv=[]
arquivos=os.listdir(file_path)
for arquivo in arquivos:
    if arquivo.endswith('.csv'):
        if arquivo!='dados_exemplares.csv':
            arquivo_csv.append(file_path+arquivo)

#Colocando todos os dados de emprestimo em um único DataFrame

data_set=pd.DataFrame()
data_set= pd.concat([pd.read_csv(f) for f in arquivo_csv], ignore_index=True)
data_set.drop_duplicates(inplace=True)

#Com os exemplares convertido em csv é possível mesclar os dois

exemplares=pd.DataFrame()
exemplares=pd.read_csv(file_path + 'dados_exemplares.csv')
dados=data_set.merge(exemplares)

#Criando uma função que classifica as categorias

def classifica(tag):
    if tag>=0 and tag<=99:
        return 'Generalidades'
    elif tag>=100 and tag<=199:
        return 'Filosofia e psicologia'
    elif tag>=100 and tag<=199:
        return 'Religião'
    elif tag>=100 and tag<=199:
        return 'Ciências sociais'
    elif tag>=100 and tag<=199:
        return 'Classe vaga'
    elif tag>=100 and tag<=199:
        return 'Matemática e ciências naturais'
    elif tag>=100 and tag<=199:
        return 'Ciências aplicadas'
    elif tag>=100 and tag<=199:
        return 'Belas artes'
    elif tag>=100 and tag<=199:
        return 'Linguagem. Língua. Linguística'
    else:
        return 'Geografia. Biografia. História'

#Classificando em tipos os livros usando o sistemas cdu

dados['categoria']='Categoria'
dados['categoria']=dados['localizacao'].apply(classifica)

#Os itens da coluna matricula_ou_siape não estão formataddos para string 
##Função para facilitar a conversão

def converte(num):
    return str(num)
dados['matricula_ou_siape']=dados['matricula_ou_siape'].apply(converte)

#Emprestimos por ano

dados['data_emprestimo']=pd.to_datetime(dados['data_emprestimo'])
dados['ano_emprestimo']=dados['data_emprestimo'].dt.year

#Filtrando e analisando o comportamento dos empréstimos

emprestimos_por_ano = dados['ano_emprestimo'].value_counts().sort_index()
plt.bar(emprestimos_por_ano.index, emprestimos_por_ano.values, color='skyblue')
plt.title('Emprétimos por Ano da UFRN')
plt.xlabel('Ano de Empréstimo')
plt.ylabel('Número de Empréstimos')
plt.xticks(emprestimos_por_ano.index, rotation=0)
plt.tight_layout()
plt.show()

#Descobrindo sobre o número de empréstimos mensais
## Usando seaborn para fazer um gráfico de linhas
dados['mes_emprestimo']=dados['data_emprestimo'].dt.month
emprestimos_mensais=dados['mes_emprestimo'].value_counts().sort_index()
plt.bar(emprestimos_mensais.index,emprestimos_mensais.values,color='skyblue')
plt.title('Empréstimos Mensais da UFRN')
plt.xlabel('Meses')
plt.ylabel('Número de Empréstimos')
plt.xticks(emprestimos_mensais.index, rotation=45)
plt.tight_layout()
plt.show()

#Descobrindo sobre os horários mais movimentados do dia
dados['hora_do_emprestimo']=dados['data_emprestimo'].dt.hour
horario=dados['hora_do_emprestimo'].value_counts().sort_index()
plt.bar(horario.index,horario.values, color='skyblue')
plt.title('Fluxo')
plt.xlabel('Horário')
plt.ylabel('Número de Empréstimos')
plt.tight_layout()
plt.show()