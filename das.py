import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt

# Set display options for Pandas
pd.set_option('display.max_columns', None)

# Load the JSON data from the file
with open("/home/nisha/Desktop/web/message.json", 'r') as file:
    json_data = json.load(file)

# Extract relevant data
results = json_data["results"]

# Normalize the data to extract the 'total' patients information
data = []
for result in results:
    diagnosis_id = result["diagnosisId"]
    disease = result["disease"]
    code = result["code"]
    total_patients = result["patients"]["total"]
    
    for gender, count in total_patients.items():
        data.append({
            "diagnosisId": diagnosis_id,
            "disease": disease,
            "code": code,
            "gender": gender,
            "count": count
        })

# Create a DataFrame from the extracted data
df = pd.DataFrame(data)
print(df.head(5))

# Print the columns of the DataFrame
# print("DataFrame columns:", df.columns)

# # Print the first few rows of the DataFrame
# print("DataFrame head:")
# print(df.head())

# # Plotting using Seaborn
# plt.figure(figsize=(14, 8))
# sns.barplot(x='disease', y='count', hue='gender', data=df)
# plt.xlabel('Disease')
# plt.ylabel('Number of Patients')
# plt.title('Number of Patients by Disease and Gender')
# plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
# plt.show()

    # Create a DataFrame from the extracted data
# df = pd.DataFrame(data)

# # Print the columns of the DataFrame
# print("DataFrame columns:", df.columns)

# # Print the first few rows of the DataFrame
# print("DataFrame head:")
# print(df.head())

# # Plotting using Seaborn
# plt.figure(figsize=(14, 8))
# sns.barplot(x='disease', y='count', hue='gender', data=df)
# plt.xlabel('Disease')
# plt.ylabel('Number of Patients')
# plt.title('Number of Patients by Disease and Gender')
# plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
# plt.show()
    
    
# normalized_data = pd.json_normalize(json_data)

# print("DataFrame columns:", normalized_data.columns)
# print("DataFrame head:")
# print(normalized_data.head())

# # normalized_data.head()
# # normalized_data.tail()
# # normalized_data.info()

# # normalized_data.describe()
# normalized_data['disease'].unique()

# unique_items_counts = normalized_data['disease'].value_counts()


# # unique_items_counts.plot( kind='bar',color='blue')
# sns.catplot(kind='bar', data=normalized_data, x='patients.new.male',y='di')
# # plt.title('new patients')
# # plt.xlabel('patients.new.male')
# # plt.label('patients.new.female')
# # plt.xlabel('patients.new.other')
# # plt.ylabel('Counts')
# # plt.xticks(rotation=45)
# # plt.show()





