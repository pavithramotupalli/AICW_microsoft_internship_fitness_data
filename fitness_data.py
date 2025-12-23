# Fitness Tracker using OOPS, File Handling and Error Handling

class FitnessTracker:
    def __init__(self, filename="fitness_data.txt"):
        self.filename = filename

    def add_record(self):
        try:
            date = input("Enter date (DD-MM-YYYY): ")
            steps = int(input("Enter steps walked: "))
            calories = int(input("Enter calories burned: "))
            workout_time = int(input("Enter workout time (minutes): "))

            with open(self.filename, "a") as file:
                file.write(f"{date},{steps},{calories},{workout_time}\n")

            print("✅ Fitness record added successfully!")

        except ValueError:
            print("❌ Please enter valid numeric values.")
        except Exception as e:
            print("❌ Error:", e)

    def view_records(self):
        try:
            with open(self.filename, "r") as file:
                records = file.readlines()

                if not records:
                    print("No fitness records found.")
                    return

                print("\n📊 Fitness Records:")
                print("Date | Steps | Calories | Workout Time")
                print("---------------------------------------")

                for record in records:
                    date, steps, calories, time = record.strip().split(",")
                    print(f"{date} | {steps} | {calories} | {time} mins")

        except FileNotFoundError:
            print("❌ No data file found. Please add records first.")
        except Exception as e:
            print("❌ Error:", e)


# Main Program
tracker = FitnessTracker()

while True:
    print("\n--- Fitness Tracker Menu ---")
    print("1. Add Fitness Record")
    print("2. View Fitness Records")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            tracker.add_record()
        elif choice == 2:
            tracker.view_records()
        elif choice == 3:
            print("👋 Exiting Fitness Tracker. Stay Healthy!")
            break
        else:
            print("❌ Invalid choice. Try again.")

    except ValueError:
        print("❌ Please enter a number.")