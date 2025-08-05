from datetime import datetime

print("🎂 Welcome to the Age Calculator!")

birth_year = input("Enter your birth year: ")

if not birth_year.isdigit():
    print("❌ Please enter a valid year.")
else:
    birth_year = int(birth_year)
    current_year = datetime.now().year
    age = current_year - birth_year
    print(f"🎉 You are {age} years old in {current_year}!")
