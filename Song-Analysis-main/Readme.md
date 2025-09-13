# 🎶 Song Popularity Prediction

A complete end-to-end data science project focused on understanding the patterns behind a song’s popularity using real-world audio and platform-level data — and building a predictive model to estimate Spotify stream counts.

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







