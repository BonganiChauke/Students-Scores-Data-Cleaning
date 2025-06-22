# Student Scores Data Cleaning Tool

This Python script cleans a dataset of student scores by handling missing values, validating dates, and ensuring grade validity. The tool uses pandas for efficient data manipulation.

## Features

- Removes rows with null values in critical columns (Math, Science, English, Grade)
- Validates and cleans the EnrollmentDate column by removing invalid entries
- Ensures grades are valid (A-F only)
- Provides before/after cleaning summary statistics
- Saves cleaned data to a new CSV file

## Prerequisites

- Python 3.6+ [Download](https://code.visualstudio.com/download)
- pandas library
- VS Code [Download](https://code.visualstudio.com/download)

## Installation
```bash
pip install pandas
```

## How to Run in VS Code

1. Open VS Code and navigate to the folder containing the script  
2. Ensure you have the Python extension installed in VS Code  
3. Place your input CSV file (`student_scores_dirty.csv`) in the same directory  
4. Open the `student_scores_cleaning.py` file  
5. Run the script using one of these methods:  
   - Click the "Run Python File" button in the top-right corner  
   - Right-click in the editor and select "Run Python File in Terminal"  
   - Open the terminal (<kbd>Ctrl</kbd>+<kbd>`</kbd>) and run:  

```bash
python student_scores_cleaning.py
```
## Expected Output

When you run the script successfully, you should see output similar to this in your terminal:

```text
Initial Dataset Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 5 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   Math            95 non-null     float64
 1   Science         97 non-null     float64
 2   English         96 non-null     float64
 3   Grade           98 non-null     object 
 4   EnrollmentDate  100 non-null    object 
dtypes: float64(3), object(2)
memory usage: 4.0+ KB
None

   Math  Science  English Grade EnrollmentDate
0  85.0     92.0     88.0    A     2022-09-01
1  78.0     85.0      NaN    B     invalid_date
2   NaN     76.0     82.0    C     2022-09-01

Cleaning Summary:
Before Cleaning: 100 rows
After Cleaning: 89 rows

Sample of Cleaned Data:
   Math  Science  English Grade EnrollmentDate
0  85.0     92.0     88.0    A     2022-09-01
3  92.0     88.0     95.0    A     2022-09-01
4  76.0     81.0     79.0    B     2022-09-01

Cleaned data has been saved to 'student_scores_cleaned.csv'.
```
