## B22 – Enhance the Cybersecurity of a Website from the Community
### Description:
In order to boost the website's security posture, I used OWASP ZAP to do a defensive cybersecurity assessment on a community website. Finding frequent online security misconfigurations and defensive security enhancements were the main goals of the evaluation.
### Security Issues Identified:
1. **Missing Content Security Policy (CSP) Header**
2. **Missing Anti-Clickjacking Protection**
3. **Missing Subresource Integrity (SRI) Attributes**
### Recommended Security Improvements:
1. **Content Security Policy Header**
I suggested utilizing a Netlify _headers configuration file to include a Content Security Policy (CSP) header to enhance the security of the website. By limiting the resources the browser is permitted to load, this helps lower the danger of clickjacking, malicious content injection, and cross-site scripting (XSS).
```
/*
  Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; frame-ancestors 'none'; object-src 'none'; base-uri 'self';
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
