from setuptools import setup, find_packages

setup(
    name="study_reminders",  # Your package name
    version="1.0",
    packages=find_packages(),  # Automatically find your study_reminders package
    include_package_data=True,  # Include non-Python files if needed (like students.json)
    description="A Python package that automates personalized study reminders for students.",
    author="Daniel Ogbalidet",
    author_email="daniel.ogbalidet@example.com",
    install_requires=[
        "schedule",  # Required for scheduler.py
    ],
    entry_points={
        'console_scripts': [
            # This allows running "study-reminders" from the terminal if you want
            'study-reminders=study_reminders.main:main',
        ],
    },
)
