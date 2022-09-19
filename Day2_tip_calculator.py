print("Welcome to tip calculator!")
bill=float(input("What was the total bill? $"))
percentage=int(input("What percentage tip would you like to give? 10, 20 or 15?"))
split=int(input("How many people to split the bill?"))
percentage_money=percentage/100
bill_money=bill*percentage_money
total_bill=bill+bill_money
split_money=total_bill/split
money=round(split_money,2)
print(f"Each person should pay {money}")
