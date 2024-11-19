#Imports
import streamlit as st
import requests
import time
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to fetch top animes by genre with caching
@st.cache_data
def fetch_animes_by_genre(genre_id, limit=25):
    url = f"https://api.jikan.moe/v4/anime?genres={genre_id}&limit={limit}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if 'data' in data:
            return data['data']
        else:
            st.error("Error: 'data' key not found in API response")
            return []
    except requests.RequestException as e:
        st.error(f"Request failed: {e}")
        return []

# Function to fetch all animes with caching
@st.cache_data
def fetch_all_animes(max_pages=5):
    all_animes = []
    url = "https://api.jikan.moe/v4/anime?page="
    page = 1
    while page <= max_pages:
        try:
            response = requests.get(url + str(page))
            if response.status_code == 429:
                st.warning("Rate limit exceeded. Waiting before retrying...")
                time.sleep(60)  # Wait for a minute before retrying
                continue
            response.raise_for_status()
            data = response.json()
            if 'data' in data and data['data']:
                all_animes.extend(data['data'])
                page += 1
            else:
                break
        except requests.RequestException as e:
            st.error(f"Request failed: {e}")
            break
    return all_animes

# Function to fetch genres with caching
@st.cache_data
def fetch_genres():
    url = "https://api.jikan.moe/v4/genres/anime"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if 'data' in data:
            return data['data']
        else:
            st.error("Error: 'data' key not found in API response")
            return []
    except requests.RequestException as e:
        st.error(f"Request failed: {e}")
        return []

# Function to clean synopsis by removing unwanted text
def clean_synopsis(synopsis):
    clean_text = synopsis.split('[Written by MAL Rewrite]')[0]
    return clean_text.strip()

# Function to display the list of animes in a dropdown
def display_animes(anime_list, widget_key_prefix):
    if not anime_list:
        st.write("No anime found.")
        return None

    st.markdown("### Top Animes")
    anime_titles = [anime['title'] for anime in anime_list]

    # Dropdown (selectbox) to choose an anime
    selected_anime_title = st.selectbox("Select an Anime", anime_titles, key=f"{widget_key_prefix}_anime_selector")

    # Find the selected anime based on its title
    selected_anime = next((anime for anime in anime_list if anime['title'] == selected_anime_title), None)

    if selected_anime:
        st.session_state.selected_anime_id = selected_anime['mal_id']  # Store the selected anime ID in session state
        st.image(selected_anime['images']['jpg']['image_url'], width=200)
        st.write(selected_anime['title'])
        return selected_anime

# Function to get details of a specific anime with retry logic
def display_anime_details(anime_id):
    url = f"https://api.jikan.moe/v4/anime/{anime_id}"
    attempt = 0
    while attempt < 3:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if 'data' in data:
                anime = data['data']
                st.markdown(f"## {anime['title']}")
                st.image(anime['images']['jpg']['large_image_url'], use_column_width=True)
                st.markdown(f"**Rating:** {anime.get('score', 'N/A')}")
                st.markdown(f"**Episodes:** {anime.get('episodes', 'N/A')}")
                st.markdown(f"**Synopsis:** {clean_synopsis(anime.get('synopsis', 'No synopsis available.'))}")
                st.markdown(f"**Type:** {anime.get('type', 'N/A')}")
                st.markdown(f"**Status:** {anime.get('status', 'N/A')}")
                st.markdown(f"**Aired:** {anime.get('aired', {}).get('string', 'N/A')}")
                st.markdown(f"**Duration:** {anime.get('duration', 'N/A')}")
                st.markdown(f"**Genres:** {', '.join(genre['name'] for genre in anime.get('genres', []))}")
                st.markdown(f"**Producers:** {', '.join(producer['name'] for producer in anime.get('producers', []))}")
                st.markdown(f"**Studios:** {', '.join(studio['name'] for studio in anime.get('studios', []))}")
                st.markdown(f"**Source:** {anime.get('source', 'N/A')}")
                st.markdown(f"**Rating:** {anime.get('rating', 'N/A')}")
                st.markdown(f"**Popularity:** {anime.get('popularity', 'N/A')}")
                st.markdown(f"**Members:** {anime.get('members', 'N/A')}")
                st.markdown(f"**Favorites:** {anime.get('favorites', 'N/A')}")
                if anime.get('trailer') and anime['trailer'].get('embed_url'):
                    st.video(anime['trailer']['embed_url'])
                else:
                    st.write("No trailer available.")
                return anime
            else:
                st.write("No details found for this anime.")
                return None
        except requests.RequestException as e:
            st.error(f"Request failed: {e}")
            attempt += 1
            time.sleep(2)  # wait before retrying
    st.write("Failed to fetch anime details after several attempts.")
    return None

