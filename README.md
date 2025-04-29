# School Enrollment Web App
This is my initial full-stack web application: a school website that allows users to register, log in, and enroll in courses.

## Features
- User registration and authentication  
- Student login with session management  
- View list of available courses  
- Enroll in selected courses with feedback/alerts  
- Flash messages for user actions  
- Clean HTML/CSS frontend with responsive layout

## Tech Stack
- Frontend: HTML, CSS, Bootstrap  
- Backend: Python (Flask)  
- Database: MongoDB (with MongoEngine ORM)  
- Templating: Jinja2  
- Authentication: Flask-WTF + Flask sessions

##  How It Works
1. Visit the registration page and create a new student account  
2. Log in with your email and password  
3. Browse the list of available courses  
4. Select and enroll in any course you like  
5. Flash messages confirm success or alert duplicates  

## Setup Instructions
1. Clone the repo  
   ```bash
   git clone https://github.com/yourusername/school-enrollment-app.git
   cd school-enrollment-app
   ```
2. Create a virtual environment and install dependencies  
   ```bash
   python -m venv venv  
   source venv/bin/activate  # or venv\Scripts\activate on Windows  
   pip install -r requirements.txt  
   ```
3. Start the Flask app  
   ```bash
   flask run  
   ```
4. Visit `http://127.0.0.1:5000` in your browser  

## Screenshots  
Home Page:

![image](https://github.com/user-attachments/assets/ee099ab7-f398-40de-8c14-7bdfa127e06f)

Registration Form:

![image](https://github.com/user-attachments/assets/a5dcf623-45dd-4050-9009-77a173659c5e)

Courses list:

![image](https://github.com/user-attachments/assets/f4642c3e-25e9-492e-a964-845d126a7f1f)

## Lessons I Learned
- Working with Flask routes and templates  
- User session management  
- Integrating MongoDB with a Python app  
- Debugging form validation, redirects, and CSS bugs. 

## Future Improvements
- Switch to Flask-Login for cleaner auth  
- Add user dashboards and admin controls  
- REST API for enrollment data  
- UI/UX improvements with JavaScript or React
