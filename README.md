# 🎬 IMDb Top 1000 Movies — Data Scraping, Cleaning & Power BI Dashboard

> **End-to-end Data Analyst project:** Data Scraping → Data Extraction → Data Cleaning → Data Validation → Exploratory Analysis → Power BI Dashboard

This project was created to answer a simple question:

**What does the Top 1000 IMDb movie dataset look like, and what patterns can we find in ratings, votes, release years, certificates, and movie duration?**

Instead of manually collecting movie information, I built a Python-based data scraping process to collect the data, cleaned and validated the resulting dataset, explored it in a spreadsheet, and finally built an interactive **Power BI dashboard**.

The final dashboard contains KPIs, rankings, distributions, trends, filters, and a detailed movie-level table.

---

## 📊 Dashboard Preview

![IMDb Top 1000 Movies Power BI Dashboard](movie_dashboard.png)

The dashboard contains:

- Total Movies
- Average IMDb Rating
- Total Number of Votes
- Average Duration
- Earliest Movie Year
- Latest Movie Year
- Top 10 Most Voted Movies
- Top 10 Average IMDb Rating
- Movies by Release Year
- Certificate Distribution
- IMDb Rating vs Number of Votes
- Duration Distribution
- Movie-level detail table
- Interactive filters for Year, Certificate, IMDb Rating, and Duration

The final dashboard contains **1,000 movies**, with an average IMDb rating of **8.2**, total votes of approximately **327M**, average duration of **120.36 minutes**, and release years ranging from **1902 to 2026**. These figures are shown in the Power BI dashboard supplied with this project. fileciteturn0file0L65-L94

---

# 🎯 Project Objective

The goal was not simply to create a Power BI dashboard.

The goal was to build a small **end-to-end data analytics pipeline**.

I wanted to:

1. Collect movie data programmatically.
2. Understand how the source data was structured.
3. Decide how to extract the data efficiently.
4. Build a clean dataset.
5. Validate the data outside Python.
6. Identify and fix data-quality issues.
7. Explore the cleaned data.
8. Create meaningful analytical metrics.
9. Build an interactive Power BI dashboard.
10. Present the results in a way that is easy for someone else to understand.

---

# 🔄 Overall Process

```text
Business Question
       ↓
Understand the Data Source
       ↓
Identify JSON/API Data
       ↓
Python Data Scraping
       ↓
Data Extraction
       ↓
Create DataFrame
       ↓
Save as CSV
       ↓
Spreadsheet Data Validation
       ↓
Identify Data Quality Issues
       ↓
Python Cleaning Functions
       ↓
Clean Dataset
       ↓
Exploratory Analysis
       ↓
Power BI
       ↓
Interactive Dashboard
       ↓
Insights
```

---

# 1. Understanding the Goal

Before writing the scraping code, I first defined what I wanted to analyze.

The objective was to work with approximately **1,000 movies** and analyze attributes such as:

- Movie name
- Certificate
- Release year
- Duration
- IMDb rating
- Number of votes

This helped determine what information needed to be collected and what the final dataset should look like.

---

# 2. Understanding the Source

The source provided movie information through a JSON endpoint:

```text
https://www.yidio.com/redesign/json/browse_results.php?sort=imdb_rating&type=movie&index=0&limit=1000
```

The endpoint allowed the movie records to be retrieved in a structured JSON response.

The response contained movie-level information, including the movie name and URL.

I then used each movie URL to request the individual movie page and extract additional attributes.

---

# 3. Why JSON Instead of Scraping Everything From HTML?

One of the important decisions in this project was understanding **where the data actually existed**.

The initial movie list was available through a JSON response.

Instead of trying to scrape the entire movie listing from HTML, I used:

```python
data = res.json()
movies = data["response"]
```

This made the initial extraction easier because JSON provides structured data.

For example, instead of trying to identify movie cards, HTML classes, nested elements, and text manually, the movie records could be accessed directly as Python dictionaries.

### JSON approach

```text
JSON response
     ↓
Movie records
     ↓
Movie name
Movie URL
     ↓
Individual movie page
     ↓
Movie attributes
```

This also made the code easier to work with using Python.

However, the individual movie pages still needed to be requested because the additional attributes I wanted were available inside the page structure.

So the final approach was a **hybrid extraction process**:

```text
JSON → Get movie list + URLs
              ↓
HTML → Get movie attributes
```

