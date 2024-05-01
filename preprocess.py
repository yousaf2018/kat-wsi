# import pandas as pd

# # Read the first CSV file containing patches names
# patches_df = pd.read_csv('C:\\Users\\Mahmood Yousaf\\Desktop\\kat-wsi\\zenodo_patches_names.csv')

# # Read the second CSV file containing selected data
# selected_df = pd.read_csv('C:\\Users\\Mahmood Yousaf\\Desktop\\kat-wsi\\selected_data.csv')

# # Extract the 'PATIENT' column from patches_df based on the pattern
# patches_df['PATIENT_ID'] = patches_df['PATIENT'].str.split('-').str[2]

# # Extract the 'PATIENT' and 'MSIStatus' columns from selected_df
# selected_df['PATIENT'] = selected_df['PATIENT'].str.split('-').str[2]

# # Create a new column 'Label' in patches_df based on matching 'PATIENT' and 'MSIStatus'
# patches_df['Label'] = patches_df['PATIENT_ID'].isin(selected_df.loc[selected_df['MSIStatus'] == 'MSI-H', 'PATIENT']).astype(int)

# # Save the modified DataFrame patches_df to a new CSV file
# patches_df.to_csv('C:\\Users\\Mahmood Yousaf\\Desktop\\kat-wsi\\patches_with_label.csv', index=False)

# print("New CSV file created with Label column.")


# import pandas as pd
# from sklearn.model_selection import train_test_split

# # Read the generated CSV file containing patches with labels
# patches_df = pd.read_csv('C:\\Users\\Mahmood Yousaf\\Desktop\\kat-wsi\\patches_with_label.csv')

# # Split the data into train and test sets with a 70:30 ratio
# train_df, test_df = train_test_split(patches_df, test_size=0.3, random_state=42)

# # Save the train and test sets to CSV files
# train_df.to_csv('C:\\Users\\Mahmood Yousaf\\Desktop\\kat-wsi\\train.csv', index=False)
# test_df.to_csv('C:\\Users\\Mahmood Yousaf\\Desktop\\kat-wsi\\test.csv', index=False)

# print("Train and test CSV files created.")


# import pandas as pd

# # Read the train.csv file into a DataFrame
# train_df = pd.read_csv('C:\\Users\\Mahmood Yousaf\\Desktop\\kat-wsi\\test.csv')
# train_df['r_path'] = train_df['PATIENT']

# # Rename the 'Label' column to 'label'
# train_df.rename(columns={'Label': 'label'}, inplace=True)
# train_df.rename(columns={'PATIENT': 'name'}, inplace=True)

# # Remove the 'PATIENT_ID' column
# train_df.drop(columns=['PATIENT_ID'], inplace=True)

# # Create a copy of the 'PATIENT' column as the 'PATIENT_PATH' column

# # Save the modified DataFrame back to train.csv file
# train_df.to_csv('C:\\Users\\Mahmood Yousaf\\Desktop\\kat-wsi\\test.csv', index=False)

# print("Train.csv file modified successfully.")


import pandas as pd

# Read the train.csv file into a DataFrame
train_df = pd.read_csv('C:\\Users\\Mahmood Yousaf\\Desktop\\kat-wsi\\test.csv')

# Reorder the columns
train_df = train_df[train_df.columns[[0, 2, 1]]]

# Save the modified DataFrame back to train.csv file
train_df.to_csv('C:\\Users\\Mahmood Yousaf\\Desktop\\kat-wsi\\test.csv', index=False)

print("Column location changed successfully in train.csv.")
