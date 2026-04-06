This folder contains documentation for Part 1 cybersecurity portfolio activities.

## Activity A1 – Security concepts used on campus
### Description:
I explored and identified various security concepts implemented across my university campus (UWA). These systems are designed to protect students, staff, and university property from both physical and digital threats.
### Identified Security Concepts:
1. **Surveillance Systems (CCTV Cameras)**
CCTV cameras are installed in lecture halls, libraries, entrances, and outdoor areas. These cameras continuously monitor activity and help deter theft, vandalism, and suspicious behaviour.
2. **Access Control Systems (Staff Only)**  
A door in a workplace that reads "Staff Only/Authorized Personnel Only." The sign makes it very obvious that only employees are permitted inside after that point. By restricting access to just those who are authorized, this straightforward physical access control helps safeguard critical data and back-office spaces.
3. **Security On-Campus**  
Campus security personnel are present around campus, especially during late hours and there’s also an emergency contact present everywhere. They monitor activities, respond to incidents, and ensure overall safety.
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
1. **Information Centre**
I watched the information desk at a nearby bus station, where employees assist travelers with schedules, route details, and ticket inquiries. People don't need to browse the entire station for information because this desk serves as a focal point for inquiries and assistance. Because travelers may promptly ask employees for assistance, report suspicious activity, or obtain instructions rather than going into prohibited areas, it enhances safety and security.
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
1. **Home Surveillance and Fence**
the main entrance has the cameras installed so that the entrance can be monitored through the security room and fence is installed all around the apartment.
2. **Physical Locks**  
to prevent unauthorised entry, the apartment's main door has a rim lock which ensures double security.
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

## Activity A6 - Discover cryptographic implementation used offline
### Description:
In this activity, I explored how cryptography is used offline to protect data without requiring an internet connection. Encryption is used by many common tools, cards, and systems to safely store and safeguard private data even while they are not in use.
### Identified Cryptographic Implementation:
1. **Bank card chip**
EMV chips, which contain encrypted payment information, are used in modern debit and credit cards.
The chip uses secure methods (such as RSA, DES, or ECC) to perform offline cryptographic authentication when inserted into a payment terminal, ensuring that the card is authentic.
2. **Device Encryption**
Apple devices uses FileVault which operates offline and protects all files, documents, and system data by encrypting the whole internal drive using XTS-AES-128 with a 256-bit key. The data cannot be accessed without my recovery key or login password, even if the laptop is stolen and the SSD is taken out. Data is always encrypted while it's at rest, not simply when the device is linked to a network.
### Analysis:
Offline cryptography plays an important role in physical world because if a device is lost or stolen, full-disk encryption (such as FileVault) ensures that private data cannot be accessed. Cryptographic algorithms are used by EMV chips to offer safe authentication and protect personal data.
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
Text messages, voice notes, voice calls, video calls, images, videos, and file attachments are all protected by WhatsApp's end-to-end encryption. Before a message leaves my phone, it is instantly encrypted on my device using the recipient's public key, turning its content into meaningless ciphertext. Internet service providers, hackers on the same network, governmental organizations, and even WhatsApp itself are unable to decrypt or read this ciphertext as it moves via Wi-Fi or mobile networks and passes through WhatsApp's servers. Since the corresponding private key is kept private and stored on the intended recipient's device, decryption is only possible there. Because of its architecture, end-to-end encryption is a powerful online privacy tool because even if someone were to intercept the traffic or obtain access to WhatsApp's servers, they would still be unable to see the actual messages.
### Analysis:
It is one of the strongest online privacy techniques available today because it ensures the confidentiality, integrity, and privacy. In the event of a data breach, messaging apps could access or leak messages without E2EE. Because E2EE avoids extensive types of digital spying and interception, it is used by several contemporary privacy-focused online platforms, such as WhatsApp, Signal, and iMessage. This method facilitates safe interpersonal contact and provides users ownership over their data.
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

