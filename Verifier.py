
users = [

    {"username": "Chris", "email": "c1@gmail.com"},
    {"username": "Kai", "email": "k2@gmail.com"},
    {"username": "Shai", "email": "sh3@gmail.com"},
]
def get_user (accounts):
 for user in users:
     if accounts.lower() == user['email'].lower() or accounts.lower() == user['username'].lower():
        return user


 return None


def post_account (username, email):
    if get_user(email) or get_user(username):
        return "Account already exists"

    else:
        users.append({"Username " : username, "Email" : email})
        return "Account created successfully"


def put_account(accounts, newusername, newemail):
    for i, user in enumerate(users):
        if accounts.lower() == user['email'].lower() or accounts.lower() == user['username'].lower():
            users[i]['username'] = newusername
            users[i]['email'] = newemail
            return "Account updated successfully"

    return "Account not found"

def delete_account(accounts):
    user = get_user(accounts)
    if user:
        users.remove(user)
        return "User deleted"
    return "User not found"


print("Welcome!")
while True:
    Options = input(
        "\nWhat would you like to do with your account?\n"
        "1. Log in\n"
        "2. Create new\n"
        "3. Delete account\n"
        "4. Replace account\n"
        "5. Exit\n"
        "Choose option (1-5): "
    )

    match Options:
        case "1":
            accounts = input("Enter username or email: ")
            user = get_user(accounts)
            if user:
                print("Account verified")
                print("Hello", user['username'])
            else:
                print("Account not found")

        case "2":
            username = input("Enter username: ")
            email = input("Enter email: ")
            print(post_account(username, email))

        case "3":
            accounts = input("Enter username or email to delete: ")
            print(delete_account(accounts))

        case "4":
            accounts = input("Enter username or email to update: ")
            newusername = input("New username: ")
            newemail = input("New email: ")
            print(put_account(accounts, newusername, newemail))

        case "5":
            print("Exiting")
            break

        case _:
            print("Invalid operation.")





