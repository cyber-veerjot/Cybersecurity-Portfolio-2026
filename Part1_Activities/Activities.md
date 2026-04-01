This folder contains documentation for Part 1 cybersecurity portfolio activities.

## Activity A1 – Security concepts used on campus
### Description:
I explored and identified various security concepts implemented across my university campus (UWA). These systems are designed to protect students, staff, and university property from both physical and digital threats.
### Identified Security Concepts:
1. **Surveillance Systems (CCTV Cameras)**
CCTV cameras are installed in lecture halls, libraries, entrances, and outdoor areas. These cameras continuously monitor activity and help deter theft, vandalism, and suspicious behaviour.
2. **Access Control Systems (Student ID Cards)**  
Certain buildings and rooms require student ID card access. This ensures that only authorised individuals can enter restricted areas such as labs or staff-only zones.
3. **Physical Security (Security Guards)**  
Campus security personnel are present around campus, especially during late hours. They monitor activities, respond to incidents, and ensure overall safety.
4. **Alarm Systems**  
Emergency alarms are installed in buildings and can be triggered during dangerous situations such as fires or security threats.
### Analysis:
These security concepts work together to create a layered security approach. Surveillance helps in monitoring and recording activities, access control restricts entry to authorised users, and security personnel provide real-time response. This combination significantly reduces risks and improves overall campus safety.
### Evidence:
These observations were made during my daily visits to campus, including the library, lecture halls, and main entrances. CCTV cameras and ID card access points were clearly visible and actively used. These evidences are all inside the evidence folder.

## Activity A2 - Discover security concepts used in public space
### Description:
To do this activity, i explored the bus station, shopping centre and city as there are multiple security systems implemented. These systems are designed to protect people from potential harm and prevent crimes.
### Identified Security Concepts:
1. **Surveillance Systems (CCTV Cameras)**
CCTV cameras in public areas such as bus stations and shopping centres are used to monitor large crowds and detect suspicious behaviour.
2. **Security Patrols**
Security guards patrol areas such as bus stations, city to maintain order and respond to incidents.
3. **Emergency Systems**
Public places have emergency alarms and help points that people can use during unsafe situations.
4. **Lighting and Visibility**  
Well-lit areas reduce crime by increasing visibility at night. 
### Analysis:
Public security systems focus on crime prevention and safety of large groups of people. Surveillance and guards work together to reduce risks such as theft and vandalism.
### Evidence:
These observations were made at the bus station, shopping centre, and city areas. Supporting images such as CCTV cameras, access control systems, and alarm systems have been uploaded in the Evidence folder.

## Activity A3 - Discover security concepts used in your house
### Description:
For this activity, I explored the security measures used in my home to protect personal safety and private information.
### Identified Security Concepts:
1. **Home Surveillance (CCTV / Apartment Security)**
CCTV cameras are installed at the main entrance of the apartment building and monitored through a security room.
2. **Physical Locks**  
Our front door has a deadbolt and also chain is attached for the extra security and the windows have locks, which prevent unauthorised physical entry.
3. **Wifi Security**
Our home network uses a strong password and encryption so neighbours cannot connect and see our traffic.
4. **Device Security**
Phones and laptops use PINs or biometrics to protect personal data if a device is lost or stolen.
### Analysis:
At home, security focuses on protecting family members and personal data. Physical controls (locks, cameras) protect against intruders, while digital controls (Wi‑Fi encryption, screen locks) protect our online accounts and devices.
### Evidence:
These observations were made at my home and apartment building. Supporting images such as door locks and CCTV systems are available in the Evidence folder.

## Activity A5 - Discover cryptographic implementation used online
### Description:
I looked at how encryption is used by today's websites to safeguard data while it is in transit. Encryption technologies are used by many websites to guarantee secure transactions, safe browsing, and the defense of private data from hackers.
### Identified Cryptographic Implementation:
1. **HTTPS (TLS Encryption)**
The majority of secure websites use HTTPS, which encrypts communication between my browser and the server using TLS (Transport Layer Security). By looking at the icon near to https://apps.cas.uwa.edu.au/even-student/timetable.htm in the browser address bar, I was able to confirm that it has a secure connection. The site uses TLS to encrypt requests and responses so that login details, personal information, and other data are protected while travelling across the internet.
2. **Password Hashing**
Online platforms store passwords in encrypted form instead of plain text. They securely store password hashes using cryptographic hashing methods (such as SHA-256 and bcrypt). Websites make reference to this in their privacy or security documentation, even though users cannot see it directly. The uwa website is also using a SHA-256 cryptographic hashing algorithm.
3. **Secure Cookies**
Secure cookies are frequently used by websites; they are encrypted and have the features Secure and HttpOnly. Cookie theft and session hijacking are less common because of these cryptographic protections.
### Analysis:
Cryptography ensures confidentiality and integrity of data. It prevents attackers from intercepting or modifying sensitive information such as passwords and personal details. these techniques like TLS which protects data from being intercepted, Certificates which prevent fake websites from tricking users and Hashing which protects stored credentials even if a database is compromised, collaborate to build a safe online environment and stop threats like phishing scams, man-in-the-middle attacks, and credential theft.
### Evidence:
i captured the screenshots of the uwa website to show the certificates and TLS Encryption and uploaded in the evidence folder.