## Activity A11 - Discover 5 unique access control devices
### Description:
I investigated several access control systems utilized in both digital and physical settings for this exercise. Access control devices are made to limit access to only those who are authorized. These devices make sure that only authorized users may access or utilize a system, protecting buildings, rooms, data, and personal belongings.
### Identified Access Control Devices:
1. **Biometric Scanner**
Smartphones, computers, and office access systems all use fingerprint scanners. Only if the fingerprint matches the biometric data that has been stored is access allowed. Strong security is provided by biometric access since fingerprints are distinct.
2. **KeyPad Lock**
These are found in offices, garages, homes, and gates and to unlock the door, a person must input the correct number code.
3. **RFID Card Reader**  
Uses radio-frequency cards (e.g., student ID) to grant access and commonly use in the offices, appartments and universities.
4. **Facial Recognition System**  
Identifies individuals based on facial features.
5. **Mobile Access Control Systems**
Smartphones are used by users of mobile access control systems to unlock doors. These systems enable communication between the access control device and the smartphone via Bluetooth, NFC, or Wi-Fi.
### Analysis:
By limiting access to areas and systems to only those who are authorized, these access control devices improve security. Different authentication techniques, such as biometrics, PIN numbers, RFID cards, or mobile credentials, are used by each device. This lowers the possibility of theft, misuse, and unauthorized access to personal or company property. Security is strengthened and made more difficult to get around by combining digital and physical access control techniques.
### Evidence:
The evidences includes the photos of these devices in the evidence folder.

## Activity A12 – Discover 5 unique offline security tools
### Description:
In this activity, I explored security tools that function without requiring internet connectivity.
### Identified Security Tools:
1. **Window Security Bars**
Metal bars called window security bars are put on windows to keep people from breaking in. Particularly on ground-floor flats or windows that are easily accessible, they serve as a robust physical barrier.
2. **Chain Lock**
Installing a door chain lock on front doors is a straightforward physical security measure. It prevents complete access while permitting a door to be partially opened for identification. 
3. **Fireproof Document Safe**  
It is a security tool which protects the documents such as passports, ids, certificates from fire and heat damage even though it isn't a locking mechanism but still it keeps private documents safe from loss and damage.
4. **Security Camera System (Local Recording)**  
Instead of uploading video footage to the cloud, these cameras store footage locally on a physical device, such as a microSD card, Network Video Recorder (NVR), or Digital Video Recorder (DVR). This method improves privacy, does not require internet access, and does away with monthly subscription payments.
5. **Security Seal / Tamper‑Evident Seal**
Applying a security or tamper-evident seal on doors, containers, or packages—like ballot boxes, medicine, or freight—provides solid evidence in the event that tampering or unlawful access takes place. Rather than completely blocking access, these seals are intended to identify theft, contamination, or counterfeiting.
### Analysis:
These offline security technologies protect physical locations and belongings by constructing strong, internet-independent barriers. While window bars and chain locks prevent or prevent forced entry, fireproof safes shield important documents from physical damage like heat or fire. Local-storage security cameras enhance privacy because footage stay on the device instead than being uploaded online. By revealing illegal entrance attempts, tamper-evident seals aid in the detection of theft or interference. When combined, these offline technologies increase security since they rely on physical defense rather than digital systems, which allows them to continue operating even in the case of a network or power outage.
### Evidence:
For this activity, the photos are provided in the evidence folder.

## Activity A13 - Discover 5 unique online security tools
### Description:
In this activity, I discovered the tools that enhance security in online environments by searching in google.
### Identified Security Tools:
1. **Virus Total**
A free web service that allows you to submit files or URLs for scanning by several threat intelligence feeds and antivirus engines.
2. **Have I Been Pwned (HIBP)**
A service that allows users to see if known data breaches contain their email addresses and also tells to change passwords immediately if their email addresses contains in the known breaches.
3. **Cloudflare DNS (1.1.1.1) Security**
Uses a secure DNS resolver to protect users by blocking harmful websites, phishing domains, and malware.
4. **Multifactor Authenticator App**
My internet accounts are protected with an authenticator program that creates time-based one-time passwords (TOTPs). I type both my password and the app code when I log into a protected account, which keeps me safe even if my password is stolen.
5. **Google Password Checkup**
This free tool looks for weak, repeated, or compromised passwords within Chrome or your Google account.
### Analysis:
By screening for malware, identifying exposed credentials, blocking dangerous websites, and bolstering account security, these online security solutions assist users in defending themselves against online threats. While password checkers and authenticator applications lessen the likelihood of accounts being stolen, tools like VirusTotal and Cloudflare DNS stop harmful content from reaching the user. When combined, they lower dangers like phishing, data breaches, and illegal access while also making online activities safer.
### Evidence:
The screenshots for each tool are in the evidence folder.

