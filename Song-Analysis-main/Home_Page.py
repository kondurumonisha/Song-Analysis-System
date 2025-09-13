import streamlit as st
from PIL import Image

# Page config
st.set_page_config(
    page_title="🎵 Song Popularity Dashboard",
    layout="wide"
)

# Centered Title
st.markdown("<h1 style='text-align: center; color: #4A4A4A;'>🎵 Song Popularity Prediction Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>An end-to-end Data Science project on music analytics</p>", unsafe_allow_html=True)
st.write("")


# Optional: Banner image at the top
image = Image.open("images/banner.jpg")
resized_image = image.resize((1000, 400))  # Adjust dimensions as needed (width, height)

st.image(resized_image)


# Author section
with st.container():
    st.markdown("### 👤 Author")
    st.markdown("""
    - **Name:** Advait Joshi  
    - **Bio:** AI Engineer Intern @DRDO | Research Intern @IIT Kanpur, IIT Patna | Blockchain Developer Intern @Inspiring Wave | SVIT CSE(DS) '2027  
    - **Linkedin:** [Advait Joshi](https:/www.linkedin.com/in/advaitszone)  
    - **Project Goal:** Showcase complete data science workflow from analysis to deployment.
    """)

# Problem Statement
st.markdown("---")
st.markdown("### 🧩 Problem Statement")
st.markdown("""
As a data scientist at a music streaming company, your task is to analyze the key **musical** and **platform-related** features that influence a song’s popularity in 2023.

We aim to:
- Predict the popularity of a song based on its **audio** and **platform** attributes.
- Provide **actionable insights** to the **Marketing** and **A&R teams**.
- Help with playlist curation, cross-platform promotion, and artist scouting decisions.
""")

# Project Workflow
st.markdown("---")
st.markdown("### 🔍 Project Workflow")
st.markdown("""
We followed the complete data science lifecycle:

1. **Understanding the Dataset**  
   - Explored each feature, cleaned, and converted necessary columns.

2. **EDA (Exploratory Data Analysis)**  
   - Used graphs and charts to derive deep insights.
   - Tackled questions relevant to marketing and A&R teams.

3. **Model Building**  
   - Trained multiple regression models: `Linear Regression`, `Random Forest`, and `XGBoost`.
   - Compared performance using both raw and log-transformed data.

4. **Evaluation**  
   - Used metrics like MAE, MSE, R², and Cross-Validation scores.
   - Chose the best performing model for deployment.

5. **Deployment**  
   - Built this frontend using **Streamlit**.
   - Added prediction capability and summarized insights.
""")

# Final Message
st.markdown("---")
st.success("Use the sidebar to navigate through insights, model training, predictions, and final takeaways.")