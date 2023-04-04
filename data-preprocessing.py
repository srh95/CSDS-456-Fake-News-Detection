import pandas as pd

file_name = "Liar-dataset/valid.tsv"

data = pd.read_csv(file_name, sep='\t', index_col=0)

# Remove irrelevant columns (keep only statement, label, speaker, and subject)
print(data)
cols = [4, 5, 6, 7, 8, 9, 10, 11, 12]
data.drop(data.columns[cols], axis=1, inplace=True)
print(data)

# Delete any rows with null or blank value
data.dropna(axis=0, how='any', inplace=True)

# Name columns
data.columns =['Label', 'Statement', 'Subject', 'Speaker']

# Convert labels to true and false 
data['Label'] = data['Label'].replace(['true', 'mostly-true', 'half-true'], 'TRUE')
data['Label'] = data['Label'].replace(['barely-true', 'false', 'pants-fire'], 'FALSE')

# Output as csv file
header = ['Statement', 'Label', 'Subject', 'Speaker']
data.to_csv("four-variable-files/valid.csv", columns = header, index=False)
