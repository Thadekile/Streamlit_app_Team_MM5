# Unsupervised_Learning_Project_2401FTDS_Team_MM5
![Python logo](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
<div id="main image" align="center">
  <img src="https://github.com/Thadekile/Unsupervised_Learning_Project_2401FTDS_Team_MM5/blob/main/1_animes_japoneses_entenda_o_que_sao_e_o_porque_de_fazerem_tanto_sucesso-18726989.jpg" width="450" height="300" alt=""/>
</div>


## Table of contents

* [1. Project Overview](#project-description)
* [2. Dataset](#dataset)
* [3. Packages](#packages)
* [4. Environment](#environment)
* [5. Team Members](#team-members)

## 1. Project Overview <a class="anchor" id="project-description"></a>

In today’s technology-driven world, recommender systems are socially and economically critical for ensuring that individuals can make appropriate choices surrounding the content they engage with on a daily basis. One application where this is especially true is movie content recommendations, where intelligent algorithms can help viewers find great titles from tens of thousands of options.

Ever wondered how Netflix, Amazon Prime, Showmax, Disney, and the likes somehow know what to recommend to you?

Well, we have built a system to show you exactly how this works! Our project involved using all our skills to build a collaborative and content-based recommender system for a collection of anime titles. This system is capable of accurately predicting how a user will rate an anime title they have not yet viewed, based on their historical preferences.

The dataset consists of thousands of users and thousands of anime titles, gathered from myanimelist.net.

 The analysis includes the following:
1. Importing Packages
2. Data Loading
3. Data Cleaning
4. Exploratory Data Analysis
5. Data Preprocessing
6. Model Building
7. Model Performance Evaluation
8. MLflow Integration
9. Streamlit App Development
10. Conclusions



## 2. Dataset <a class="anchor" id="dataset"></a>
Data Overview
This dataset contains information on anime content (movies, television series, music, specials, OVA, and ONA*), split between a file related to the titles (anime.csv) and one related to user ratings of the titles (training.csv). The test.csv file will be used to create the rating predictions and must be submitted for grading. The submissions.csv file illustrates the expected format of submissions.

*OVA: Original Video Animation - anime film / series made for release in home-video formats, ONA: Original Net Animation is an anime that is directly released onto the Internet.

Supplied files:
anime.csv: This file contains information about the anime content, including aspects such as the id, name, genre, type, number of episodes (if applicable), an average rating based on views, and the number of members in the anime 'group'.
train.csv:This file contains rating data, supplied by individual users for individual anime titles. It contains user_id information, the anime_id of the title watched, and the rating given (if applicable).
test.csv: This file will be used to create the final submission. It contains a user_id and an anime_id column only - no rating (that's your task!). These ids will be used to create the rating predictions.
submission.csv:This file is for illustrative purposes only, showing the submission format for the final predictions.
Detailed file description:
Anime.csv

anime_id - myanimelist.net's unique id identifying an anime.
name - full name of anime.
genre - comma-separated list of genres for this anime.
type - movie, TV, OVA, etc.
episodes - the number of episodes in the series. (1 if movie).
rating - average rating out of 10 for this anime.
members - number of community members that are in this anime's "group".
train.csv

user_id - non-identifiable randomly generated user id.
anime_id - the anime that this user has rated.
rating - rating out of 10 this user has assigned (-1 if the user watched it but didn't assign a rating).
test.csv

user_id - non-identifiable randomly generated user id.
anime_id - the anime that this user has rated.


## 3. Packages <a class="anchor" id="packages"></a>

Packages are collections of Python modules that provide specific functionality and tools, making it easier to perform various tasks without having to write code from scratch. They are essential for extending the capabilities of Python by providing pre-built functions and classes that help with tasks such as data manipulation, numerical computations, machine learning, and visualization.


To ensure the project runs smoothly, you need to install the following packages:
1. matplotlib==3.8.4
2. missingno==0.5.2
3. mlflow==2.5.0
4. nltk==3.8.1
5. numpy==1.26.4
6. pandas==2.2.2
7. plotly==5.22.0
8. requests==2.31.0
9. scikit-learn==1.4.2
10. scipy==1.13.0
11. seaborn==0.13.2
12. wordcloud==1.9.3



## 4. Environment <a class="anchor" id="environment"></a>

An environment is a self-contained directory that holds a specific set of Python and package versions.Environments ensures that your code runs consistently and avoids conflicts with other projects. 

The instructions provided below will guide you on how to create an environment:
**A. Create a New Environment:**

To create a new environment, use the conda create command.

For example:

  **conda create --name myenv**

This command creates a new environment named myenv. You can replace myenv with whatever name you prefer.

**B. Activate the Environment:**

After creating the environment, you need to activate it. Use the conda activate command:

  **conda activate myenv**

**D.Package-management system and Installing Packages:**

Install the Python package manager called pip within the Conda environment.

  **conda install pip**

It's like adding an extra tool to manage Python packages within Conda.

  **(i) Installing packages from a text file .txt:**

      Using requirements.txt: requirements.txt is a file that contains a list of the specific package versions needed for this project.

       Download the requirements.txt file (if not already downloaded).
       (Optional) Move the txt file to your desired location.
       On your Terminal, navigate to the directory/folder containing this text file.
      If you have a requirements.txt file listing the project dependencies, and have navigated to the directory containing the file and install them using pip:

   **pip install -r requirements.txt**

*This will install NumPy, Pandas, Matplotlib, and other packages listed in your requirements.txt file into your current environment.*



**D. Deactivate the Environment (optional):**

When you're done working in your environment, you can deactivate it using the conda deactivate command:

  **conda deactivate**


## 5. Team Members<a class="anchor" id="team-members"></a>

This project was a collaborative effort by the following team members:

| Name                                                                                        |  Email              
|---------------------------------------------------------------------------------------------|--------------------             
| [Chuma Gqola](https://github.com/Chuma-Gqola)                                               | chuma.gqolacg@gmail.com
| [Ndivho Mamphiswana](https://github.com/ndibo)                                              | mamphiswanan@gmail.com
| [Thandekile Sikhakhane](https://github.com/Thadekile)                                       | thandohas@gmail.com
| [Thapelo Raphala](https://github.com/RobynRaps)                                             | robynraps18@gmail.com
| [Lebogang Malata](https://github.com/LebogangMalata)                                        | mich.malata@gmail.com
| [Nomkhosi Sibiya](https://github.com/Zemikhosi)                                             | nomkhosisyamthanda@gmail.com

 Together, we successfully built a recommender system for anime titles, demonstrating the power and utility of collaborative and content-based filtering techniques. The final product includes a Streamlit app that allows users to explore and receive recommendations based on their preferences.