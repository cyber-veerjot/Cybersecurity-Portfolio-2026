## B27 - Apply a learned concept in this unit to a real-world application/problem/environment
### Description:
In this exercise, I used a real-world Flask web application created for the CITS3403 Agile Web Development project to apply defensive cybersecurity ideas I acquired in CITS2006. The project was a multiplayer online game including leaderboards, profile management, user authentication, and gaming features.
### Cybersecurity Concepts Applied:
1. **Password Hashing**
Instead of being saved as plaintext passwords, passwords were securely hashed before being stored in the database to increase authentication security. In the event that the database was ever compromised, this helped safeguard user credentials.
- Implementaion:
```python
from werkzeug.security import generate_password_hash
hashed_password = generate_password_hash(password)
```
2. **Access Control**
Flask-Login was used to construct access control methods so that only users who were authenticated could access protected pages, like gameplay routes and profile pages.
- Implementation:
```python
@login_required
def profile():
```
As a result, protected functionality could not be accessed by unauthorized individuals.

3. **CSRF Protection**
Flask-WTF forms and CSRF tokens were used to develop CSRF protection, which shields forms from malicious or fraudulent requests.
- Implementation:
```python
{{ form.hidden_tag() }}
```
CSRF tokens were automatically added to protected forms as a result.

4. **Input Validation**
To decrease invalid input and enhance account security, validation checks were put in place for user account credentials such usernames and email addresses.
- Implementation:
```python
existing_account = Account.query.filter_by(email=email).first()
if existing_account and existing_account.id != current_user.id:
    flash("Email already in use.")
```
This enhanced account integrity and prevented duplicate email registrations.

5. **Secure Database Handling**
Instead of using risky raw SQL queries for database operations, the project employed SQLAlchemy ORM. SQL injection vulnerabilities were less likely as a result.
- Implementation:
```python
Account.query.filter_by(email=email).first()
```
Secure database interaction and safer user data handling were enhanced by the use of ORM queries.
### Analysis:
This exercise illustrated how the unit's defensive cybersecurity ideas may be immediately applied to the creation of practical web applications. The project's overall security posture was enhanced and safe software development standards were reinforced by the implementation of password hashing, authentication security, CSRF protection, input validation, access control, and secure database handling.
### Evidence:
https://github.com/Games4Doritos/CITS3403-Project.git -- Project Repository.
