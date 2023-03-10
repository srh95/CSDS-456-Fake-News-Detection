import pandas as pd

file_name = "Liar-dataset/valid.tsv"

data = pd.read_csv(file_name, sep='\t', index_col=0)

# Remove irrelevant columns (keep only statement and label)
cols = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
data.drop(data.columns[cols], axis=1, inplace=True)


# Delete any rows with null or blank value
data.dropna(axis=0, how='any', inplace=True)

# Name columns
data.columns =['Label', 'Statement']

# Convert labels to true and false 
data['Label'] = data['Label'].replace(['true', 'mostly-true', 'half-true'], 'TRUE')
data['Label'] = data['Label'].replace(['barely-true', 'false', 'pants-fire'], 'FALSE')

# Output as csv file
header = ['Statement', 'Label']
data.to_csv("valid.csv", columns = header, index=False)