# Function to recommend animes based on genres
def recommend_animes_based_on_genres(searched_anime, all_animes):
    df = pd.DataFrame(all_animes)
    if df.empty:
        st.write("No animes available for recommendations.")
        return []

    # Create a combined genre string for each anime
    df['genres_combined'] = df['genres'].apply(lambda x: ' '.join(genre['name'] for genre in x))
    
    # Create a TF-IDF vectorizer and fit it on the anime genres
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['genres_combined'])
    
    # Calculate the cosine similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Find the index of the searched anime
    idx = df.index[df['mal_id'] == searched_anime['mal_id']].tolist()
    if not idx:
        return []
    
    idx = idx[0]
    
    # Get similarity scores for the searched anime
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort by similarity and exclude the searched anime itself
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = [i for i in sim_scores if i[0] != idx]
    
    # Get the top 5 recommendations
    top_indices = [i[0] for i in sim_scores[:5]]
    recommendations = df.iloc[top_indices]
    
    return recommendations.to_dict('records')

# Function to search for an anime by title with caching and display related entries
@st.cache_data
def search_anime(title):
    url = f"https://api.jikan.moe/v4/anime?q={title}&limit=10"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if 'data' in data and data['data']:
            return data['data']
        else:
            st.write("No anime found with that title.")
            return []
    except requests.RequestException as e:
        st.error(f"Request failed: {e}")
        return []

# Main function to run the Streamlit app
def main():
    st.title("🌟 Anime Explorer 🌟")
    st.markdown("Welcome to the Anime Explorer! Discover top animes and search for your favorites.")

    # Initialize session state
    if 'selected_anime_id' not in st.session_state:
        st.session_state.selected_anime_id = None
    if 'search_results' not in st.session_state:
        st.session_state.search_results = None
    
    # Fetch genres and create genre selector
    genres = fetch_genres()
    if genres:
        genre_options = [genre['name'] for genre in genres]
        genre_selected = st.selectbox("Select Genre", genre_options, key="genre_selector")
        
        genre_id = next((genre['mal_id'] for genre in genres if genre['name'] == genre_selected), None)
        if genre_id:
            animes = fetch_animes_by_genre(genre_id)
            if animes:
                display_animes(animes, widget_key_prefix="genre")
            else:
                st.write("No anime data available.")
        else:
            st.write("Invalid genre selected.")
    
    # Search functionality
    col1, col2 = st.columns([4, 1])
    with col1:
        search_query = st.text_input("Search for an anime", key="search_input")
    with col2:
        search_button = st.button("Search", key="search_button")

    if search_button and search_query:
        st.session_state.search_results = search_anime(search_query)
        if st.session_state.search_results:
            for anime in st.session_state.search_results:
                st.session_state.selected_anime_id = anime['mal_id']
                selected_anime = display_anime_details(anime['mal_id'])
                
                if selected_anime:
                    # Fetch all anime data for recommendations
                    all_animes = fetch_all_animes()
                    if all_animes:
                        recommendations = recommend_animes_based_on_genres(selected_anime, all_animes)
                        if recommendations:
                            st.markdown("### Recommendations")
                            for rec in recommendations:
                                st.image(rec['images']['jpg']['image_url'], width=200)
                                st.write(rec['title'])
                        else:
                            st.write("No recommendations found.")
                    else:
                        st.write("Failed to fetch all animes for recommendations.")
        else:
            st.write("No anime found with that title.")
    
    # Display details for selected anime (if any)
    if st.session_state.selected_anime_id and not st.session_state.search_results:
        selected_anime = display_anime_details(st.session_state.selected_anime_id)
        if selected_anime:
            # Fetch all anime data for recommendations
            all_animes = fetch_all_animes()
            if all_animes:
                recommendations = recommend_animes_based_on_genres(selected_anime, all_animes)
                if recommendations:
                    st.markdown("### Recommendations")
                    for rec in recommendations:
                        st.image(rec['images']['jpg']['image_url'], width=200)
                        st.write(rec['title'])
                else:
                    st.write("No recommendations found.")
            else:
                st.write("Failed to fetch all animes for recommendations.")

if __name__ == "__main__":
    main()
