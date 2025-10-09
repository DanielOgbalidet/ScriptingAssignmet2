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

def run_once(manager):
    """Manually trigger reminder sending once (for testing)."""
    # manager = StudentsManager()

    for student in manager.get_students():
        reminder = generate_reminder(student['name'], student['course'])
        send_reminder(student['email'], reminder)
        log_reminder(student, reminder)


def run_scheduler(manager):
    """Run the daily scheduled reminders (infinite loop)."""
    # manager = StudentsManager()
    schedule_reminders(
        students_manager=manager,
        reminder_generator=generate_reminder,
        reminder_sender=send_reminder,
        logger=log_reminder
    )


def add_student(manager):
    """Adding student to list"""
    manager.add_student("Daniel", "daniel@example.com", "AI", "16:30")
    manager.add_student("Even", "even@example.com", "Econ", "16:30")
    manager.save_students()


def remove_student(manager):
    """Removing student"""
    manager.remove_student("Daniel")


def list_students(manager):
    """Listing students"""
    manager.get_students()
    manager.list_students()

def main():
    """Main entry point for the console command."""
    # Creating manager
    manager = StudentsManager()

    # add and list students
    add_student(manager)
    print("Current list of students")
    list_students(manager)
    remove_student(manager)
    print("\nListing students after removing student")
    list_students(manager)

    print("Welcome to the Study Reminders automation system!\n")
    print("1. Send reminders once (manual test)")
    print("2. Run daily scheduler")
    choice = input("\nChoose an option (1 or 2): ")
    
    if choice == "1":
        run_once(manager)
    elif choice == "2":
        print("Starting daily scheduler... Press Ctrl+C to stop.")
        run_scheduler(manager)
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()
