# Import pandas library
import pandas as pd

# Create a DataFrame (like a table)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Full DataFrame:")
print(df)

# Access a single column
print("\nNames Column:")
print(df['Name'])

# Filter rows (Age > 30)
print("\nPeople older than 30:")
print(df[df['Age'] > 30])

# Add a new column
df['Salary'] = [50000, 60000, 70000, 80000]
print("\nDataFrame with Salary:")
print(df)

# Basic statistics
print("\nAverage Age:", df['Age'].mean())

# Save to CSV
df.to_csv('output.csv', index=False)