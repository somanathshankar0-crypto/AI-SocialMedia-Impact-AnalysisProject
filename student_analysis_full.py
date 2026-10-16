# ============================================================
# AI & SOCIAL MEDIA STUDENT DATASET - EXPLORATORY DATA ANALYSIS
# Part A: Pandas analysis   Part B: Seaborn plots
# Note: close each plot window to see the next one.
# ============================================================
import numpy as n
import pandas as p
import matplotlib.pyplot as m
import seaborn as s

# ============================================================
# PART A: PANDAS ANALYSIS
# ============================================================

# ------------------------------------------------------------
# SECTION 1: LOAD DATA AND CHECK DATA QUALITY
# ------------------------------------------------------------
df = p.read_csv("AI_SocialMedia_Student_Dataset.csv")

# Number of rows and columns
shape = df.shape
print("Rows, columns:", shape)

# Column names, data types and non-null counts
df.info()

# Missing values in each column
missing = df.isna().sum()
print("\nMissing values per column:\n", missing)

# Number of fully duplicated rows (.duplicated() alone gives True/False per row)
duplicates = df.duplicated().sum()
print("Duplicate rows:", duplicates)

# Summary statistics for numeric columns
print(df.describe().round(2))

# ------------------------------------------------------------
# SECTION 2: GENDER AND EDUCATION OVERVIEW
# ------------------------------------------------------------
# Number of students of each gender
gender_counts = df["Gender"].value_counts()

# Number of students in each education level
edu_counts = df["Education_Level"].value_counts()
print("\n", gender_counts, "\n\n", edu_counts)

# ------------------------------------------------------------
# SECTION 3: GENDER-WISE TOTALS AND AVERAGES
# Totals depend on how many students each gender has, so compare
# AVERAGES when judging which gender does more of something.
# ------------------------------------------------------------
# Total social media hours by gender
sm_total = df.groupby("Gender")["Daily_Social_Media_Hours"].sum()

# Total AI tool usage hours by gender
ai_total = df.groupby("Gender")["Daily_AI_Tool_Usage_Hours"].sum()

# Total sleep hours by gender
sleep_total = df.groupby("Gender")["Sleep_Hours"].sum()

# Total mental health score by gender
mental_total = df.groupby("Gender")["Mental_Health_Score"].sum()

# Total physical activity hours by gender
activity_total = df.groupby("Gender")["Physical_Activity_Hours"].sum()

# Average social media and AI tool hours by gender
sm_avg = df.groupby("Gender")["Daily_Social_Media_Hours"].mean()
ai_avg = df.groupby("Gender")["Daily_AI_Tool_Usage_Hours"].mean()

# Average sleep, mental health score and physical activity by gender
sleep_avg = df.groupby("Gender")["Sleep_Hours"].mean()
mental_avg = df.groupby("Gender")["Mental_Health_Score"].mean()
activity_avg = df.groupby("Gender")["Physical_Activity_Hours"].mean()

print("\nAverages by gender:\n",
      p.concat([sm_avg, ai_avg, sleep_avg, mental_avg, activity_avg], axis=1).round(2))

# ------------------------------------------------------------
# SECTION 4: CREATE AGE GROUPS
# Bins are (15,20], (20,25], (25,30], (30, infinity). The left
# edge is excluded, so an age of exactly 15 would become NaN.
# ------------------------------------------------------------
df["Age_of_student"] = p.cut(df["Age"], bins=[15, 20, 25, 30, float("inf")],
                             labels=["15-20", "20-25", "25-30", "30+"])
print("\nAge range:", df["Age"].min(), "to", df["Age"].max())
print("Students left without an age group (NaN):", df["Age_of_student"].isna().sum())

# ------------------------------------------------------------
# SECTION 5: COUNT PIVOT TABLES
# ------------------------------------------------------------
# Count of each gender in each age group
age_gender_count = p.pivot_table(df, values="Age", index="Age_of_student",
                                 columns="Gender", aggfunc="count", observed=False)

# Count of students by gender and education level
gender_edu_count = p.pivot_table(df, values="Student_ID", index="Gender",
                                 columns="Education_Level", aggfunc="count")

# Count of males and females in each age group (gender as rows)
gender_age_count = p.pivot_table(df, values="Student_ID", index="Gender",
                                 columns="Age_of_student", aggfunc="count", observed=False)
print("\n", gender_edu_count, "\n\n", gender_age_count)

# ------------------------------------------------------------
# SECTION 6: GENDER x EDUCATION LEVEL PIVOTS
# NaN in a pivot means no students in that combination, not missing data.
# ------------------------------------------------------------
# Total and max social media hours
sm_sum_pivot = p.pivot_table(df, values="Daily_Social_Media_Hours", index="Gender",
                             columns="Education_Level", aggfunc="sum")
