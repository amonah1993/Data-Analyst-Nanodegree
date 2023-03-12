### Project 3 : Investigate a Dataset (TMDB Database)

### Project Overview
In this project, you will analyze a dataset and then communicate your findings about it. You will use the Python libraries NumPy, pandas, and Matplotlib to make your analysis easier.

Data wrangling and EDA were made on the dataset, therefore five questions were answered through analysing this dataset:
* Movie that had the most runtime and least? 

![image1](https://github.com/amonah1993/Data-Analyst-Nanodegree/blob/main/Investigate%20a%20Dataset/Screen%20Shot%201444-08-20%20at%205.54.37%20PM.png)

* Movie that is most popular in all years? 

![image2](https://github.com/amonah1993/Data-Analyst-Nanodegree/blob/main/Investigate%20a%20Dataset/Screen%20Shot%201444-08-20%20at%205.54.49%20PM.png)

* Average runtime of all movies? 

109.22029060716139

* Revenue of all years? 

![image2](https://github.com/amonah1993/Data-Analyst-Nanodegree/blob/main/Investigate%20a%20Dataset/Screen%20Shot%201444-08-20%20at%205.54.55%20PM.png)

* Most Movie Revenue of all years?
      
      Avatar


### Conclusion

In the end it has been found that the dataset need cleaning such as : changing the type of release date to date time that if not changed would affect the analysis process, droping some unused columns that has no use of being in the dataset, removing duplicate that if not it will cause redundancy in the dataset, and removing all 0 in the revenue and budget columns that are erroneous and will affect the analysis result if not removed

All of those were must to be handeled for the analysis process to not be affected and the results of it to be clear

Also through the dataset it has been answered 5 questions such as:

* The revenue of all years that will show the relationship of realse year vs revenue
* Average of runtime via calculating it with numpy function
* Most Movie Revenue of all years that shows the name of the most revenue with the year
* Movie that is most popular in all years that will show the most popular movie
* Movie that had the most runtime and least that will show the least and most movie runtime and has a plot to emphasis on that

### Limitations 

TMBD Dataset is used for analysis that has a number of columns such as revenue, runtime and release time. The analysis may have limitations in many ways:

* It is not a sure thing that the dataset is correct or up to date
* Because of the revenue and budget columns have some rows with zero that must be handle by deleting them and also the deleting may affect the overall analysis but also them being there in the dataset with being handeled with him also will affect the overall analysis more than being deleting
* The budget and revenue columns does not have a currency unit and each movie might have different currency from the other that may affect the overall analysis
