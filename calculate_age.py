def calculate_age(birth_year, current_year):
    return current_year - birth_year

birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))

age = calculate_age(birth_year, current_year)
print(f"You are {age} years old.")
