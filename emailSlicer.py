# collect email from user
# split email using the eg. hello@david.com @, save the first part as the username, second as the domain
# split domain using .

def main():
    print("Welcome to the email slicer")
    print("")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain , extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)
while True: 
    main()