sm_max_pivot = p.pivot_table(df, values="Daily_Social_Media_Hours", index="Gender",
                             columns="Education_Level", aggfunc="max")

# AI tool usage: sum, max, min, mean
ai_pivot = p.pivot_table(df, values="Daily_AI_Tool_Usage_Hours", index="Gender",
                         columns="Education_Level", aggfunc=["sum", "max", "min", "mean"])

# Mental health score: sum, max, min, mean
mental_pivot = p.pivot_table(df, values="Mental_Health_Score", index="Gender",
                             columns="Education_Level", aggfunc=["sum", "max", "min", "mean"])

# Physical activity hours: sum, max, min, mean
activity_pivot = p.pivot_table(df, values="Physical_Activity_Hours", index="Gender",
                               columns="Education_Level", aggfunc=["sum", "max", "min", "mean"])

# Sleep hours: sum, max, mean
sleep_pivot = p.pivot_table(df, values="Sleep_Hours", index="Gender",
                            columns="Education_Level", aggfunc=["sum", "max", "mean"])

# Physical health score: sum, mean, max
physical_pivot = p.pivot_table(df, values="Physical_Health_Score", index="Gender",
                               columns="Education_Level", aggfunc=["sum", "mean", "max"])
print("\nMean mental health score, gender x education:\n", mental_pivot["mean"].round(2))

# ------------------------------------------------------------
# SECTION 7: AGE GROUP x EDUCATION LEVEL PIVOTS
# fill_value is NOT used: filling a mean or max with 0 would wrongly
# say these students spend 0 hours. NaN is the honest result.
# ------------------------------------------------------------
agg3 = ["sum", "mean", "max"]

# Social media hours
age_sm = p.pivot_table(df, values="Daily_Social_Media_Hours", index="Age_of_student",
                       columns="Education_Level", aggfunc=agg3, observed=False)

# AI tool usage hours
age_ai = p.pivot_table(df, values="Daily_AI_Tool_Usage_Hours", index="Age_of_student",
                       columns="Education_Level", aggfunc=agg3, observed=False)

# Mental health score
age_mental = p.pivot_table(df, values="Mental_Health_Score", index="Age_of_student",
                           columns="Education_Level", aggfunc=agg3, observed=False)

# Sleep hours
age_sleep = p.pivot_table(df, values="Sleep_Hours", index="Age_of_student",
                          columns="Education_Level", aggfunc=agg3, observed=False)

# Physical activity hours
age_activity = p.pivot_table(df, values="Physical_Activity_Hours", index="Age_of_student",
                             columns="Education_Level", aggfunc=agg3, observed=False)

# Physical health score
age_physical = p.pivot_table(df, values="Physical_Health_Score", index="Age_of_student",
                             columns="Education_Level", aggfunc=agg3, observed=False)
print("\nMean social media hours, age group x education:\n", age_sm["mean"].round(2))

# ============================================================
# PART B: SEABORN PLOTS (each has its own figure, title and labels)
# ============================================================

# ------------------------------------------------------------
# SECTION 8: AVERAGES BY EDUCATION LEVEL, SPLIT BY GENDER
# ------------------------------------------------------------
# Plot 1: Social Media Hours by Education Level and Gender. Look for: which education level uses social media most, and do genders differ?
m.figure(figsize=(8, 5))
s.barplot(x="Education_Level", y="Daily_Social_Media_Hours", hue="Gender", data=df)
m.xlabel("Education Level")
m.ylabel("Avg Daily Social Media Hours")
m.title("Social Media Hours by Education Level and Gender")
m.tight_layout()
m.show()

# Plot 2: AI Tool Usage by Education Level and Gender. Look for: does AI tool use rise with education level?
m.figure(figsize=(8, 5))
s.barplot(x="Education_Level", y="Daily_AI_Tool_Usage_Hours", hue="Gender", data=df)
m.xlabel("Education Level")
m.ylabel("Avg Daily AI Tool Usage (hours)")
m.title("AI Tool Usage by Education Level and Gender")
m.tight_layout()
m.show()

# Plot 3: Physical Activity by Education Level and Gender. Look for: which group is the most active?
m.figure(figsize=(8, 5))
s.barplot(x="Education_Level", y="Physical_Activity_Hours", hue="Gender", data=df)
m.xlabel("Education Level")
m.ylabel("Avg Physical Activity (hours)")
m.title("Physical Activity by Education Level and Gender")
m.tight_layout()
m.show()

