## Projeto House Rocket Sales

![image](https://queroficarrico.com/blog/wp-content/uploads/2014/01/imoveis-mercado-imobiliario.jpg)

### Projeto pessoal de análise de dados  para uma empresa do setor imobiliário
### Prestando serviços para House Rocket Sales
A empresa House Rocket é uma instituição totalmente fictícia, que tem como principal ramo de negócio compra e venda de imóveis, sua forma de lucar é através de compras de imóveis abaixo do valor médio de mercado, e revendê-los.

Dentro desse contexto apresentado, existe uma série de desafios que o time de negócio precisa resolver, esses fatores interferem diretamente no lucro da empresa, pois a empresa precisa prospectar a compra de imóveis que esteja em custo baixo e garantir que a venda tenha alta rentabilidade. Para resolver essas questões, o CEO da House Rocket me contratou para ajuda-los na tomada de decisões, pois o objetivo dele é responder as principais perguntas de negócio que são:

-  Quais casas a House Rocket deveria comprar e por qual preço de compra?
- Uma vez a casa em posse da empresa, qual o melhor momento para vendê-las e qual seria o preço da venda?
Partir desse problema de negócio  vou planejar a melhor solução e através da análise exploratória dos dados (EDA), e isso vai me permitir gerar os insights que serão transformados em informação para o CEO e essas informações poderam serem observadas serão disponibilizadas ao CEO e suas equipes por meio de um dashboard web.




Para realizaçao do projeto o dataset utilizado foi coletado do Kaggle: <https://www.kaggle.com/datasets/harlfoxem/housesalesprediction>

As ferramentas utilizada para todo o projeto foram: 

- Tratamento dos dados e análise de dados [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
- Desenvolvimento do dashboard - Streamlit 
- Serviço em cloud de hospedagem do dashboard [![forthebadge made-with-python](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://www.heroku.com/)

Nesse conjunto de dados está listadas as casas a venda em King County - USA, entre os anos de 2014 e 2015 cada atributo 
representa uma coluna da base de dados

|    Atributos    |                         Definição                            |
| :-------------: | :----------------------------------------------------------: |
|       id        |       Numeração única de identificação de cada imóvel        |
|      date       |                    Data da venda do imóvel                   |
|      price      |         Preço que o imóvel foi colocado a venda                   |
|    bedrooms     |                      Número de quartos                       |
|    bathrooms    | Número de banheiros (0.5 = banheiro sem chuveiro)            |
|   sqft_living   | Medida (em pés quadrado) do espaço interior dos apartamentos |
|    sqft_lot     |     Medida (em pés quadrado) quadrada do espaço terrestre     |
|     floors      |                 Número de andares do imóvel                  |
|   waterfront    | Variável que indica a presença ou não de vista para água (0 = não e 1 = sim) |
|      view       | Um índice de 0 a 4 que indica a qualidade da vista da propriedade. Varia de 0 a 4, onde: 0 = baixa  4 = alta |
|    condition    | Um índice de 1 a 5 que indica a condição da casa. Varia de 1 a 5, onde: 1 = baixo \|-\| 5 = alta |
|      grade      | Um índice de 1 a 13 que indica a construção e o design do edifício. Varia de 1 a 13, onde: 1-3 = baixo, 7 = médio e 11-13 = alta |
|  sqft_basement  | A metragem quadrada do espaço habitacional interior acima do nível do solo |
|    yr_built     |               Ano de construção de cada imóvel               |
|  yr_renovated   |                Ano de reforma de cada imóvel                 |
|     zipcode     |                         CEP da casa                          |
|       lat       |                           Latitude                           |
|      long       |                          Longitude                           |
| sqft_livining15 | Medida (em pés quadrado) do espaço interno de habitação para os 15 vizinhos mais próximo |
|   sqft_lot15    | Medida (em pés quadrado) dos lotes de terra dos 15 vizinhos mais próximo |



# Planejamento da Solução.

1 - Coleta dos dados em seu local de origem (Kaggle)

2 - Entendimento do negócio

3 - Limpeza e tratamento do DF
    
      Checagem de outliers impactantes no resultado final
      Transformação de variáveis que apresentavam o tipo errado
      Limpeza de valores vazios NaN dentro da base
      Limpeza de valores duplicados

4 - Análise exploratória dos dados

5 - Criação de hipóteses para extração de insights para o negócio

6 - Criação do web app com dashboards de auxílio a tomada de decisão da companhia

7 - Conclusão

       Resultado financeiro do projeto
       Considerações finais
       




