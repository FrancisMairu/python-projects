#prompt user to enter list items and then display their input following alphabetical order and no duplicates
teams = []
while True:
    values = input("Enter values (type 'stop' when done): ")
    if values.lower() == "stop":
        break
    teams.append(values)

# Remove duplicates by converting list to a set and back to a list
unique_teams = list(set(teams))

# Sort the list of unique teams alphabetically
unique_teams.sort()

# Calculate the total number of teams
total_teams = len(unique_teams)

# Print the sorted list of unique teams
print("Unique teams in alphabetical order:")
for team in unique_teams:
    print(team)

# Print the total number of teams
print(f"Total number of unique teams printed: {total_teams}")
