# B20 - Security Enhancements for Flask Game Project
# Four security issues identified and improved:
#
# 1. Secure session cookie settings
# 2. Login rate limiting
# 3. Debug mode disabled by default
# 4. Secure secret key validation


import os

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


# ── ISSUE 1: Missing secure session cookie settings ──────────────────────
# VULNERABILITY:
# Session cookies were not explicitly protected.
#
# RISK:
# Cookies may be exposed to client-side scripts or unsafe transmission.
#
# FIX:
# Configure secure Flask session cookie settings.

class SecureCookieConfig:
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = True

# WHAT IT DOES:
# SESSION_COOKIE_HTTPONLY prevents JavaScript from accessing cookies.
# SESSION_COOKIE_SAMESITE helps reduce cross-site request attacks.
# SESSION_COOKIE_SECURE ensures cookies are only sent over HTTPS.


# ── ISSUE 2: No rate limiting on login route ─────────────────────────────
# VULNERABILITY:
# The login route allowed unlimited repeated login attempts.
#
# RISK:
# Attackers may attempt brute-force password attacks.
#
# FIX:
# Add Flask-Limiter to restrict repeated login requests.

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Apply limiter to login route:

@auth.route("/login", methods=["GET", "POST"])
@limiter.limit("5 per minute")
def login():
    pass

# WHAT IT DOES:
# Restricts login attempts to 5 requests per minute per IP address.
# This reduces brute-force and credential guessing attacks.


# ── ISSUE 3: Debug mode enabled by default ───────────────────────────────
# VULNERABILITY:
# Flask debug mode was enabled directly in the application.
#
# RISK:
# Debug mode can expose internal errors, stack traces,
# application paths, and sensitive information.
#
# FIX:
# Control debug mode using an environment variable.

debug_mode = os.environ.get("FLASK_DEBUG", "0") == "1"

if __name__ == "__main__":
    app.run(debug=debug_mode)

# WHAT IT DOES:
# Debug mode stays disabled unless intentionally enabled
# through the FLASK_DEBUG environment variable.


# ── ISSUE 4: Secret key not safely validated ─────────────────────────────
# VULNERABILITY:
# The Flask secret key was loaded without validation.
#
# RISK:
# The application may start without a valid secret key,
# weakening session security and CSRF protection.
#
# FIX:
# Validate the secret key before application startup.

class Config:
    SECRET_KEY = os.environ.get("GAME_SECRET_KEY")

    @staticmethod
    def validate():
        if not Config.SECRET_KEY:
            raise ValueError(
                "GAME_SECRET_KEY environment variable is not set."
            )

# WHAT IT DOES:
# Prevents the application from starting without a valid secret key.
# This improves session security and CSRF protection.