## Activity A6 - Discover cryptographic implementation used offline.
### Description:
In this activity, I explored how cryptography is used offline to protect data without requiring an internet connection. Encryption is used by many common tools, cards, and systems to safely store and safeguard private data even while they are not in use.
### Identified Cryptographic Implementation:
1. **Bank card chip**
EMV chips, which contain encrypted payment information, are used in modern debit and credit cards.
The chip uses secure methods (such as RSA, DES, or ECC) to perform offline cryptographic authentication when it is put into a payment terminal, ensuring that the card is authentic and hasn't been cloned.
2. **Device Encryption**
As i use macbook, apple uses a full-disk encryption technology which is file vaults. FileVault operates offline and protects all files, documents, and system data by encrypting the whole internal drive using XTS-AES-128 with a 256-bit key. The data cannot be accessed without my recovery key or login password, even if the laptop is stolen and the SSD is taken out. Data is always encrypted while it's at rest, not simply when the device is linked to a network.
### Analysis:
To protect data even when devices are not connected to the internet, offline cryptography is crucial and plays an important role in physical world. If a device is lost or stolen, full-disk encryption (such as FileVault) guarantees that private data cannot be accessed. Cryptographic algorithms are used by EMV chips to offer safe authentication and protect personal data.
### Evidence:
To support this activity, i have taken the screenshots of fileVault, bank card chip and uploads in the evidence folder.

## Activity A7 - Discover cryptography used in modern networks
### Description:
In this activity, I explored how cryptography is used in modern networks to protect data while it is being transmitted between devices. Unlike offline cryptography, network cryptography focuses on securing communication over wireless and internet-based systems.
### Identified Cryptographic Implementation:
1. **Wi-Fi Encryption (WPA2/WPA3)**  
Modern wireless networks use encryption protocols such as WPA2 (AES‑CCMP) or WPA3 (Simultaneous Authentication of Equals) to secure communication between devices and the router. This ensures that data transmitted over the network cannot be easily intercepted. WPA3 improves security by using more robust key exchange methods, making it harder to crack the Wi‑Fi password offline.
2. **HTTPS/TLS Encryption**
The fundamental protocol (used in HTTPS) combines symmetric (for data transmission) and asymmetric (for handshake) encryption to secure web surfing, email, and API communications.
### Analysis:
Modern networks use multiple layers of cryptographic protection. Wi-Fi encryption (WPA2/WPA3) secures the wireless communication channel, while TLS encryption protects the data being transmitted over the network. These layers work together to ensure that sensitive information remains secure from interception and unauthorized access. For this activity, i used the wireshark to capture the network traffic of secure website over the wifi and wifi uses WPA3. I observed the TLSv1.2/TLSv1.3 encrypted packets and Application Data (encrypted) which confirms that modern Wi‑Fi networks transport encrypted traffic.
### Evidence:
The screenshots of the wireshark capture and the Wifi security settings, i attached in the evidence folder.

## Activity A9 - Discover privacy technique used online
### Description:
For this exercise, I investigated privacy strategies frequently employed on internet platforms to prevent unauthorized parties from accessing private data and communications. End-to-end encryption (E2EE) is one of the most popular and efficient online privacy strategies. Even if the connection goes over servers or networks, this technique guarantees that messages or data can only be viewed by the sender and the intended receiver.
### Identified Privacy Techniques:
1. **WhatsApp End-to-End Encryption(E2EE)**
Whatsapp uses the end-to-end encryption to secure all user to user communications, including audio, videos, photos and file exchanges. it implies a message sent by a user is encrypted on their device. The internet service providers, hackers, governments, and even WhatsApp itself are unable to decrypt the message as it moves over the network. The private key needed to decrypt the communication is only on the intended recipient's device.
### Analysis:
It is one of the strongest online privacy techniques available today because it ensures the confidentiality, integrity, and privacy. In the event of a data breach, messaging apps could access or leak messages without E2EE. Because E2EE avoids extensive types of digital spying and interception, it is used by several contemporary privacy-focused online platforms, such as WhatsApp, Signal, and iMessage.
This method facilitates safe interpersonal contact and provides users ownership over their data.
### Evidence:
i have attached the screenshots for the whatsapp encryption in the evidence folder.

## Activity A10 - Discover privacy technique used offline
In this activity, i explored the privacy techniques that are used to protect personal information without accessing the internet. 
### Identified Privacy Techniques:
1. **Document Protection (Shredding Sensitive Papers)**  
Before being disposed of, sensitive documents like bank statements or personal details are shredded. In order to prevent documents from being read or reconstructed from the trash, a paper shredder breaks them up into tiny bits. By doing this, private information is shielded from illegal access.
2. **Locked Mail Box**
Letters that might contain private information, such bills or bank statements, cannot be readily accessed by others if the mailbox is locked. 
The mailbox can only be opened by someone with the key, which lowers the possibility of identity fraud and mail theft.
### Analysis:
Even in the absence of online networks, strategies like document shredding and sealed mailboxes guarantee that personal information cannot be accessed, stolen, or exploited. Because not all privacy dangers originate from the internet, some come from people physically accessing equipment or data, offline privacy solutions are crucial. By limiting who can physically access personal information, these offline techniques collectively offer robust protection, proving that privacy is not just a digital issue but also necessitates the safe handling of physical objects.
### Evidence:
All supporting evidence for this activity is stored in the folder of evidence.













