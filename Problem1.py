import re
validator = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


def check_email(email):
    if re.search(validator, email):
        return True


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        email = input()
        emails.append(email)
    correct_emails = filter(check_email, emails)
    for e in correct_emails:
        print(e)

