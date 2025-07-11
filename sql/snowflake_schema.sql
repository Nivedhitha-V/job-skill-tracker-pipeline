CREATE OR REPLACE TABLE top_skills_daily (
    skill STRING,
    count INT,
    date DATE
);


-- data file 

SELECT * 
FROM top_skills_daily
ORDER BY date, count DESC;


-- overall skill demand 

SELECT skill, SUM(count) AS total_count FROM TOP_SKILLS_DAILY
GROUP BY skill
ORDER BY total_count DESC;


-- Top 5 skills overall

SELECT skill, SUM(count) AS total_count
FROM top_skills_daily
GROUP BY skill
ORDER BY total_count DESC
LIMIT 5;


-- Skill trend by day

SELECT date, skill, count
FROM top_skills_daily
WHERE skill IN ('python', 'sql', 'aws')
ORDER BY date;

WITH ranked_skills AS (
    SELECT
        skill,
        date,
        count,
        ROW_NUMBER() OVER (PARTITION BY date ORDER BY count DESC) AS no
    FROM top_skills_daily
),
pivot_ready AS (
    SELECT
        no,
        TO_CHAR(date, 'DD-MM-YYYY') AS day,
        skill
    FROM ranked_skills
    WHERE no <= 10
)
SELECT *
FROM pivot_ready
PIVOT(
    MAX(skill) FOR day IN (
        '01-07-2025', 
        '02-07-2025', 
        '03-07-2025', 
        '04-07-2025', 
        '05-07-2025', 
        '06-07-2025', 
        '07-07-2025', 
        '08-07-2025', 
        '09-07-2025', 
        '10-07-2025'
    )
)
ORDER BY no;

