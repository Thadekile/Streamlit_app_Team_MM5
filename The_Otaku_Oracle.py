# import streamlit as st
# import streamlit.components.v1 as components
# import pandas as pd
# import pickle
# import base64
# import matplotlib.pyplot as plt
# import seaborn as sns

# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url(data:image/png;base64,{encoded_string.decode()});
#             background-size: cover;
#             background-attachment: fixed;
#         }}
#         .content-block {{
#             background-color: rgba(255, 255, 255, 0.8);  /* White background with 80% opacity */
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
#             position: relative;  /* Ensure it stays on top of the background */
#             z-index: 1;  /* Make sure it is above the background image */
#         }}
#         .animation-container {{
#             display: inline-block;
#             width: 100px;
#             height: 100px;
#             vertical-align: middle;
#         }}
#         .button-container {{
#             display: flex;
#             align-items: center;
#             gap: 10px;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def load_data():
#     with open('anime_data.pkl', 'rb') as f:
#         df_encoded = pickle.load(f)
#     with open('similarity_matrix.pkl', 'rb') as f:
#         similarity_matrix = pickle.load(f)
#     return df_encoded, similarity_matrix

# df_encoded, similarity_matrix = load_data()

# def get_recommendations(anime_name, similarity_matrix, df_encoded, top_n=3, threshold=0.5):
#     try:
#         idx = df_encoded[df_encoded['name'].str.lower() == anime_name.lower()].index[0]
#         sim_scores = list(enumerate(similarity_matrix[idx]))
#         sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#         sim_scores = sim_scores[1:top_n+1]
#         similar_indices = [i[0] for i in sim_scores if i[1] >= threshold]
#         return df_encoded[['name', 'genre', 'type']].iloc[similar_indices].to_dict(orient='records')  # Return dict for easier display
#     except IndexError:
#         print(f"Anime '{anime_name}' not found in the dataset.")
#         return []

# # Sidebar navigation
# st.sidebar.title('Navigation')
# page = st.sidebar.radio('Go to', ['Home', 'Exploratory Data Analysis'])

# # Add the background image at the beginning of your app
# add_bg_from_local('Screen+Shot+2023-04-22+at+3.50.40+PM.png')

# if page == 'Home':
#     # Home Page
#     st.title('The Otaku Oracle')
#     st.text('Your Anime Recommender')

#     # Wrap content in a block with the "content-block" class
#     with st.markdown("""
#         <div class="content-block">
#         <h2>The Otaku Oracle</h2>
#         <p>Your Anime Recommender</p>
#         <div class="button-container">
#             <!-- Button to get recommendations -->
#             <button id="recommend-button">Get Recommendations</button>
#             <!-- Add the animation -->
#             <div class="animation-container">
#                 <iframe src="https://app.lottiefiles.com/animation/4fb34dd2-e58e-4b7c-acf7-d936097a2f0d" 
#                         style="width: 100%; height: 100%; border: none;" 
#                         frameborder="0" 
#                         allowfullscreen></iframe>
#             </div>
#         </div>
#         </div>
#         """, unsafe_allow_html=True):
        
#         # Autocomplete Anime Selection
#         anime_names = df_encoded['name'].unique()  # Get all unique anime names
#         selected_anime = st.selectbox('Select or start typing an anime name:', anime_names)

#     if st.button('Get Recommendations'):
#         if selected_anime:
#             recommendations = get_recommendations(selected_anime, similarity_matrix, df_encoded)  # Use the recommender function to make recommendations
#             if recommendations:
#                 st.subheader('Recommended Anime:')
#                 for anime in recommendations:
#                     st.markdown(f"""
#                     **{anime['name']}**

#                     * **Genre:** {', '.join(anime['genre'])}
#                     * **Type:** {anime['type']}
#                     """)  # Display more information
#             else:
#                 st.write(f"No recommendations above the threshold (0.5) found for '{selected_anime}'.")
#         else:
#             st.warning('Please select an anime.')

# elif page == 'Exploratory Data Analysis':
#     # EDA Page
#     st.title('Exploratory Data Analysis')

#     # Display basic statistics
#     st.subheader('Basic Statistics')
#     st.write(df_encoded.describe(include='all'))

#     # Plot distributions
#     st.subheader('Genre Distribution')
#     genre_counts = df_encoded['genre'].explode().value_counts()
#     st.bar_chart(genre_counts)

#     st.subheader('Type Distribution')
#     type_counts = df_encoded['type'].value_counts()
#     st.bar_chart(type_counts)

#     # Example scatter plot for ratings
#     st.subheader('Ratings Distribution')
#     fig, ax = plt.subplots()
#     sns.histplot(df_encoded['ratings'], kde=True, ax=ax)
#     ax.set_title('Ratings Distribution')
#     st.pyplot(fig)

