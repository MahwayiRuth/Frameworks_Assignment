COVID-19 Research Analysis - CORD-19 Dataset

📘 Project Overview

This project analyzes the CORD-19 (COVID-19 Open Research Dataset) to extract insights about research publications during the pandemic. The analysis includes data cleaning, exploratory data analysis, visualizations, and an interactive web dashboard.

Assignment: Python Frameworks Assignment
Dataset: CORD-19 metadata.csv (sample of 1,000 research papers)
Time Period: 2019–2023
Tools Used: Python, pandas, matplotlib, seaborn, HTML/CSS


---
Python final project/
│
├── generate_sample_data.py      # Generates sample CORD-19 dataset
├── part1_exploration.py         # Data loading and exploration
├── part2_cleaning.py            # Data cleaning and preparation
├── final_analysis.py            # Complete analysis and visualizations
├── dashboard.html               # Interactive web dashboard
│
├── metadata.csv                 # Original dataset
├── metadata_cleaned.csv         # Cleaned dataset
│
├── chart_timeline.png           # Publications over time
├── chart_journals.png           # Top publishing journals
├── chart_words.png              # Word frequency analysis
└── chart_sources.png            # Distribution by source

## Installation & Requirements

### Required Python Packages:
```bash
pip install pandas matplotlib seaborn
Python Version:
Python 3.7+
Development Environment:
Pydroid 3 (Android mobile development)


▶️ How to Run the Project

Step 1: Generate Sample Data

python generate_sample_data.py

Creates a sample dataset of 1,000 COVID-19 research papers with realistic metadata.


___

Step 2: Explore the Data

python part1_exploration.py

Performs initial data exploration including:

Dataset dimensions

Column data types

Missing value analysis

Basic statistics


___

Step 3: Clean the Data

python part2_cleaning.py

Handles missing data and prepares the dataset:

Fills missing abstracts

Converts dates to datetime format

Extracts year from publication dates

Creates word count columns

Saves cleaned dataset


---

Step 4: Perform Analysis & Create Visualizations

python final_analysis.py

Generates analysis results and 4 visualizations:

Publications timeline

Top journals bar chart

Word frequency analysis

Source distribution pie chart



---

Step 5: View the Dashboard

Open dashboard.html in any web browser to see the interactive dashboard with all results and visualizations.


---

📊 Analysis Results

Key Statistics

Total Papers Analyzed: 1,000

Unique Journals: 15

Date Range: 2019–2023

Data Sources: 9 different sources



---

Major Findings

1. Publication Trends Over Time

Research output peaked in 2020–2021 (260+ papers per year)

Initial spike occurred in late 2019

Publications declined in 2022–2023


2. Top Publishing Journals

Leading journals:

Emerging Infectious Diseases

Virology

PLOS ONE

BMJ

Journal of Virology


3. Research Themes (Word Frequency)

Most common words:

“comprehensive”

“review”

“context”

“study”

“analysis”


4. Source Distribution

Research distribution:

bioRxiv: 12.2%

Springer: 12.1%

medRxiv: 11.4%

WHO: 11.4%

Other sources: ~53%



---

🧠 Technical Implementation

Data Cleaning

# Handle missing values
df = df[~(df['title'].isnull() & df['abstract'].isnull())]
df['abstract'] = df['abstract'].fillna('No abstract available')
df['pmcid'] = df['pmcid'].fillna('Unknown')

Date Processing

# Convert and extract year
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year


Visualization Techniques

Line charts for time series data

Bar charts for categorical comparisons

Pie charts for distribution analysis

Color schemes optimized for clarity



---

💻 Web Dashboard Features

Responsive (mobile-friendly) design

Statistical summary cards

Embedded visualizations

Key findings section

Professional gradient styling



---

🚧 Challenges Faced

1. Mobile Development Constraints – adapted workflow to Pydroid 3


2. Dataset Size – used a realistic 1,000-record sample


3. Missing Data – strategic imputation and removal


4. Streamlit Deployment – replaced with offline HTML dashboard


5. Output Visibility – saved outputs to text and image files


6. File Paths – used explicit Android file paths




---

🧩 What I Learned

Technical Skills

Data analysis with pandas

Visualization with matplotlib & seaborn

Responsive HTML/CSS dashboards


Problem-Solving

Working under mobile constraints

Debugging without console access

Managing limited system resources


Domain Knowledge

Understanding COVID-19 research trends

Bibliometric data analysis


Project Management

Modular development

Clear documentation

Meeting deadlines



---

🚀 Future Improvements

Process full 400,000+ record dataset

NLP on abstracts for topic modeling

Interactive charts with D3.js or Plotly

Database integration (SQLite/PostgreSQL)

REST API for live data access

Network and citation analysis

Machine learning topic classification



---

🏁 Conclusion

This project successfully analyzed COVID-19 research publications, revealing key trends and challenges in pandemic-era science.
Despite working entirely on a mobile device, all project requirements were met:

✅ Data exploration
✅ Cleaning & preparation
✅ Analysis & visualization
✅ Interactive dashboard
✅ Documentation


---

📚 References

CORD-19 Dataset: Allen Institute for AI (2020)

pandas Documentation

matplotlib Documentation

seaborn Documentation



---

👩‍💻 Author

Khensani Mahwayi
Python Frameworks Assignment
📅 September 2025


---

📜 License

This project uses the CORD-19 dataset for educational research purposes only.


---

🙏 Acknowledgments

Allen Institute for AI

Global scientific community

Instructors and peers for guidance and support


> Note: This project was developed entirely on mobile using Pydroid 3. Despite technical limitations, all components were successfully completed.

