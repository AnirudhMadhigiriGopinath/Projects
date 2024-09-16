# Anime Explorer

Anime Explorer is a web application built with Streamlit that allows users to explore and discover anime based on genres, search for specific titles, and receive recommendations. The app leverages the Jikan API to fetch anime data and uses machine learning techniques for recommendations.

## Features

- **Explore Animes by Genre**: Select a genre to view top animes.
- **Search Functionality**: Search for animes by title.
- **Detailed Anime Information**: View detailed information about selected animes.
- **Anime Recommendations**: Get recommendations based on genre similarity.

## Installation

### Prerequisites

- Python 3.7 or later
- pip (Python package manager)
- Streamlit, and sci-kit

### Steps

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate

### Install Dependencies

### Install the required Python packages using pip:

   bash
   pip install -r requirements.txt

### If requirements.txt is not provided, you can manually install the necessary packages:

   bash
   pip install streamlit requests pandas scikit-learn
   Start the Streamlit Server.

### Run the Streamlit application using the following command:

   bash
   streamlit run anime_explorer.py

## Interact with the Application

-Select a Genre: Use the dropdown to select a genre and view top animes.
-Search for an Anime: Enter an anime title in the search box and click "Search" to find specific animes.
-View Details: Click on an anime to view detailed information.
-Get Recommendations: After viewing details, recommendations based on genre similarity will be displayed.

## Code Overview

### Main Components
-Data Fetching Functions: Functions to fetch animes and genres using the Jikan API.
-Display Functions: Functions to display animes and their details.
-Recommendation System: Uses TF-IDF and cosine similarity to recommend animes.
-Search Functionality: Allows users to search for animes by title.

### Key Functions
-fetch_animes_by_genre: Fetches top animes by genre.
-fetch_all_animes: Fetches a list of all animes for recommendations.
-fetch_genres: Fetches available anime genres.
-display_animes: Displays a list of animes for selection.
-display_anime_details: Shows detailed information about a selected anime.
-recommend_animes_based_on_genres: Recommends animes based on genre similarity.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
