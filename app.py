import streamlit as st
import pandas as pd
import snowflake.connector

# ------------------------
# 🎯 PAGE CONFIG
# ------------------------
st.set_page_config(
    page_title="Job Skill Tracker Dashboard",
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
date_query = "SELECT DISTINCT DATE FROM top_skills_daily ORDER BY DATE"
date_df = pd.read_sql(date_query, conn)
available_dates = date_df['DATE'].astype(str).tolist()

# Sidebar select box for date
selected_date = st.sidebar.st.slider("Select a Date", options=available_dates)

# ------------------------
# 📥 LOAD DATA
# ------------------------
query = "SELECT * FROM top_skills_daily"
df = pd.read_sql(query, conn)

# Ensure columns are uppercase
df.columns = [col.upper() for col in df.columns]

# Filter for selected date
daily_skills = df[df['DATE'].astype(str) == selected_date]

# ------------------------
# 📊 BAR CHART - Top Skills
# ------------------------
st.subheader("Top 15 Skills on Selected Date")
if not daily_skills.empty:
    top_skills = daily_skills.sort_values("COUNT", ascending=False).head(15)
    st.bar_chart(top_skills.set_index("SKILL")["COUNT"])
else:
    st.info("Bar chart will show here once data is loaded.")

# ------------------------
# 📈 TREND LINE CHART (User-selected skill)
# ------------------------
st.sidebar.header("📌 Skill Trend")
selected_skill = st.sidebar.selectbox("Choose a Skill", sorted(df['SKILL'].unique()))

st.subheader(f"📈 Skill Trend Over Time: {selected_skill}")

trend_data = df[df['SKILL'] == selected_skill]

if not trend_data.empty:
    st.line_chart(trend_data.set_index('DATE')['COUNT'])
else:
    st.info("No trend data available for the selected skill.")


# ------------------------
# 📄 RAW DATA TABLE
# ------------------------
st.subheader("📄 Raw Data")
st.dataframe(daily_skills)

# ------------------------
# 📥 Download CSV Button
# ------------------------
csv = daily_skills.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📤 Download This View as CSV",
    data=csv,
    file_name=f"{selected_date}_skills.csv",
    mime='text/csv'
)

