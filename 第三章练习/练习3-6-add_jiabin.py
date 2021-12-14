investe_names = ['aa', 'bb', 'cc']
print(f"I would like to invest {investe_names[0]}, {investe_names[1]}, {investe_names[2]} to have dinner.")
print(f"But,I just learned {investe_names[0]} could not keep the appointment, so I will revise the name list, change to:")
investe_names[0] = 'dd'
print(investe_names)
print(f"{investe_names[0]}, I would like to invest you to have dinner.")
print(f"{investe_names[1]}, I would like to invest you to have dinner.")
print(f"{investe_names[2]}, I would like to invest you to have dinner.")
print(f"Just now, I find a bigger table, I will invest more person.")
investe_names.insert(0, 'ee')
investe_names.insert(2, 'ff')
investe_names.append('gg')
print(f"{investe_names[0]}, I would like to invest you to have dinner.")
print(f"{investe_names[1]}, I would like to invest you to have dinner.")
print(f"{investe_names[2]}, I would like to invest you to have dinner.")
print(f"{investe_names[3]}, I would like to invest you to have dinner.")
print(f"{investe_names[4]}, I would like to invest you to have dinner.")
print(f"{investe_names[5]}, I would like to invest you to have dinner.")

print("===or, use cycle===")
for i in investe_names:
    print(f"{i}, I would like to invest you to have dinner.")