## Activity A15 - Discover 5 recent security incidents
### Description:
I looked over five recent global cybersecurity issues for this assignment. I documented who was impacted, what transpired, what systems or data were affected, and what lessons could be learned from each occurrence.
### Identified Security Incidents:
1. **Change Healthcare Ransomware Attack (2024)**
Summary: In February 2024, a ransomware attack targeted Change Healthcare, a significant U.S. healthcare payment processor controlled by UnitedHealth Group. After gaining access through a weakly secured remote access system, the attackers moved laterally throughout the network, stole a significant amount of data, and encrypted vital systems that processed pharmaceutical and medical claim transactions.
Impact: Many organizations were forced to use manual procedures as a result of the hack, which impacted pharmaceutical services and healthcare payments nationwide. Numerous patients' personal and medical information was compromised, and UnitedHealth's costs were expected to be in the billions.
Lesson: The event demonstrates the significance of multi-factor authentication and robust access controls for remote access systems, as well as how ransomware attacks now combine service interruption with widespread data theft that has long-term financial and legal repercussions.
2. **Ivanti VPN zero‑day exploitation (2024-2025)**
Summary: Early in 2025, Ivanti Connect Secure VPN appliances were found to have a number of previously unidentified vulnerabilities. In order to get around authentication and execute code on susceptible VPN gateways that were connected to the internet, attackers used these vulnerabilities in the wild.
Impact: Attackers gained a foothold right at the network's edge, enabling them to install malware, steal credentials, and establish persistent backdoors in organizations that relied on these VPN equipment for remote access.
Lesson:VPN and remote access devices are high-value targets that need to be promptly patched and continuously watched. Risk is significantly increased when such management interfaces are exposed directly to the internet.
3. **Axios npm package supply‑chain attack (March 2026)**
Sumamry: Two malicious versions of the well-known Axios JavaScript HTTP client package were released in March 2026 after a maintainer account on npm was hijacked. On computers that installed the package, these versions installed a phony dependency that downloaded and executed a remote access Trojan via a post-install script.
Impact: Due to the widespread use of Axios, any server, build pipeline, or developer workstation that installed the malicious versions during the impacted time may have been backdoored, revealing credentials, API keys, and other secrets and perhaps resulting in additional breaches in downstream applications.
Lesson: This instance demonstrates how malware can spread throughout the software supply chain from a single corrupted open-source requirement. It emphasizes the necessity of restricting the automated execution of install scripts, carefully reviewing and monitoring dependency updates, and implementing robust security on maintainer accounts (such as multi-factor authentication).
4. **Qantas customer data breach (2025)**
Summary: Qantas revealed that a hacked third-party system linked to its CRM platform allowed hackers to obtain frequent-flyer user data. Numerous loyalty accounts were affected by the breach.
Impact: Names and contact information for airline passengers were among the exposed data, raising the possibility of targeted phishing and social engineering attacks that appear as Qantas or associated businesses.
Lesson: This case illustrates how, even in situations where the primary organization's systems are reasonably safe, third-party and supply-chain vulnerabilities can disclose customer data. It emphasizes the necessity of strict control over integrations with outside sources and robust vendor-risk management.
5. **Large credential dump (around 16 billion passwords, 2025)**
Summary:Security experts discovered that infostealer malware records were being discussed on criminal forums, and a massive collection of almost 16 billion credentials was assembled from prior data breaches. Passwords and email addresses were included in several of the submissions.
Impact:Because many users continued to use the same passwords on many websites, this dump made it much simpler for attackers to launch credential-stuffing attacks against numerous online services.
Lesson: The event demonstrates why password managers are crucial, why users should never reuse passwords, and why multi-factor authentication is required to secure accounts even in cases where credentials are compromised.
### Analysis:
The exploitation of remote access, the compromising of third-party or open-source components, and the misuse of huge collections of credentials that have been obtained are common patterns among these instances. This highlights the significance of multi-factor authentication, prompt edge device patching, cautious vendor and software dependency management, and improved user password habits.
### Evidence:
The supporting documents are in the evidence folder.

