users = ["jen", "sarah", "edward", "phil", "lihua", "jan"]
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}
for user in users:
    if user in favorite_languages.keys():
        print(f"{user}, Thanks four your engaging.")
    else:
        print(f"{user}, Please you engage our investigate.")