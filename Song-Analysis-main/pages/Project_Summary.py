import streamlit as st

st.set_page_config(page_title="Project Summary", layout="wide")
st.title("Project Summary")

st.markdown("""
## Problem Statement

The goal of this project was to analyze and predict the **popularity of songs on streaming platforms** such as Spotify, Apple Music, and Deezer. The key metric used was the number of Spotify streams. By leveraging audio features and platform presence data, we aimed to identify which factors influence a song’s streaming success and build a reliable regression model to estimate future song popularity.

---

## Methodology Followed

We followed a typical data science lifecycle structured into the following phases:

### 1. Data Exploration and Cleaning
- Removed unnecessary columns such as track names and artist names to avoid NLP-based influence.
- Checked for missing values and cleaned the dataset.
- Performed exploratory analysis to visualize feature distributions and relationships with the target (`streams`).

### 2. Data Transformation
- Observed heavy right-skew in the `streams` distribution.
- Applied log transformation to reduce skew and improve model performance on outliers.

### 3. Model Training
- Trained three regression models: Linear Regression, Random Forest, and XGBoost.
- Evaluated models using R², MAE, and MSE.
- Performed cross-validation to assess generalizability.

### 4. Feature Importance
- Extracted and visualized feature importance scores for Random Forest and XGBoost.
- Identified which features most strongly influence predictions.

### 5. Model Deployment
- Saved the best performing model (Random Forest after log transformation).
- Built a clean and interactive front-end using Streamlit for predictions and data exploration.

---

## Key Learnings and Insights

- **Platform presence** (especially Spotify playlists and charts) is a strong predictor of success.
- **Audio features** like energy, danceability, and tempo show moderate predictive power.
- Song metadata such as **release month** and **artist count** influence popularity trends.
- Pure musical features like key and mode had **less direct impact** on performance.

---

## Business Implications

- Early playlist traction can act as a **signal for marketing investment**.
- Understanding platform influence allows **A&R and marketing teams** to plan better campaigns.
- Release timing, energy, and exposure data can be used to **forecast breakout tracks** and improve ROI on promotions.

---

## Next Steps

- Incorporate additional sources (e.g., YouTube, TikTok trends) for richer prediction signals.
- Experiment with ensemble models or neural networks for better accuracy.
- Enable bulk predictions and CSV export functionality.
- Monitor model drift and retrain periodically with updated data.

---

This project offers both **technical insight** and **business value**, showcasing how data-driven analysis can support decision-making in the music industry.
""")
