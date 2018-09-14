# group_collaboration-
This project based on data sets that were taken from Kaggle and The World Bank Data Catalog. They consist information on world population, average life expectancy, infant mortality, fertility rate, gdp, climate and more. This project analyzes the average life expectancy rate for each country and how it changes over time. Also this project answers the question if there is any correlation between life expectancy, infant mortality, fertility rate and climate. 

The final report includes the following plots:

* Countries by Life Expectancy 2016
* Average Life Excpectancy in the World Over Time
* Average Fertility Rate in the World Over Time
* Life Expectancy vs GDP and Climate
* Infant mortality vs GDP and Climate
* Fertility Rate vs GDP and Climate

Project Findings:

* There is some correlation between climate and life expectancy. Almost all the countries with high rates of life expectancy are located in the coolest part of the graph. There is also a strong correlation between GDP and life expectancy. Citizens of the countries with the highest GDP live longer.

* There is no correlation between climate and infant mortality and fertility rate. They are correlated by GDP size.

This project was completed using the pandas, numpy, scipy.stats and Matplotlib libraries, and Jupiter Notebook.

Files included within this projects:

* this README.md
* country_population_analysis.ipynb 
* cckp_historical_data_0.csv  
* countries_of_the_world.csv 
* country_population.csv
* fertility_rate.csv
* life_expectancy.csv
* average_fertility_rate.png
* average_life_expectancy.png
* countries_by_life_expectancy.png
* fertility_rate_climate.png
* infant_mortality_climate.png
* life_expectancy_climate.png
=======

#Create a write-up summarizing your major findings. This should include a heading for each “question” you asked of your data, and under each heading, a short description of what you found and any relevant plots.

Christine Ton

Does GDP have an impact on Life Expectancy?
- I took a look at countries of the world and life expectancy data provided by Kaggle and World Bank Data Catalog.  With this data, there was a merge of data based on countries. 
- From this, I took the average life expectancy ages and sorted them into bins.  From there, calculated the average GPD of the countries they were in.  
- A country's GDP has one of the biggest impacts on life expectancy. There is a clear coorelation that the higher a country's GPD, the higher the life expectancy. 


Does GPD and Population have an impact on Life Expectancy?
- Using the combined Kaggle and World Bank Data Catalog, I created a bubble chart to see if there may be a coorelation on population size and the ability to have high GDP.
- There continues to be a higher coorelation between GPD and life expectancy and population does not have an impact on life expectancy. 

Does Free Health Care help increase Life Expectancy?
- Using data from Wikipedia and Kaggle, I merge the data together to get a list of countries that provide Free Health Care and their Life Expectancy. 
- Average Life Expectancy increase by 10 years for countries that provide Free Health Care. 


Does Universal Health Care help increase Life Expectancy? 
- Similar method to Free Health Care, I combined data from Wikipedia and Kaggle to get a list of countries that provide Universal Health Care. Just like Free Health Care, the average Life Expectancy increases by 10 years for countries that provide Universal Health Care
