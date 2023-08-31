POUNDS_PER_TALENT = 20
LOTS_PER_POUND = 32
GRAMS_PER_LOT = 13.3
GRAMS_PER_KILOGRAM = 1000

talents = float(input("Enter the mass in talents: "))
pounds = float(input("Enter the mass in pounds: "))
lots = float(input("Enter the mass in lots: "))

talents_to_grams = talents * POUNDS_PER_TALENT * LOTS_PER_POUND * GRAMS_PER_LOT
pounds_to_grams = pounds * LOTS_PER_POUND * GRAMS_PER_LOT
lots_to_grams = lots * GRAMS_PER_LOT

total_in_grams = talents_to_grams + pounds_to_grams + lots_to_grams

kilograms = total_in_grams // GRAMS_PER_KILOGRAM
remaining_grams = total_in_grams % GRAMS_PER_KILOGRAM

# Output the result
print("The mass is approximately:")
print(f"{kilograms:.0f} kilograms and {remaining_grams:.2f} grams")