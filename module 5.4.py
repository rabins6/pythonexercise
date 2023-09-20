cities = []

for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)

print("City names:")
for city in cities:
    print(city)