import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Model Training Results", layout="wide")
st.title("📈 Model Training Results")

st.markdown("## ⚙️ Before Log Transformation")

st.markdown("### 🔁 Single Train-Test Split")
st.code("""
Model: LinearRegression
MAE : 186,665,575.46
MSE : 70,164,083,509,558,752.00
R²  : 0.71
------------------------------
Model: RandomForestRegressor
MAE : 133,711,848.62
MSE : 43,282,841,307,622,696.00
R²  : 0.82
------------------------------
Model: XGBRegressor
MAE : 136584608.00
MSE : 44398928069656576.00
R²  : 0.82
------------------------------
""", language='text')

st.markdown("### 📊 Cross-Validation (5-Fold)")
st.code("""
Model: LinearRegression
Mean R² : 0.58
Mean MAE: 211,822,873.16
Mean MSE: 103,002,216,302,624,640.00
------------------------------
Model: RandomForestRegressor
Mean R² : 0.71
Mean MAE: 167,541,351.68
Mean MSE: 69,794,061,190,678,208.00
------------------------------
Model: XGBRegressor
Mean R² : 0.80
Mean MAE: 150190956.80
Mean MSE: 64537216253794712.00
------------------------------
""", language='text')

st.markdown("---")
st.markdown("## 🔁 After Log Transformation (Improved Stability & Reduced Skew)")

st.markdown("### 🔁 Single Train-Test Split")
st.code("""
Model: LinearRegression
MAE : 0.55
MSE : 0.49
R²  : 0.52
------------------------------
Model: RandomForestRegressor
MAE : 0.36
MSE : 0.22
R²  : 0.79
------------------------------
Model: XGBRegressor
MAE : 0.37
MSE : 0.23
R²  : 0.78
------------------------------
""", language='text')

st.markdown("### 📊 Cross-Validation (5-Fold)")
st.code("""
Model: LinearRegression
Mean R² : 0.46
Mean MAE: 0.61
Mean MSE: 0.77
------------------------------
Model: RandomForestRegressor
Mean R² : 0.73
Mean MAE: 0.36
Mean MSE: 0.42
------------------------------
Model: XGBRegressor
Mean R² : 0.67
Mean MAE: 0.37
Mean MSE: 0.48
------------------------------
""", language='text')

st.markdown("---")
st.markdown("## 🧠 Feature Importance Visualizations")

image_dir = "images"

def show_image(image_file, caption):
    image_path = os.path.join(image_dir, image_file)
    image = Image.open(image_path)
    st.image(image, caption=caption, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    show_image("Random Forest Feature Importance.png", "🔍 Random Forest Feature Importance")

with col2:
    show_image("XGRegressor Feature Importance.png", "📌 XGBoost Feature Importance")

st.markdown("""
### 🧠 Final Observations

- **Playlist Features Dominate**: `in_spotify_playlists`, `in_spotify_charts`, and `in_apple_playlists` are the strongest contributors.
- **Tempo/Energy-Driven Features** like `danceability`, `energy`, and `valence` show moderate influence.
- **Low Impact Features** like `key`, `mode`, and `speechiness` had minimal impact.
- **Model Choice**: RandomForest offered the best performance and generalizability with acceptable MAE after log transformation.
""")
