from authentication import register_user, login_user

print("1: Signup")
print("2: Login")
print("3: Exit")

choice = input("Choose your option: ")
if choice == "1":
    register_user()
elif choice == "2":
    abc = login_user()
    if abc:
        user_id, user_name, password, user_role = abc
        print(f"Welcome {user_name}! You are logged in as {user_role}.")
else:
    print("Exited")
