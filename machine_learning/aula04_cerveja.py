# %% importando biblioteca 
import pandas as pd

# %% carregando o arquivo com os dados da cerveja
df = pd.read_excel("data/dados_Cerveja.xlsx")
# exibindo as primeiras linhas do df para inspeção
df.head()

# %% definindo as características (features) e a variável resposta (target)

# características (variáveis independentes) utilizadas para prever a classe da cerveja
features = ['temperatura', 'copo', 'espuma', 'cor']

# variável resposta (target) que queremos prever: a classe da cerveja
target = 'classe'

# separando as características (X) e a variável resposta (y)
X = df[features]
y = df[target]

# %% ajustando o modelo de Árvore de Decisão

# importando o modelo de árvore de decisão do scikit-learn
from sklearn import tree

# explicação do que é um modelo:
# um modelo é como um padrão que você ajusta de acordo com os dados
# -> após o ajuste, ele pode ser usado para prever outras instâncias (novos dados)
# no caso da Árvore de Decisão, estamos ajustando um modelo baseado em características (X) para prever a classe (y)

# como o X possui variáveis não numéricas, vamos convertê-las para números
# isso é feito criando variáveis dummy -> substituímos as variáveis textuais por números

# transformando variáveis categóricas em variáveis numéricas
X = X.replace({
    "mud": 1, "pint": 2,  
    "sim": 1, "não": 0,   
    "clara": 0, "escura": 1,  
})

# criando e ajustando o modelo 
model = tree.DecisionTreeClassifier()  
model.fit(X=X, y=y) 

# %% visualizando a árvore de decisão

# importando o matplotlib para visualização
import matplotlib.pyplot as plt

# configurando o gráfico
plt.figure(dpi=400)

# plotando a árvore de decisão
tree.plot_tree(model,
               feature_names=features,  
               class_names=model.classes_,  
               filled=True 
               )
