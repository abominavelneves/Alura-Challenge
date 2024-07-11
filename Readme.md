## 7DaysofCode - Desafio da Alura
Nesse desafio de uma semana a Alura disponibilizou dados dos empréstimos da biblioteca da UFRN desde o primeiro semestre de 2010 até o primeiro semestre de 2020. A ideia do desafio é fazer uma análise destes dados usando Python para tirar insigths para melhorias da biblioteca. A cada dia foi dado um novo desafio para encontrar novas interpretações dos dados.
### Day One
No primeiro dia, foram realizadas pequenas modificações nos dados da UFRN. Nessa etapa inicial, as tabelas de cada semestre foram organizadas em um Data Frame junto com a identificação dos exemplares.
```python
#Criando uma lista com todos os csv files

file_path='D:/Projects1/7Days_of_Code/Data_Set/'
emprestimos = os.listdir(file_path)
emprestimos=emprestimos[1:len(emprestimos)-1]
files = [file_path + str(elemento) for elemento in emprestimos]

#Colocando todos os dados de emprestimo em um único DataFrame

data_set=pd.DataFrame()
data_set= pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
data_set.drop_duplicates(inplace=True)

#Com os exemplares convertido em csv é possível mesclar os dois

exemplares=pd.DataFrame()
exemplares=pd.read_csv('D:/Projects1/7Days_of_Code/dados_exemplares.csv')
dados=data_set.merge(exemplares)
```
### Desafio do Dia 2
No Dia 2 foram feitas as primeiras alterações para facilitar a análise dos exemplares da faculdade. Aqui foi separado em categorias cada um dos livros, para isso foi feita uma função para achar a localização do livro e substituir pela categoria equivalente.
```python
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

```
Com essa função ficou mais fácil de encontrar e classificar corretamente a categoria de cada livro da biblioteca.
```python
dados['categoria']='Categoria'
dados['categoria']=dados['localizacao'].apply(classifica)
```
### Desafio do Dia 3
No dia 3 o desafio foi descobrir o comportamneto dos empréstimos no decorrer dos anos para saber se houve um aumento ou uma redução no número de empréstimos. Para visualizar melhor este comportamento entre o primeiro semestre de 2010 e o primeiro semestre de 2020 foi utilizada a biblioteca Matplotlib.
```python
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
```
De forma similar a essa primeira parte foi realizado a mesma análise para os meses no mesmo período.
```python
dados['mes_emprestimo']=dados['data_emprestimo'].dt.month
emprestimos_mensais=dados['mes_emprestimo'].value_counts().sort_index()
plt.bar(emprestimos_mensais.index,emprestimos_mensais.values,color='skyblue')
plt.title('Empréstimos Mensais da UFRN')
plt.xlabel('Meses')
plt.ylabel('Número de Empréstimos')
plt.xticks(emprestimos_mensais.index, rotation=45)
plt.tight_layout()
plt.show()
```
<img src="D:/Projects1/7Days_of_Code/Data_Set/emprestimos_anuais.png">