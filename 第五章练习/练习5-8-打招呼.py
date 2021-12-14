user_names = ['aa', 'bbb', 'cdd', 'dsd', 'admin']
for user_name in user_names:
    if user_name == 'admin':
        print('Hello admin, would you like to see a atatus report?')
    else:
        print(f'Hello {user_name}, thank you for logging in again.')
