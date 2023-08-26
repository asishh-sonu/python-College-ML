# Create a dictionary representing the population of five cities
city_population = {
    "New York": 8537673,
    "Los Angeles": 3979576,
    "Chicago": 2693976,
    "Houston": 2129784,
    "Phoenix": 1680992
}

# A. Add two more cities and their population to the dictionary
city_population["London"] = 8982000
city_population["Toronto"] = 2731571

# B. Find the city with the highest population
highest_population_city = max(city_population, key=city_population.get)
highest_population = city_population[highest_population_city]

print("City with the highest population:", highest_population_city)
print("Population of the city with the highest population:", highest_population)

# C. Check if a city "London" is present in the dictionary
is_london_present = "London" in city_population

# D. Remove a city and its population from the dictionary
city_to_remove = "Phoenix"
if city_to_remove in city_population:
    del city_population[city_to_remove]
    print(f"{city_to_remove} and its population have been removed from the dictionary.")
else:
    print(f"{city_to_remove} is not present in the dictionary.")

# Print the updated dictionary and check for London's presence
print("Updated city population dictionary:", city_population)
print("Is 'London' present in the dictionary?", is_london_present)
