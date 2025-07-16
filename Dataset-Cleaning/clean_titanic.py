import pandas as pd
df = pd.read_csv('titanic.csv')
df.drop_duplicates(inplace=True)
df['Age'] = df['Age'].fillna(df['Age'].mean())  # Updated line
df.to_csv('cleaned_titanic.csv', index=False)
print("Dataset cleaned and saved as 'cleaned_titanic.csv'")