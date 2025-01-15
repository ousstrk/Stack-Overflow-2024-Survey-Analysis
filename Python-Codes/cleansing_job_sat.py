import pandas as pd
import numpy as np
import os

path = r"C:\Users\avogu\Desktop\DA Portfolio\Stackoverflow"
file = 'df_job_sat.csv'

df = pd.read_csv(f"{path}\{file}")

#determining the column list to work with
column_list = list(df.columns)
column_list.remove('ResponseId')
column_list.remove('JobSat')

#changing job sat result from 10 to 100 scala
df.loc[df["JobSat"] < 11, "JobSat"] *= 10
#changing the answers given in 10 scala
df.loc[(df[column_list] < 11).all(axis=1), column_list] *= 10

df.iloc[:, 1:] = df.iloc[:, 1:].replace(0, np.nan)

#removing old file
try:
    # Construct the full file path
    file_path = os.path.join(path, file)

    # Check if the file exists
    if os.path.exists(file_path):
        os.remove(file_path)  # Remove the file
        print(f"File '{file}' successfully removed from '{path}'.")
    else:
        print(f"File '{file}' does not exist in '{path}'.")

except Exception as e:
    print(f"An error occurred while removing the file: {e}")

#creating new file
df.to_csv(f'{path}\{file}', index=False)