## Activity A16 - Discover 3 local security incidents
### Description:
In this activity, I explored cybersecurity incidents that occurred in Australia.
### Identified Security Incidents:
1. **University of Western Australia password breach (Aug 2025)**
Summary: UWA reported a cyber incident in which hackers gained access to systems that held staff, student, and visitor passwords. As a precaution, the institution reset all accounts. 
Impact: Everyone had to change their password, and until the reset was finished, they were unable to use online services like email, LMS, and VPN.  
Lesson: Universities need to keep a careful eye on their authentication systems, enforce multi-factor authentication and strong password policies, and have a clear process in place for promptly revoking and resetting credentials in the event of a breach.
2. **Noosa Shire Council cyber fraud (Dec 2024, disclosed 2025)**
Summary: In the 2024 Christmas period, scammers deceived the Noosa Shire Council in Queensland into transferring council payments to fake bank accounts by using persuasive emails and documents.
Impact: Before some money was recovered, the council lost almost $2 million in ratepayer payments; nevertheless, no personal information or internal IT systems were directly compromised.
Lesson: Strict verification procedures for payment adjustments and frequent staff training to identify unusual requests are necessary since social engineering and payment redirection schemes can still be successful even in secure systems.
3. **University of Sydney code library breach (Dec 2025)**
Summary:The University of Sydney reported that the site was pulled offline for an inquiry after hackers gained access to an internal online code library used by researchers and employees.  
Impact: Teams had to inspect systems that used the impacted code and rotate any exposed credentials when some projects experienced a temporary loss of access to their code repository.  
Lesson: Code repositories require strong access controls, secret management, and frequent security evaluations since they frequently include sensitive data and are valuable targets.
### Analysis:
These examples demonstrate the vulnerability of local Australian organizations of various kinds, including a council and universities, to cyber threats that target development tools, business processes, and passwords. They point out that rather than using only technical exploits, attackers frequently succeed through social engineering, compromised secrets, or poor authentication. In general, they emphasize the necessity of robust identity controls (passwords, MFA), safe code and credential management, and well-thought-out procedures with employee training to identify fraud and promptly address security breaches.
### Evidence:
the supporting documents are in the evidence folder.

## Activity A17 - Discover 10 different types of locks in use
### Description:
For this exercise, I searched around my house, the university, and public areas to find 10 various types of physical locks and how they are utilized for security.
### Identified different types of locks in use:
1. **Pad lock**
A portable lock with a shackle that fastens to gates, lockers, or chains. typical for bike chains, barns, and lockers. 
2. **Deadbolt lock**
Strong door locks, seen on home or apartment doors, have a robust metal bolt that glides into the door frame.
3. **Knob Lock**
For basic security, inside office or classroom doors frequently include a lock integrated into the handle.
4. **Lever lock**
A lever lock is a kind of door lock that offers security by requiring a code or key to open and unlock the door.
5. **Bike U‑lock / D‑lock**
Bicycle frames are fastened to racks or poles using a stiff U-shaped metal lock that is resistant to cutting and levering.
6. **Cable lock**
Bicycles, scooters, and equipment can be fastened to permanent objects using flexible steel cables with integrated or separate locks.
7. **Combination Lock**
Padlocks, which are frequently found on school and gym lockers, unlock using a spinning dial or numbered wheels rather than a key.
8. **Lever Latch**
Often used on internal passage doors, a lever handle with a latch keeps a door closed 
9. **Window lock with thumb‑turn**
A lock installed on a sliding door or window that secures the panel so it cannot be opened from the outside using a thumb-turn and occasionally a key.
10. **Barrel bolt lock**
A straightforward surface-mounted lock that manually inserts a straight metal bolt into a little catch plate on the frame. By manually sliding the bolt across to keep the door closed, it is frequently used on internal doors, gates, cabinets, and bathroom doors to provide additional security or privacy.
### Analysis:
The level of physical security offered by various lock types varies based on their design and intended purpose. While some locks, like knob locks and barrel bolts, offer minimal security or privacy, others, like deadbolts and U-locks, provide robust protection against forced entrance. By restricting physical access, using various lock types helps secure windows, doors, bicycles, and personal items. When combined, these locks provide several levels of security that lower the possibility of theft and unwanted access in residences, public areas, and educational institutions.
### Evidence:
The all photos of locks are in the evidence folder.

