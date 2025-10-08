# main.py
"""
Main script for the study_reminders package.
Integrates all modules to automate study reminder generation, sending, and logging.
"""

from study_reminders import (
    StudentsManager,
    generate_reminder,
    send_reminder,
    log_reminder,
    schedule_reminders
)


def run_once():
    """Manually trigger reminder sending once (for testing)."""
    manager = StudentsManager()

    # Iterate over all students
    for student in manager.get_students():
        # Generate personalized reminder
        reminder = generate_reminder(student['name'], student['course'])
        
        # Simulate sending
        send_reminder(student['email'], reminder)
        
        # Log the reminder
        log_reminder(student, reminder)


def run_scheduler():
    """Run the daily scheduled reminders (infinite loop)."""
    manager = StudentsManager()
    schedule_reminders(
        students_manager=manager,
        reminder_generator=generate_reminder,
        reminder_sender=send_reminder,
        logger=log_reminder
    )


if __name__ == "__main__":
    print("Welcome to the Study Reminders automation system!\n")
    print("1. Send reminders once (manual test)")
    print("2. Run daily scheduler")
    choice = input("\nChoose an option (1 or 2): ")

    if choice == "1":
        run_once()
    elif choice == "2":
        print("Starting daily scheduler... Press Ctrl+C to stop.")
        run_scheduler()
    else:
        print("Invalid choice. Exiting.")
