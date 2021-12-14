def make_album(singer_name, album_name, singer_count=None):
    full_name = {"singer_name": singer_name, "album_name":album_name}
    # full_name["singer_name"] = singer_name
    # full_name["album_name"] = album_name

    if singer_count:
        full_name["singer_count"] = singer_count
    return full_name

while True:
    singer_name = input("\nPlease input the singer of the album: ")
    album_name = input("Please input the album's name of the album: ")
    full_name = make_album(singer_name, album_name)
    print(full_name)
    q = input("Would you want to quit?(yes or no)")
    if q == "yes":
        break