## Activity A18 - Discover two hallucination cases when using a generative AI system
### Description:
I investigated how generative AI systems might occasionally generate inaccurate results, or "hallucinations," for this exercise. When an AI model provides confident answers that are incorrect because of misunderstandings, wrong assumptions, or inadequate context, this is known as an AI hallucination. As I worked on my cybersecurity portfolio, I directly interacted with a generative AI system and discovered three instances of hallucinations and one discover online.
### Identified Hallunication cases:
1. ** Case 1 - Incorrect Identification of Web Browser**
The AI recognized that I was using Safari when I uploaded a screenshot of my web browser displaying security information. This information was inaccurate, though, as the screenshot's browser was actually Google Chrome. Without enough proof, the AI made this claim without seeking clarification. This is an instance of a contextual hallucination, in which the AI confidently came to the wrong conclusion based on few contextual signals after misinterpreting visual or interface features.
2. **Misinterpretation of GitHub Repository Structure**
In another instance, I provided an explanation of my GitHub repository structure along with a screenshot. The AI falsely reported that my part1_activities folder contained two README.md files. In actuality, the part1_activities folder included no duplicate README.md and only one README.md at the repository root. This happened as a result of the AI misinterpreting the file structure and assuming false information rather than asking for clarification. When an AI confidently misinterprets organizational information from a screenshot, it is called a contextual or structural hallucination.
3. **Fabrication of Academic References (Published Case)**
Emsley (2023) describes a documented incidence of hallucinations in which ChatGPT produced realistic-looking but nonexistent academic references when requested to back up a scientific claim. None of the fake publications could be located in PubMed or other scholarly databases, despite having plausible titles, authors, and journals. This is an example of a factual hallucination, demonstrating how AI can provide convincing but inaccurate information that could mislead people if outputs are not validated.
### Analysis:
These examples demonstrate that AI hallucinations can take many different forms, such as factual, structural, and contextual errors. Responses may still be inaccurate even if they seem assured and competent. This emphasizes how crucial it is to assess and validate AI-generated results critically, particularly in technical and scholarly contexts like cybersecurity research and documentation.
### Evidence:
The all supporting documents and references are included in the evidence folder.

## Activity A19 - Join a CS/DS/cybersecurity club
### Description:
In order to interact with students who are interested in cybersecurity, computer science, and digital safety, I joined a cybersecurity group at my institution. Students can study cooperatively, stay updated on cybersecurity issues, and take part in conversations or activities regarding the discipline by joining a club.
### PArticipation and learning
I became a member of the University Computer Club, or UCC. I registered for membership and interacted with the club via its internet channels. I also joined the Discord server to take part in conversations, get information, and interact with other members, and I followed the club on Instagram to keep up with announcements and activities. I was able to access cybersecurity-related posts, conversations, announcements, and other educational opportunities that the club published via various channels. Members of the Discord community can interact, exchange information, and pose cybersecurity-related queries.
### Analysis:
Participating in a cybersecurity club fosters knowledge of practical cybersecurity issues outside of the classroom. It promotes cooperation, information exchange, and interaction with colleagues who share similar academic and career goals. It is simpler to stay updated, ask questions, and interact with cybersecurity content in a casual learning setting thanks to online platforms like Instagram and Discord.
### Evidence:
The proof of Membership, discord and instagram accounts are in evidence folder.

