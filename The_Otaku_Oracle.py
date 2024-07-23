import streamlit as st
import pandas as pd
import pickle
import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
        background-size: cover;
    }}
    </style>
    """,
        unsafe_allow_html=True
    )
    
#Add the background image at the beginning of your app
add_bg_from_local('Background_image.jpeg')  # Make sure the image is in the same directory  



# Load data and similarity matrix
@st.cache_data  
def load_data():
    with open('anime_data.pkl', 'rb') as f:
        df_encoded = pickle.load(f)
    with open('similarity_matrix.pkl', 'rb') as f:
        similarity_matrix = pickle.load(f)

    return df_encoded, similarity_matrix

df_encoded, similarity_matrix = load_data()

### Recommender Function
def get_recommendations(anime_name, similarity_matrix, df_encoded, top_n=3, threshold=0.5):
    try:
        idx = df_encoded[df_encoded['name'].str.lower() == anime_name.lower()].index[0]
        sim_scores = list(enumerate(similarity_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_n+1]
        similar_indices = [i[0] for i in sim_scores if i[1] >= threshold]
        return df_encoded[['name', 'genre', 'type']].iloc[similar_indices].to_dict(orient='records')  # Return dict for easier display

    except IndexError:
        print(f"Anime '{anime_name}' not found in the dataset.")
        return []

 #The start of the App
st.title('The Otaku Oracle')
st.text('Your Anime Recommender')

# Autocomplete Anime Selection
anime_names = df_encoded['name'].unique()  # Get all unique anime names
selected_anime = st.selectbox('Select or start typing an anime name:', anime_names)

if st.button('Get Recommendations'):
    if selected_anime:
        recommendations = get_recommendations(selected_anime, similarity_matrix, df_encoded) # Use the recommender function to make recomendations.
        if recommendations:
            st.subheader('Recommended Anime:')
            for anime in recommendations:
                st.markdown(f"""
                **{anime['name']}**

                * **Genre:** {', '.join(anime['genre'])}
                * **Type:** {anime['type']}
                """)  # Display more information
        else:
            st.write(f"No recommendations above the threshold (0.5) found for '{selected_anime}'.")
    else:
        st.warning('Please select an anime.')
