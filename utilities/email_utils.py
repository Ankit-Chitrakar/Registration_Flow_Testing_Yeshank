import random
import string

class EmailUtils:
    existing_emails = []

    @staticmethod
    def generate_random_email():
        domain = "gmail.com"
        local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        email = f"{local_part}@{domain}"
        return email

    @staticmethod
    def get_next_email():
        if EmailUtils.existing_emails:
            return EmailUtils.existing_emails[0]
        else:
            new_email = EmailUtils.generate_random_email()
            EmailUtils.existing_emails.append(new_email)
            return new_email