# import streamlit as st
# import streamlit.components.v1 as components
# import pandas as pd
# import pickle
# import base64
# import matplotlib.pyplot as plt
# import seaborn as sns

# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url(data:image/png;base64,{encoded_string.decode()});
#             background-size: cover;
#             background-attachment: fixed;
#         }}
#         .content-block {{
#             background-color: rgba(0, 0, 0, 0.8);  /* Black background with 80% opacity */
#             color: white;  /* White text color for better readability */
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def load_data():
#     with open('anime_data.pkl', 'rb') as f:
#         df_encoded = pickle.load(f)
#     with open('similarity_matrix.pkl', 'rb') as f:
#         similarity_matrix = pickle.load(f)
#     return df_encoded, similarity_matrix

# df_encoded, similarity_matrix = load_data()

# def get_recommendations(anime_name, similarity_matrix, df_encoded, top_n=3, threshold=0.5):
#     try:
#         idx = df_encoded[df_encoded['name'].str.lower() == anime_name.lower()].index[0]
#         sim_scores = list(enumerate(similarity_matrix[idx]))
#         sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#         sim_scores = sim_scores[1:top_n+1]
#         similar_indices = [i[0] for i in sim_scores if i[1] >= threshold]
#         return df_encoded[['name', 'genre', 'type']].iloc[similar_indices].to_dict(orient='records')
#     except IndexError:
#         print(f"Anime '{anime_name}' not found in the dataset.")
#         return []

# # Sidebar navigation
# st.sidebar.title('Navigation')
# page = st.sidebar.radio('Go to', ['Home', 'Exploratory Data Analysis', 'About Us', 'Contact Us'])

# # Add the background image at the beginning of your app
# add_bg_from_local('Screen+Shot+2023-04-22+at+3.50.40+PM.png')

# if page == 'Home':
#     # Home Page
#     st.title('The Otaku Oracle')
#     st.text('Your Anime Recommender')

#     st.markdown("""
#     <div class="content-block">
#     <h2>The Otaku Oracle</h2>
#     <p>Your Anime Recommender</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Autocomplete Anime Selection
#     anime_names = df_encoded['name'].unique()  
#     selected_anime = st.selectbox('Select or start typing an anime name:', anime_names)

#     if st.button('Get Recommendations'):
#         if selected_anime:
#             recommendations = get_recommendations(selected_anime, similarity_matrix, df_encoded)  
#             if recommendations:
#                 st.subheader('Recommended Anime:')
#                 for anime in recommendations:
#                     st.markdown(f"""
#                     **{anime['name']}**

#                     * **Genre:** {', '.join(anime['genre'])}
#                     * **Type:** {anime['type']}
#                     """)
#             else:
#                 st.write(f"No recommendations above the threshold (0.5) found for '{selected_anime}'.")
#         else:
#             st.warning('Please select an anime.')

# elif page == 'Exploratory Data Analysis':
#     # EDA Page
#     st.title('Exploratory Data Analysis')

#     # Display basic statistics
#     st.subheader('Basic Statistics')
#     st.write(df_encoded.describe(include='all'))

#     # Plot distributions
#     st.subheader('Genre Distribution')
#     genre_counts = df_encoded['genre'].explode().value_counts()
#     st.bar_chart(genre_counts)

#     st.subheader('Type Distribution')
#     type_counts = df_encoded['type'].value_counts()
#     st.bar_chart(type_counts)

#     # Example scatter plot for ratings
#     st.subheader('Ratings Distribution')
#     fig, ax = plt.subplots()
#     sns.histplot(df_encoded['ratings'], kde=True, ax=ax)
#     ax.set_title('Ratings Distribution')
#     st.pyplot(fig)

# elif page == 'About Us':
#     # About Us Page
#     st.title('About Us')
#     st.markdown("""
#     <div class="content-block">
#     <h2>About The Otaku Oracle</h2>
#     <p>The Otaku Oracle is a recommendation system designed to help anime fans discover new anime to watch based on their preferences. Our system uses advanced machine learning algorithms to provide personalized recommendations.</p>
#     </div>
#     """, unsafe_allow_html=True)

# elif page == 'Contact Us':
#     # Contact Us Page
#     st.title('Contact Us')
#     st.markdown("""
#     <div class="content-block">
#     <h2>Contact Us</h2>
#     <p>If you have any questions or feedback, feel free to reach out to us at:</p>
#     <p>Email: support@otakuoracle.com</p>
#     <p>Phone: +1234567890</p>
#     </div>
#     """, unsafe_allow_html=True)

