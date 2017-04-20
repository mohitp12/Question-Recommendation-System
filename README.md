# Question Recommendation System
Suggest Hacker Rank questions to a user on the basis of users behaviour.

Implemented three data mining algorithms to get the respective results from the dataset of 28500 rows.
1. Naive Bayes theorem to classify between highly qualified, more qualified and average candidates based on their previous answering behaviour.

2. Used this classification to generate pool of upcoming questions for a specific candidate to review skills of the candidate.

3. Integrated Apriori algorithm to find the associations between the type of candidate and the final results of the answered questions. 

Developed front-end in Angularjs and Bootstrap to make website responsive. Analyzed resulted data and displayed it using angular-nvd3 charts

Stress tested API's using JMETER to check the performance of the application.


#Requirements to run project:
- Download repository on a machine with Python.
- Install all the dependecies from requirements.txt using `pip install requirements.txt`
- Import Django and Angularjs libraries.
- Goto HR_recommendation_system/ and run `py pip.py` to run application
