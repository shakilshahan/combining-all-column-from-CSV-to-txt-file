import pandas as pd
import zipfile
import os

# Path to the zipped folder containing CSV files
zip_file_path = 'E:\\shahan\\AUSTRALIA\\CDU\\semester1\\Software_Now\\Assignment_2.zip'

# Path to the directory to extract the files
extracted_folder = 'E:\\shahan\\AUSTRALIA\\CDU\\semester1\\Software_Now\\Assignment_2_extracted'

# Extract the contents of the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder)  # Extract files to 'Assignment_2_extracted' folder

# List the extracted CSV files
csv_files = [file for file in os.listdir(extracted_folder) if file.endswith('.csv')]

# Columns containing text (update with actual column names)
text_columns = ['HADM_ID', 'SHORT-TEXT', 'ICD9_CODE', 'ICD9', 'Label']  # Replace with the actual column names containing texts

# Combine text from all specified columns in CSV files into a single string
combined_text = ''

for file in csv_files:
    file_path = os.path.join(extracted_folder, file)
    df = pd.read_csv(file_path)
    combined_text += f"CSV1.csv: {file}\n\n"
    for col in text_columns:
        if col in df.columns:
            texts = df[col].dropna().astype(str).tolist()
            combined_text += f"Column '{col}':\n"
            combined_text += '\n\n'.join(texts) + '\n\n'  # Add separator between texts from different columns
    combined_text += '\n\n---------------------------------------------\n\n'  # Add separator between files

# Save the combined text into a single .txt file
output_file_path = 'E:\\shahan\\AUSTRALIA\\CDU\\semester1\\Software_Now\\combined_texts.txt'

with open(output_file_path, 'w', encoding='utf-8') as txt_file:
    txt_file.write(combined_text)

print(f"Combined texts from specified columns in multiple CSV files saved to '{output_file_path}'")
