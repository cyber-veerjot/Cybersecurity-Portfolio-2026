## B19 – Find and Fix a Vulnerability from a GitHub Project
### Description:
In this exercise, I examined the login validation logic utilised in my GitHub-hosted Flask web application project. I found a weak password policy vulnerability in the signup and password reset forms throughout the review. Users were able to establish weak passwords that were nonetheless vulnerable to dictionary and brute-force attacks because the original password validation merely imposed a minimum password length restriction.
### Vulnerability Identified:
#### Original Vulnerable Password Validation:
```python
password = PasswordField(
    'Password', 
    validators=[
        DataRequired('Required'), 
        Length(min=6, max=64, message='Password must be between 6 and 64 characters') 
    ]
)
```
This validation allowed weak passwords such as:

```text
password
12345678
abcdef12
```
### Security Fix Applied:
Using `Regexp` validation, the password validation was reinforced by requiring:
- minimum 8 characters
- uppercase letters
- lowercase letters
- numbers
- special characters
### Improved Secure Password Validation:
```python
password = PasswordField(
    'Password',
    validators=[
        DataRequired(message='Required'),
        Length(min=8, max=64, message='Password must be between 8 and 64 characters'),
        Regexp(
            r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).+$',
            message='Password must include uppercase, lowercase, number, and special character'
        )
    ]
)
```
### Analysis:
The significance of secure password policies in authentication systems was illustrated by this exercise. Increasing password validation strengthens defense against brute-force attacks, weak password attacks, and credential compromise. The patch strengthened defensive cybersecurity procedures and enhanced the application's overall security posture.
### Evidence:
The file is uploaded in this folder.
The Repo Link where the vulnerability found: https://github.com/Games4Doritos/CITS3403-Project 
