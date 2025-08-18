# %% biblioteca
import pandas as pd

# %% carregando o arquivo com os dados das frutas
df = pd.read_excel("data/dados_frutas.xlsx")

# %% importando o módulo de árvores de decisão do scikit-learn
from sklearn import tree

# definindo o modelo de árvore de decisão
arvore = tree.DecisionTreeClassifier(random_state=42) 
# a semente random_state=42 garante que o modelo seja reproduzível -> qualquer pessoa rodando o código com a mesma configuração obterá o mesmo resultado

# definindo a variável resposta (y) e as características (X)
y = df["Fruta"]  # variável resposta (o que queremos prever)

# características que serão usadas para prever a fruta
caracteristicas = ["Arredondada", "Suculenta", "Vermelha", "Doce"]
X = df[caracteristicas]  # dados de entrada (características das frutas)

# %% treinando o modelo de árvore de decisão
# o modelo vai aprender a partir dos dados de X e y
arvore.fit(X, y)

# %% realizando uma previsão com um novo conjunto de características
# previsão para uma fruta com características [0, 0, 0, 0]
predicao = arvore.predict([[0, 0, 0, 0]])

# %% visualizando a árvore de decisão gerada pelo modelo
import matplotlib.pyplot as plt

# configurando o gráfico para melhor visualização
plt.figure(dpi=400, figsize=[4, 4])

# plotando a árvore de decisão
tree.plot_tree(arvore,
               feature_names=caracteristicas,  # nomes das características
               class_names=arvore.classes_,    # nomes das classes (tipos de frutas)
               filled=True)                    # colorir os nós de acordo com a classe predominante

# %% calculando a probabilidade de cada classe para uma nova entrada
# probabilidade de cada classe (fruta) para as características [1, 1, 1, 1]
proba = arvore.predict_proba([[1, 1, 1, 1]])[0]

# exibindo as probabilidades de cada classe
pd.Series(proba, index=arvore.classes_)
