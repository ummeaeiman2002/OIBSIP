# Advanced BMI Calculator

Internship: Oasis Infobyte  
Track: Python Programming  
Task: Task 2 — Advanced BMI Calculator

## Project Description

The Advanced BMI Calculator is a desktop application developed using Python and Tkinter. It calculates Body Mass Index (BMI), displays the corresponding BMI category, stores records for multiple users in an SQLite database, and provides BMI history and trend visualization.

## Features

- User-friendly graphical interface using Tkinter
- BMI calculation based on weight and height
- Color-coded BMI categories
- Input validation for invalid and non-positive values
- Multiple-user BMI records
- SQLite database for persistent history
- BMI history viewer
- BMI trend graph using Matplotlib
- Database and graph error handling

## Technologies Used

- Python
- Tkinter
- SQLite
- Matplotlib

## Installation

1. Install Python 3.
2. Install Matplotlib:

   `python -m pip install matplotlib`

3. Open a terminal in the project directory.
4. Run the application:

   `python main.py`

## How to Use

1. Enter the user's name.
2. Enter weight in kilograms.
3. Enter height in meters.
4. Click **Calculate BMI**.
5. Click **View BMI History** to see saved records.
6. Enter a user's name and click **View BMI Trend Graph** to view their BMI history graph.

## Database

The application creates an SQLite database named `bmi_records.db` automatically when it runs. BMI records are saved locally.

## Author

Developed as part of the Oasis Infobyte Python Programming Internship.
