current_users = ['aa', 'BBB', 'cdd', 'dsd', 'admin']
new_users = ['aa', 'bbb', 'dfdfj', 'fds', 'www']
for new_user in new_users:
    if new_user in current_users:
        print("This name has been used, you need to input other user name.")
    else:
        print("This name has not been used.")

current_users_copy = []
for current_user in current_users:
    current_users_copy.append(current_user.lower())
print(current_users_copy)
