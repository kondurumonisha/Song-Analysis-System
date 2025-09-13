import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Predict Song Streams", layout="wide")
st.title("🧠 Predict Song Popularity")

st.markdown("""
Welcome to the **prediction page**!  
Fill in the song attributes below and our trained Random Forest model will estimate its expected number of streams (based on historical trends).

🔒 _Note: The model is trained on **log-transformed** stream counts for better generalization._
""")

# Load model
@st.cache_resource
def load_model():
    return joblib.load("models/random_forest_log_model.pkl")

model = load_model()

st.subheader("🔧 Song Attributes")

# Layout for input fields
col1, col2, col3 = st.columns(3)

with col1:
    artist_count = st.number_input("Number of Artists", min_value=1, max_value=10, value=1)
    released_year = st.selectbox("Release Year", options=range(2015, 2025), index=7)
    released_month = st.slider("Release Month", 1, 12, 6)
    released_day = st.slider("Release Day", 1, 31, 15)
    key_encoded = st.slider("Musical Key (Encoded)", 0, 11, 0)

with col2:
    in_spotify_playlists = st.slider("In Spotify Playlists", 0, 500, 30)
    in_spotify_charts = st.slider("In Spotify Charts", 0, 200, 5)
    in_apple_playlists = st.slider("In Apple Playlists", 0, 200, 3)
    in_apple_charts = st.slider("In Apple Charts", 0, 200, 2)
    in_deezer_playlists = st.slider("In Deezer Playlists", 0, 100, 1)

with col3:
    in_deezer_charts = st.slider("In Deezer Charts", 0, 100, 1)
    in_shazam_charts = st.slider("In Shazam Charts", 0.0, 100.0, 2.5)
    bpm = st.slider("Beats Per Minute (BPM)", 60, 200, 120)
    mode = st.radio("Mode", options=[0, 1], index=1, format_func=lambda x: "Minor" if x == 0 else "Major")
    danceability = st.slider("Danceability (%)", 0, 100, 70)
    valence = st.slider("Valence (%)", 0, 100, 60)
    energy = st.slider("Energy (%)", 0, 100, 65)
    acousticness = st.slider("Acousticness (%)", 0, 100, 15)
    instrumentalness = st.slider("Instrumentalness (%)", 0, 100, 10)
    liveness = st.slider("Liveness (%)", 0, 100, 20)
    speechiness = st.slider("Speechiness (%)", 0, 100, 5)

# Input DataFrame
input_df = pd.DataFrame({
    'artist_count': [artist_count],
    'released_year': [released_year],
    'released_month': [released_month],
    'released_day': [released_day],
    'in_spotify_playlists': [in_spotify_playlists],
    'in_spotify_charts': [in_spotify_charts],
    'in_apple_playlists': [in_apple_playlists],
    'in_apple_charts': [in_apple_charts],
    'in_deezer_playlists': [in_deezer_playlists],
    'in_deezer_charts': [in_deezer_charts],
    'in_shazam_charts': [in_shazam_charts],
    'bpm': [bpm],
    'mode': [mode],
    'danceability_%': [danceability],
    'valence_%': [valence],
    'energy_%': [energy],
    'acousticness_%': [acousticness],
    'instrumentalness_%': [instrumentalness],
    'liveness_%': [liveness],
    'speechiness_%': [speechiness],
    'key_encoded': [key_encoded]
})

st.markdown("---")

if st.button("🎯 Predict Number of Streams"):
    try:
        log_pred = model.predict(input_df)[0]
        predicted_streams = int(np.exp(log_pred))
        st.success(f"🎧 **Estimated Streams:** {predicted_streams:,}")
        st.caption("This prediction assumes distribution similar to the dataset and average platform visibility.")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
