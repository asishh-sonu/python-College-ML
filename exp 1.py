# Create a Python list containing the names of five countries
countries = ["United States", "Canada", "Australia", "Germany", "Brazil"]

# a. Add two more countries to the list
countries.append("China")
countries.append("India")

# b. Print the third country in the list
third_country = countries[2]
print("Third country in the list:", third_country)

# c. Sort the list in alphabetical order
countries.sort()

# d. Check if a country "India" is present in the list
is_india_present = "India" in countries

# Print the updated list and check for India's presence
print("Updated countries list:", countries)
print("Is 'India' present in the list?", is_india_present)
