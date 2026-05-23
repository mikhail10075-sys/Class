def total_calc(bill_amount, tip_perc):
    return bill_amount*(tip_perc/100)

bill_amount = int(input("Enter Bill Amount: "))
tip_perc = int(input("Enter tip % "))

y = total_calc(bill_amount, tip_perc)
x = bill_amount + y

print(x, "is the total amount.")

