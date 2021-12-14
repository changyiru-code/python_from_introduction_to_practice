# def make_album(singer_name, album_name):
#     full_name = {}
#     full_name["singer_name"] = singer_name
#     full_name["album_name"] = album_name
#     return full_name
#
#
# full_name = make_album("Jason", "未.live")
# print(full_name)
# full_name = make_album("zhangliangying", "我相信")
# print(full_name)
# full_name = make_album("xuezhiqian", "意外")
# print(full_name)



def make_album(singer_name, album_name, singer_count=None):
    full_name = {"singer_name": singer_name, "album_name":album_name}
    # full_name["singer_name"] = singer_name
    # full_name["album_name"] = album_name

    if singer_count:
        full_name["singer_count"] = singer_count
    return full_name


full_name = make_album("Jason", "未.live", 288)
print(full_name)
full_name = make_album("zhangliangying", "我相信")
print(full_name)
full_name = make_album("xuezhiqian", "意外")
print(full_name)
