## B22 – Enhance the Cybersecurity of a Website from the Community
### Description:
In order to boost the website's security posture, I used OWASP ZAP to do a defensive cybersecurity assessment on a community website. Finding frequent online security misconfigurations and defensive security enhancements were the main goals of the evaluation. I only recommended the solutions because i didn't get the consent for this activity.
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
```
2. **Anti-Clickjacking Protection**
I suggested using the X-Frame-Options header or a similar frame-ancestors Content Security Policy directive to strengthen defense against clickjacking attacks. By doing this, dangerous websites are less likely to put their content inside obscured frames that are intended to deceive users into taking unwanted activities.
```
X-Frame-Options: DENY
```
Alternatively:
```
Content-Security-Policy: frame-ancestors 'none';
```
3. **Subresource Integrity (SRI)**
I suggested adding Subresource Integrity (SRI) properties to third-party scripts and stylesheets to enhance the security and integrity of externally loaded resources. By doing this, attackers are less likely to alter materials hosted externally and insert malicious code into the website.
```
<link
  rel="stylesheet"
  href="https://example.com/style.css"
  integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/ux..."
  crossorigin="anonymous">
```
### Analysis:
This exercise showed how defensive cybersecurity principles may be used to enhance website security in practical settings. The evaluation enhanced knowledge of HTTP security headers, frequent web security misconfigurations, and defensive defense techniques used to lessen web-based threats.
### Evidence:
All screenshots are in this folder.
### References:
https://owasp.org/www-community/attacks/Clickjacking?utm_source=chatgpt.com - Anti-Clickjacking

https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity - Subresource Integrity

https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP - CSP