## Activity A20 - Participate in a discussion with your friends about cybersecurity event
### Description:
I took part in an in-person conversation on a real-world cybersecurity incident with my friend as a part of this activity. Understanding how cyberattacks happen, who perpetrates them, and how they affect businesses and users were the main topics of debate.
### Discussion:
We talked about the Ticketmaster data leak, which was allegedly connected to the ShinyHunters hacker collective. During the conversation, we discussed:
- When the assault took place and how it was found
- The attack's methodology, includes data theft and illegal access
- Ticketmaster's massive consumer data storage is the reason it was targeted.
- ShinyHunters' identity and reputation as a cybercrime organization
- ShinyHunters has previously committed other significant breaches.
- Attack methods, including database leaks, data breaches, and the sale of stolen data on internet forums
We also talked about the consequences of the breach, including identity theft, privacy issues for users, and the significance of robust security measures like data encryption and multi-factor authentication.
### Analysis:
Talking about actual cybersecurity issues with friends increases understanding of how cyberattacks happen in real-world settings. It promotes critical thinking regarding the reasons for attacks, security flaws, and the significance of safeguarding personal data. I now have a better understanding of how organized cybercrime groups function and why businesses with sensitive user data are frequently targeted.
### Evidence:
For this activity, we have a voice recording which is uploaded in the evidence folder.

## Activity A21 - Participate in an online cybersecurity discussion
### Description:
For this activity, I participated in online discussions about cybersecurity in public internet forums. These sites allow users to ask questions, exchange stories, and engage with others from diverse backgrounds regarding cybersecurity challenges.
### Discussions:
I used my Reddit account, u/Bubbly-Psychology387, to take part in two discussions. As a student at university, I asked a question in r/cybersecurity about how to advance my defensive (blue-team) abilities beyond simple hashing and Python. In response, a security expert advised me to start by developing solid IT foundations, including networking, operating systems, and authentication.
I posted a request for websites or online video channels for cybersecurity instruction in r/learnprogramming. Another user replied with a link to a free online resource that I could use to get started. These discussions showed me that online communities may provide useful resources for beginning cybersecurity education as well as guidance on what to study (IT fundamentals).
### Analysis:
Engaging in online cybersecurity forums exposes students to real-world security issues and offers helpful guidance from experienced professionals. These conversations encourage lifelong learning and offer perspectives that aren't typically addressed in conventional education.
### Evidence:
The screenshot of reddits are in the evidence folder.

## Activity A30 - Complete an online cybersecurity module
### Description:
I finished the TryHackMe module "Module 1: Start your Cyber Security Journey and Module 2: Linux fundamentals part 1," which focuses on basic Linux, web hacking, defensive security, networking. These rooms are a component of TryHackMe's basic learning path, which aims to provide new students with fundamental cybersecurity knowledge. This interactive lesson teaches useful cybersecurity skills through challenges and guided virtual machines.
### Modules Content:
I observed basic examples of attacks and defenses, learnt about the key components of cybersecurity (offensive vs. defensive security), and investigated several career options in cyber in Start Your Cybersecurity Journey. I worked through a number of rooms during the module that addressed issues like command-line basics on the terminal, virustotal, and there other given prompts. I set up a Linux system in the browser and practiced fundamental terminal operations including ls, cd, echo, whoami, and basic file navigation and search in Linux Fundamentals Part 1. I completed the challenges by following the directions, executing the necessary commands or tools, responding to the questions in the room, and capturing flags.
### Skills and tools learned:
This program taught me how to scan a target, use virustotal, shodan.io, locate open services, find and exploit simple vulnerabilities, or analyze logs to spot malicious activity and gave me practice with tools like Linux command line. My confidence in working on a Linux command line or terminal, following to a systematic approach, and recording my actions while resolving security issues has increased as a result.
### Reflection:
After finishing this TryHackMe lesson, I realized how crucial practical experience is to comprehending cybersecurity principles rather than merely reading theory. Additionally, I discovered that taking thorough notes during each lesson makes it simpler to duplicate the methods later on and to describe my methodology in labs, tests, and future job applications.
### Evidence:
all the screenshots of completing module are in the folder.

