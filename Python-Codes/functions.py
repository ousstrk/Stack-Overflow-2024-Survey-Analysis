import pandas as pd
import os


def getting_null_info(csv_file, path):
    """ function is designed to analyze a CSV file, load it into a pandas DataFrame, and print out information about
    the number of null (missing) and non-null (not missing) values for each column in the dataset."""

    database = pd.read_csv(f"{path}\{csv_file}")
    column_list = database.columns.to_list()

    for i in column_list:
        null_values = database[i].isnull().sum()
        not_null_values = database[i].notnull().sum()
        print(f'{i} column has {null_values} null values and {not_null_values} non-null values.')


def sep_and_bool(csv_file, path, column_name):
    """processes a CSV file containing a column of semicolon-separated strings and creates a new DataFrame with
    additional boolean columns. These columns indicate the presence of each unique value (from the semicolon-separated
    entries) in the original column. The function then outputs a new CSV file with the updated data."""

    df = pd.read_csv(f"{path}\{csv_file}")
    col = df[column_name]

    # making array from columns and minimizing the data ro handle easily
    arr = col.unique()

    # splitting values and making nested list with them
    nested_lists = [str(i).split(";") for i in arr]

    # getting all the unique values from list (getting the new column names)
    unique_values = set()
    for sublist in nested_lists:
        unique_values.update(sublist)
    unique_values = sorted(unique_values)
    #unique_values.remove('nan')
    try:
        unique_values.remove('nan')
    except ValueError:
        print("'nan' not found in the list.")

    # making new df with boolean, isinstance to avoid null/nan values
    new_df = pd.DataFrame(col)
    for column in unique_values:
        new_df[f'{column_name} - {column}'] = df[column_name].apply(lambda x: column in x if isinstance(x, (list, str))
        else False)

    #replacing null values with "Missing" and non-null values with "Present" for selected column for future analysis
    df[column_name] = df[column_name].apply(lambda x: "Missing" if pd.isnull(x) else "Present")

    #combining new df with old one
    df_combined = pd.concat([df, new_df], axis=1)
    df_combined.drop(column_name, axis='columns', inplace=True)

    try:
        # Construct the full file path
        file_path = os.path.join(path, csv_file)

        # Check if the file exists
        if os.path.exists(file_path):
            os.remove(file_path)  # Remove the file
            print(f"File '{csv_file}' successfully removed from '{path}'.")
        else:
            print(f"File '{csv_file}' does not exist in '{path}'.")

    except Exception as e:
        print(f"An error occurred while removing the file: {e}")

    df_combined.to_csv(f'{path}\{csv_file}', index=False)



def detect_semicolon(csv_file, path):
    """function reads a CSV file and checks for the presence of a semicolon (;) in any column of the first 20 rows.
    If a column contains a semicolon in any of the first 20 rows, the function adds the column name to a list and
    returns that list."""

    #getting CSV file
    file_path = f"{path}/{csv_file}"
    df = pd.read_csv(file_path)

    #inspecting the first 20 rows for performance issues
    first_20_rows = df.head(20)

    #loop through each column and check for semicolons and making list from columns that contains semicolon
    list_w_semicolon = []
    for column in first_20_rows.columns:
        # Check if any cell in the first 5 rows of this column contains a semicolon
        contains_semicolon = first_20_rows[column].apply(lambda x: ';' in str(x)).any()
        if contains_semicolon:
            list_w_semicolon.append(column)

    return list_w_semicolon

def cleansing_csv(csv_file, path):
    """function is designed to clean a CSV file by processing columns that contain semicolons. It identifies those
    columns and then passes them to the sep_and_bool function for further processing."""
    for column in detect_semicolon(csv_file, path):
        sep_and_bool(csv_file, path, column)


