# Cross Selling in the Health Insurance Business  
![cs_img](images/cross_selling.png)
_Disclaimer:_ All the scenarios, descriptions, and situations in this project are fictional and do not represent any of this company’s views, actions, or opinions. The processes, results, recommendations, and any other information provided in this project have the sole intention of describing my Data Science skills using real-world approaches, applications, and solutions provided. The data used in this project was retrieved from [this public source](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction). The data are available on Kaggle's website and comply with Kaggle's terms and conditions.

### The main characteristic of this project is that it rank-order potential clients using their propensity scores.

##### This project was made by Thiago Oliveira Borges.  

# Rationale  
Cross-selling refers to suggesting and successfully selling additional services or products to existing clients. This strategy may induce a win-win relationship between the company and the client by:  
    * Strengthening customer relationship - Engaging clients with relevant recommendations;  
    * Improving customer experience - Introducing complementary products that solve their problems more efficiently;  
    * Boosting customer lifetime value - Satisfied clients become more valuable assets;  
    * Optimizing inventory - Move slow-moving inventory;  
    * Reducing marketing costs - Selling to existing customers is generally cheaper than acquiring new ones;  
    * Increasing revenue - Bumping up the average order value.  

Therefore, cross-selling is a powerful strategy for companies wanting to unlock higher revenue, build a stronger relationship with current clients, and provide excellent additional services or products to help clients solve their problems.  

# 1. Business Problem.  

The (fictional) company "Are you insured?" provides health insurance services to thousands of clients. The company expanded its service portfolio and inquired its current clients whether they would be interested in acquiring their new product - car insurance service.  

After 304 thousand clients replying to the inquiry, the company still has to offer the car insurance service to approximately 75 thousand clients that have not answered the research. Due to budget limitations, the company can contact only 20 thousand clients, out of those 75 thousand. Therefore, an optimized, ranked list would be required to increase the chances of contacting clients with actual interest in buying this new product. Therefore, an objective solution must be developed to optimize the operation.  


# 2. Business Assumptions.  

The sales team already uses the Google Sheet as a corporation tool. Therefore, incorporating the solution into the Google Sheet would facilitate and optimize the use of the solution by the company. 

# 3. Development of the Solution  

To deliver the final data product to the company, there are a few steps to be followed:  

## 3.1. The deliverable  
A functional button will be set in the Google Sheets, where will be possible to retrieve the calculated propensity score and create a rank-ordered list.  

## 3.2. Tools  

This project was developed using the following tools:

  * Python 3.10.4;
  * Jupyter Notebook;
  * Git and GitHub;
  * Google Sheet App Scripts;
  * Microsoft Visual Studio Code;
  * Render Cloud;
  * Flask, and Python API;
  * Regression and classification machine learning techniques;  

## 3.3. Process  

This is a learn-to-rank project [LTR.](https://en.wikipedia.org/wiki/Learning_to_rank#:~:text=Learning%20to%20rank%20or%20machine,models%20for%20information%20retrieval%20systems.) I have used the CRISP-DS approach to deal with each step of the project, which is described below:


  **Step 01. Data:**  
  * The dataset was downloaded from the Kaggle website;  
  * Then, the original dataset was split as train, validation, and testing data (randomly separated 70%, 15%, and 15% of the data, respectively).  
  * Then, after a thorough inspection of the data description provided in the source and of the train data I was able to check and understand the features;  
  * Also, I edited some column names, verified data dimensions, and data types, and identified and treated null data;  
  * The descriptive statistics performed here helped to analyze data attributes.
    
**Step 02. Feature Engineering:**  
  * Feature engineering was done with the help of the business mindmap;  
  * Mindmap inspired the creation hypothesis in which the Engineered features helped with testing.  


**Step 03. Data Filtering:**  
  * Filter data according to business restrictions;  


**Step 04. Exploratory Data Analysis (EDA):**  
  * Apply univariate analysis to inspect the characteristics of the data;  
  * Apply bivariate analysis to validate the hypothesis and generate business insights.  


**Step 05. Data Preparation:**  
  * Standardize normally distributed numerical attributes;  
  * Re-scale non-normally distributed numerical attributes;  
  * Code categorical attributes to numerical attributes;  
  * Apply the procedures described above on validation and test data.


**Step 06. Feature Selection:**  
  * In this step, I used the Boruta algorithm to select the relevant features for the project;  
  * Cross-check the results, with the results estimated during the EDA;  
  * Select only the relevant features to use them to train the machine learning models.  


**Step 07. Machine Learning Modelling:**  
  * Search for the best model: kNN Classifier, Logistic Regression, Random Forest, LGBM Classifier, Gradient Boost Classifier, XGBoost Classifier;  
  * Inspect the Cumulative Gain and Lift Curve, and calculate precision and recall at k for each model;  
  * Compared the cross-validated performance of each model and chose the best fit to be implemented.  


**Step 08. Performance Metrics:**  
  * Fine-tune the hyperparameters of the chosen model, searching for the best set of parameters to maximize the learning ability;  
  * Apply cross-validation to the model, reducing selection bias;  
  * Submit these models to test data and plot their cumulative gain and lift curve;  
  * Compare precision@k and recall@k of training and test, assessing the model's ability of generalization.


**Step 09. Convert Model Performance to Business Values:**  
  * Reply to the business questions;  
  * Compare results of the propensity scores present in the random list with the ranked list;  
  * Translate the model's performance to revenue results to the company.


**Step 10. Deploy Model to Production:**  
  * Create the Class to publish in production;  
  * Test the Class locally;  
  * Publish the model in Render Cloud;  
  * Create an App Script in Google Sheets to call in the production model;  
  * Include a button to check the buying propensity in Google Sheets, and test the solution.

# 4. Insights from the EDA  
  The EDA is an important part of a Data Science project since it allows it to understand the data and prepare them for the rest of the project. In this project, the top 
  3 insights where generated after checking a few hypothesis:  

  **H1 - The interest in the car insurance is pronounced for costumer with newer vehicles.**  
  **FALSE:** The data show cars newer than 1 year, those that has been used between 1 and 2 years, and those cars older than two years. 
  The hypothesis that owner with newer car would be interested in buying car insurance is false. The data show that owners of the intermediate 
  group are the majority of interested in buying car insurance.  



  **H2 - Older clients are the ones interested in buying car insurance**  
  **FALSE** - Clients with age between 40 and 55 are the ones most interested in car insurance.  


  **H3 - Clients who were previously insured were the ones interested in buying car insurance**  
  **FALSE** - Clients that have shown interest are those with no prior car insurance service.