### Activity A4 - Discover a vulnerable website
### Description:
In this exercise, I examined a publically available website (https://www.captainfinishing.ca) for possible security flaws using OWASP ZAP (Zed Attack Proxy).
### Identified Vulnerabilities:
1. **Content Security Policy (CSP) Header Not Set**
Some responses lacked a Content-Security-Policy header, such as sitemap.xml. The site owner can limit the sources of scripts, styles, and other content the browser can load by using a CSP header. The impact of content-injection attacks is increased in the absence of CSP since the browser is more likely to execute JavaScript if an attacker is able to inject it (for instance through an XSS vulnerability).
2. **Missing Anti-Clickjacking Header (X-Frame-Options)**
Additionally, ZAP identified "Missing Anti-clickjacking Header" (no CSP frame-ancestors or X-Frame-Options). Clickjacking attacks, in which a user is tricked into clicking hidden buttons or links inside an iframe, are made possible by the absence of these headers, which allow the website to be framed by another domain. The website would not be embedded on untrusted pages if X-Frame-Options: DENY or a suitable frame-ancestors policy was set.
3. **Subresource Integrity (SRI) Attribute Missing**
Subresource Integrity was not used by an external stylesheet that was loaded from fonts.googleapis.com, according to another alert. For an external script or style, SRI enables the developer to provide a cryptographic hash so the browser can confirm it hasn't been changed. Without SRI, malicious code could be placed onto the website without the browser noticing if the third-party CDN is compromised.
### Analysis:
Common security misconfigurations, one of the most common reasons for online exploitation, are demonstrated by these vulnerabilities. Although missing HTTP security headers does not necessarily indicate that a website has been compromised, they greatly raise the risk by making attacks like content injection, clickjacking, and XSS possible. This exercise emphasizes the significance of safe server-side configuration and demonstrates how defensive technologies, such as OWASP ZAP, can find vulnerabilities before they are exploited.
### Evidence:
the screenshot of ZAP for scanning the website are in the evidence folder.

## Activity A23 - Enhance the cybersecurity at home
### Description:
For this exercise, I improved network access controls, device security, and account protection to strengthen the cybersecurity of my home environment. The emphasis was on lowering the possibility of unwanted access and safeguarding household members' personal information.
### Security Improvements Implemented:
1. **Multi-Factor Authentication (MFA)**
Initially, I set up my iPhone's authenticator app to only open after passing Face ID. This implies that even if someone were to gain physical access to my phone, they would not be able to view my MFA codes without my face because they are all stored inside an app that requires biometric identification. Face ID is supported by iOS for auto filling passwords and unlocking secure apps. I told my uncle to set MFA and then also setup same thing on his phone.
2. **Device Security (Passwords and Biometrics)**  
To prevent someone from just disabling connectivity or turning off the phone without unlocking it, I finally shut down my Control Centre and device access. When the device is locked, iOS lets you limit Control Centre and other features by requiring a Face ID or passcode verification before using those controls.
3. **Wi-Fi Password Security Enhancements**
Every time I need to see my saved Wi-Fi password, I rely on Face ID. My home Wi-Fi password is secure and cannot be viewed by anyone who does not pass biometric checks because the Wi-Fi password screen on both my uncle’s and my phone only display the password after Face ID or passcode verification.
### Analysis:
Improving home cybersecurity helps in defending shared systems and individuals against online attacks. If a device is lost or stolen, unauthorized access to personal data is prevented by using biometrics and strong device passwords. An additional layer of security is added to standard passwords by using Face ID to access the authenticator app and expose Wi-Fi credentials. Even if passwords are stolen, enabling MFA lowers the chance of account breach. Additionally, locking the Control Centre on the lock screen keeps my device and data safer by preventing someone from simply shutting down phone or cutting off connectivity. When combined, these actions strengthen and secure the cybersecurity environment at home.
### Evidence:
All screenshots are in the folder of evidence.

### Activity A24 - Teach your family about cybersecurity topic of your choice
### Description:
In order to increase a family member's awareness of online hazards, I taught them about a cybersecurity issue for this assignment. Since many real-world attacks rely on taking advantage of human behavior rather than technical flaws, it is crucial to teach cybersecurity concepts to non-technical users.
### Teaching Details:
Since phishing schemes are among the most frequent sources of online fraud and account compromise, I decided to utilize them as the cybersecurity theme.
i explained: 
- What is phishing, and how do attackers pretend to be trustworthy businesses like banks, delivery services, or government agencies?
- False "account warning" or "package delivery" emails are common examples of phishing.
- Poor grammar, odd links, hurry, and false sender addresses are warning signs to be aware of.
- Refusing to open links in unexpected messages, manually typing website addresses, and never transferring passwords or one-time verification codes are all safe practices to follow.
Additionally, I described how multi-factor authentication (MFA) can lower risk even in the event that a password is compromised.
### How I Delivered It:
I explained this subject orally using simple language and real-world examples. I encouraged my uncle to ask questions and told them to get in touch with me if they had any concerns about any odd emails or communications.
### Analysis:
The risk that common people will become victims of online fraud can be reduced by increasing awareness of phishing. Many cybersecurity attacks employ social engineering rather than technology exploitation. When phishing indications and safe response procedures are explained, family members are better able to identify threats and protect their personal information. This project also gave me the opportunity to try communicating technical security ideas in a clear way
### Evidence:
My voice recording is in the evidence folder.

## Activity A29 - Analyse AI-generated media using a detection tool
### Description:
In this task, I examined a freely accessible AI-produced media to assess its authenticity. As generative AI becomes more prevalent, identifying altered or AI-created content is crucial for stopping misinformation, fraud, and identity theft.
### Media Selected:
I chose an image from the internet that seemed realistic but might have been produced by artificial intelligence.
### Tool Used:
- HiveModeration AI Detection Tool
### Detecting Media:
Hive Moderation conducted a detailed examination of the video, frame by frame, and determined it to be probably AI-generated, with a confidence level of 99.9%. The tool also noted that the content revealed characteristics typical of AI-generated visual media.
### Analysis:
Without specific tools, it can be challenging to distinguish AI-generated photos and videos from real content due to their similar resemblance. Visual patterns, inconsistencies, and artifacts created by generative AI models are analyzed using detection tools such as Hive Moderation. My understanding of how deepfakes and synthetic media can be identified and the importance of verification tools for preserving security and trust in online settings has improved as a result of this exercise.
### Evidence:
The picture are in the evidence folder.

## Activity A28 - Implement a security solution of your choice and put it on your GitHub
### Description:
I used Python to create a straightforward security solution for this exercise, which I then submitted to GitHub. The project is a strength tester for passwords.
### Implementation of Security Solution:
I used Python to create a password strength checker. The software evaluates a password according to its length, complexity, and variety of characters. It offers suggestions to assist users strengthen weak passwords.
### How It Works:
The script analyses a password based on:
- Length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
### Analysis:
Protecting user accounts requires strong passwords. By promoting improved password practices, this security solution helps in preventing attacks like brute-force and credential-stuffing. Putting this method into practice shows how fundamental programming can greatly enhance cybersecurity.
### Evidence:
The python file is uploaded in the evidence folder.

### Activity A25 - Design and implement a privacy-preserving technique for an appropriate application
### Description:
In order to complete this task, I created and put into practice a privacy-preserving method for a customer account management application that requires the safe presentation of private information without complete disclosure.
### Implementation:
I used Python to build a data masking approach. In order to prevent sensitive information from being totally exposed, the application accepts personal data, such as phone numbers and email addresses, and presents it in a masked manner.
For example:
testuser@gmail.com → te****@gmail.com
9876543210 → ******3210
The program works correctly and produces masked output when executed.
### Analysis:
A popular privacy-preserving method in real-world applications including banking platforms, healthcare systems, and customer support portals is data masking. It lessens the exposure of sensitive data while enabling systems to operate normally.
In the context of this application, masking guarantees:
- Support personnel can identify accounts without having access to all personal information.
- There is less chance of unintentional disclosure.
- Even if unauthorized people are watching the screen, privacy is maintained.
This method follows to the data minimization principle, which specifies that systems should only reveal the bare minimum of personal information. Data masking at the application level enhances user confidence and is consistent with privacy-by-design best practices.
### Evidence:
The python file and output is in the evidence folder.


















