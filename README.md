# Student Scores Data Cleaning Tool

This Python script cleans a dataset of student scores by handling missing values, validating dates, and ensuring grade validity. The tool uses pandas for efficient data manipulation.

## Features

- Removes rows with null values in critical columns (Math, Science, English, Grade)
- Validates and cleans the EnrollmentDate column by removing invalid entries
- Ensures grades are valid (A-F only)
- Provides before/after cleaning summary statistics
- Saves cleaned data to a new CSV file

## Prerequisites

- Python 3.6+
- pandas library
- VS Code

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

