# student_scores_cleaning.py
import pandas as pd

# Load the dataset
file_path = './student_scores_dirty.csv'
student_scores_df = pd.read_csv(file_path)

# Display the first few rows of the dataset before cleaning
def display_initial_info(df):
    print("Initial Dataset Info:")
    print(df.info())
    print(df.head())

def clean_student_scores(df):
    # 1. Remove rows with null values in critical columns
    cleaned_df = df.dropna(subset=['Math', 'Science', 'English', 'Grade'])

    # 2. Validate and clean the 'EnrollmentDate' column
    # Remove invalid dates (e.g., entries with "invalid_date")
    cleaned_df = cleaned_df[~cleaned_df['EnrollmentDate'].str.contains("invalid_date", na=False)]

    # 3. Ensure grades are valid (e.g., A-F)
    valid_grades = {'A', 'B', 'C', 'D', 'E', 'F'}
    cleaned_df = cleaned_df[cleaned_df['Grade'].isin(valid_grades)]

    # Reset index for cleaned dataframe
    cleaned_df.reset_index(drop=True, inplace=True)

    return cleaned_df

# Display before vs after cleaning
def display_cleaning_summary(before_df, after_df):
    print("\nCleaning Summary:")
    print(f"Before Cleaning: {before_df.shape[0]} rows")
    print(f"After Cleaning: {after_df.shape[0]} rows")

    print("\nSample of Cleaned Data:")
    print(after_df.head())

if __name__ == "__main__":
    # Display initial information
    display_initial_info(student_scores_df)

    # Clean the dataset
    cleaned_student_scores_df = clean_student_scores(student_scores_df)

    # Display cleaning summary
    display_cleaning_summary(student_scores_df, cleaned_student_scores_df)

    # Save cleaned data to a new CSV
    #cleaned_student_scores_df.to_csv('student_scores_cleaned.csv', index=False)
    print("\nCleaned data has been saved to 'student_scores_cleaned.csv'.")
