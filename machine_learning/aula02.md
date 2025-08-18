# Machine Learning 

## Definição
O **aprendizado automático** é um subcampo da Engenharia e da Ciência da Computação que evoluiu do estudo de reconhecimento de padrões e da teoria do aprendizado computacional em inteligência artificial. Em 1959, **Arthur Samuel** definiu aprendizado de máquina como o  
> "campo de estudo que dá aos computadores a habilidade de aprender sem serem explicitamente programados".  

- [Fonte Britannica](https://www.britannica.com/technology/machine-learning)  
- [Livro de referência](https://books.google.com.br/books?id=Dn-Gdoh66sgC&pg=PA89&redir_esc=y#v=onepage&q&f=false)  
- [Wikipedia - Aprendizado de máquina](https://pt.wikipedia.org/wiki/Aprendizado_de_m%C3%A1quina)  

---

## Intuição com exemplo de frutas

Imagine que queremos adivinhar qual fruta uma pessoa vai comer.  

- Existem **7 frutas possíveis** → probabilidade inicial: `1/7`.  
- Recebemos dicas: *redonda, suculenta, vermelha, doce*.  
- O espaço amostral é reduzido para **2 frutas** → probabilidade agora: `1/2`.  
- Exemplo: probabilidade de ser **banana** com essas dicas = `0`.  

Isso é um exemplo de **probabilidade condicional**, onde o espaço amostral vai sendo **restringido** conforme novas informações chegam.

---

## Representação em tabela

| Arredondada | Suculenta | Vermelha | Doce | Fruta    |
|-------------|-----------|----------|------|----------|
| 0           | 1         | 1        | 1    | Morango  |
| 1           | 0         | 0        | 0    | Limão    |
| 1           | 1         | 0        | 1    | Pera     |
| 0           | 0         | 0        | 1    | Banana   |
| 1           | 1         | 1        | 1    | Cereja   |
| 1           | 1         | 1        | 0    | Tomate   |
| 1           | 1         | 1        | 1    | Maçã     |

- **Atributos (variáveis explicativas / independentes / covariáveis):**  
  arredondada, suculenta, vermelha, doce  

- **Alvo (variável dependente / resposta):**  
  fruta  

Os **algoritmos de ML** descobrem regras com base nesses exemplos. Eles só "conhecem" os objetos/eventos apresentados e trabalham com probabilidades associadas.

---

## Exemplo com cervejas 🍺

- **Tipos de cerveja (alvo):**  
  - Pale Ale  
  - Weissbier  
  - Pilsen  

- **Atributos (variáveis preditoras):**  
  - Temperatura  
  - Tipo de copo  
  - Espuma  
  - Cor
    
### Algoritmo: Árvore de Decisão 
- Funciona como uma sequência de **ifs**, mas gerada automaticamente.  
- O algoritmo vai particionando os dados em "nós" cada vez mais **puros** (ou seja, onde só resta um tipo de resposta).  
- Problema: se continuarmos dividindo até cada nó ter apenas **uma amostra**, caímos em **overfitting** (o modelo aprende demais os exemplos e não generaliza).  

---

## Observações importantes
- Nem todas as variáveis ajudam na classificação → só descobrimos testando modelos.  
- Quanto mais variáveis, mais chances de algumas serem úteis.  
- Para variáveis categóricas, podemos usar **teste qui-quadrado** para verificar associação entre variáveis.

---

## Resumo
- Machine Learning = ensinar o computador a **aprender padrões** e tomar decisões com base em dados.  
- Trabalha de forma **probabilística**.  
- Usa **atributos (entradas)** → para prever um **alvo (saída)**.  
- Risco de **overfitting** se o modelo aprender "demais".  
- Diferentes algoritmos existem para diferentes problemas (ex.: árvores de decisão, regressões, redes neurais, etc.).  
