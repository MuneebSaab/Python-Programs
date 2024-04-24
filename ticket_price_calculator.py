# Ticket Price Calculator for Rollercoaster
print("Welcome to the Rollercoaster!")
# Determining whether somebody is capable of Riding the Rollercoaster
height = int(input("What is your height in cm?\n"))

if height >= 120:
  print("You can ride the rollercoaster!")
  # Determining Ticket Price for Age
  age = int(input("What is your age?\n"))
  if age < 12:
    print("Please pay 5$.")
  elif age <= 18: 
    print("Please pay 7$.")
  else:
    print("Please pay 12$.")
# Determining whether somebody is not capable of Riding the Rollercoaster
else:
  print("Sorry, you have to grow taller to ride the rollercoaster.")
