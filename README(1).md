# 🎬 IMDb Top 1000 Movies Analysis & Power BI Dashboard

An end-to-end **movie data analysis project** using Python for data collection and cleaning, followed by **Power BI** for interactive visualization and analysis.

The project explores IMDb movie ratings, votes, release years, certificates, and movie duration across 1,000 movies.

---

## 📊 Dashboard

The Power BI dashboard provides an interactive overview of the IMDb Top 1000 Movies dataset.

### Key KPIs

- **Total Movies:** 1,000
- **Average IMDb Rating:** 8.2
- **Total Votes:** 327M
- **Average Duration:** 120.36 minutes
- **Earliest Movie:** 1902
- **Latest Movie:** 2026

### Dashboard Visuals

- Top 10 Most Voted Movies
- Top 10 Average IMDb Rating
- Movies by Release Year
- Certificate Distribution
- IMDb Rating vs Number of Votes
- Duration Distribution
- Detailed movie table
- Interactive filters for:
  - Year of Release
  - Certificate
  - IMDb Rating
  - Duration

---

## 🛠️ Tech Stack

[![Python][Python]][Python-url]
[![Pandas][Pandas]][Pandas-url]
[![BeautifulSoup][BeautifulSoup]][BeautifulSoup-url]
[![Requests][Requests]][Requests-url]
[![Power BI][PowerBI]][PowerBI-url]
[![Excel][Excel]][Excel-url]
[![GitHub][GitHub]][GitHub-url]

---

## 🔄 Project Workflow

```text
Data Collection
      ↓
Python + Requests
      ↓
Data Extraction
      ↓
BeautifulSoup
      ↓
Data Cleaning & Transformation
      ↓
CSV Export
      ↓
Spreadsheet Exploration & Validation
      ↓
Power BI
      ↓
Interactive Dashboard
```

---

## 🐍 Data Collection

Python was used to collect movie information from the source dataset/API.

The project used:

- `requests` for retrieving data
- `BeautifulSoup` for parsing HTML where required
- `pandas` for data manipulation
- Python functions for cleaning and standardizing fields

---

## 🧹 Data Cleaning

After saving the collected data into CSV format, the dataset was further explored using a spreadsheet.

During validation, some movies had missing fields such as **Certificate**. Because of the inconsistent structure of some records, values such as **Duration** could occasionally appear in the wrong column.

To handle these issues, custom Python cleaning functions were used to:

- Detect incorrectly shifted values
- Identify missing or misplaced values
- Correct column alignment
- Standardize movie attributes
- Convert numerical fields into usable formats
- Handle missing values
- Prepare the final dataset for Power BI

This additional validation step helped make the dataset more reliable before visualization.

---

## 📈 Power BI Analysis

The cleaned dataset was imported into Power BI to build an interactive dashboard.

### Most Voted Movies

The dashboard highlights movies with the highest number of IMDb votes, including:

- The Shawshank Redemption
- The Dark Knight
- Inception
- Fight Club
- Interstellar
- Forrest Gump

### Highest Average IMDb Ratings

The dashboard also displays movies with the highest average IMDb ratings, including entries such as:

- SodaPop
- MMTB Best Short Film Collection of ...
- Psychic
- I Was a Stranger
- The Shawshank Redemption
- Disneyland Around the Seasons

### Release Year Analysis

The release-year chart shows how the number of movies in the dataset is distributed across different years, from **1902 to 2026**.

### Certificate Analysis

A donut chart displays the distribution of movie certificates such as:

- NR
- R
- PG-13
- PG
- G
- Other certificate categories

### Rating vs Votes

A scatter plot compares **IMDb Rating** against **Number of Votes**, allowing patterns between audience votes and ratings to be explored.

### Duration Analysis

The dashboard includes a duration distribution showing how movie runtimes are distributed across the dataset.

---

## 🎯 Project Goals

- Practice real-world data collection using Python
- Clean and validate messy movie data
- Work with missing and incorrectly positioned values
- Perform exploratory data analysis
- Build an interactive Power BI dashboard
- Practice KPI creation and data visualization
- Present analytical insights in a business-friendly format

---

## 📁 Project Structure

```text
IMDb-Movie-Analysis/
│
├── data/
│   └── movies.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   └── main.py
│
├── dashboard/
│   └── movie_analysis.pbix
│
├── movie_dashboard.png
│
└── README.md
```

---

## 📌 Key Takeaway

This project demonstrates a complete beginner-to-intermediate data analytics workflow:

**Collect → Clean → Validate → Analyze → Visualize**

It combines Python data processing with Power BI dashboard development to turn raw movie data into an interactive analytical report.

---

## 📷 Dashboard Preview

![IMDb Top 1000 Movies Power BI Dashboard](movie_dashboard.png)

---

## 👨‍💻 Author

**Varun Rana**

Data Analyst | Python | SQL | Power BI | Data Visualization

[![GitHub][GitHub]][GitHub-url]

---

<!-- Technology badge links -->

[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Pandas]: https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/

[BeautifulSoup]: https://img.shields.io/badge/BeautifulSoup-4B8BBE?style=for-the-badge&logo=python&logoColor=white
[BeautifulSoup-url]: https://www.crummy.com/software/BeautifulSoup/

[Requests]: https://img.shields.io/badge/Requests-2C2C2C?style=for-the-badge&logo=python&logoColor=white
[Requests-url]: https://requests.readthedocs.io/

[PowerBI]: https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black
[PowerBI-url]: https://powerbi.microsoft.com/

[Excel]: https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white
[Excel-url]: https://www.microsoft.com/microsoft-365/excel

[GitHub]: https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white
[GitHub-url]: https://github.com/kogrees
