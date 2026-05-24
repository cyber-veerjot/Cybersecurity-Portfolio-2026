## B20 – Enhance the Security of a GitHub Project
### Description:
In this exercise, I improved authentication, session security, and production security options for my Flask web application project hosted on GitHub. Protecting user sessions and authentication systems is crucial because the project incorporates login, signup, profile management, and gameplay features.
### Security Enhancements Implemented:
1. **Secure Session Cookie Settings**
To strengthen the security of authenticated user sessions, secure session cookie settings were added.
```python
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SECURE = True
```
These settings guarantee that cookies are exclusively sent over HTTPS connections, lower the possibility of cross-site requests, and prohibit client-side access to cookies.
2. **Login Rate Limiting**
Flask-Limiter was used to add rate restriction to the login path.
```python
@auth.route("/login", methods=["GET", "POST"])
@limiter.limit("5 per minute")
def login():
```
By preventing multiple login attempts from the same IP address, this lessens brute-force password attacks.
3. **Debug Mode Protection**
At first, the project started the application straight in Flask debug mode.
```python
app.run(debug=True)
```
By using environment variables to adjust debug mode, this was improved.
```python
debug_mode = os.environ.get("FLASK_DEBUG", "0") == "1"
app.run(debug=debug_mode)
```
By doing this, the possibility of disclosing internal application data outside of development environments is minimized.
4. **Secure Secret Key Validation**
By verifying the environment variable prior to application startup, the Flask secret key handling was enhanced.
```python
SECRET_KEY = os.environ.get("GAME_SECRET_KEY")
```
In order to stop the application from launching without a secure secret key, validation was introduced. This enhances CSRF protection and session security.
### Analysis:
This exercise illustrated how defensive cybersecurity techniques can enhance a real-world Flask application's security posture. The danger of authentication attacks, information disclosure, and insecure session management can be decreased by improving session protection, login security, debug settings, and secret key handling.
### Evidence:
The file is uploaded in the folder. The repository link is: https://github.com/Games4Doritos/CITS3403-Project