# import streamlit as st
# import streamlit.components.v1 as components
# import pandas as pd
# import pickle
# import base64
# import matplotlib.pyplot as plt
# import seaborn as sns

# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)), 
#                         url(data:image/png;base64,{encoded_string.decode()});
#             background-size: cover;
#             background-attachment: fixed;
#         }}
#         .content-block {{
#             background-color: rgba(0, 0, 0, 0.8);  /* Black background with 80% opacity */
#             color: white;  /* White text color for better readability */
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def load_data():
#     with open('anime_data.pkl', 'rb') as f:
#         df_encoded = pickle.load(f)
#     with open('similarity_matrix.pkl', 'rb') as f:
#         similarity_matrix = pickle.load(f)
#     return df_encoded, similarity_matrix

# df_encoded, similarity_matrix = load_data()

# def get_recommendations(anime_name, similarity_matrix, df_encoded, top_n=3, threshold=0.5):
#     try:
#         idx = df_encoded[df_encoded['name'].str.lower() == anime_name.lower()].index[0]
#         sim_scores = list(enumerate(similarity_matrix[idx]))
#         sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#         sim_scores = sim_scores[1:top_n+1]
#         similar_indices = [i[0] for i in sim_scores if i[1] >= threshold]
#         return df_encoded[['name', 'genre', 'type']].iloc[similar_indices].to_dict(orient='records')
#     except IndexError:
#         print(f"Anime '{anime_name}' not found in the dataset.")
#         return []

# # Sidebar navigation
# st.sidebar.title('Navigation')
# page = st.sidebar.radio('Go to', ['Home', 'Exploratory Data Analysis', 'About Us', 'Contact Us'])

# # Add the background image at the beginning of your app
# add_bg_from_local('Screen+Shot+2023-04-22+at+3.50.40+PM.png')

# if page == 'Home':
#     # Home Page
#     st.title('The Otaku Oracle')
#     st.text('Your Anime Recommender')

#     st.markdown("""
#     <div class="content-block">
#     <h2>The Otaku Oracle</h2>
#     <p>Your Anime Recommender</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Autocomplete Anime Selection
#     anime_names = df_encoded['name'].unique()  
#     selected_anime = st.selectbox('Select or start typing an anime name:', anime_names)

#     if st.button('Get Recommendations'):
#         if selected_anime:
#             recommendations = get_recommendations(selected_anime, similarity_matrix, df_encoded)  
#             if recommendations:
#                 st.subheader('Recommended Anime:')
#                 for anime in recommendations:
#                     st.markdown(f"""
#                     **{anime['name']}**

#                     * **Genre:** {', '.join(anime['genre'])}
#                     * **Type:** {anime['type']}
#                     """)
#             else:
#                 st.write(f"No recommendations above the threshold (0.5) found for '{selected_anime}'.")
#         else:
#             st.warning('Please select an anime.')

# elif page == 'Exploratory Data Analysis':
#     # EDA Page
#     st.title('Exploratory Data Analysis')

#     # Display basic statistics
#     st.subheader('Basic Statistics')
#     st.write(df_encoded.describe(include='all'))

#     # Plot distributions
#     st.subheader('Genre Distribution')
#     genre_counts = df_encoded['genre'].explode().value_counts()
#     st.bar_chart(genre_counts)

#     st.subheader('Type Distribution')
#     type_counts = df_encoded['type'].value_counts()
#     st.bar_chart(type_counts)

#     # Example scatter plot for ratings
#     st.subheader('Ratings Distribution')
#     fig, ax = plt.subplots()
#     sns.histplot(df_encoded['ratings'], kde=True, ax=ax)
#     ax.set_title('Ratings Distribution')
#     st.pyplot(fig)

# elif page == 'About Us':
#     # About Us Page
#     st.title('About Us')
#     st.markdown("""
#     <div class="content-block">
#     <h2>About The Otaku Oracle</h2>
#     <p>The Otaku Oracle is a recommendation system designed to help anime fans discover new anime to watch based on their preferences. Our system uses advanced machine learning algorithms to provide personalized recommendations.</p>
#     </div>
#     """, unsafe_allow_html=True)

# elif page == 'Contact Us':
#     # Contact Us Page
#     st.title('Contact Us')
#     st.markdown("""
#     <div class="content-block">
#     <h2>Contact Us</h2>
#     <p>If you have any questions or feedback, feel free to reach out to us at:</p>
#     <p>Email: support@otakuoracle.com</p>
#     <p>Phone: +1234567890</p>
#     </div>
#     """, unsafe_allow_html=True)

# import streamlit as st
# import streamlit.components.v1 as components
# import pandas as pd
# import pickle
# import base64
# import matplotlib.pyplot as plt
# import seaborn as sns

# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)), 
#                         url(data:image/png;base64,{encoded_string.decode()});
#             background-size: cover;
#             background-attachment: fixed;
#         }}
#         .content-block {{
#             background-color: rgba(0, 0, 0, 0.8);  /* Black background with 80% opacity */
#             color: white;  /* White text color for better readability */
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
#         }}
#         .recommendation-block {{
#             background-color: rgba(255, 255, 255, 0.8);  /* White background with 80% opacity */
#             color: black;  /* Black text color for better readability */
#             padding: 10px;
#             margin-bottom: 10px;
#             border-radius: 5px;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def load_data():
#     with open('anime_data.pkl', 'rb') as f:
#         df_encoded = pickle.load(f)
#     with open('similarity_matrix.pkl', 'rb') as f:
#         similarity_matrix = pickle.load(f)
#     return df_encoded, similarity_matrix

# df_encoded, similarity_matrix = load_data()

# def get_recommendations(anime_name, similarity_matrix, df_encoded, top_n=3, threshold=0.5):
#     try:
#         idx = df_encoded[df_encoded['name'].str.lower() == anime_name.lower()].index[0]
#         sim_scores = list(enumerate(similarity_matrix[idx]))
#         sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#         sim_scores = sim_scores[1:top_n+1]
#         similar_indices = [i[0] for i in sim_scores if i[1] >= threshold]
#         return df_encoded[['name', 'genre', 'type']].iloc[similar_indices].to_dict(orient='records')
#     except IndexError:
#         print(f"Anime '{anime_name}' not found in the dataset.")
#         return []

# # Sidebar navigation
# st.sidebar.title('Navigation')
# page = st.sidebar.radio('Go to', ['Home', 'Exploratory Data Analysis', 'About Us', 'Contact Us'])

# # Add the background image at the beginning of your app
# add_bg_from_local('Screen+Shot+2023-04-22+at+3.50.40+PM.png')

# if page == 'Home':
#     # Home Page
#     st.title('The Otaku Oracle')
#     st.text('Your Anime Recommender')

#     st.markdown("""
#     <div class="content-block">
#     <h2>The Otaku Oracle</h2>
#     <p>Your Anime Recommender</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Autocomplete Anime Selection
#     anime_names = df_encoded['name'].unique()  
#     selected_anime = st.selectbox('Select or start typing an anime name:', anime_names)

#     if st.button('Get Recommendations'):
#         if selected_anime:
#             recommendations = get_recommendations(selected_anime, similarity_matrix, df_encoded)  
#             if recommendations:
#                 st.subheader('Recommended Anime:')
#                 for anime in recommendations:
#                     st.markdown(f"""
#                     <div class="recommendation-block">
#                     **{anime['name']}**

#                     * **Genre:** {', '.join(anime['genre'])}
#                     * **Type:** {anime['type']}
#                     </div>
#                     """, unsafe_allow_html=True)
#             else:
#                 st.write(f"No recommendations above the threshold (0.5) found for '{selected_anime}'.")
#         else:
#             st.warning('Please select an anime.')

# elif page == 'Exploratory Data Analysis':
#     # EDA Page
#     st.title('Exploratory Data Analysis')

#     # Display basic statistics
#     st.subheader('Basic Statistics')
#     st.write(df_encoded.describe(include='all'))

#     # Plot distributions
#     st.subheader('Genre Distribution')
#     genre_counts = df_encoded['genre'].explode().value_counts()
#     st.bar_chart(genre_counts)

#     st.subheader('Type Distribution')
#     type_counts = df_encoded['type'].value_counts()
#     st.bar_chart(type_counts)

#     # Example scatter plot for ratings
#     st.subheader('Ratings Distribution')
#     fig, ax = plt.subplots()
#     sns.histplot(df_encoded['ratings'], kde=True, ax=ax)
#     ax.set_title('Ratings Distribution')
#     st.pyplot(fig)

# elif page == 'About Us':
#     # About Us Page
#     st.title('About Us')
#     st.markdown("""
#     <div class="content-block">
#     <h2>About The Otaku Oracle</h2>
#     <p>The Otaku Oracle is a recommendation system designed to help anime fans discover new anime to watch based on their preferences. Our system uses advanced machine learning algorithms to provide personalized recommendations.</p>
#     </div>
#     """, unsafe_allow_html=True)

# elif page == 'Contact Us':
#     # Contact Us Page
#     st.title('Contact Us')
#     st.markdown("""
#     <div class="content-block">
#     <h2>Contact Us</h2>
#     <p>If you have any questions or feedback, feel free to reach out to us at:</p>
#     <p>Email: support@otakuoracle.com</p>
#     <p>Phone: +1234567890</p>
#     </div>
#     """, unsafe_allow_html=True)

