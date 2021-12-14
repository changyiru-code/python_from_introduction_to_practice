def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_info = build_profile("Li", "hua", age=8, sex=1, tall=180)
print(user_info)
