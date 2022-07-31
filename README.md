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

3 - Want to access purchase suggestions remotely.


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

- H1: Houses in better condition have prices above the median
  - **TRUE - Houses classified as in good condition have a median price above the median of the portfolio**

- H2: Homes built before 1960 are 30% cheaper
  - **FALSE - Homes built before 1960 are only 4.4% cheaper**
  
- H3: Homes located overlooking the water are 50% more expensive on average
  - **FALSE - Homes with a water view are approximately 200% more expensive, on average, compared to those without a water view**
  
- H4: In the first half of the year the price of the house is 20% more expensive, on average
  - **FALSE - In the first semester, houses are only 2.3% more expensive, on average, when compared to the second semester**

- H5: Houses that have been renovated are priced higher than the median
  - **TRUE - Houses that have undergone renovation have prices higher than the median of the portfolio**

- H6: Houses that have 3 bedrooms and 2 bathrooms are priced above the median
  - **TRUE - Homes with more than 3 bedrooms and more than 2 bathrooms are priced around 19% higher than the portfolio median**

- H7: House prices have a 10% MoM (Month over Month) increase
  - **FALSE - MoM growth is not linear and does not reach 10% higher in any month**

- H8: Homes with a basement are 20% more expensive, on average
  - **TRUE - Homes with a basement are more expensive than the portfolio median and 25% more expensive compared to those without a basement**

- H9: Houses with a number of floors above 2 are 20% more expensive, on average
  - **FALSE - Houses with 2 floors and above tend to be more expensive, but are not 20% more expensive than average**

- H10: Homes are 20% more expensive in summer, on average
  - **FALSE - Houses are more expensive in spring and summer and cheaper in winter, but in summer they don't have this 20% impact**



#### Hypotheses and results:

|Hypothesis  |  Conclusion  |  Relevance  |
|----------- | -----------  | ------------|
|H1          | True         | Low         |
|H2          | False        | Medium      |
|H3          | False        | High        |
|H4          | False        | Medium      |
|H5          | True         | Low         |
|H6          | True         | Medium      |
|H7          | False        | Medium      |
|H8          | True         | High        |
|H9          | False        | Medium      |
|H10         | False        | High        |


## Correlation

#### Numeric - Pearson Correlation
<p align="center">
  <img src="images/corr.png"/>
</p>

## Results

* Answering questions
  - The purchase suggestion was created following the solution assumptions.
  - 4025 homes were suggested for purchase
  - The total profit is $401,706,161.00 
  - The profit percentage is 23.60%
  - Best time to sell is spring and summer or first semester of year
  - To access remotely, a dashboard was created and deployed using heroku 

## Deploy

- Link: https://analytics-kc-house.herokuapp.com/

<p align="center">
  <img src="images/i3.jpeg"/>
</p>

<p align="center">
  <img src="images/i4.jpeg"/>
</p>

<p align="center">
  <img src="images/i1.jpeg"/>
</p>

<p align="center">
  <img src="images/i2.jpeg"/>
</p>