# import streamlit as st
# import streamlit.components.v1 as components
# import pandas as pd
# import pickle
# import base64
# import matplotlib.pyplot as plt
# import seaborn as sns

# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url(data:image/png;base64,{encoded_string.decode()});
#             background-size: cover;
#             background-attachment: fixed;
#         }}
#         .content-block {{
#             background-color: rgba(0, 0, 0, 0.8);  /* Black background with 80% opacity */
#             color: white;  /* White text color for better readability */
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
#         }}
#         .recommendation-block {{
#             background-color: rgba(255, 255, 255, 0.8);  /* White background with 80% opacity */
#             color: black;  /* Black text color for better readability */
#             padding: 10px;
#             margin-bottom: 10px;
#             border-radius: 5px;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def load_data():
#     with open('anime_data.pkl', 'rb') as f:
#         df_encoded = pickle.load(f)
#     with open('similarity_matrix.pkl', 'rb') as f:
#         similarity_matrix = pickle.load(f)
#     return df_encoded, similarity_matrix

# df_encoded, similarity_matrix = load_data()

# def get_recommendations(anime_name, similarity_matrix, df_encoded, top_n=3, threshold=0.5):
#     try:
#         idx = df_encoded[df_encoded['name'].str.lower() == anime_name.lower()].index[0]
#         sim_scores = list(enumerate(similarity_matrix[idx]))
#         sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#         sim_scores = sim_scores[1:top_n+1]
#         similar_indices = [i[0] for i in sim_scores if i[1] >= threshold]
#         return df_encoded[['name', 'genre', 'type']].iloc[similar_indices].to_dict(orient='records')
#     except IndexError:
#         print(f"Anime '{anime_name}' not found in the dataset.")
#         return []

# # Sidebar navigation
# st.sidebar.title('Navigation')
# page = st.sidebar.radio('Go to', ['Home', 'Exploratory Data Analysis', 'About Us', 'Contact Us'])

# # Add the background image at the beginning of your app
# add_bg_from_local('Screen+Shot+2023-04-22+at+3.50.40+PM.png')

# if page == 'Home':
#     # Home Page
#     st.title('The Otaku Oracle')
#     st.text('Your Anime Recommender')

#     st.markdown("""
#     <div class="content-block">
#     <h2>The Otaku Oracle</h2>
#     <p>Your Anime Recommender</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Autocomplete Anime Selection
#     anime_names = df_encoded['name'].unique()  
#     selected_anime = st.selectbox('Select or start typing an anime name:', anime_names)

#     if st.button('Get Recommendations'):
#         if selected_anime:
#             recommendations = get_recommendations(selected_anime, similarity_matrix, df_encoded)  
#             if recommendations:
#                 st.subheader('Recommended Anime:')
#                 for anime in recommendations:
#                     st.markdown(f"""
#                     <div class="recommendation-block">
#                     **{anime['name']}**

#                     * **Genre:** {', '.join(anime['genre'])}
#                     * **Type:** {anime['type']}
#                     </div>
#                     """, unsafe_allow_html=True)
#             else:
#                 st.write(f"No recommendations above the threshold (0.5) found for '{selected_anime}'.")
#         else:
#             st.warning('Please select an anime.')

# elif page == 'Exploratory Data Analysis':
#     # EDA Page
#     st.title('Exploratory Data Analysis')

#     # Display basic statistics
#     st.subheader('Basic Statistics')
#     st.write(df_encoded.describe(include='all'))

#     # Plot distributions
#     st.subheader('Genre Distribution')
#     genre_counts = df_encoded['genre'].explode().value_counts()
#     st.bar_chart(genre_counts)

#     st.subheader('Type Distribution')
#     type_counts = df_encoded['type'].value_counts()
#     st.bar_chart(type_counts)

#     # Example scatter plot for ratings
#     st.subheader('Ratings Distribution')
#     fig, ax = plt.subplots()
#     sns.histplot(df_encoded['ratings'], kde=True, ax=ax)
#     ax.set_title('Ratings Distribution')
#     st.pyplot(fig)

# elif page == 'About Us':
#     # About Us Page
#     st.title('About Us')
#     st.markdown("""
#     <div class="content-block">
#     <h2>About The Otaku Oracle</h2>
#     <p>The Otaku Oracle is a recommendation system designed to help anime fans discover new anime to watch based on their preferences. Our system uses advanced machine learning algorithms to provide personalized recommendations.</p>
#     </div>
#     """, unsafe_allow_html=True)

