# Student Management System

## Overview

This is a Python-based Student Management System that allows management of students, courses, registrations, scheduling, and student scores. It also generates text reports and displays charts showing academic progress and course enrollment.


## Features

- **Student Management**
  - Create students with name, student ID, and major
  - View student details including registered courses and GPA
  - Search students by name or student ID
  - Register or withdraw students from courses
  - Schedule courses for students
  - Add scores and calculate average GPA

- **Course Management**
  - Create courses with name, course code, and credits
  - View course details and enrolled students

- **Reporting**
  - Generate student reports with scores
  - Generate course enrollment reports
  - Display bar charts for:
    - Student academic progress (average scores)
    - Course enrollment numbers


## Requirements

- Python 3.x
- `matplotlib` library for plotting

Install dependencies:

```bash
pip install matplotlib
```

## Usage

Run the program:

```bash
python student_management_system.py
```

Use the interactive menu to:
- Create students and courses
- Register/withdraw students from courses
- Schedule courses
- Add student scores
- Search students
- Generate reports
- Exit the program

Charts will display after exiting.

## Code Structure

- `Student` class: manages student info, registrations, scheduling, and scores
- `Course` class: manages course info and enrolled students
- `StudentManagementSystem` class: main system controller
- Main script: command-line interactive interface


## Notes

- Data is stored in memory only; no database persistence
- Terminal clears screen between actions for clarity
- Simple input validation; ensure correct data entry
- Charts display upon program exit

