import os
import functions as f

directory = r"C:\Users\avogu\Desktop\DA Portfolio\Stackoverflow"

all_files = os.listdir(directory)
items_to_work = [item for item in all_files if item.startswith('df')]

print(items_to_work)

for item in items_to_work:
    f.cleansing_csv(item,directory)