# elif page == 'Contact Us':
#     # Contact Us Page
#     st.title('Contact Us')
#     st.markdown("""
#     <div class="content-block">
#     <h2>Contact Us</h2>
#     <p>If you have any questions or feedback, feel free to reach out to us at:</p>
#     <p>Email: support@otakuoracle.com</p>
#     <p>Phone: +1234567890</p>
#     </div>
#     """, unsafe_allow_html=True)

# import streamlit as st
# import pandas as pd
# import pickle
# import base64
# import matplotlib.pyplot as plt
# import seaborn as sns

# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url(data:image/png;base64,{encoded_string.decode()});
#             background-size: cover;
#             background-attachment: fixed;
#         }}
#         .content-block {{
#             background-color: rgba(0, 0, 0, 0.8);  /* Black background with 80% opacity */
#             color: white;  /* White text color for better readability */
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
#         }}
#         .recommendation-block {{
#             background-color: rgba(255, 255, 255, 0.8);  /* White background with 80% opacity */
#             color: black;  /* Black text color for better readability */
#             padding: 10px;
#             margin-bottom: 10px;
#             border-radius: 5px;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def load_data():
#     with open('anime_data.pkl', 'rb') as f:
#         df_encoded = pickle.load(f)
#     with open('similarity_matrix.pkl', 'rb') as f:
#         similarity_matrix = pickle.load(f)
#     return df_encoded, similarity_matrix

# def load_svd_model():
#     with open('svd_best_model.pkl', 'rb') as f:
#         svd_model = pickle.load(f)
#     return svd_model

# df_encoded, similarity_matrix = load_data()
# svd_model = load_svd_model()

# def get_content_based_recommendations(anime_name, similarity_matrix, df_encoded, top_n=3, threshold=0.5):
#     try:
#         idx = df_encoded[df_encoded['name'].str.lower() == anime_name.lower()].index[0]
#         sim_scores = list(enumerate(similarity_matrix[idx]))
#         sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#         sim_scores = sim_scores[1:top_n+1]
#         similar_indices = [i[0] for i in sim_scores if i[1] >= threshold]
#         return df_encoded[['name', 'genre', 'type']].iloc[similar_indices].to_dict(orient='records')
#     except IndexError:
#         print(f"Anime '{anime_name}' not found in the dataset.")
#         return []

# def get_collaborative_recommendations(user_id, df_encoded, svd_model, top_n=3):
#     user_ratings = df_encoded[df_encoded['user_id'] == user_id]
#     user_unrated = df_encoded[~df_encoded['anime_id'].isin(user_ratings['anime_id'])]

#     user_unrated['est_rating'] = user_unrated['anime_id'].apply(lambda x: svd_model.predict(user_id, x).est)
#     top_recommendations = user_unrated.sort_values('est_rating', ascending=False).head(top_n)

#     return top_recommendations[['name', 'genre', 'type']].to_dict(orient='records')

# # Sidebar navigation
# st.sidebar.title('Navigation')
# page = st.sidebar.radio('Go to', ['Content-Based Recommendation System', 'Collaborative-Based Recommendation System', 'Exploratory Data Analysis', 'About Us', 'Contact Us'])

# # Add the background image at the beginning of your app
# add_bg_from_local('Screen+Shot+2023-04-22+at+3.50.40+PM.png')

# if page == 'Content-Based Recommendation System':
#     st.title('Content-Based Recommendation System')
#     st.text('Get recommendations based on anime content similarity.')

#     st.markdown("""
#     <div class="content-block">
#     <h2>Content-Based Recommendation System</h2>
#     <p>Get recommendations based on anime content similarity.</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     anime_names = df_encoded['name'].unique()
#     selected_anime = st.selectbox('Select or start typing an anime name:', anime_names)

#     if st.button('Get Content-Based Recommendations'):
#         if selected_anime:
#             recommendations = get_content_based_recommendations(selected_anime, similarity_matrix, df_encoded)
#             if recommendations:
#                 st.subheader('Recommended Anime:')
#                 for anime in recommendations:
#                     st.markdown(f"""
#                     <div class="recommendation-block">
#                     **{anime['name']}**

#                     * **Genre:** {', '.join(anime['genre'])}
#                     * **Type:** {anime['type']}
#                     </div>
#                     """, unsafe_allow_html=True)
#             else:
#                 st.write(f"No recommendations above the threshold (0.5) found for '{selected_anime}'.")
#         else:
#             st.warning('Please select an anime.')

# elif page == 'Collaborative-Based Recommendation System':
#     st.title('Collaborative-Based Recommendation System')
#     st.text('Get recommendations based on user ratings.')

