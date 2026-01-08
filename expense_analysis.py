
import pandas as pd
import matplotlib.pyplot as plt

# --- STEP 2: CREATE DATA (Section 3.3 & 6.1) ---
# We use a Dictionary to create the dataset
data = {
    'Date': ['2024-01-01', '2024-01-05', '2024-01-10', '2024-01-15', '2024-01-20', '2024-01-25'],
    'Category': ['Rent', 'Groceries', 'Transport', 'Groceries', 'Entertainment', 'Transport'],
    'Amount': [1500, 200, 50, 150, 100, 60]
}

# Convert dictionary to a Pandas DataFrame
df = pd.DataFrame(data)


# A. Calculate Total Spending per Category (Group By)
category_analysis = df.groupby('Category')['Amount'].sum().reset_index()

# B. Calculate Financial Summary
total_income = 3000  # Fixed Income
total_expense = df['Amount'].sum()
total_savings = total_income - total_expense

# Print the text report
print("--- FINANCIAL REPORT ---")
print(f"Total Income:   ${total_income}")
print(f"Total Expenses: ${total_expense}")
print(f"Total Savings:  ${total_savings}")
print("\n--- SPENDING BY CATEGORY ---")
print(category_analysis)


# Create a Bar Chart
plt.figure(figsize=(8, 5)) # Set the size of the picture
plt.bar(category_analysis['Category'], category_analysis['Amount'], color='skyblue')

# Add labels and title
plt.title('Monthly Expenses by Category')
plt.xlabel('Category')
plt.ylabel('Amount Spent ($)')
plt.grid(axis='y', linestyle='--', alpha=0.7) # Add light grid lines

# Show the plot
plt.show()
