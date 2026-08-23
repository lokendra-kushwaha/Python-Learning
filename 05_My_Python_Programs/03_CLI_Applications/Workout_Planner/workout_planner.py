"""
Workout Routine Planner 🏋️‍♂️

A simple Command Line Interface (CLI) utility that displays a daily 
workout routine based on the user's input. Utilizes Python's structural 
pattern matching (match-case).

Created By: Lokendra Kushwaha
"""

def main():
    day1 = "Day - 1 : Upper Body Workout \n1. Regular Pushups\n2. Pike Walkouts \n3. Diamond Pushups"
    day2 = "Day - 2 : Lower Body Workout \n1. Squat Jumps\n2. All Side Lunges \n3. Squat Hold"
    day3 = "Day - 3 : Core Workout \n1. Star Crunches\n2. Bicycle Kicks \n3. Plank Hold"
    day4 = "Day - 4 : Upper Body Workout \n1. Regular Pushups\n2. Pike Walkouts \n3. Diamond Pushups"
    day5 = "Day - 5 : Lower Body Workout \n1. Squat Jumps\n2. All Side Lunges \n3. Squat Hold"
    day6 = "Day - 6 : Core Workout \n1. Star Crunches\n2. Bicycle Kicks \n3. Plank Hold"
    day7 = "Day - 7 : Yoga or Meditation 🧘‍♂️"

    print("=" * 50)
    print("       💪 WEEKLY WORKOUT PLANNER 💪       ")
    print("=" * 50)

    while True:
        input_day = input("\nEnter Workout Day (1-7) or type 'exit' to quit: ").strip().lower()
        
        if input_day == "exit":
            print("\nKeep pushing your limits! See you tomorrow. 🚀")
            break
        
        print("-" * 50)
        match input_day:
            case "1":
                print(day1)
            case "2":
                print(day2)
            case "3":
                print(day3)
            case "4":
                print(day4)
            case "5":
                print(day5)
            case "6":
                print(day6)
            case "7":
                print(day7)
            case _:
                print("❌ Invalid Input! Please enter a number between 1 and 7.")
        print("-" * 50)

if __name__ == "__main__":
    main()