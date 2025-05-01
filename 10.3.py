def create_vcard(name, phone, email, address, filename="contact.vcf"):
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
ADR;TYPE=HOME:;;{address}
END:VCARD
"""
    with open(filename, 'w') as file:
        file.write(vcard)
    print(f"vCard saved as '{filename}'.")

# Accepting input from the user
name = input("Enter full name: ")
phone = input("Enter phone number: ")
email = input("Enter email address: ")
address = input("Enter address: ")

create_vcard(name, phone, email, address)