#     st.markdown("""
#     <div class="content-block">
#     <h2>Collaborative-Based Recommendation System</h2>
#     <p>Get recommendations based on user ratings.</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     user_ids = df_encoded['user_id'].unique()
#     selected_user_id = st.selectbox('Select or start typing a user ID:', user_ids)

#     if st.button('Get Collaborative-Based Recommendations'):
#         if selected_user_id:
#             recommendations = get_collaborative_recommendations(selected_user_id, df_encoded, svd_model)
#             if recommendations:
#                 st.subheader('Recommended Anime:')
#                 for anime in recommendations:
#                     st.markdown(f"""
#                     <div class="recommendation-block">
#                     **{anime['name']}**

#                     * **Genre:** {', '.join(anime['genre'])}
#                     * **Type:** {anime['type']}
#                     </div>
#                     """, unsafe_allow_html=True)
#             else:
#                 st.write(f"No recommendations found for user ID '{selected_user_id}'.")
#         else:
#             st.warning('Please select a user ID.')

# elif page == 'Exploratory Data Analysis':
#     st.title('Exploratory Data Analysis')

#     st.subheader('Genre Distribution')
#     genre_counts = df_encoded['genre'].explode().value_counts()
#     st.bar_chart(genre_counts)

#     st.subheader('Type Distribution')
#     type_counts = df_encoded['type'].value_counts()
#     st.bar_chart(type_counts)


# elif page == 'About Us':
#     st.title('About Us')
#     st.markdown("""
#     <div class="content-block">
#     <h2>About The Otaku Oracle</h2>
#     <p>The Otaku Oracle is a recommendation system designed to help anime fans discover new anime to watch based on their preferences. Our system uses advanced machine learning algorithms to provide personalized recommendations.
#     OUR TEAM
#     Thandekile Sikhakhane 
#     Chuma Gqola
#     Ndivho Mamphiswana
#     Lebogang Malata</p>
#     </div>
#     """, unsafe_allow_html=True)


