"""
Student Performance Analysis
Author: Salwa Chaib
Description: Analysis of student scores using Pandas & Matplotlib
"""
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'student': ['Ahmed', 'Fatima', 'Karim', 'Salma', 'Youssef'],
    'math': [85, 92, 78, 88, 95],
    'physics': [80, 89, 85, 90, 92],
    'french': [75, 88, 82, 95, 85]
}
df = pd.DataFrame(data)
df['average'] = df[['math', 'physics', 'french']].mean(axis=1)

print("Top students by average:")
print(df.sort_values('average', ascending=False))

# Visualization
df.plot(x='student', y=['math', 'physics', 'french'], kind='bar')
plt.title('Student Scores Comparison')
plt.savefig('scores.png')
print("Analysis completed successfully!")
