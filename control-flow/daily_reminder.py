# daily_reminder.py

# Prompt for task description
task = input("Enter your task: ")

# Prompt for priority level
priority = input("Priority (high/medium/low): ").lower().strip()

# Prompt for time sensitivity
time_bound_input = input("Is it time-bound? (yes/no): ").lower().strip()

# Convert time_bound_input to boolean
time_bound = True if time_bound_input == "yes" else False

# Use match-case to handle priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
        if time_bound:
            message += " that requires immediate attention today!"
        else:
            message += "."
        print(message)
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
        if time_bound:
            message += " but consider addressing it soon!"
        else:
            message += "."
        print(message)
    case "low":
        message = f"Note: '{task}' is a low priority task"
        if time_bound:
            message += " but make sure to handle it today if possible."
        else:
            message += " You can do it when you have free time."
        print(message)
    case _:
        print("Invalid priority level entered. Please enter high, medium, or low.")