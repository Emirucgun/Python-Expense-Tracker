# 💰 Expense Tracker

A simple Python program to track **daily expenses** and **category-wise expenses** from a text file.

## 📌 Features
✅ Reads expenses from `expenses.txt`  
✅ Calculates **total expenses**  
✅ Displays **daily totals**  
✅ Displays **category-wise totals**  
✅ Allows **sorting by Date, Amount, or Category**  

---

## 📂 File Structure
```
Expense-Tracker/
│── expenses.txt          # Input file with expense data
│── program.py            # Main Python script
│── README.md             # This file
```

---

## 📥 Input Format (`expenses.txt`)
Each line should be in the format:
```
DATE AMOUNT CATEGORY "DESCRIPTION"
```
- `DATE` → in **YYYY-MM-DD** format  
- `AMOUNT` → **float** (money spent)  
- `CATEGORY` → single word (e.g., FOOD, TRANSPORT)  
- `DESCRIPTION` → **inside double quotes** (optional, multiple words)  

### **Example:**
```
2025-02-01 12.50 FOOD "Lunch at McDonald's"
2025-02-01 3.20 TRANSPORT "Bus ticket"
2025-02-02 8.90 ENTERTAINMENT "Movie night"
2025-02-02 15.00 FOOD "Dinner at a restaurant"
2025-02-03 45.00 SHOPPING "New shoes"
2025-02-03 2.50 TRANSPORT "Metro ticket"
```

---

## ⚡ How to Run the Program
Make sure you have Python installed, then run:
```bash
python program.py
```

---

## 📊 Example Output
### **Sorted by Date**
```
Sorted by Date:
2025-02-01: 15.70
2025-02-02: 23.90
2025-02-03: 47.50
```
### **Sorted by Category**
```
Sorted by Category:
ENTERTAINMENT: 8.90
FOOD: 27.50
SHOPPING: 45.00
TRANSPORT: 5.70
```
### **Sorted by Amount**
```
Sorted by Amount:
2025-02-01: 15.70
2025-02-02: 23.90
2025-02-03: 47.50
```


---

## 👨‍💻 Author
- **Emir Ucgun**  
- GitHub: [github.com/Emirucgun](https://github.com/Emirucgun)


---

🎉 **Happy Budgeting!** 🚀  
