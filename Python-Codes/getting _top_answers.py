import pandas as pd
import os

def getting_top(path, csv):
    data = pd.read_csv(f"{path}\{csv}")
    column_list = list(data.columns)

    # Calculate True counts for each column (excluding 'ResponseId')
    true_counts = data.iloc[:, 1:].sum()

    #getting top columns
    if len(column_list) >= 40:
        sorted_data = true_counts.sort_values(ascending=False).head(15)
        column_list_to_hold = [key for key, value in sorted_data.to_dict().items()]
    elif len(column_list) >= 20:
        sorted_data = true_counts.sort_values(ascending=False).head(10)
        column_list_to_hold = [key for key, value in sorted_data.to_dict().items()]
    else:
        return

    # dropping columns that have less true counts from top 15 or 10 according to total column num
    column_to_drop = list(set(column_list) - set(column_list_to_hold))
    column_to_drop.remove("ResponseId")

    df_new = data.drop(columns=column_to_drop)

    try:
        # Construct the full file path
        file_path = os.path.join(path, csv)

        # Check if the file exists
        if os.path.exists(file_path):
            os.remove(file_path)  # Remove the file
            print(f"File '{csv}' successfully removed from '{path}'.")
        else:
            print(f"File '{csv}' does not exist in '{path}'.")

    except Exception as e:
        print(f"An error occurred while removing the file: {e}")

    df_new.to_csv(f'{path}\{csv}', index=False)

path = r"C:\Users\avogu\Desktop\DA Portfolio\Stackoverflow"
files = ['df_ai_ben.csv', 'df_ai_tool_use_cause.csv', 'df_AIsearch.csv', 'df_database.csv', 'df_language.csv',
         'df_learn_code_from.csv', 'df_opsys.csv', 'df_platform.csv']

for csv in files:
    getting_top(path, csv)
