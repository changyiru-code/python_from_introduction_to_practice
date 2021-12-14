user_names = ['aa', 'bbb', 'cdd', 'dsd', 'admin']
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print('Hello admin, would you like to see a atatus report?')
        else:
            print(f'Hello {user_name}, thank you for logging in again.')
else:
    print('We need to find some users!')
for i in range(len(user_names)):
    del user_names[0]
if not user_names:
    print('We need to find some users!')