This was a practical choice based on how the source data was structured.

---

# 4. Data Scraping

## Libraries Used

```python
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
```

### Purpose of each library

| Library | Purpose |
|---|---|
| `requests` | Send HTTP requests and retrieve web data |
| `BeautifulSoup` | Parse HTML and extract movie attributes |
| `pandas` | Store, clean, transform and export the dataset |

---

# 5. Data Extraction Code

The main scraping process was:

```python
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

movies_data = []

res = requests.get(
    "https://www.yidio.com/redesign/json/browse_results.php?"
    "sort=imdb_rating&type=movie&index=0&limit=1000"
)

soup = bs(res.content, "html.parser")

data = res.json()

movies = data["response"]

for movie in movies:

    movie_url = movie["url"]

    movie_request = requests.get(movie_url)

    movie_soup = bs(movie_request.content, "html.parser")

    details = movie_soup.find(
        "div",
        class_="details"
    ).find(
        "ul",
        class_="attributes"
    )

    items = details.find_all("li")

    certificate = (
        items[0].get_text(strip=True)
        if len(items) > 0 else ""
    )

    year = (
        items[1].get_text(strip=True)
        if len(items) > 1 else ""
    )

    duration = (
        items[2].get_text(strip=True)
        if len(items) > 2 else ""
    )

    imdb_rating = (
        items[3].get_text(strip=True)
        if len(items) > 3 else ""
    )

    movies_data.append({
        "Name": movie["name"],
        "Certificate": certificate,
        "Year of relase": year,
        "Duration": duration,
        "IMDB Rating": imdb_rating
    })

df = pd.DataFrame(movies_data)

df["id"] = range(1, len(df) + 1)

df = df[
    [
        "id",
        "Name",
        "Certificate",
        "Year of relase",
        "Duration",
        "IMDB Rating"
    ]
]

df.to_csv("movies_data.csv", index=False)

print(df.head())
```

---

# 6. Creating the Dataset

After extracting the records, I converted the scraped data into a Pandas DataFrame:

```python
df = pd.DataFrame(movies_data)
```

I then created an ID for each movie:

```python
df["id"] = range(1, len(df) + 1)
```

Finally, I selected the required columns and exported the dataset:

```python
df.to_csv("movies_data.csv", index=False)
```

The resulting CSV became the main dataset used for the next stages of the project.

---

# 7. Data Validation

This was an important part of the project.

After exporting the CSV, I opened the dataset in a spreadsheet to further inspect the records.

This helped me notice that some rows did not contain all of the expected attributes.

For example, some movies did not have a certificate.

Because the scraping logic initially assumed that:

```text
items[0] = Certificate
items[1] = Year
items[2] = Duration
items[3] = IMDb Rating
```

a movie with a missing certificate could cause the values to shift.

For example:

```text
Expected:

Certificate | Year | Duration | IMDb Rating
PG-13       | 2014 | 120      | 8.2
```

But if the certificate was missing, the extracted values could become:

```text
Certificate | Year | Duration | IMDb Rating
2014        | 120  | 8.2      | ...
```

This meant that **Duration could end up inside the Certificate column**, and the remaining values could also move into the wrong columns.

This was discovered during spreadsheet validation.

That is an important lesson from this project:

> **A dataset can look correct immediately after scraping but still contain structural data-quality issues.**

---

# 8. Fixing the Misaligned Data

To solve this, I used a Python cleaning function that checks whether values appear to belong to the correct column.

The basic idea is to identify values based on their expected format.

For example:

- Certificates are expected to look like certificate labels.
- Years should be numeric years.
- Duration should be a number followed by minutes or a numeric duration.
- IMDb Rating should be a decimal value in the expected rating range.

A cleaning function can be written like this:

