# e-logbook

Project Title: E-Logbook System

Project Overview:
The E-Logbook System is a web application designed to facilitate the efficient assessment of students undergoing industrial training (IT) by their supervisors. The system allows students to log their daily activities, submit reports, and receive assessments from both IT supervisors and school supervisors.

Key Features:
User Categories:
Student:

Registration Details:
1. Full Name
2. University/College/Polytechnic Name (selectable from a list)
3. College/Faculty (based on the selected institution)
4. Department (based on the selected college/faculty)
5. Matriculation Number
6. Phone Number
7. Password
8. Gender
9. Place of IT (i.e. location of IT)
10. Photograph
11. Email

Daily Activity Logging:

1. Each student has a profile where they can input daily activities.
2. Activities are organized into weeks (64 weeks for the duration of IT).
3. Students must indicate their start date for IT.
4. Students can only input information for the current day or days in the past.

Activity Details:
1. Each week is further divided into days.
2. Students can mark each day as a holiday or a day with activities.
3. Students can input text and upload images for each day.
4. A switch allows students to indicate if there is a holiday or if there will be activity for a particular day.

Supervisor Interaction:

1. Students can send invites to IT supervisors.
2. Supervisors can access the logbook for each week if the student approves the request.

IT Supervisor:
Registration Details:

1. Full Name
2. Organization Name
3. Role at Organization
4. Phone Number
5. Email

Supervision:

IT supervisors can view the logbook of students who have approved their access.
Supervisors can assess and mark the activities for each week.

School Supervisor:

Registration Details:

1. Full Name
2. Institution Name
3. Role at Institution
4. Phone Number
5. Email
6. Supervision:

Similar to IT supervisors, school supervisors can view the logbook of students under their supervision.
School supervisors can assess and mark the activities for each week.
System Workflow:
Student Workflow:

Sign up and provide necessary details.
Log daily activities, marking days as holidays or active.
Invite IT and school supervisors.
Receive assessments and feedback.
IT Supervisor Workflow:

Receive invites from students.
Access the logbook of approved students.
Assess and mark student activities for each week.
School Supervisor Workflow:

Receive invites from students.
Access the logbook of approved students.
Assess and mark student activities for each week.
Security Measures:
Each user has a unique username for easy identification.
Authentication and authorization mechanisms are in place to ensure secure access to logbooks.
Technical Specifications:
Frontend: HTML, CSS, JavaScript
Backend: Django (Python)
Database: SQLite (for simplicity, can be upgraded based on production needs)
User Authentication: Django built-in authentication system
File Storage: Django storage for handling uploaded images

Future Enhancements:
Notification System:
Implement a notification system to inform users of logbook assessments and feedback.
Advanced Reporting:
Incorporate advanced reporting features for a comprehensive overview of student activities.
