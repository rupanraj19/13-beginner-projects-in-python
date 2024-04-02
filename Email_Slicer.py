# collect email from user
# split email using the @ character, the first part as user name, the second part as domain
# split domain using .,

def main():
    email = input("Enter your email address: ")
    user, domain = email.split('@')
    (domain, extension) = domain.split('.')
    print(f"User: {user}, Domain: {domain}, Extension: {extension}")

while True:
    main()
    print("ctrl + c to exit...")