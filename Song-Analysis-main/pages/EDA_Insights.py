import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="EDA Insights", layout="wide")

st.markdown("""
# 📊 EDA Insights

Welcome to the **Exploratory Data Analysis** section.  
Here we break down patterns that help explain what drives a song’s popularity on streaming platforms.
---
""")

image_dir = "images"

# --- Helper to show images aesthetically ---
def display_insight(image_filename, caption, insight_text, img_width=700):
    img_path = os.path.join(image_dir, image_filename)
    image = Image.open(img_path)
    image.thumbnail((img_width, img_width))
    
    st.markdown(f"### 🔍 {caption}")
    st.image(image, use_container_width=False)
    with st.expander("📝 Insight", expanded=True):
        st.markdown(insight_text)
    st.markdown("---")

# 1. Average Streams
display_insight(
    "Distribution of spotify streams.png",
    "Distribution of Average Streams",
    """**Insight**:   
    **Skewed Distribution:**
- The stream count distribution is heavily right-skewed.
→ Most songs have relatively low streams, but a few songs go viral and dominate.

**Real-World Pattern:**
- This mirrors the “winner-takes-most” trend in digital platforms like Spotify, YouTube, etc.

**Why It Matters for Modeling:**

- Models trained on such data can get biased by extreme values (outliers).

- These high-stream songs may mask the general trend in the rest of the dataset.

- To solve this, we later applied a log transformation on stream counts to:

        - Reduce skew

        - Improve learning

        - Focus on relative performance rather than absolute outliers

**Business Implications:**

- Since only a few songs achieve viral success, it's crucial to identify early breakout signals.

**Marketing & A&R teams can focus on:**

- Songs with rapid early playlist growth

- Cross-platform exposure trends

Promoting these potential hits early can have a huge ROI due to the unequal distribution of success."""
)

# 2. Boxplot by Key
display_insight(
    "correlation matrix.png",
    "Correlation Matrix of Numerical Features",
    """**Insight**:

**What We Analyzed:**
- We created a correlation heatmap to understand how each numerical feature in our dataset relates to "streams" (our target variable).
- It also helped us detect patterns or redundancies across features.

**Key Observations:**

- **Strongest Positive Correlations with Streams:**
    - `in_spotify_playlists` → 0.79
    - `in_spotify_charts` → 0.60
    - `in_apple_playlists`, `in_apple_charts`, and `in_shazam_charts` → moderate correlation  
    → These represent platform visibility — songs on charts/playlists are more likely to be streamed.

- **Moderate/Negative Correlations:**
    - `acousticness_%` and `instrumentalness_%` → mild negative correlation
    - `danceability_%` and `energy_%` → mildly positive  
    → More energetic, less acoustic songs tend to perform better.

- **Low/No Correlation:**
    - Features like `speechiness_%`, `liveness_%`, `key_encoded` showed little or no correlation with streams.
    - These may not be useful in linear models or may require complex modeling techniques.

**Why This Matters:**
- Shows which features truly influence popularity — critical for model performance.
- Helps prioritize feature selection and avoid redundancy (e.g., multicollinearity in regression).
- Informs business teams on what traits to focus on.

**Business Implications:**
- Playlist/chart inclusion (especially Spotify) strongly correlates with success.
    - Marketing teams should push for playlist placements.
    - A&R teams can track early playlist presence as a success indicator.
- Audio traits like energy and danceability support virality — useful for genre-focused promotion.

**Summary Takeaway:**
Correlation helps us filter signal from noise — and aligns both modeling efforts and business focus toward features that actually matter.

    """
)

# 3. Boxplot by Mode
display_insight(
    "feature vs, streams.png",
    " Scatterplots — Audio Features vs. Streams",
    """**Insight**: 

 **What We Looked At:**
 We plotted scatter plots for the features:
    - Danceability (%)
    - Valence (%)
    - Energy (%)
    against the number of streams to understand if these core audio traits influence popularity.

**Key Observations:**
    - Danceability & Energy:
        - Songs with moderate to high danceability and energy tend to have higher streams.
        - There isn’t a strong linear relationship, but the majority of top-streamed songs are in the 60–80% range for both.
        - However, there are also many songs in this range with average or low streams → so these features alone aren’t enough to predict success, but they play a supporting role.

    -  Valence (positivity):
        - The distribution is much wider here — some very positive (happy-sounding) songs are streamed a lot, but many aren't.
        - So, valence isn’t a clear indicator of popularity by itself.

**What This Tells Us:**
    - These features do matter, but not independently. They may work better as interacting variables in a model.
    - A song being energetic and danceable might make it playlist-friendly or suitable for certain moods, which could help it go viral — but only when backed by platform visibility.

**Business Use-Cases:**
    - The marketing team can boost promotion of songs with high danceability and energy in dance/workout or party playlists.
    - A&R teams can use this to identify emerging tracks with the right energy profile that are more likely to do well with proper exposure.
    """
)