```python
import re
import pandas as pd


KNOWN_CERTIFICATES = {
    "G",
    "PG",
    "PG-13",
    "R",
    "NC-17",
    "NR",
    "TV-G",
    "TV-PG",
    "TV-14",
    "TV-MA",
    "Approved",
    "Passed",
    "Not Rated",
    "Unrated"
}


def clean_movie_row(row):

    values = [
        row.get("Certificate"),
        row.get("Year of relase"),
        row.get("Duration"),
        row.get("IMDB Rating")
    ]

    values = [
        "" if pd.isna(value) else str(value).strip()
        for value in values
    ]

    certificate = ""
    year = ""
    duration = ""
    imdb_rating = ""

    # Identify certificate
    for value in values:
        if value in KNOWN_CERTIFICATES:
            certificate = value
            break

    # Identify year
    for value in values:
        if re.fullmatch(r"\d{4}", value):
            year = value
            break

    # Identify IMDb rating
    for value in values:
        try:
            number = float(value)

            if 0 <= number <= 10:
                imdb_rating = number
                break

        except (ValueError, TypeError):
            pass

    # Identify duration
    for value in values:
        duration_match = re.search(
            r"(\d{1,4})\s*(?:min|mins|minutes)?",
            value.lower()
        )

        if duration_match:
            number = int(duration_match.group(1))

            # Avoid treating the year or IMDb rating as duration
            if number != int(year) if year else True:
                if number > 10:
                    duration = number
                    break

    row["Certificate"] = certificate
    row["Year of relase"] = year
    row["Duration"] = duration
    row["IMDB Rating"] = imdb_rating

    return row
```

The function can then be applied to the dataset:

```python
df = df.apply(clean_movie_row, axis=1)
```

The exact cleaning logic can be adjusted depending on the values returned by the source.

### Why this approach?

Instead of blindly trusting column position, the cleaning process checks the **meaning and format of the value**.

This is an important data-analysis principle:

```text
Do not only ask:
"Which column is this value in?"

Also ask:
"Does this value actually belong in this column?"
```

---

# 9. Data Cleaning

After identifying the structural issues, the dataset was cleaned and standardized.

The cleaning stage focused on:

- Missing values
- Incorrectly shifted values
- Certificate validation
- Year validation
- Duration extraction
- IMDb rating validation
- Numeric conversion
- Consistent column names
- Duplicate/invalid records where applicable

The goal was to make the final dataset reliable enough for analysis.

---

# 10. Exploratory Analysis

Once the dataset was cleaned, I started exploring the data.

The questions included:

### Movies

- How many movies are in the dataset?
- Which movies have the most votes?
- Which movies have the highest IMDb ratings?

### Ratings

- What is the average IMDb rating?
- How does rating relate to number of votes?

### Time

- How are movies distributed by release year?
- Which years have the highest number of movies?

### Certificates

- Which certificates are most common?
- What is the distribution of movie certificates?

### Duration

- What is the average movie duration?
- What does the distribution of movie duration look like?
- Are there unusually long or short movies?

---

# 11. Power BI Dashboard

After cleaning and validating the dataset, I imported the final CSV into **Power BI**.

The purpose of the dashboard was to convert the raw dataset into a simple interactive analytical report.

## KPI Cards

The dashboard includes:

```text
Total Movies
Average IMDb Rating
Number of Votes
Average Duration
Earliest Movie Year
Latest Movie Year
```

The supplied dashboard shows:

| KPI | Value |
|---|---:|
| Total Movies | 1,000 |
| Average IMDb Rating | 8.2 |
| Number of Votes | 327M |
| Average Duration | 120.36 |
| Earliest Movie Year | 1902 |
| Latest Movie Year | 2026 |

These are the values displayed in the final dashboard. fileciteturn0file0L75-L94

---

# 12. Dashboard Visualizations

## Top 10 Most Voted Movies

This visual identifies movies with the highest number of IMDb votes.

The dashboard includes movies such as:

- The Shawshank Redemption
- The Dark Knight
- Inception
- Fight Club
- Interstellar
- Forrest Gump

The ranking and vote counts are shown in the dashboard. fileciteturn0file0L3-L14

---

## Top 10 Average IMDb Rating

This visual highlights movies with the highest average IMDb rating in the dataset.

The dashboard displays ratings reaching as high as **9.9** among the listed results. fileciteturn0file0L16-L27

---

## Movies by Release Year

A distribution chart shows how the movies are spread across release years.

The dataset covers movies from **1902 to 2026**. fileciteturn0file0L29-L39

---

## Certificate Distribution

A donut chart shows how movies are distributed across certificate categories.

The dashboard includes categories such as:

- NR
- R
- PG-13
- PG
- G

along with other certificate values present in the dataset. fileciteturn0file0L40-L51

---

## IMDb Rating vs Number of Votes

A scatter plot was used to compare:

```text
IMDb Rating
        vs
Number of Votes
```

This makes it possible to visually explore whether highly rated movies also tend to receive large numbers of votes. fileciteturn0file0L53-L58

