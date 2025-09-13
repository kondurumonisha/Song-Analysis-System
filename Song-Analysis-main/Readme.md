# 🎶 Song Popularity Prediction

A complete end-to-end data science project focused on understanding the patterns behind a song’s popularity using real-world audio and platform-level data — and building a predictive model to estimate Spotify stream counts.

---
### Live Link: [https://song-analysis-data-science-project.streamlit.app/]
---

## 📁 Project Structure

```bash
.
├── assets/
│   └── images/                # All EDA & feature importance visualizations
├── models/
│   └── random_forest_log_model.pkl   # Final saved model
├── notebook/
│   └── song_popularity_analysis.ipynb  # All EDA + model dev in notebook
├── pages/
│   ├── 1_EDA_Insights.py
│   ├── 2_Model_Training.py
│   ├── 3_Prediction_Tool.py
│   └── 4_Project_Summary.py
├── utils/
│   └── (optional helper scripts)
├── Home_Page.py               # Landing page for the Streamlit app
└── requirements.txt
```

---

## 🧠 Problem Statement

Music streaming platforms like Spotify and Apple Music host millions of tracks, but only a small percentage become viral or popular. This project aims to analyze what drives song popularity, and build a predictive tool that can estimate a song's success (in terms of streams) based on audio features and platform-level metadata.

---

## ⚙️ Tech Stack

- **Languages:** Python
- **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost, joblib, streamlit
- **Deployment:** Streamlit web app (local or cloud)
- **Modeling:**
    - Linear Regression
    - Random Forest Regressor
    - XGBoost Regressor

---

## 📊 Key Highlights

### 🔍 Exploratory Data Analysis (EDA)
- Distribution and seasonality of stream counts
- Role of playlists & platform visibility
- Correlation heatmaps and feature vs. streams trends
- Audio trait impacts (danceability, energy, valence, etc.)

### 🏗️ Modeling
- Tried 3 models before and after log transformation
- Trained with and without cross-validation
- Random Forest after log transformation gave the best results (R² ≈ 0.79)

### 📈 Feature Importance
- Playlist presence on Spotify, Apple had the highest predictive power
- Audio features like energy & danceability had moderate importance

### 🌐 Streamlit App
Fully modular multi-page dashboard:
- Landing page with author & process
- EDA insights page with visualizations
- Model training results page
- Live prediction tool
- Final summary for stakeholders

### 🔮 Prediction Tool
Users can input custom values for:
- Audio features (danceability, energy, etc.)
- Platform metrics (playlist/chart presence)
- Release details (month, year, etc.)
- And get predicted stream counts, backed by the trained ML model.

---

## 💼 Business Implications

- Helps A&R teams scout high-potential songs
- Assists marketing teams in planning release schedules
- Reveals the platform strategy impact on song success
- Shows how audio traits can boost playlist compatibility

---

## 🚀 Getting Started

1. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Streamlit app:**
    ```bash
    streamlit run Home_Page.py
    ```

This will launch the interactive dashboard in your browser.

---

## ✨ Author

**Advait Joshi**  
AI Engineer Intern @DRDO | Research Intern @IIT Kanpur, IIT Patna | Blockchain Developer Intern @Inspiring Wave | SVIT CSE(DS) '2027   
[LinkedIn](https:/www.linkedin.com/in/advaitszone)

---

## 🧾 License

This project is open for educational and non-commercial use. Feel free to fork and customize it!