# elif page == 'Contact Us':
#     st.markdown("""
#     <h1 style="color: black;">Contact Us</h1>
#     <div class="content-block">
#     <p>If you have any questions or feedback, feel free to reach out to us at:</p>
#     <p>Email: support@otakuoracle.com</p>
#     <p>Phone: +1234567890</p>
#     </div>
#     """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import pickle
import base64
import matplotlib.pyplot as plt
import seaborn as sns
from surprise import SVD

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string.decode()});
            background-size: cover;
            background-attachment: fixed;
        }}
        .content-block {{
            background-color: rgba(0, 0, 0, 0.8);  /* Black background with 80% opacity */
            color: white;  /* White text color for better readability */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }}
        .recommendation-block {{
            background-color: rgba(255, 255, 255, 0.8);  /* White background with 80% opacity */
            color: black;  /* Black text color for better readability */
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def load_data():
    with open('anime_data.pkl', 'rb') as f:
        df_encoded = pickle.load(f)
    with open('similarity_matrix.pkl', 'rb') as f:
        similarity_matrix = pickle.load(f)
    return df_encoded, similarity_matrix

def load_svd_model():
    with open('svd_best_model.pkl', 'rb') as f:
        svd_model = pickle.load(f)
    return svd_model

df_encoded, similarity_matrix = load_data()
svd_model = load_svd_model()

def get_content_based_recommendations(anime_name, similarity_matrix, df_encoded, top_n=3, threshold=0.5):
    try:
        idx = df_encoded[df_encoded['name'].str.lower() == anime_name.lower()].index[0]
        sim_scores = list(enumerate(similarity_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_n+1]
        similar_indices = [i[0] for i in sim_scores if i[1] >= threshold]
        return df_encoded[['name', 'genre', 'type']].iloc[similar_indices].to_dict(orient='records')
    except IndexError:
        st.warning(f"Anime '{anime_name}' not found in the dataset.")
        return []

def get_collaborative_recommendations(user_id, df_encoded, svd_model, top_n=3):
    user_ratings = df_encoded[df_encoded['anime_id'] == user_id]
    user_unrated = df_encoded[~df_encoded['anime_id'].isin(user_ratings['anime_id'])]

    user_unrated['est_rating'] = user_unrated['anime_id'].apply(lambda x: svd_model.predict(user_id, x).est)
    top_recommendations = user_unrated.sort_values('est_rating', ascending=False).head(top_n)

    return top_recommendations[['name', 'genre', 'type']].to_dict(orient='records')

# Sidebar navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Content-Based Recommendation System', 'Collaborative-Based Recommendation System', 'Exploratory Data Analysis', 'About Us', 'Contact Us'])

# Add the background image at the beginning of your app
add_bg_from_local('Screen+Shot+2023-04-22+at+3.50.40+PM.png')

if page == 'Content-Based Recommendation System':
    
    st.markdown("""
    <div class="content-block">
    <h2>Content-Based Recommendation System</h2>
    <p>Get recommendations based on anime content similarity.</p>
    </div>
    """, unsafe_allow_html=True)
    
    anime_names = df_encoded['name'].unique()
    selected_anime = st.selectbox('Select or start typing an anime name:', anime_names)

    if st.button('Get Content-Based Recommendations'):
        if selected_anime:
            recommendations = get_content_based_recommendations(selected_anime, similarity_matrix, df_encoded)
            if recommendations:
                st.subheader('Recommended Anime:')
                for anime in recommendations:
                    st.markdown(f"""
                    <div class="recommendation-block">
                    **{anime['name']}**

                    * **Genre:** {', '.join(anime['genre'])}
                    * **Type:** {anime['type']}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.write(f"No recommendations above the threshold (0.5) found for '{selected_anime}'.")
        else:
            st.warning('Please select an anime.')

elif page == 'Collaborative-Based Recommendation System':

    st.markdown("""
    <div class="content-block">
    <h2>Collaborative Based Recommendation System</h2>
    <p>Get recommendations based on user ratings.</p>
    </div>
    """, unsafe_allow_html=True)
    
    anime_ids = df_encoded['anime_id'].unique()
    selected_user_id = st.selectbox('Select or start typing a user ID:', anime_ids)

    if st.button('Get Collaborative-Based Recommendations'):
        if selected_user_id:
            recommendations = get_collaborative_recommendations(selected_user_id, df_encoded, svd_model)
            if recommendations:
                st.subheader('Recommended Anime:')
                for anime in recommendations:
                    st.markdown(f"""
                    <div class="recommendation-block">
                    **{anime['name']}**

                    * **Genre:** {', '.join(anime['genre'])}
                    * **Type:** {anime['type']}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.write(f"No recommendations found for user ID '{selected_user_id}'.")
        else:
            st.warning('Please select a anime ID.')

elif page == 'Exploratory Data Analysis':
    st.title('Exploratory Data Analysis')

    st.subheader('Genre Distribution')
    genre_counts = df_encoded['genre'].explode().value_counts()
    st.bar_chart(genre_counts)

    st.subheader('Type Distribution')
    type_counts = df_encoded['type'].value_counts()
    st.bar_chart(type_counts)

elif page == 'About Us':
    st.markdown("""
    <style>
    .team-member {
        border: 1px solid #000;
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
        background-color: #000;
        color: white;
    }
    .team-member h2 {
        margin: 0;
        font-size: 1.2em;
    }
    .team-member p {
        margin: 5px 0 0;
    }
    .description {
        color: white;
    }
    </style>
    <h1 style="color: black;">About Us</h1>
    <div class="content-block">
    <p class="description">The Otaku Oracle is a recommendation system designed to help anime fans discover new anime to watch based on their preferences. Our system uses advanced machine learning algorithms to provide personalized recommendations.</p>
    
    <div class="team-member">
        <h2>Thandekile Sikhakhane</h2>
        <p>Thandekile is a data scientist with a passion for anime and machine learning. She is responsible for developing the recommendation algorithms.</p>
    </div>
    <div class="team-member">
        <h2>Chuma Gqola</h2>
        <p>Chuma specializes in backend development and ensures that our system runs smoothly and efficiently. Her love for anime drives her to create the best user experience.</p>
    </div>
    <div class="team-member">
        <h2>Ndivho Mamphiswana</h2>
        <p>Ndivho is an expert in data analysis and visualization. He is responsible for analyzing user data to improve our recommendation system continuously.</p>
    </div>
    <div class="team-member">
        <h2>Lebogang Malata</h2>
        <p>Lebogang focuses on the frontend design and user interface of The Otaku Oracle. She ensures that the platform is user-friendly and visually appealing.</p>
    </div>
    <div class="team-member">
        <h2>Nomkhosi Sibiya</h2>
        <p>Nomkhosi is a content strategist who curates the anime database and ensures that the recommendations align with the latest trends in the anime community.</p>
    </div>
    <div class="team-member">
        <h2>Thapelo Raphala</h2>
        <p>Thapelo is a machine learning engineer with a keen interest in natural language processing. He works on refining the algorithms that power our recommendation system.</p>
    </div>
    </div>
    """, unsafe_allow_html=True)

elif page == 'Contact Us':
    st.markdown("""
    <h1 style="color: black;">Contact Us</h1>
    <div class="content-block">
    <p>If you have any questions or feedback, feel free to reach out to us at:</p>
    <p>Email: support@otakuoracle.com</p>
    <p>Phone: +1234567890</p>
    </div>
    """, unsafe_allow_html=True)