---

## Duration Distribution

A distribution chart was created to understand how movie runtimes are spread across the dataset.

This also helps identify unusual duration values that may require additional data validation. fileciteturn0file0L57-L63

---

# 13. Interactive Filters

The Power BI dashboard includes filters for:

- Year of Release
- Certificate
- IMDb Rating
- Duration

This allows the user to move from an overall view to a more specific analysis.

For example, a user can filter the dashboard to investigate movies released during a specific period or movies within a specific IMDb rating range.

---

# 14. Detailed Movie Table

The dashboard also contains a detailed table with fields such as:

```text
Movie
Year of Release
Certificate
Duration
IMDb Rating
Number of Votes
```

This allows the user to move from high-level KPIs and charts to individual movie records. fileciteturn0file0L65-L74

---

# 🧠 What This Project Demonstrates

This project is designed to demonstrate practical **Data Analyst skills**, not just visualization.

### Data Collection

- Web data extraction
- JSON/API response handling
- HTML parsing
- HTTP requests

### Python

- Requests
- BeautifulSoup
- Pandas
- Functions
- Data transformation
- CSV handling

### Data Quality

- Missing values
- Misaligned columns
- Data validation
- Format-based validation
- Data cleaning
- Spreadsheet-based validation

### Analysis

- KPI creation
- Distribution analysis
- Ranking
- Trend analysis
- Relationship analysis
- Exploratory Data Analysis

### Power BI

- KPI cards
- Bar charts
- Donut charts
- Scatter plots
- Distribution charts
- Tables
- Slicers
- Interactive filtering
- Dashboard design

---

# 💡 Key Data Analyst Lesson

One of the biggest lessons from this project was that **data extraction is only the beginning**.

The actual workflow was:

```text
Collect Data
    ↓
Understand Data
    ↓
Validate Data
    ↓
Clean Data
    ↓
Analyze Data
    ↓
Visualize Data
    ↓
Communicate Results
```

The spreadsheet validation stage was particularly useful because it revealed an issue that was not immediately obvious from the Python output.

This demonstrates why a Data Analyst should not simply assume that scraped or exported data is correct.

---

# 📁 Suggested Project Structure

```text
IMDb-Top-1000-Movies/
│
├── data/
│   └── movies_data.csv
│
├── src/
│   ├── scraper.py
│   └── cleaning.py
│
├── dashboard/
│   └── IMDb_Top_1000.pbix
│
├── movie_dashboard.png
│
└── README.md
```

---

# 🚀 How to Run the Project

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd IMDb-Top-1000-Movies
```

## 2. Install dependencies

```bash
pip install requests pandas beautifulsoup4
```

## 3. Run the scraper

```bash
python scraper.py
```

This creates:

```text
movies_data.csv
```

## 4. Validate the CSV

Open the CSV in Excel or another spreadsheet application and inspect:

- Missing values
- Incorrect values
- Shifted columns
- Unexpected formats
- Duplicate records

## 5. Run the cleaning process

Apply the cleaning functions to correct structural issues and standardize the data.

## 6. Open Power BI

Import the cleaned CSV into Power BI.

Then create the required:

- Measures
- KPIs
- Charts
- Slicers
- Tables

Finally, build the dashboard shown above.

---

# 🛠️ Tech Stack

[![Python][Python]][Python-url]
[![Pandas][Pandas]][Pandas-url]
[![BeautifulSoup][BeautifulSoup]][BeautifulSoup-url]
[![Requests][Requests]][Requests-url]
[![Power BI][PowerBI]][PowerBI-url]
[![Excel][Excel]][Excel-url]
[![GitHub][GitHub]][GitHub-url]

---

# 📌 Project Summary

This project started with a simple analytical question:

> **What can we learn from the Top 1000 IMDb movies?**

To answer it, I built an end-to-end workflow:

**JSON Data Source → Python Scraping → HTML Extraction → Pandas → CSV → Spreadsheet Validation → Data Cleaning → Exploratory Analysis → Power BI Dashboard**

The project helped me practice the complete lifecycle of a Data Analyst project, from **understanding the source and collecting data to validating, cleaning, analyzing, visualizing, and communicating the results.**

---

# 👨‍💻 Author

**Varun Rana**

Data Analyst | Python | SQL | Power BI | Data Visualization

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
[GitHub-url]: https://github.com/
