users = {}

while True:
    print("\n=== Active Directory User Manager ===")
    print("1. Create User")
    print("2. View Users")
    print("3. Disable User")
    print("4. Search User")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Enter username: ")

        users[username] = "Active"

        print("User Created")

    elif choice == "2":
        if len(users) == 0:
            print("No Users Found")
        else:
            for user, status in users.items():
                print(user, "-", status)

    elif choice == "3":
        username = input("Enter username to disable: ")

        if username in users:
            users[username] = "Disabled"
            print("User Disabled")
        else:
            print("User Not Found")

    elif choice == "4":
        username = input("Search username: ")

        if username in users:
            print(username, "-", users[username])
        else:
            print("User Not Found")

    elif choice == "5":
        print("Goodbye")
        break

    else:
        print("Invalid Option")

print("Created by Darwin Brown")

