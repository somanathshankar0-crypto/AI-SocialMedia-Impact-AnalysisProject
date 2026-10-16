# AI-SocialMedia-Impact-AnalysisProject
# AI & Social Media Student Data Analysis

## 📌 Project Overview

This project explores the relationship between students' social media usage, AI tool usage, sleep patterns, physical activity, and health scores using Python.

The goal is to perform exploratory data analysis (EDA), identify patterns in the dataset, compare student groups, and visualize relationships between daily habits and wellbeing indicators.

## 🎯 Objectives

- Examine dataset structure and data quality.
- Compare usage patterns across gender and education levels.
- Analyze differences across student age groups.
- Explore distributions of social media usage, AI tool usage, sleep, physical activity, and health scores.
- Investigate correlations between student habits and wellbeing indicators.
- Present findings using clear visualizations.

## 📂 Dataset

**File:** `AI_SocialMedia_Student_Dataset.csv`

The dataset contains 16,000 student records and 10 columns describing student demographics, daily habits, AI tool usage, and health-related scores.

The analysis uses columns such as:

- `Student_ID`
- `Age`
- `Gender`
- `Education_Level`
- `Daily_Social_Media_Hours`
- `Daily_AI_Tool_Usage_Hours`
- `Sleep_Hours`
- `Physical_Activity_Hours`
- `Mental_Health_Score`
- `Physical_Health_Score`

*Note: The dataset is used for learning and exploratory analysis. Its apparent synthetic nature means the results should not be generalized to real student populations.*

## 🛠️ Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## 🔍 Analysis Performed

### 1. Data Quality Assessment
- Checked the number of rows and columns.
- Inspected data types and non-null values.
- Checked for missing values and duplicate rows.
- Generated descriptive statistics.

### 2. Demographic Analysis
- Compared student counts by gender and education level.
- Created age groups for demographic comparisons.
- Used pivot tables to examine group sizes.

### 3. Group Comparisons
- Compared average social media usage and AI tool usage.
- Examined sleep duration and physical activity.
- Compared mental and physical health scores.
- Used gender, education level, and age group to organize comparisons.

### 4. Statistical Summaries
- Calculated sums, means, minimums, and maximums.
- Created multi-index pivot tables.
- Calculated a correlation matrix for selected numerical variables.

### 5. Data Visualization
Created visualizations using Seaborn and Matplotlib, including:

- Bar plots
- Histograms with KDE curves
- Correlation heatmaps
- Regression plots
- Box plots
- Count heatmaps

## 📊 Key Findings

The following findings are based on the dataset analyzed:

- **Social media and mental health:** Daily social media usage showed a negative correlation with mental health scores (*r* ≈ −0.40).
- **Social media and sleep:** Higher social media usage was associated with fewer hours of sleep (*r* ≈ −0.30).
- **Social media and physical health:** A negative association was observed (*r* ≈ −0.31).
- **Physical activity and physical health:** Physical activity showed a positive correlation with physical health scores (*r* ≈ +0.42).
- **Sleep and mental health:** Sleep duration showed a positive association with mental health scores (*r* ≈ +0.31).
- **AI tool usage:** AI tool usage showed little correlation with social media usage (*r* ≈ 0.00) and weak negative correlations with sleep and mental health scores.

These are associations within this dataset, not evidence that one factor causes another.

## ⚠️ Limitations

- The dataset appears highly structured and may be synthetic.
- Correlation does not establish causation.
- Age and education level overlap completely in this dataset, limiting the ability to study their effects independently.
- The findings describe this dataset and should not be treated as conclusions about all students.

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

### 2. Install the required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### 3. Keep the dataset and Python script in the same folder

Example structure:

```text
AI-Social-Media-Student-Analysis/
├── AI_SocialMedia_Student_Dataset.csv
├── your_analysis_script.py
└── README.md
```

Replace `your_analysis_script.py` with the actual name of your Python file.

### 4. Run the analysis

```bash
python your_analysis_script.py
```

The script prints analysis results in the terminal and displays the plots. Close each plot window to continue to the next one.

## 📚 What I Learned

- Data inspection and cleaning with Pandas.
- Grouping and aggregation using `groupby()`.
- Creating pivot tables with multiple aggregation functions.
- Working with age groups and categorical variables.
- Creating statistical visualizations with Seaborn and Matplotlib.
- Interpreting correlations and communicating analytical limitations.

## 🚀 Future Improvements

- Create a concise dashboard for exploring the dataset.
- Add confidence intervals and hypothesis testing after learning inferential statistics.
- Improve plot presentation and summarize key findings in a report.
- Explore predictive modeling only when appropriate for the dataset and project goals.

---

**Project focus:** Exploratory Data Analysis (EDA)  
**Skills:** Python · Pandas · NumPy · Matplotlib · Seaborn
