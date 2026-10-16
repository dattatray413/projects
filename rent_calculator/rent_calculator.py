# inputs we need from user

room_Rent = int(input("enter your room rent = "))
food_Spend = int(input("enter your food spend = "))
ectricity_Usage = int(input("enter your electricity usage = "))
per_unit = int(input("enter per unit charge of electricity = "))
persons_Inroom = int(input("enter number of people living in room = "))

electricity_bill = ectricity_Usage * per_unit

# total room rent calculation
total_spend = room_Rent + food_Spend + electricity_bill

# room rent calculation as per person
perPerson_Rent = total_spend / persons_Inroom

# outpus of total rent and per person rent
print(f"total rent of room = {total_spend}")
print(f"per person rent of room = {perPerson_Rent}")
