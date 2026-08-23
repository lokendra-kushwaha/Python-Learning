"""
Study Hours Tracker ⏱️📚

A simple CLI tool to track daily study hours and compare them 
against a daily target (10 hours). Demonstrates the use of a while-loop 
accumulator and basic conditional logic.

Created By: Lokendra Kushwaha
"""

def main():
    total_hours = 0.0 
    daily_target = 10.0

    print("=" * 50)
    print("           🎯 DAILY STUDY TRACKER 🎯           ")
    print("=" * 50)

    while True:
        hours_input = input("Enter your Study Time in Hours (or '0' to finish): ")
        
        try:
            hours = float(hours_input)
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        if hours == 0:
            break

        total_hours += hours
        print(f"Logged: {hours} hours. (Total so far: {total_hours} hrs)")

    print("-" * 50)
    print(f"📊 Today's Total Study Hours: {total_hours} Hours")

    # Checking against the target
    if total_hours < daily_target:
        remaining = daily_target - total_hours
        print(f"⚠️ Your 10-hour target isn't completed yet.")
        print(f"⏳ Remaining hours needed: {remaining} hours")
    else:
        print("🏆 Well Done! Your daily target is completed. 😊")
    print("=" * 50)

if __name__ == "__main__":
    main()