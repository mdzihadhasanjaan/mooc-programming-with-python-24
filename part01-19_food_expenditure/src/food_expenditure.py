# Write your solution here
time = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
spend = float(input("How many money do you spend on groceries in a week?"))
daily = (spend // 7) + price 
weekly = spend + (price * spend)
print("Average food expenditure:")
print(f"Daily: {daily: .2f} euros")
print(f"Weekly: {weekly: .2f} euros")

