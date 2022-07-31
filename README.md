# Project KC House - Insights

### This project is an insight study based on public real estate data from KC House provided by Kaggle. The project is not intended to propose solutions for the company, being only an object of demonstration of analytical skills.

<p align="center">
  <img src="images/wall.jfif"/>
</p>

## Understanding Business Questions 
KC is a real estate sales company where its profit is in the arbitrage of the purchase, that is, 
in buying real estate for a value 'x' and selling it later for a higher value. However, the CEO had 
a question, given a portfolio of properties, from which they should be purchased and, once purchased, 
when should the sale be carried out in order to guarantee a profit. 

**Questions:**

The CEO of KC House held a meeting and the company's metrics were discussed. The CEO's requests are:

1 - Which property should be purchased and for what value?

2 - Once purchased, when is the best period to sell?


## Solution Planning

To answer the CEO's questions, the following purchase conditions were suggested:
- Houses built before 1960 in good condition, and below average price;
- Houses overlooking the water with price below average;
- Houses that have not undergone renovation and are in good condition, and below average price;
- Houses that have a basement and price below the median.

And the following conditions of sale:
- If the sale period is bad, sale value = 'House value + 10%'
- If the sale period is good, sale value = 'House value + 30%'
     > Good period for purchase = (Spring or Summer) and 1st semester of the year

     > Bad period = otherwise

## Main Insights

#### Hypothesis creation and correlation visualization.

- H1: A maioria das casas com 3 quartos são acima da mediana do preço.
    - **FALSA**  A maioria das casa com 3 quartos são abaixo da mediana do preço.


- Hypotheses and results:

|Hipoteses  |  Conclusão  |  Relevancia|
|----------- | ----------- | ------------|
|H1          | Falsa       | Baixa |
|H2          | Falsa       | Alta |
|H3          | Verdadeira  | Alta |
|H4          | Verdadeira  | Alta |
|H5          | Verdadeira  | Baixa |
|H6          | Verdadeira  | Baixa |
|H7          | Verdadeira  | Media |
|H8          | Verdadeira  | Media |
|H9          | Verdadeira  | Alta |
|H10         | Verdadeira  | Media |