# Plot 4: Mental Health Score by Education Level and Gender. Look for: does any group score noticeably lower or higher?
m.figure(figsize=(8, 5))
s.barplot(x="Education_Level", y="Mental_Health_Score", hue="Gender", data=df)
m.xlabel("Education Level")
m.ylabel("Avg Mental Health Score")
m.title("Mental Health Score by Education Level and Gender")
m.tight_layout()
m.show()

# Plot 5: Physical Health Score by Education Level and Gender. Look for: same comparison, for physical health.
m.figure(figsize=(8, 5))
s.barplot(x="Education_Level", y="Physical_Health_Score", hue="Gender", data=df)
m.xlabel("Education Level")
m.ylabel("Avg Physical Health Score")
m.title("Physical Health Score by Education Level and Gender")
m.tight_layout()
m.show()

# ------------------------------------------------------------
# SECTION 9: DISTRIBUTIONS OF SINGLE COLUMNS
# ------------------------------------------------------------
# Plot 6: Distribution of Physical Activity Hours. Look for: shape, peak, unusual values.
m.figure(figsize=(8, 5))
s.histplot(data=df, x="Physical_Activity_Hours", kde=True)
m.xlabel("Physical Activity (hours)")
m.ylabel("Number of Students")
m.title("Distribution of Physical Activity Hours")
m.tight_layout()
m.show()

# Plot 7: Distribution of Daily Social Media Hours. Look for: typical usage level and spread.
m.figure(figsize=(8, 5))
s.histplot(data=df, x="Daily_Social_Media_Hours", kde=True)
m.xlabel("Daily Social Media Hours")
m.ylabel("Number of Students")
m.title("Distribution of Daily Social Media Hours")
m.tight_layout()
m.show()

# Plot 8: Distribution of Daily AI Tool Usage. Look for: light or heavy use for most students?
m.figure(figsize=(8, 5))
s.histplot(data=df, x="Daily_AI_Tool_Usage_Hours", kde=True)
m.xlabel("Daily AI Tool Usage (hours)")
m.ylabel("Number of Students")
m.title("Distribution of Daily AI Tool Usage")
m.tight_layout()
m.show()

# Plot 9: Distribution of Mental Health Scores. Look for: clustered high, low or spread out?
m.figure(figsize=(8, 5))
s.histplot(data=df, x="Mental_Health_Score", kde=True)
m.xlabel("Mental Health Score")
m.ylabel("Number of Students")
m.title("Distribution of Mental Health Scores")
m.tight_layout()
m.show()

# Plot 10: Distribution of Physical Health Scores. Look for: shape compared with mental health.
m.figure(figsize=(8, 5))
s.histplot(data=df, x="Physical_Health_Score", kde=True)
m.xlabel("Physical Health Score")
m.ylabel("Number of Students")
m.title("Distribution of Physical Health Scores")
m.tight_layout()
m.show()

# ------------------------------------------------------------
# SECTION 10: AVERAGES BY AGE GROUP, SPLIT BY GENDER
# ------------------------------------------------------------
# Plot 11: Social Media Hours by Age Group and Gender. Look for: do younger students spend more time?
m.figure(figsize=(8, 5))
s.barplot(x="Age_of_student", y="Daily_Social_Media_Hours", hue="Gender", data=df)
m.xlabel("Age Group")
m.ylabel("Avg Daily Social Media Hours")
m.title("Social Media Hours by Age Group and Gender")
m.tight_layout()
m.show()

# Plot 12: AI Tool Usage by Age Group and Gender. Look for: does AI use rise or fall with age?
m.figure(figsize=(8, 5))
s.barplot(x="Age_of_student", y="Daily_AI_Tool_Usage_Hours", hue="Gender", data=df)
m.xlabel("Age Group")
m.ylabel("Avg Daily AI Tool Usage (hours)")
m.title("AI Tool Usage by Age Group and Gender")
m.tight_layout()
m.show()

# Plot 13: Physical Activity by Age Group and Gender. Look for: does activity drop in the older group?
m.figure(figsize=(8, 5))
s.barplot(x="Age_of_student", y="Physical_Activity_Hours", hue="Gender", data=df)
m.xlabel("Age Group")
m.ylabel("Avg Physical Activity (hours)")
m.title("Physical Activity by Age Group and Gender")
m.tight_layout()
m.show()

# Plot 14: Sleep Hours by Age Group and Gender. Look for: does any group sleep noticeably less?
m.figure(figsize=(8, 5))
s.barplot(x="Age_of_student", y="Sleep_Hours", hue="Gender", data=df)
m.xlabel("Age Group")
m.ylabel("Avg Sleep Hours")
m.title("Sleep Hours by Age Group and Gender")
m.tight_layout()
m.show()

