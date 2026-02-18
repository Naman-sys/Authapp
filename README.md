# Flask Authentication App

A simple Flask web application with user authentication features including registration, login, and dashboard.

## Features

- User Registration with validation
- User Login with password authentication
- Secure Password Hashing using bcrypt
- User Dashboard
- Session Management
- Logout functionality

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- bcrypt

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Activate the virtual environment
2. Run the application:
   ```
   python app.py
   ```
3. Open your browser and navigate to `http://localhost:5000`

## Project Structure

- `app.py` - Main Flask application
- `templates/` - HTML templates
  - `base.html` - Base template
  - `index.html` - Home page
  - `register.html` - Registration page
  - `login.html` - Login page
  - `dashboard.html` - User dashboard
- `instance/` - Instance folder for database

## Validation Rules

### Registration
- Name should not be empty
- Email should not be empty
- Email should be unique
- Password should not be empty
- Password should be at least 6 characters

## Database

The application uses SQLite database with the following user model:
- id (Integer, Primary Key)
- name (String, Required)
- email (String, Unique)
- password (String, Hashed with bcrypt)

## License

This project is open source.
