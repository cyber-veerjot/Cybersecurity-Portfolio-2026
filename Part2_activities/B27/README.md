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
