import streamlit as st
import pandas as pd
import snowflake.connector

# ------------------------
# 🎯 PAGE CONFIG
# ------------------------
st.set_page_config(
    page_title="Job Skill Trends Dashboard",
    page_icon="📊",
    layout="wide"
)

# ------------------------
# 🔐 Snowflake Connection
# ------------------------
conn = snowflake.connector.connect(
    user=st.secrets["snowflake"]["user"],
    password=st.secrets["snowflake"]["password"],
    account=st.secrets["snowflake"]["account"],
    warehouse=st.secrets["snowflake"]["warehouse"],
    database=st.secrets["snowflake"]["database"],
    schema=st.secrets["snowflake"]["schema"]
)

# ------------------------
# 🧠 HEADER
# ------------------------
st.title("📊 Job Skill Tracker Dashboard")
st.markdown("Explore top job skills from Snowflake data — filter by date, visualize trends, and empower your hiring team.")

# ------------------------
# 🎛️ SIDEBAR FILTER
# ------------------------
st.sidebar.header("🔍 Filters")

# Get available dates from Snowflake
date_query = "SELECT DISTINCT date FROM top_skills_daily ORDER BY date"
date_df = pd.read_sql(date_query, conn)
available_dates = date_df['DATE'].astype(str).tolist()

# Sidebar date filter
selected_date = st.sidebar.selectbox("Select a Date", options=available_dates)

# ------------------------
# 📥 LOAD DATA
# ------------------------
query = "SELECT * FROM top_skills_daily"
df = pd.read_sql(query, conn)

# Filter for selected date
daily_skills = df[df['DATE'] == selected_date]

# ------------------------
# 📊 BAR CHART
# ------------------------
st.subheader("Top 15 Skills on Selected Date")
if not daily_skills.empty:
    bar_data = daily_skills.sort_values('COUNT', ascending=False)
    st.bar_chart(bar_data.set_index('SKILL')['COUNT'])
else:
    st.info("Bar chart will show here once data is loaded.")

# ------------------------
# 📈 TREND LINE CHART
# ------------------------
st.subheader("Skill Trend Over Time")
if not daily_skills.empty:
    top_skill = daily_skills.sort_values('COUNT', ascending=False)['SKILL'].iloc[0]
    trend_data = df[df['SKILL'] == top_skill]
    st.line_chart(trend_data.set_index('DATE')['COUNT'])
else:
    st.info("Line chart will show here once data is loaded.")

# ------------------------
# 🧾 RAW DATA
# ------------------------
st.subheader("📄 Raw Data")
st.dataframe(daily_skills)
