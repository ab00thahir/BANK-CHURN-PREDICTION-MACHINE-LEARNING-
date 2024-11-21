Developed a machine learning model to predict customer churn, improving retention strategies by identifying at-risk customers. The model, trained on 10,000 customer records, leveraged features like credit score, balance, and tenure.

Key Contributions:
Data Preprocessing:
Encoded categorical features, addressed missing data, and handled class imbalance (20% churned vs. 80% retained) using SMOTE for better model performance.

Exploratory Data Analysis (EDA):
Performed EDA to uncover insights into customer behavior, visualizing relationships with heatmaps, count plots, and correlation matrices.

Model Development:
Built and compared 6 algorithms:

Random Forest (86.5% accuracy)
Gradient Boosting (85.2% accuracy)
Decision Tree (84.7% accuracy)
Hyperparameter tuning via GridSearchCV further optimized Random Forest’s performance.
Performance Metrics:
Evaluated models using accuracy, precision (87%), and recall (82%). Generated a confusion matrix and classification report for detailed insights.

Visualization:
Created visualizations including a churn distribution pie chart and bar charts comparing churn rates across demographics like gender and tenure.

Prediction System:
Built a real-time prediction system for customer churn using new data (e.g., country, age, balance).

Model Persistence:
Saved the trained model with Pickle for future use and deployment.

Tools & Technologies:
Python, Pandas, Scikit-learn, SMOTE, Pickle
Machine Learning Algorithms: Random Forest, Decision Tree, Gradient Boosting, KNN, SVC, Logistic Regression
Evaluation Techniques: Accuracy, Precision, Recall, Confusion Matrix
Hyperparameter Tuning: GridSearchCV