# Plot 15: Physical Health Score by Age Group and Gender. Look for: does health score change across age groups?
m.figure(figsize=(8, 5))
s.barplot(x="Age_of_student", y="Physical_Health_Score", hue="Gender", data=df)
m.xlabel("Age Group")
m.ylabel("Avg Physical Health Score")
m.title("Physical Health Score by Age Group and Gender")
m.tight_layout()
m.show()

# ------------------------------------------------------------
# SECTION 11: RELATIONSHIPS BETWEEN COLUMNS
# ------------------------------------------------------------
num_cols = ["Daily_Social_Media_Hours", "Daily_AI_Tool_Usage_Hours", "Physical_Activity_Hours",
            "Sleep_Hours", "Mental_Health_Score", "Physical_Health_Score"]
corr = df[num_cols].corr()
print("\nCorrelation matrix:\n", corr.round(2))

# Plot 16: Correlation heatmap. Correlation does NOT prove cause.
m.figure(figsize=(9, 7))
s.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f")
m.title("Correlation Matrix of Student Habits and Health")
m.tight_layout()
m.show()

# Plot 17: Social media hours vs mental health score
m.figure(figsize=(8, 5))
s.regplot(data=df, x="Daily_Social_Media_Hours", y="Mental_Health_Score")
m.xlabel("Daily Social Media Hours")
m.ylabel("Mental Health Score")
m.title("Social Media Hours vs Mental Health Score")
m.tight_layout()
m.show()

# Plot 18: Sleep hours vs mental health score
m.figure(figsize=(8, 5))
s.regplot(data=df, x="Sleep_Hours", y="Mental_Health_Score")
m.xlabel("Sleep Hours")
m.ylabel("Mental Health Score")
m.title("Sleep Hours vs Mental Health Score")
m.tight_layout()
m.show()

# Plot 19: Physical activity vs physical health score
m.figure(figsize=(8, 5))
s.regplot(data=df, x="Physical_Activity_Hours", y="Physical_Health_Score")
m.xlabel("Physical Activity (hours)")
m.ylabel("Physical Health Score")
m.title("Physical Activity vs Physical Health Score")
m.tight_layout()
m.show()

# Plot 20: Spread of social media hours by education level
m.figure(figsize=(8, 5))
s.boxplot(data=df, x="Education_Level", y="Daily_Social_Media_Hours")
m.xlabel("Education Level")
m.ylabel("Daily Social Media Hours")
m.title("Spread of Social Media Hours by Education Level")
m.tight_layout()
m.show()

# Plot 21: Number of students by gender and education level
m.figure(figsize=(8, 5))
s.heatmap(gender_edu_count, annot=True, fmt="d")
m.xlabel("Education Level")
m.ylabel("Gender")
m.title("Number of Students by Gender and Education Level")
m.tight_layout()
m.show()

# 1. DATA QUALITY: 16,000 students, 10 columns, no missing values, no duplicate rows.
#    Ages run from 13 to 25. Gender has three groups: Male (7,744), Female (7,628)
#    and Non-binary (628). Education: High School 6,083, University 5,027, College 4,890.

# 2. GENDER: Differences are negligible. Average daily social media hours are 4.55 (Female),
#    4.54 (Male) and 4.51 (Non-binary). Mental health scores are about 72.5 for all three,
#    and sleep is about 6.5 hours for all three. Gender does not separate students in this data.

# 3. EDUCATION LEVEL AND AGE GROUP: Also nearly identical. Social media use is 4.49 to 4.57
#    hours across education levels and 4.51 to 4.56 hours across age groups, and mental
#    health scores stay between 72.3 and 72.7. Education level is fully determined by age
#    in this dataset, so the two cannot be compared separately.

# 4. SOCIAL MEDIA AND WELLBEING (the main finding): More social media use is associated
#    with lower mental health (r = -0.40), less sleep (r = -0.30) and lower physical
#    health (r = -0.31). Students using 0-2 hours a day average a mental health score of
#    77.7 and 7.1 hours of sleep, versus 65.0 and 5.8 hours for students using 8+ hours.
#    (2,507 students are in the first group and 1,269 in the second.)

# 5. OTHER RELATIONSHIPS: Physical activity has the strongest link with physical health
#    (r = 0.42) and a smaller one with mental health (r = 0.25). Sleep is positively
#    associated with mental health (r = 0.31). AI tool usage is almost unrelated to social
#    media (r = 0.00) and only weakly related to sleep (r = -0.14) and mental health (r = -0.11).

# 6. LIMITATIONS: These are associations, not proof of cause. Low sleep or poor mental
#    health could also lead to more social media use. The group averages are almost
#    identical, the data looks synthetic, and age and education overlap completely, so
#    the findings describe this dataset only.