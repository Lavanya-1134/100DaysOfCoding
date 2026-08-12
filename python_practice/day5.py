print("=== ResQHub Rescue Animal List ===")

num_reports = int(input("How many animals do you want to report? "))

animals = []

for i in range(1, num_reports + 1):
    animal_name = input(f"Enter animal {i} name: ")
    animals.append(animal_name)

print("\n=== Rescue Reports ===")

for i in range(len(animals)):
    print(f"{i + 1}. {animals[i]}")

print(f"\nTotal Animals Reported: {len(animals)}")