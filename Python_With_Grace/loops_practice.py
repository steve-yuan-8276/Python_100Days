money = 1000
cost = 0
while money > 0:
    spend = input("How much money do you want to spend? ")
    spend = int(spend)
    if spend > money:
        print("You dont have enough money.")
        break
    cost = spend + cost
    money = money - spend
print(f"You spent {cost} in all")
print(f"you have {money} dollars left!")
