def mask_email(email):
    name, domain = email.split("@")
    return name[:2] + "****@" + domain

def mask_phone(phone):
    return "******" + phone[-4:]

email = input("Enter email address: ")
phone = input("Enter phone number: ")

print("\nMasked Output:")
print("Masked Email:", mask_email(email))
print("Masked Phone:", mask_phone(phone))