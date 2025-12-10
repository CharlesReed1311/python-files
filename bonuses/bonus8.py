date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10?\n")
thoughts = input("Let your thoughts flow:\n")

with open(f"apps/journal/{date}.txt", 'w') as file:
    file.write(mood + '\n')
    file.write(thoughts)