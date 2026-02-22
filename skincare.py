# Skincare & Self-Care Tracker

records = []

print("---------- SKINCARE & SELF-CARE TRACKER ----------")
choice = int(input(
    "1. Add Daily Record\n"
    "2. View Daily Records\n"
    "3. View Final Skin Report\n"
    "4. Exit\n"
    "Choose an option: "
))

if choice == 1:
    water = int(input("Enter water intake (in glasses): "))
    skincare = input("Did you complete morning skincare? (yes/no): ")
    sunscreen = input("Did you apply sunscreen today? (yes/no): ")
    night = input("Did you complete night skincare? (yes/no): ")
    hours = float(input("Enter sleep hours: "))

    score = 0

    if water >= 8:
        score += 2
    if skincare == "yes":
        score += 2
    if sunscreen == "yes":
        score += 2
    if hours >= 7:
        score += 2

    records.append(score)

    print(f"Daily Score : {score}/8")


elif choice == 2:
    if len(records) == 0:
        print("No Records Found")
    else:
        print("Daily Skincare Score")
        day = 1
        for s in records:
            print(f"Day {day} : {s}/8")
            day += 1


elif choice == 3:
    if len(records) == 0:
        print("No Data Available")
    else:
        total = sum(records)
        days = len(records)
        average = total / days

        print("Total Score:", total)
        print("Number of days:", days)
        print("Average Score:", average)


elif choice == 4:
    print("Exiting program")


else:
    print("Invalid choice")