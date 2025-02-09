# Open the file in read mode
expensesData = open("expenses.txt", "r")

total_expense = 0
daily_expenses = {}
category_expenses = {}

# Loop through each line in the file
for line in expensesData:
    parts = line.strip().split(" ")  # Remove extra spaces and split by space
    
    dates = parts[0]  # First part is the date
    amounts = float(parts[1])  # Convert amount to float
    categories = parts[2]  # Third part is the category
    descriptions = " ".join(parts[3:])  # Combine the rest for the full description

    total_expense += amounts  # Add to total expense

    # Store daily expenses
    if dates not in daily_expenses:
        daily_expenses[dates] = amounts
    else:
        daily_expenses[dates] += amounts

    # Store category expenses
    if categories not in category_expenses:
        category_expenses[categories] = amounts
    else:
        category_expenses[categories] += amounts  

# Sorting section
sortingExpensesStyle = input("Sort by (Date, Amount, or Category): ").capitalize().strip()

if sortingExpensesStyle == "Date":
    sortedDates = sorted(daily_expenses.items()) 
    print("\nSorted by Date:")
    for date, total in sortedDates:
        print(f"{date}: {total:.2f}")

elif sortingExpensesStyle == "Amount":
    sortedAmounts = sorted(daily_expenses.items(), key=lambda x: x[1]) 
    print("\nSorted by Amount:")
    for date, total in sortedAmounts:
        print(f"{date}: {total:.2f}")

elif sortingExpensesStyle == "Category":
    sortedCategories = sorted(category_expenses.items())
    print("\nSorted by Category:")
    for category, total in sortedCategories:
        print(f"{category}: {total:.2f}")

else:
    print("Invalid sorting option! Please choose Date, Amount, or Category.")


print(f"\nYour total expense is: {total_expense:.2f}") #Printing the total
# Close the file after reading
expensesData.close()