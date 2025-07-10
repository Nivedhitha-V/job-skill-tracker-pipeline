import streamlit as st

# ------------------------
# 🎯 PAGE CONFIG
# ------------------------
st.set_page_config(
    page_title="Job Skill Trends Dashboard",
    page_icon="📊",
    layout="wide"
)

# ------------------------
# 🧠 HEADER
# ------------------------
st.title("📊 Job Skill Tracker Dashboard")
st.markdown("Explore top job skills from Snowflake data — filter by date, visualize trends, and empower your hiring team.")

# ------------------------
# 🎛️ SIDEBAR FILTERS
# ------------------------
st.sidebar.header("🔍 Filters")

# Placeholder for date filter (we’ll make this dynamic later)
selected_date = st.sidebar.selectbox(
    "Select a Date",
    options=[],
    index=0,
    disabled=True,
    help="This will be enabled after we connect to Snowflake."
)

# ------------------------
# 📊 MAIN VIEW
# ------------------------
st.subheader("Top 15 Skills on Selected Date")
st.info("Bar chart will show here once data is loaded.")

st.subheader("Skill Trend Over Time")
st.info("Line chart will show here once data is loaded.")

st.subheader("📄 Raw Data")
st.dataframe([], height=200)
