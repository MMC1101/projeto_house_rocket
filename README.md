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

- Tratamento dos dados e análise de dados[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
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

![portfolio_AdobeExpress](https://user-images.githubusercontent.com/65685947/196809179-3b7b355e-9c16-464e-b0a1-078c2a4becb8.gif)

7 - Conclusão

       Resultado financeiro do projeto
       Considerações finais
       


# Insights gerados ao final da Análise e Tomada decisões que podem serem realizadas 


### Hipótese_1 - Imóveis com vista para água são mais valorizados em mais de  130 % 

Falso: A valorização é muito maior em torno de 212% dos imóveis com vista para água comparados ao imóveis sem vista, concluído que é bastante rentável comprar imóveis com vista para água

![insights_1](https://user-images.githubusercontent.com/65685947/193933833-46600c31-a0fa-4d56-9d50-cfaaabf2bfd4.png)

### Hipótese_2 Imóveis com mais de 2 pisos são mais valorizados em 20 % em relação os imóveis com únicos piso

Falso: Imóveis com mais de 2 pisos não tem o dobro de valorização comparado aos imóveis que só tem único pisco 
imóveis com maios de 2 pisos possui valorização média de 39% comparado aos imóveis com único piso

![insights_2](https://user-images.githubusercontent.com/65685947/193936235-a544d0a6-6534-4774-9f61-f5fadaf25f43.png)


### Hipótese_3 Imóveis novos sem reforma são 20% mais caros que imóveis velhos reformados
Falso: Os imóveis novos sem reforma são 10% mais baratos que os imóveis velhos reformados , assim no momento de compra da House Rocket priorizar imóveis novos sem reforma

![insights_3](https://user-images.githubusercontent.com/65685947/193936835-3d67e3dc-b956-4de9-8b17-d5afb06f2f74.png)


### H4 - Imóveis com 3 ou mais Banheiros tem lucro de 50% a mais que imóveis que tem menos de 3 banheiros
Falso: Os imóveis com 3 ou mais Banheiros , são em torno de 25% mais lucrativo em média em comparação com imóveis que tem menos de 3 banheiros

![insights_7](https://user-images.githubusercontent.com/65685947/194678186-9ea15fe7-683e-4a6e-8cd7-62d069ad8c9e.png)


### H5 A estação do verão tem em média de lucro em 30% a mais em relação a todas outras estações 
Falso: A estação de verão tem em média lucro de 3% a mais em relação a todas outras estações

![ìnsights_5](https://user-images.githubusercontent.com/65685947/194676845-c997cdf8-4f47-4975-940f-35767ac1a914.png)


| **Insights**                                                   | **Aplicação na tomada de decisão de negócio**                                                  | 
| ------------------------------------------------------------ |  ------------------------------------------------------------ |
| **1** - Imóveis com vista para água são valorizados em mais de 212% | Realizar compras de imóveis com vista para água                      |
| **2** -  imóveis com mais de 2 pisos possui valorização média de 39% comparado aos imóveis com único piso | Comprar imóveis com pelo menos dois pisos, ou comprar imóvel com único banheiro e dependendo da condição do imóvel adicionar um banheiro  porque irá valorizar em 39 % na venda|
| **3** - Imóveis novos sem reforma são 10% mais baratos que imóveis antigos reformados | Realizar compra de imóveis novos diminui os gastos com reforma e se mantém valorizando                      |
| **4** - Imóveis com 3 ou mais banheiros são 25% mais lucrativo em comparação com imóveis que tem menos de 3 banheiros| Investir na compra de imóveis que tem 3 ou mais  banheiros|
| **5** - A estação de verão tem em média lucro de 3% a mais em relação a todas outras estaçõe | Investir na venda de imóveis no período do verão ou no período da primavera  

# Dashboard solicitado pelo CEO Preview.

https://user-images.githubusercontent.com/65685947/196807775-9fc63ba7-38e0-4907-af6d-ef960ef95ac7.mp4