# 4. Correlation Matrix
display_insight(
    "boxplot-key.png",
    " Boxplot — Streams by Musical Key",
    """**Insight**: 
    
**What We Observed:**
    - The boxplot helped us compare how many streams songs got based on their musical key.
    - Some keys like C# and E showed a slightly higher median number of streams.
    - But overall, the variation across keys was not that significant.
    - A few keys had outlier songs with really high stream counts — but that’s probably because of the artist's brand or platform push, not just the key.

**Takeaway:**
    - The musical key alone doesn’t determine popularity.
    - It may have minor influence, but it's not something the team should heavily rely on when making playlist or promotion decisions.
    """
)

# 5. BPM Distribution
display_insight(
    "boxplot-mode.png",
    "Boxplot — Streams by Mode (Major/Minor)",
"""**Insight**: 
**What We Observed:**
    - We compared the stream distribution of songs in major (1) and minor (0) modes.
    - Songs in major mode tend to have slightly higher median streams.
    - Also, more outliers (viral songs) exist in major mode.

**Takeaway:**
    - Major mode songs might be perceived as happier or more energetic, which may explain their slight advantage.
    - However, this difference isn’t huge — so it’s not a strong standalone predictor.
    - Still, for feel-good or mainstream playlists, favoring major key songs might help.


    """
)

# 6. Spotify Chart vs Playlist
display_insight(
    "Distribution of bpm.png",
    "Distribution of BPM (Tempo)",
    """**Insight**:

**What We Observed:**
    - Most songs fall between 80 and 140 BPM, with a big peak around 120 BPM.
    - This aligns with common tempos for pop, dance, and mainstream genres.
    - There are fewer very fast-paced songs (above 160 BPM), suggesting such tracks aren’t the norm.

**Takeaway:**
    - Moderate tempos (~120 BPM) seem to be a sweet spot for most popular songs.
    - This could help A&R teams when screening or producing tracks, especially for mainstream releases.
    - For data-driven curation, this tempo range can act as a baseline for building hit-friendly playlists.
    """
)

# 7. Platform Presence vs Streams
display_insight(
    "avg-streams.png",
    "Average Streams by Release Month",
    """**Insight**: 
    
**What We Observed:**
    - When we looked at how many streams songs got on average depending on which month they were released, we found a clear trend.
    - January, May, and September stood out with higher average stream counts compared to other months.
    - Some months like July or November showed slightly lower averages.
    - This could be because of seasonal listening behavior — like people being more active on music platforms around:
        - New Year resolutions (Jan),
        - Exam breaks or summer (May),
        - Festive buildup or post-vacation vibes (Sept).

**Business Implications:**
    - This insight is very actionable — especially for the marketing team and release planning teams.
    - If you’re planning to launch a major artist, debut single, or viral track attempt — timing it around January or September could give it a natural boost.
    - Similarly, up-and-coming artists could benefit from releasing when competition is slightly lower (e.g., months with fewer hits or lower averages).
    - This doesn’t mean songs released in other months won’t work — but release strategy does matter, especially for first-week performance and playlist push.

**A&R/Marketing Takeaway:**
    - Use this monthly trend to:
        - Strategize launch windows for high-potential songs.
        - Align marketing budgets and playlist campaigns with high-traffic months.
        - Prepare promotional content in advance for seasonal spikes.
    """
)

# 8. Playlist Count vs Streams
display_insight(
    "playlists vs. streams.png",
    "Number of Playlists vs Streams",
    """**Insight**:  Playlist Presence Drives Streams
    
**What We Found:**
    - Across Spotify, Apple Music, and Deezer, there’s one thing that stands out —
        More playlist presence = more streams.
    - The trend is strongest on Spotify — songs featured in multiple playlists tend to get way more streams.
    - This isn’t surprising, considering how much reach Spotify editorial and algorithmic playlists have.
    - Apple Music shows a similar pattern, though the data’s a bit more spread out. Still, the influence is there.
    - For Deezer, the trend is weaker and less clear — probably because not many songs had wide Deezer presence in our dataset.

**Business Implications:**
    - If you’re looking to maximize a song’s reach, getting it featured in as many relevant playlists as possible is key.
    - Spotify should be your top priority when it comes to playlist pitching and partnerships.
    - Apple Music also offers good value, especially for artists with existing fanbases or genre-specific reach.

**For the Marketing Team:**
    - Actively work with playlist curators, editorial teams, and UGC playlist creators.
    - Invest effort into metadata optimization, social buzz, and early traction — all of which help trigger algorithmic inclusion.
    - Make playlist marketing a key part of the rollout plan, not an afterthought.

**For A&R Teams:**
    - When scouting artists or songs, don’t just look at raw stream counts — check how well a song is performing relative to playlist support.
    - A song doing great without much playlist support might be organically strong and worth investing in.

**Final Note:**
    - While we did drop artist/track name features to focus purely on behavior-driven insights (no NLP), these results still reflect how platform strategy can majorly influence a song’s performance.

    - If you understand this early, you can build smarter release campaigns with higher chances of success.
    
    """
)
