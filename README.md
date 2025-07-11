#  Real-Time Job Skills Tracker & Market Analytics Dashboard

StreamLit :  [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://top-skills-dashboard-nivedhitha.streamlit.app/)
 
 Track trending skills, hiring hotspots, and market demand in real time.

---

##  What This Project Solves

The job market evolves rapidly — new tools trend overnight, company needs shift, and demand for specific skills changes weekly. But most candidates, HR teams, and even training platforms still rely on outdated reports or static CSV analyses.

This project was built to solve that gap.

---

# My Goal
To create a realistic, end-to-end data pipeline that simulates real-time tracking of job skills, just like how a hiring insights system would work.

- Instead of scraping (which was blocked), I used a Kaggle dataset of 5,000+ job listings
- Simulated daily job feeds by splitting data into day-wise batches
- Built a modular ETL pipeline to clean, extract, and normalize skill data
- Ingested results into Snowflake
- Visualized insights using both Power BI (offline) and a live Streamlit dashboard



---

## Goals & Outcomes

✅ Ingest and process job listing data (role, skills, company, location, date)  
✅ Normalize & extract skillsets from long job descriptions  
✅ Store and query structured skill data using Snowflake  
✅ Visualize insights using **Power BI** & **Streamlit dashboards**  
✅ Simulate daily pipeline runs with modular scripts  
✅ Showcase a full-stack **DE project that mimics a real job environment**
                 

---

##  Project Architecture

This project simulates a real-time job skill tracking pipeline — even without live scraping — by mimicking daily data ingestion, transformation, storage, and dashboarding using real-world tools. Here's how the full flow works:

1). **Kaggle Job Listings Dataset (5K+ Records)**

2). **Data Cleaning & Skill Normalization (Google Colab)**
- Removed nulls, duplicates, unwanted characters
- Extracted skills from job descriptions (JD) & normalized terms
- Grouped similar skills (e.g, 'Structured Query Language' → 'SQL')
- Created: top_150_skills.csv

3). **Basic Skill Frequency Analysis (Google Colab)**
- Visualized skill counts using bar charts & word clouds
- Helped identify top in-demand skills 

4). **Simulated Daily Job Feed (Data Splitting Logic)**
       - Split main cleaned dataset into 10 smaller files (daily1.csv to daily10.csv)
       - Extracted skills from each, saved as: skills_day1.csv to skills_day10.csv

5). **Snowflake Cloud Data Warehouse (Ingestion via Python)**
       - Used Snowflake Connector for Python to ingest daily skill CSVs
       - Tables created manually via SQL; data inserted programmatically
       - Sample SQL queries run to validate ingestion


6). **Power BI Dashboard (Offline, Local)**
       - Visualized only **Top 15 Skills** using Snowflake as the backend
       - Built using clustered bar charts and slicers for quick filtering
       - Power BI file not hosted online (used for demo purpose only)

 7). **Streamlit Web App (Live via GitHub + Snowflake)**
       - Dashboard built in Python, deployed via Streamlit Cloud
       - Reads live skill data from Snowflake tables
       - Visualizes:
         ✔️ Top skills
         ✔️ Skill frequency by date
       - Interactive dropdowns to filter by skill or date
       - No location, role, or company-based filtering (not present in daily skill data)


---

##  Tech Stack Used

| Tool           | Purpose                          |
|----------------|----------------------------------|
| **Python**     | Data cleaning, skill extraction, automation |
| **Google Colab** | Code execution, preprocessing |
| **Snowflake**  | Cloud data warehouse for structured ingestion |
| **Power BI**   | Visual dashboard (non-interactive) |
| **Streamlit**  | Web app dashboard for live skill tracking (interactive) |
| **GitHub**     | Version control & project repo |

---

##  Live Demo

Try the dashboard yourself (no setup needed):  
🔗 [**Streamlit App**](https://top-skills-dashboard-nivedhitha.streamlit.app/)

---

## Connect

This project demonstrates foundational Data Engineering skills, from raw file ingestion to clean, analysis-ready output.

Feel free to **star** the repo or **fork** for practice or extension!

Made with 💙 by Nivedhitha V 
[Github](https://github.com/Nivedhitha-V)
[Email](nivedhithav0407@gmail.com)
[LinkedIn](https://www.linkedin.com/in/nivedhitha-v/)
